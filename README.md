# Mini Project 2: Text analysis for articles about Gaza War
## Overview of the whole project
The mini project 2 for Digital Humanities focuses on extracting and visualizing place names and their alternate names from a large corpus of news articles about the was of Gaza, sourced from Aljazeera.

The project uses two main computational methords:

**Regex and Gazetteer**: This methord uses predefined lists of place names (gazetteers) combined with regex (regular expresions) to identify location names in the text.

**Named Entity Recognition(NER)**: NER automatically recognizes, identifies and classifies named entities such as locations within unstructued texts.
After using both the methods mentioned above, the project uses geocodes for toponyms to obtain their latitude and longitude coordinates. By doing this we can map and visualise the geographic scope of the news coverage over time which will show us possible shifts in intensity in diffrent areas of Gaza.

Furthermore the project also includes a comparitive analysis of the two extraction techniques and the resulting maps. This will also involve talking about the advantages and diadvantages of each approach in terms of accuracy, coverage, hadeling of alternate spellings, and adaptability to the datasets linguistic challenges.

Overall, this mini project will explore data mining, NLP, geospatial analysi and visualiation of maps to explore how place names of Gaza war are reported and evolve across news articles overtime.
