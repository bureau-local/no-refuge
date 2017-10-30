from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import csv


# put all recipients from the csv into a python list 
inputfile = open("all_recipients.csv", "rU")
csv_reader = csv.reader(inputfile)
next(csv_reader) # skip headers
recipients = [row[0] for row in csv_reader] 


# create a file to write the output in
outputfile = open("matches.csv", "wb")
csv_writer = csv.writer(outputfile)
csv_writer.writerow(["la", "type", "county", "best_match", "second_match", "third_match"])


# for every local authority in England
# find the three best matches in the list of recipients
# write the results in the output file
inputfile = open("la.csv", "rU")
csv_reader = csv.reader(inputfile)
next(csv_reader)
for row in csv_reader:
	la = row[0]
	matches = process.extract(la, recipients, limit=3, scorer=fuzz.token_set_ratio)
	matches = [match[0] for match in matches]
	row.extend(matches)
	csv_writer.writerow(row)
