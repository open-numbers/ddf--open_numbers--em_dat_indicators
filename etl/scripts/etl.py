"""
Notebook for creating em-dat indicators.

- Drought affected annual number
- Drought deaths annual number
- Earthquake affected annual number
- Earthquake deaths annual number
- Epidemic affected annual number
- Epidemic deaths annual number
- Extreme temperature affected annual number
- Flood affected annual number
- Flood deaths annual number
- Plane crash affected annual number
- Plane crash deaths annual number
- Storm affected annual number
- Storm deaths annual number
- Tsunami affected annual number
- Tsunami deaths annual number
"""

import polars as pl
import os

# Project root directory, calculated from this script's location.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def save_df(df, filename):
    """Saves a dataframe to a csv file."""
    filepath = os.path.join(PROJECT_ROOT, filename)
    df.write_csv(filepath)
    print(f"Created {filename}")


def format_datapoints_df(
    df, disaster_type, metric_col, concept_name, min_year, max_year, disaster_subtype=None
):
    """
    Creates a DDF datapoints dataframe for a given indicator.
    """
    filtered_df = df.filter(pl.col("Disaster Type") == disaster_type)
    if disaster_subtype:
        filtered_df = filtered_df.filter(pl.col("Disaster Subtype") == disaster_subtype)

    datapoints = (
        filtered_df.group_by(["Start Year", "ISO"])
        .agg(pl.col(metric_col).sum())
        .rename({"Start Year": "time", "ISO": "geo", metric_col: concept_name})
        .with_columns(pl.col("geo").str.to_lowercase())
    )

    # Create a full grid of all geos and all years
    all_geos = df.select(pl.col("ISO").unique()).rename({"ISO": "geo"})
    all_geos = all_geos.with_columns(pl.col("geo").str.to_lowercase())
    all_years = pl.DataFrame({"time": range(min_year, max_year + 1)})
    full_grid = all_geos.join(all_years, how="cross")

    # Join with datapoints, fill missing values, sort and select columns
    datapoints = (
        full_grid.join(datapoints, on=["geo", "time"], how="left")
        .with_columns(pl.col(concept_name).fill_null(0).cast(pl.Int64))
        .select(["geo", "time", concept_name])
        .sort("geo", "time")
    )

    return datapoints


def format_geo_entities_df(df):
    """
    Creates DDF entities dataframe for geo.
    """
    geo_entities = (
        df.select(["ISO", "Country"])
        .unique(subset=["ISO"], keep="first")
        .sort("ISO")
        .rename({"ISO": "geo", "Country": "name"})
    )

    # convert geo to lowercase
    geo_entities = geo_entities.with_columns(pl.col("geo").str.to_lowercase())

    return geo_entities


def format_concepts_df(indicators):
    """
    Creates the DDF concepts dataframe.
    """
    # Define base concepts
    concepts_data = [
        {"concept": "geo", "name": "Geo", "concept_type": "entity_domain"},
        {"concept": "time", "name": "Time", "concept_type": "time"},
        {"concept": "name", "name": "Name", "concept_type": "string"},
    ]

    # Add measure concepts from indicators list
    for indicator in indicators:
        concept_name = indicator["concept_name"]
        # Create a human-readable name from the concept name
        human_name = concept_name.replace("_", " ").capitalize()
        concepts_data.append(
            {"concept": concept_name, "name": human_name, "concept_type": "measure"}
        )

    concepts_df = pl.DataFrame(concepts_data)

    return concepts_df


