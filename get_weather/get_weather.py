#This is a simple script that pulls weather from U.S. cities using urllib and BeuatifulSoup
#Author: Daniel Kuhman
#Contact: danielkuhman@gmail.com
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

city_input = input('Enter U.S. city:')
city_input = city_input.lower()

url = 'https://www.timeanddate.com/weather/usa/' + city_input
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

location = soup.find(class_ = 'pg-title__title').get_text()
temp = soup.find(class_ = 'h2').get_text()
descript = soup.find(class_ = 'mtt').get('title')
print('Showing',location)
print('Temperature:',temp)
print('Description:',descript)
