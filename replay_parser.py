# Parses html file to find list of replays, then parses list of 
# replays to create a csv of teams

from bs4 import BeautifulSoup as soup
import requests

base_webpage = open("replays_by_date.html",'r')
replays_list = open("replays.txt","w")
Teams_CSV = open("teams.csv","w")

soup_webpage = soup(base_webpage,'html.parser') # Create soup of webpage

# Find all <li> tags from soup
all_li = soup_webpage.find_all('li')

# Extract all the <a> tags into a list.
tags = soup_webpage.find_all('a')
 
# ExtractURLs from the attribute href in the <a> tags.
for tag in tags:
    replays_list.write(tag.get('href'))
    replays_list.write('\n')

# Close replays_list and reopen for reading instead of writing
replays_list.close()
replays_list = open("replays.txt","r")
f = replays_list.read()

# Extract teams from each replay url
for replay in f.splitlines():
    team1 = []
    team2 = []
    r = requests.get(replay + ".log")
    for line in r.content.decode("utf-8").splitlines():
        if "|poke|p1|" in line:
            array = line[9:].split(",")
            team1.append(array[0])
        if "|poke|p2|" in line:
            array = line[9:].split(",")
            team2.append(array[0])

    Teams_CSV.write(', '.join(team1))
    Teams_CSV.write('\n')
    Teams_CSV.write(', '.join(team2))
    Teams_CSV.write('\n')
    # print(team1)
    # print(team2)

# Close all file streams
base_webpage.close()
replays_list.close()
Teams_CSV1.close()