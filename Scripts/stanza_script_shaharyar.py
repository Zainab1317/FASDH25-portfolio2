
#import libraries and import language model
import re
import stanza
import os
stanza.download("en")
#create pipeline and specify language
nlp = stanza.Pipeline(lang="en", processors="tokenize,mwt,ner")
#path to the repository
!git clone https://github.com/Zainab1317/FASDH25-portfolio2.git

corpus = "/content/FASDH25-portfolio2/articles"

files = os.listdir(corpus)

jan_2024_files = []
#loop through the entities putting them in a separate list
for file in files:
    if file.startswith("2024-01"):
       jan_2024_files.append(file)
#opening and reading the file
place_counts = {}
for file in jan_2024_files:
    filepath = f"{corpus}/{file}"
    with open(filepath, encoding="utf8") as file:
        text = file.read()
#isolating required entities (gpes and locs)
    doc = nlp(text)
    for sentence in doc.sentences:
      for entity in sentence.ents:
        if entity.type in ["GPE", "LOC"]:
          place = entity.text.strip()
          place_counts[place] = place_counts.get(place, 0) + 1

#cleaning the named entities
clean_counts = {}

for place, count in place_counts.items():
    place = re.sub(r"['`]s\b", "", place)

    place = re.sub(r"[^\w\s]", "", place)

    place = re.sub(r"^the\s+", "", place, flags=re.IGNORECASE)

    clean_counts[place] = clean_counts.get(place, 0) + count

# Write cleaned and sorted data to a TSV file
items = [[place, count] for place, count in clean_counts.items()]

with open("ner_counts.tsv", "w", encoding="utf-8") as file:
    file.write("place\tcount\n")
    for item in items:
        file.write(f"{item[0]}\t{item[1]}\n")

# Read and print the TSV file contents
with open("/content/ner_counts.tsv", encoding="utf-8") as file:
    print(file.read())
