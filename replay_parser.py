# Parses html file to find list of replays, then parses list of 
# replays to create a csv of teams

from bs4 import BeautifulSoup as soup
import requests
import re

base_webpage = open("replays_by_date.html",'r')
replays_list = open("replays.txt","w")
Teams_CSV = open("teams.csv","w")

soup_webpage = soup(base_webpage,'html.parser') # Create soup of webpage

# Find all <li> tags from soup
all_li = soup_webpage.find_all('li')

# Extract all the <a> tags into a list.
# Only adds urls that are replays (../gen8vgc2020-xxxxxxxxxx)
tags = soup_webpage.find_all('a', href=re.compile("gen8vgc2020-")) 
 
# Extract URLs from the attribute href in the <a> tags.
i = 0
for tag in tags:
        if(i != 0): # Prevent unecessary newline at top of file
            replays_list.write('\n')
        replays_list.write(tag.get('href'))
        i = 1 # Enable newline

# Close replays_list and reopen for reading instead of writing
replays_list.close()
replays_list = open("replays.txt","r")
f = replays_list.read()

# Extract teams from each replay url
topNewline = 0
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
    # Prevents unecessary newline at top of file
    if(topNewline == 0):
        Teams_CSV.write(', '.join(team1))
        Teams_CSV.write('\n')
        Teams_CSV.write(', '.join(team2))
    else:
        Teams_CSV.write('\n')
        Teams_CSV.write(', '.join(team1))
        Teams_CSV.write('\n')
        Teams_CSV.write(', '.join(team2))
    topNewline = 1
    # print(team1)
    # print(team2)

# Close all file streams
base_webpage.close()
replays_list.close()
Teams_CSV.close()