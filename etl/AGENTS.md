# Agent rules

This is a dataset project. The goal is to create a dataset from source data.

## project sturcture

- etl/scripts for scripts
- etl/source for source files
- etl/source/docs for documentations for source data
- final dataset files lives in project root
- etl/requirements.txt for python requirements

## before doing tasks

- read project README

## tools to use

- data files in etl/source are usually large; use tools like rg/jq/python with polars/duckdb/pandas to explore the data.
- use `uv` to manage script requirements, run scripts
