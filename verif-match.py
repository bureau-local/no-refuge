import csv

# this file was written to check if a district
# that hadn't received funding directly
# might have received funding through their council
# so logically we want to ask
# a. did the local authority received funding directly
# b. if not is it a district
# c. if yes did it's county received funding
# d. if yes indicate a match as "via [name of county]"

# puts all local authority in a python dictionary
# with their correct match after manual cleaning
inputfile = open("match-clean.csv", "rU")
csv_reader = csv.reader(inputfile)
headers = next(csv_reader)
matches = {row[0]: row[1] for row in csv_reader}

# loads information about all local authorities
# like the type of authority and county authority
inputfile = open("la.csv", "rU")
csv_reader = csv.reader(inputfile)
next(csv_reader)
las = {row[0]: row[1:] for row in csv_reader}

# create a file to write the output in
outputfile = open("covered.csv", "wb")
csv_writer = csv.writer(outputfile)
csv_writer.writerow(["la", "covered-by"])

# this is where we execute the logical operation
# mentioned at the top of the file
inputfile = open("match-clean.csv", "rU")
csv_reader = csv.reader(inputfile)
next(csv_reader)
for row in csv_reader:
	la = row[0]
	match = row[1]
	if match == "":
		if las[la][0] == "Two-Tier District":
			if matches[las[la][1]] != "":
				row[1] = "via " + matches[las[la][1]]
	# we don't want the two-tier non metropolitan counties
	# to avoid duplicate coverage with district
	if las[la][0] != "Two-Tier County": 
		csv_writer.writerow(row) 
