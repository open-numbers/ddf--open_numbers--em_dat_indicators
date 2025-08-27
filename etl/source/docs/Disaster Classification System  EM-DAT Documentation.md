Historical and Current Classification System of Disasters

## A Brief History of the EM-DAT Classification System

EM-DAT’s classification system originally started with a simple 20-type list<sup id="fnref:1"><a href="https://doc.emdat.be/docs/data-structure-and-content/disaster-classification-system/#fn:1" role="doc-noteref">1</a></sup>. However, in 1992, CRED and other international stakeholders proposed a hierarchical classification system<sup id="fnref:2"><a href="https://doc.emdat.be/docs/data-structure-and-content/disaster-classification-system/#fn:2" role="doc-noteref">2</a></sup> that distinguishes natural and man-made disasters (described as technological disasters in EM-DAT). A further distinction was based on the timing of disasters: slow vs. rapid onset disasters.

In the 2000s, CRED collaborated with [Munich Re](https://www.munichre.com/en.html) and other stakeholders on a common classification system<sup id="fnref:3"><a href="https://doc.emdat.be/docs/data-structure-and-content/disaster-classification-system/#fn:3" role="doc-noteref">3</a></sup>. Since then, EM-DAT’s main classification system has followed the logic of referring to the hazard or event triggering the disaster. Consequently, some disasters were reclassified, and some types were removed from the primary classification system. This was the case for famines reclassified as drought for the most part<sup id="fnref:4"><a href="https://doc.emdat.be/docs/data-structure-and-content/disaster-classification-system/#fn:4" role="doc-noteref">4</a></sup>. However, “famine” offers more information than “drought.” Therefore, in order not to lose this added value, EM-DAT has adopted the secondary classification system of [Associated Disasters](https://doc.emdat.be/docs/data-structure-and-content/disaster-classification-system/#associated-disasters). This describes disasters that coincide with or result from the primary type.

In 2014, the [Integrated Research on Disaster Risk (IRDR)](https://www.irdrinternational.org/) working group, which included CRED, established a new reference called the [Peril Classification and Hazard Glossary](https://www.irdrinternational.org/knowledge_pool/publications/173). This document is currently the primary reference for classifying natural hazards in EM-DAT, which divides them into six main groups: Geophysical, Hydrological, Meteorological, Climatological, Biological, and Extra-terrestrial. EM-DAT also includes more detailed subtypes.

![](https://doc.emdat.be/docs/data-structure-and-content/disaster-classification-system/images/irdr_classification_hu3d437f177994af683f4f57ca9b57e87a_335303_700x0_resize_catmullrom_3.png)

Natural Hazards Subgroups and Types in the IRDR Peril Classification and Hazard Glossary

## Main Classification Tree

The main classification tree has four levels of depth, so disasters are divided into groups, subgroups, types, and subtypes, as presented in the [EM-DAT Public Table](https://doc.emdat.be/docs/data-structure-and-content/emdat-public-table/) columns. The two EM-DAT disaster groups are ‘Natural’ and ‘Technological’. The table below shows the complete tree for the ‘Natural’ and ‘Technological’ groups, with the occurrence for each subtype. Their corresponding definitions are available in the [Classification Glossary](https://doc.emdat.be/docs/data-structure-and-content/glossary/).

| Classification Key | Group | Subgroup | Type | Subtype | Count<sup id="fnref:5"><a href="https://doc.emdat.be/docs/data-structure-and-content/disaster-classification-system/#fn:5" role="doc-noteref">5</a></sup> |
| --- | --- | --- | --- | --- | --- |
| nat-bio-ani-ani | Natural | Biological | Animal incident | Animal incident | 1 |
| nat-bio-epi-bac | Natural | Biological | Epidemic | Bacterial disease | 781 |
| nat-bio-epi-dis | Natural | Biological | Epidemic | Infectious disease (General) | 142 |
| nat-bio-epi-fun | Natural | Biological | Epidemic | Fungal disease | 0 |
| nat-bio-epi-par | Natural | Biological | Epidemic | Parasitic disease | 51 |
| nat-bio-epi-pri | Natural | Biological | Epidemic | Prion disease | 0 |
| nat-bio-epi-vir | Natural | Biological | Epidemic | Viral disease | 547 |
| nat-bio-inf-gra | Natural | Biological | Infestation | Grasshopper infestation | 16 |
| nat-bio-inf-inf | Natural | Biological | Infestation | Infestation (General) | 9 |
| nat-bio-inf-loc | Natural | Biological | Infestation | Locust infestation | 67 |
| nat-bio-inf-wor | Natural | Biological | Infestation | Worms infestation | 3 |
| nat-cli-dro-dro | Natural | Climatological | Drought | Drought | 804 |
| nat-cli-glo-glo | Natural | Climatological | Glacial lake outburst flood | Glacial lake outburst flood | 3 |
| nat-cli-wil-for | Natural | Climatological | Wildfire | Forest fire | 317 |
| nat-cli-wil-lan | Natural | Climatological | Wildfire | Land fire (Brush, Bush, Pasture) | 92 |
| nat-cli-wil-wil | Natural | Climatological | Wildfire | Wildfire (General) | 53 |
| nat-ext-imp-air | Natural | Extra-terrestrial | Impact | Airburst | 0 |
| nat-ext-imp-col | Natural | Extra-terrestrial | Impact | Collision | 1 |
| nat-ext-spa-ene | Natural | Extra-terrestrial | Space weather | Energetic particles | 0 |
| nat-ext-spa-geo | Natural | Extra-terrestrial | Space weather | Geomagnetic storm | 0 |
| nat-ext-spa-rad | Natural | Extra-terrestrial | Space weather | Radio disturbance | 0 |
| nat-ext-spa-sho | Natural | Extra-terrestrial | Space weather | Shockwave | 0 |
| nat-geo-ear-gro | Natural | Geophysical | Earthquake | Ground movement | 1544 |
| nat-geo-ear-tsu | Natural | Geophysical | Earthquake | Tsunami | 57 |
| nat-geo-mmd-ava | Natural | Geophysical | Mass movement (dry) | Avalanche (dry) | 5 |
| nat-geo-mmd-lan | Natural | Geophysical | Mass movement (dry) | Landslide (dry) | 30 |
| nat-geo-mmd-roc | Natural | Geophysical | Mass movement (dry) | Rockfall (dry) | 9 |
| nat-geo-mmd-sub | Natural | Geophysical | Mass movement (dry) | Sudden Subsidence (dry) | 1 |
| nat-geo-vol-ash | Natural | Geophysical | Volcanic activity | Ash fall | 249 |
| nat-geo-vol-lah | Natural | Geophysical | Volcanic activity | Lahar | 0 |
| nat-geo-vol-lav | Natural | Geophysical | Volcanic activity | Lava flow | 10 |
| nat-geo-vol-pyr | Natural | Geophysical | Volcanic activity | Pyroclastic flow | 4 |
| nat-geo-vol-vol | Natural | Geophysical | Volcanic activity | Volcanic activity (General) | 9 |
| nat-hyd-flo-coa | Natural | Hydrological | Flood | Coastal flood | 85 |
| nat-hyd-flo-fla | Natural | Hydrological | Flood | Flash flood | 831 |
| nat-hyd-flo-flo | Natural | Hydrological | Flood | Flood (General) | 2283 |
| nat-hyd-flo-ice | Natural | Hydrological | Flood | Ice jam flood | 0 |
| nat-hyd-flo-riv | Natural | Hydrological | Flood | Riverine flood | 2657 |
| nat-hyd-mmw-ava | Natural | Hydrological | Mass movement (wet) | Avalanche (wet) | 121 |
| nat-hyd-mmw-lan | Natural | Hydrological | Mass movement (wet) | Landslide (wet) | 609 |
| nat-hyd-mmw-mud | Natural | Hydrological | Mass movement (wet) | Mudslide | 79 |
| nat-hyd-mmw-roc | Natural | Hydrological | Mass movement (wet) | Rockfall (wet) | 3 |
| nat-hyd-mmw-sub | Natural | Hydrological | Mass movement (wet) | Sudden Subsidence (wet) | 1 |
| nat-hyd-wav-rog | Natural | Hydrological | Wave action | Rogue wave | 0 |
| nat-hyd-wav-sei | Natural | Hydrological | Wave action | Seiche | 0 |
| nat-met-ext-col | Natural | Meteorological | Extreme temperature | Cold wave | 311 |
| nat-met-ext-hea | Natural | Meteorological | Extreme temperature | Heat wave | 259 |
| nat-met-ext-sev | Natural | Meteorological | Extreme temperature | Severe winter conditions | 79 |
| nat-met-fog-fog | Natural | Meteorological | Fog | Fog | 1 |
| nat-met-sto-bli | Natural | Meteorological | Storm | Blizzard/Winter storm | 226 |
| nat-met-sto-der | Natural | Meteorological | Storm | Derecho | 6 |
| nat-met-sto-ext | Natural | Meteorological | Storm | Extra-tropical storm | 148 |
| nat-met-sto-hai | Natural | Meteorological | Storm | Hail | 111 |
| nat-met-sto-lig | Natural | Meteorological | Storm | Lightning/Thunderstorms | 189 |
| nat-met-sto-san | Natural | Meteorological | Storm | Sand/Dust storm | 20 |
| nat-met-sto-sev | Natural | Meteorological | Storm | Severe weather | 263 |
| nat-met-sto-sto | Natural | Meteorological | Storm | Storm (General) | 898 |
| nat-met-sto-sur | Natural | Meteorological | Storm | Storm surge | 7 |
| nat-met-sto-tor | Natural | Meteorological | Storm | Tornado | 296 |
| nat-met-sto-tro | Natural | Meteorological | Storm | Tropical cyclone | 2492 |
| tec-ind-che-che | Technological | Industrial accident | Chemical spill | Chemical spill | 108 |
| tec-ind-col-col | Technological | Industrial accident | Collapse (Industrial) | Collapse (Industrial) | 181 |
| tec-ind-exp-exp | Technological | Industrial accident | Explosion (Industrial) | Explosion (Industrial) | 778 |
| tec-ind-fir-fir | Technological | Industrial accident | Fire (Industrial) | Fire (Industrial) | 219 |
| tec-ind-gas-gas | Technological | Industrial accident | Gas leak | Gas leak | 61 |
| tec-ind-ind-ind | Technological | Industrial accident | Industrial accident (General) | Industrial accident (General) | 124 |
| tec-ind-oil-oil | Technological | Industrial accident | Oil spill | Oil spill | 8 |
| tec-ind-poi-poi | Technological | Industrial accident | Poisoning | Poisoning | 76 |
| tec-ind-rad-rad | Technological | Industrial accident | Radiation | Radiation | 9 |
| tec-mis-col-col | Technological | Miscellaneous accident | Collapse (Miscellaneous) | Collapse (Miscellaneous) | 305 |
| tec-mis-exp-exp | Technological | Miscellaneous accident | Explosion (Miscellaneous) | Explosion (Miscellaneous) | 220 |
| tec-mis-fir-fir | Technological | Miscellaneous accident | Fire (Miscellaneous) | Fire (Miscellaneous) | 788 |
| tec-mis-mis-mis | Technological | Miscellaneous accident | Miscellaneous accident (General) | Miscellaneous accident (General) | 275 |
| tec-tra-air-air | Technological | Transport | Air | Air | 1089 |
| tec-tra-rai-rai | Technological | Transport | Rail | Rail | 645 |
| tec-tra-roa-roa | Technological | Transport | Road | Road | 2857 |
| tec-tra-wat-wat | Technological | Transport | Water | Water | 1624 |

## Associated Disasters

In addition to the main classification system, EM-DAT makes it possible to refer to “associated disasters” to describe disaster events in more details (see `Associated Dis` in [EM-DAT Public Table](https://doc.emdat.be/docs/data-structure-and-content/emdat-public-table/#column-description)). They represent subsequent or co-occurring hazards that may have contributed to the disaster impact. These associated disasters may not fit into the main classification system and do not have a hierarchical structure. This additional tagging system allows for a better description of disaster events, particularly multi-hazard ones. The figure below shows the main associations found in the database.

![](https://doc.emdat.be/docs/data-structure-and-content/disaster-classification-system/images/sankey_hu1f0fa72a33ee9b8532c8202eefce6081_77087_800x0_resize_catmullrom_3.png)

Sankey diagram of the associations between main disaster types (MT) and associated disaster types (AT) in EM-DAT. The figure only reports MT-AT associations having an occurrence >= 50 in the database. Gray band sizes between MT and AT are proportional to the occurrence of the association in EM-DAT. Last updated: September 5, 2023.

About 14% of disaster entries in EM-DAT have an associated disaster type, and only 3% mention two associated types. The most common associations are floods with landslides (24% of associations), storms with floods (21%), and storms with landslides (8%). Earthquakes are sometimes associated with landslides (4%) and tsunamis (4%) when their damage is deemed negligible compared to ground movement damage.