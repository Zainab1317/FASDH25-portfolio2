#imports regular expression to find text patterns
import re
# imports to enable interaction with file system
import os
#imports to hadle tabular data and export tsv file
import pandas as pd

# function writes a list of data rows intotsv file using panadas
def write_tsv(rows, column_list, path):
    #list of rows is converted into panads DataFrame
    df = pd.DataFrame(rows, columns=column_list)
    #DataFrame is written into tsv
    df.to_csv(path, sep="\t", index=False) 

#Setup paths
#defining folder where articles are present
repo_path = "FASDH25-portfolio2"
folder = r"C:\Users\batoo\Downloads\FASDH25-portfolio2\articles" #1) used chatgpt to add "r" before the path so it works
#define path and load gazetteer from the tsv file having place names and alternate names
gazetteer_path = r"C:\Users\batoo\Downloads\FASDH25-portfolio2\gazetteers\geonames_gaza_selection.tsv" 

#Read Gazetteer File
with open(gazetteer_path, encoding="utf-8") as file:
    data = file.read()
    
#an empty dictionary is created for each place names and a count for matches
patterns = {}
#split gazetteer data in new lines to get eeach row on file
rows = data.split("\n") 

#Skip header because the pattern starts from next row
for row in rows[1:]:
    #seprates each column in tsv by tabs
    columns = row.split("\t")
    #ensures that first column has names for the place
    asciiname = columns[0]
    #lists name variants consisting of the standard name
    name_variants = [asciiname]
    #gets the alternate names from the 6th column which is counted as the 5th column, if present
    alternate_names = columns[5].strip()

    if alternate_names:
    #splits the alternate names with comma and gets list of other names
      alternate_list = alternate_names.split(",")
       #loops through each alternate name in the list
      for name in alternate_list:
        #.strip will remove whitespace from alternate names and .append will add alternate names to the list if prenest
        name_variants.append(name.strip())
        

# build a regex pattern that will work to find all names and match diffrent varianats of the place names aswell
#using re.escape to escape any special characters in place names and "|" is used for alternation
    regex_pattern = "|".join (re.escape(name) for name in name_variants) #2) used chatgpt in writing rregex
    #includes all names and their variants with numbers
    patterns[asciiname] = {"pattern": regex_pattern, "count": 0} 

#dictionary stores how many times each name was mentioned
mentions_per_month = {}
#set the date to filter of gaza articles from this date
war_start_date = "2023-10-07" 

#loop through each file as it counts the number of time patterns are found in the folder
for filename in os.listdir(folder):
    #extract the dates from file name in "YYYY-MM-DD" format
    date_str = filename.split("_")[0]
    #if file starts before the start war skip that
    if date_str < war_start_date: 
        continue

    file_path = f"{folder}/{filename}" #build file path to current articles
    with open(file_path, encoding="utf-8") as file: #open and read the articles 
        text = file.read()
        
#loop through each places and search for matches in text
    for place in patterns:
        pattern = patterns[place]["pattern"]
        #find all matches of the place names
        matches = re.findall(pattern, text, re.IGNORECASE) #3) used chatgpt to understand "re.IGNORECASE"
        count = len(matches) #number of times the place was found 
        patterns[place]["count"] += count #add the number of times the place was found into total places

        month_str = date_str[:7] #Extracts the year and month (YYYY-MM) from the full date string (YYYY-MM-DD)
        
#if place is not yet in the dictionary then add it with an empty dictionary for monthly data
        if place not in mentions_per_month:
            mentions_per_month[place] = {}

#if current month is not mentioned in "mention_per_month" then initialise its count as zero
        if month_str not in mentions_per_month[place]:
            mentions_per_month[place][month_str] = 0

# This adds the number of mentions found in the current article to the count for that month
        mentions_per_month[place][month_str] += count

#print output for final dictionary to show how often each names were mentioned
#loop through all places in "mentions_per_month" dictionary
for place in mentions_per_month:
    #start dictionary for current names
    print(f'"{place}": {{')
    #make a list of all months in which place names are mentioned
    month_list = list(mentions_per_month[place].keys()) 

    #loop through each month
    for month in month_list:
        #counts for each month will appear
        count = mentions_per_month[place][month] 

        #displays the output with or without comma if month is either at the end of list or not
        if month != month_list[-1]: 
            print(f'    "{month}": {count},')
        else:
            print(f'    "{month}": {count}')
    print("},") #print the number of times it was mentioned per month

#Prepare Rows and Write TSV

#create an empty list to store final data
output_rows = []
#loop through each place from the start to prepare for final export
for place in mentions_per_month: 

    #loop through each month once again and find the number of times the place is mentioned
    for month in mentions_per_month[place]:
        count = mentions_per_month[place][month]

        output_rows.append((place, month, count)) #Adds a tuple (place, month, count) to the output_rows list for TSV export

write_tsv(output_rows, ["place", "month", "count"], "regex_counts.tsv") #Write final result to tsv file for external use 



