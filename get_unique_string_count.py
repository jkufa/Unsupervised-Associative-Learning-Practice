import csv


teamsCSV = open("teams.csv","r")
fileObject = csv.reader("teams.csv")

# Get total number of teams & Pokemon
row_count = sum(1 for row in fileObject)  # fileObject is your csv.reader
print(row_count)

# Gets number of unique strings present in csv file 
# all_teams = csv.read()
# for team in all_teams.splitlines():
#     print(team)

# with open('teams.csv', 'r') as f:
#     unique_pokemon = {field.lower() 
#               for row in csv.reader(f, delimiter=',')
#               for field in row}

#     print(unique_pokemon)

# for each unique string, find the number of occurances
# for mon in uniqueMonsList:
#     csv.count(mon)
