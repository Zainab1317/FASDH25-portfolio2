# Mini Project 2: Text analysis for articles about Gaza War by Zainab Murtaza Ali, Shahrayar Amin Morani, Muhummad Saad Waheed
## Overview of the whole project
The mini project 2 for Digital Humanities focuses on extracting and visualizing place names and their alternate names from a large corpus of news articles about the war of Gaza, sourced from Aljazeera.

The project uses two main computational methords:

**Regex and Gazetteer**: This methord uses predefined lists of place names (gazetteers) combined with regex (regular expresions) to identify location names in the text.

**Named Entity Recognition(NER)**: NER automatically recognizes, identifies and classifies named entities such as locations within unstructued texts.
After using both the methods mentioned above, the project uses geocodes for toponyms to obtain their latitude and longitude coordinates. By doing this we can map and visualise the geographic scope of the news coverage over time which will show us possible shifts in intensity in diffrent areas of Gaza.

Furthermore the project also includes a comparitive analysis of the two extraction techniques and the resulting maps. This will also involve talking about the advantages and diadvantages of each approach in terms of accuracy, coverage, hadeling of alternate spellings, and adaptability to the datasets linguistic challenges.

Overall, this mini project will explore data mining, NLP, geospatial analysi and visualiation of maps to explore how place names of Gaza war are reported and evolve across news articles overtime, and it also provides insights into the geographic dynamics of media covergae during conflicts. 

## Folder structure of repository FASDH25-portfolio2

The repository contains 4 folders titled articles, gazetteers ,Scripts and output. It also has a README file
and gitignore.

### articles folder

The dataset contains articles about the Gaza war from the Al Jazeera website, with coverage dating back to 2017. 

For part 2B of the project, the task was to specify the path to this folder, filter out the articles published in January 2024, and then count how many times specific place names-such as "West Bank" and "Gaza Strip"-were mentioned in those articles.

### gazetteers folder

This directory contains two TSV files: countries.tsv, which provides the geographic coordinates for every country worldwide, and geonames_gaza_selection.tsv, which includes coordinates for specific locations within Gaza. 

This folder is essential for Part 3 of the project, where these files will be used to obtain the coordinates of place names extracted in the ner_counts.tsv file.

### Scripts folder


### README

The repository also contains this file which documents the entire project.

## Using gazetteer and regex to extract all place names in Gaza from the corpus

The objective of the first task is to extract all place names from a large collection of news articles using a gazetteer, which serves as a geographical index or dictionary. Next, the recognition of place names is enhanced by incorporating alternate spellings from another column through the use of regular expression (regex) techniques. Finally, the frequency of each place name mentioned in the articles is counted on a monthly basis and laslty export the results to a tsv file using Pandas library for visualization

### Requirements for the first script

You must have Python installed with the following libraries: 

-	re (Regular expression)

-	os (Operating system)
  
-	Pandas (Pre existing python library used for data analysis and manipulation)


### How the Script Works
**Load the Gazetteer**

Reads the file geonames_gaza_selection.tsv, which contains place names along with their alternate spellings.

Constructs a comprehensive regex pattern for each place by combining all alternate names, enhancing the accuracy and recall of place name recognition.

**Process the Articles**

Skips any articles published before October 7, 2023.

For each remaining article, performs case-insensitive regex matching to identify all occurrences of place names.

Tracks and aggregates the number of mentions for each place on a monthly basis.

**Output Results**

Displays the monthly mention counts for each place.

Saves the aggregated data to a TSV file for further analysis and visualization.

### Verifying results

After running the script, verify that the output in the regex_counts.tsv file is accurate. Compare the extracted place names against the gazetteer to identify any missing locations. Additionally, review the spelling of the place names to assess whether the regex patterns have improved recognition, and determine if further refinements to the regex can enhance the results.

## Using Stanza to Extract Place Names from Gaza Articles

This part of the project focuses on extracting all place names mentioned in news articles about the Gaza war, specifically those published in January 2024. We used Stanza, a Python NLP library, to automatically identify and count place names in the text. This script processes the relevant files, cleans up name variations, and exports the results for further analysis and visualization.

### Requirements for the Script

You need to have Python installed, along with these libraries:

stanza: For Named Entity Recognition (NER).

re: For cleaning and standardizing place names.

os: For file system operations.

### Files and Data used for this part

**News articles**:
The articles are stored in the /content/FASDH25-portfolio2/articles directory, which is cloned from the GitHub repository. Each file in this folder represents a news article, with filenames indicating their publication date.

**Output file**:
The script generates an output file named ner_counts.tsv, which contains two columns: place and count.

### How the script works for this part

 **Setting Up and Loading Data**

Load and download stanza English language model with NER

Clones the project repository containing the articles.

Defines the path to the articles folder: /content/FASDH25-portfolio2/articles.


**Filtering Articles by Date**

Loops through all files in the articles directory.

Selects only those articles published in January 2024 by checking if the filename starts with 2024-01.
makes them into a different list called jan_2024_files.


**Extracting Place Names**

For each selected article, reads the text content.

Uses Stanza’s NER pipeline to identify named entities of types GPE (Geo-Political Entities), LOC (Locations), or FAC (Facilities).

Counts how many times each place name appears across all January 2024 articles.


**Cleaning and Merging Place Names**

Removes possessive endings (e.g. "'" removes commas and apostrophes).

Strips punctuation, standardizes names and removes THE before names to make then easily searchable. 

Adds up the counts of cleaned place names to combine duplicates.


**Output results**

Writes the cleaned place names and their counts to ner_counts.tsv.

Prints the contents of the TSV file 

### Result verification

After running the script:

Check that ner_counts.tsv accurately lists place names and their counts from January 2024 articles.

Review the cleaned names to ensure duplicates and variations have been merged properly.

Confirm that the extraction and cleaning steps have improved the recognition and consistency of place names.
