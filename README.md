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

## 2A) Using gazetteer and regex to extract all place names in Gaza from the corpus

The objective of the first task is to extract all place names from a large collection of news articles using a gazetteer, which serves as a geographical index or dictionary. Next, the recognition of place names is enhanced by incorporating alternate spellings from another column through the use of regular expression (regex) techniques. Finally, the frequency of each place name mentioned in the articles is counted on a monthly basis and laslty export the results to a tsv file using Pandas library for visualization

### Requirements for the first script

You must have Python installed with the following libraries: 

-	re (Regular expression)

-	os (Operating system)
  
-	Pandas (Pre existing python library used for data analysis and manipulation)


### How the Script Works

**Loading the Gazetteer**

We began by looking the geonames_gaza_selection.tsv file, which contains a list of place names along with their alternate spellings. To ensure we captured as many variations as possible, we created a robust regex pattern that would work on all place names in the file. This approach enabled us to recognize place names even if they appeared with different spellings or formats in the articles.

**Processing the Articles**

We reviewed all the news articles, excluding any published before October 7, 2023, as our focus was on the current conflict. For each article published after that date, we applied our regex patterns in a case-insensitive manner to identify all possible occurrences of place names. We then recorded how many times each place was mentioned and organized the counts by month to observe how coverage evolved.

**Outputting the Results**

Finally, we displayed the monthly counts for each location to provide a clear overview of which places received the most attention in the news. Additionally, we saved all this information in a TSV file, allowing us to analyze or visualize the data easily at a later time. 

By combining the gazetteer with flexible regex patterns, we enhanced the accuracy and robustness of our place name extraction, even when names were spelled differently or presented in various formats throughout the articles.

### Verifying results

After running the script, verify that the output in the regex_counts.tsv file is accurate. Compare the extracted place names against the gazetteer to identify any missing locations. Additionally, review the spelling of the place names to assess whether the regex patterns have improved recognition, and determine if further refinements to the regex can enhance the results.

## 2B) Using Stanza to Extract Place Names from Gaza Articles

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

## 3) Creating a Gazetteer with Coordinates for NER Place Names

In this phase of the project, we utilized geocoding to determine the latitude and longitude for all the place names extracted through Named Entity Recognition (NER) from the ner_counts.tsv file. Our objective was to create a gazetteer file named NER_gazetteer.tsv, which includes three columns: place name, latitude, and longitude. For any locations where we could not automatically find coordinates, we marked them as “NA” and later conducted a manual lookup for those coordinates.

### Important Things to Know regarding geonames

We utilized the GeoNames API, which requires a free username for access. The API has limitations on the number of requests you can make, so we incorporated pauses to prevent exceeding those limits. If you would like to run this yourself, you will need to sign up for a GeoNames account and replace the username in the script accordingly.

### How the script works

**Using the GeoNames API to Get Coordinates**

We developed a function that sends a request to the GeoNames API for each place name. The API searches for the best match and returns the corresponding latitude and longitude coordinates. We included a brief pause between each one to prevent overwhelming the server with rapid requests. If the API cannot find any results for a particular place, the function simply returns no data.


**Reading Place Names and Getting Coordinates**

We opened the ner_counts.tsv file, which contains all the place names extracted from the news articles. For each place, we used a function to retrieve its coordinates. If the coordinates were found, we saved them along with the corresponding place name. If the coordinates could not be determined, we recorded the place name with "NA" for both latitude and longitude.


**Writing the Gazetteer File**

We created a new file named NER_gazetteer.tsv, where we stored all the place names along with their coordinates in a simple table format consisting of three columns: place, latitude, and longitude.


**Manually Adding Missing Coordinates**

After the script ran, we checked the gazetteer file for any places marked with “NA.” For those, we searched manually using Google Maps or other sources to find their coordinates and added them to the file. We also made a note of all the places we had to look up manually.

### Verifying Results

Verify that NER_gazetteer.tsv includes all place names from ner_counts.tsv along with their corresponding coordinates. Ensure that there are no missing or duplicated place names. Confirm that manual additions are accurately recorded and noted in the README file.

## 4A) Visualizing Place Names Extracted through Regex Mapping with Animation

In this part of the project, we created an interactive, animated map to show how often different places in Gaza were mentioned in news articles over time. The data we used came from the regex_counts.tsv file, which contains the number of times each place was mentioned each month, extracted using regex and a gazetteer. This visualization helps us see patterns and changes in media coverage as the conflict unfolded.

### Libraries required for this script

plotly.express (For creating interactive maps and animations)

pandas (To load and merge data from TSV files)

### How the script works:

**Prepare the Data**:

To obtain the monthly mention counts for different places, we loaded the `regex_counts.tsv` file. Additionally, we loaded the `ner_gazetteer.tsv` file, which gives each location's latitude and longitude. Then, in order to connect the coordinates of each location with the matching mention counts, we combined these two datasets using the "place" column.


**Creating Animated Map**:

We used Plotly Express to create an interactive map. Each location is represented by a marker on the map. The size of each marker indicates how often a location was mentioned; the larger the marker, the more mentions it received. Different colors for the markers help distinguish between various locations. The map is animated by month, allowing us to observe how the focus of news coverage shifted over time.


**Output for this script**

We created an interactive HTML file (regex_map.html) for the map, allowing anyone to explore it in a web browser. We also generated a static image (regex_map.png) for easy reference.


### Verifying outputs:

We ensured that every location in our dataset was represented on the map. We verified that the sizes of the markers corresponded to the frequency with which each place was mentioned. We played the animation to confirm that the month-to-month changes appeared accurate. If any locations were missing from the map, we checked for missing coordinates in the gazetteer and added them as necessary.



## Advantages and Disadvantages of using ner and gazetteers with regex 

Using these removes human effort and improves these results by being case sensitive to deferentiate between place names and people names. The loop automatically opens the text files and extract the place names. This blended approach ensures accuracy and improved coverage by cross checking the NER results agaist the gazetteer.The place names identified were also accurate enought that the results of the TSV were searched on geonames to yeild results.NER provides flexibility and contextual understanding, while the gazetteer ensures precision and consistency. This dual method can significantly improve both recall and accuracy when analyzing geographical references in text.
This can be time consuming and resource heavy especially with large datasets and corpi. This might also require manual effort to maintain and update the gazetteer. There is also a risk of redundancy or conflict if entities are matched differently by each method, which can complicate the process of merging and interpreting the results. Finally, integrating both techniques into a single workflow can add complexity in terms of code, data management, and debugging, requiring more technical overhead than using either method alone.
