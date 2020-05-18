# Parses html file to find list of replays, then parses list of replays to create
# a csv of teams

from bs4 import BeautifulSoup as soup
import requests

# webpage = open("replays_by_date.html",'r')
webpage = open("replays_by_date.html",'r')
output = open("replays.txt","r")
test = soup(webpage,'html.parser')
csv = open("teams.csv","w")

# print(test)

all_li = test.find_all('li')
# print(all_li)

# Extracting all the <a> tags into a list.
tags = test.find_all('a')
 
# # Extracting URLs from the attribute href in the <a> tags.
# for tag in tags:
#     output.write(tag.get('href=https://replay.pokemonshowdown.com/gen8vgc2020-'))
#     output.write('\n')

f = output.read()

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

    csv.write(', '.join(team1))
    csv.write('\n')
    csv.write(', '.join(team2))
    csv.write('\n')
    # print(team1)
    # print(team2)



webpage.close()
output.close()