# Parses html file to find list of replays, then parses list of replays to create
# a csv of teams

from bs4 import BeautifulSoup as soup
import requests

# webpage = open("replays_by_date.html",'r')
webpage = open("replays_by_date.html",'r')
output = open("replays.txt","r")
test = soup(webpage,'html.parser')

# print(test)

all_li = test.find_all('li')
# print(all_li)

# Extracting all the <a> tags into a list.
tags = test.find_all('a')
 
# # Extracting URLs from the attribute href in the <a> tags.
# for tag in tags:
#     output.write(tag.get('href'))
#     output.write('\n')

f = output.read()

# Extract teams from each replay url
for replay in f.splitlines():
    r = requests.get(replay)
    suup = soup(r.content,'html.parser')
    #div="class name"
    tags2 = suup.get_text()
    print(tags2)
print('megapoop')
# div class="battle-log"
# div class="inner message-log"
# div class="chat battle-history"
# <em style="color:#445566;display:block"> ... </em>


webpage.close()
output.close()