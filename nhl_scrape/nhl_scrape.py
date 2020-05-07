import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
def create_soup(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page,"html.parser")
    return soup
soup = create_soup("http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2020/seasontype/2")

all_data = ""
for record in soup.select('tr[class != "colhead"]'):
    player_data = ""
    for data in record.findAll('td'):
        player_data = player_data + "," + data.text
    all_data = all_data + "\n" + player_data[1:]

headers = "Rank,Player,Team,GP,G,A,PTS,+/-,PIM,PTS/G,SOG,PCT,GWG,PPG,PPA,SHG,SHA"
file = open(os.path.expanduser('nhl_leaders.csv'),'wb')
file.write(bytes(headers, encoding='ascii', errors='ignore'))
file.write(bytes(all_data, encoding='ascii', errors='ignore'))