def main():
    """
    Main function to run the ETL process.
    """
    source_file_path = os.path.join(
        PROJECT_ROOT, "etl/source/public_emdat_incl_hist_2025-08-11.xlsx"
    )
    df = pl.read_excel(source_file_path, engine="calamine")

    # Create a new column for total affected including deaths
    df = df.with_columns(
        (pl.col("Total Affected").fill_null(0) + pl.col("Total Deaths").fill_null(0)).alias(
            "total_affected_incl_deaths"
        )
    )

    min_year = df.select(pl.col("Start Year").min()).item()
    max_year = df.select(pl.col("Start Year").max()).item()

    # Check for cross-year events
    cross_year_events = df.filter(pl.col("Start Year") != pl.col("End Year"))
    if not cross_year_events.is_empty():
        print(f"Found {len(cross_year_events)} cross-year events.")
        print("Breakdown by disaster type:")
        print(cross_year_events.group_by("Disaster Type").len().sort("len", descending=True))
        print("-" * 30)
        print("Using Start Year as time value")

    indicators = [
        {
            "disaster_type": "Drought",
            "metric_col": "total_affected_incl_deaths",
            "concept_name": "drought_affected_annual_number",
        },
        {
            "disaster_type": "Drought",
            "metric_col": "Total Deaths",
            "concept_name": "drought_deaths_annual_number",
        },
        {
            "disaster_type": "Earthquake",
            "metric_col": "total_affected_incl_deaths",
            "concept_name": "earthquake_affected_annual_number",
            "disaster_subtype": "Ground movement",
        },
        {
            "disaster_type": "Earthquake",
            "metric_col": "Total Deaths",
            "concept_name": "earthquake_deaths_annual_number",
            "disaster_subtype": "Ground movement",
        },
        {
            "disaster_type": "Epidemic",
            "metric_col": "total_affected_incl_deaths",
            "concept_name": "epidemic_affected_annual_number",
        },
        {
            "disaster_type": "Epidemic",
            "metric_col": "Total Deaths",
            "concept_name": "epidemic_deaths_annual_number",
        },
        {
            "disaster_type": "Extreme temperature",
            "metric_col": "total_affected_incl_deaths",
            "concept_name": "extreme_temperature_affected_annual_number",
        },
        {
            "disaster_type": "Flood",
            "metric_col": "total_affected_incl_deaths",
            "concept_name": "flood_affected_annual_number",
        },
        {
            "disaster_type": "Flood",
            "metric_col": "Total Deaths",
            "concept_name": "flood_deaths_annual_number",
        },
        {
            "disaster_type": "Air",
            "metric_col": "total_affected_incl_deaths",
            "concept_name": "plane_crash_affected_annual_number",
            "disaster_subtype": "Air",
        },
        {
            "disaster_type": "Air",
            "metric_col": "Total Deaths",
            "concept_name": "plane_crash_deaths_annual_number",
            "disaster_subtype": "Air",
        },
        {
            "disaster_type": "Storm",
            "metric_col": "total_affected_incl_deaths",
            "concept_name": "storm_affected_annual_number",
        },
        {
            "disaster_type": "Storm",
            "metric_col": "Total Deaths",
            "concept_name": "storm_deaths_annual_number",
        },
        {
            "disaster_type": "Earthquake",
            "metric_col": "total_affected_incl_deaths",
            "concept_name": "tsunami_affected_annual_number",
            "disaster_subtype": "Tsunami",
        },
        {
            "disaster_type": "Earthquake",
            "metric_col": "Total Deaths",
            "concept_name": "tsunami_deaths_annual_number",
            "disaster_subtype": "Tsunami",
        },
    ]

    # create and save entities
    geo_entities_df = format_geo_entities_df(df)
    save_df(geo_entities_df, "ddf--entities--geo.csv")

    # create and save concepts
    concepts_df = format_concepts_df(indicators)
    save_df(concepts_df, "ddf--concepts.csv")

    # create and save indicators
    for indicator in indicators:
        concept_name = indicator["concept_name"]
        datapoints_df = format_datapoints_df(
            df,
            indicator["disaster_type"],
            indicator["metric_col"],
            concept_name,
            min_year,
            max_year,
            indicator.get("disaster_subtype"),
        )
        if datapoints_df.is_empty():
            print(f"Warning: DataFrame for {concept_name} is empty.")
        filename = f"ddf--datapoints--{concept_name}--by--geo--time.csv"
        save_df(datapoints_df, filename)


if __name__ == "__main__":
    main()
