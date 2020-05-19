import csv
import pandas as pd

data = pd.read_csv("teams.csv")
arr = data.count()
unique_value = data.nunique(dropna = True)
# Get total number of teams & Pokemon
print(len(arr), unique_value)

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
