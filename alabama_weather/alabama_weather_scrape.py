import urllib
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import os

#Define parser function
def create_soup(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    return soup

#Create a selenium driver; chrome_options --headless suppresses the script from actually opening the URL
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome('C:/Users/danielkuhman/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/selenium/'
                          'webdriver/chrome/chromedriver.exe', chrome_options=options)

city_list = ['birmingham', 'cleveland']

# Object to collect data from each day
day_data = ''

for city in city_list:
    #Create list of URLS
    url_list = ['https://www.timeanddate.com/weather/usa/' + city + '/historic?month=1&year=2019',
                'https://www.timeanddate.com/weather/usa/' + city + '/historic?month=2&year=2019',
                'https://www.timeanddate.com/weather/usa/' + city + '/historic?month=3&year=2019',
                'https://www.timeanddate.com/weather/usa/' + city + '/historic?month=4&year=2019',
                'https://www.timeanddate.com/weather/usa/' + city + '/historic?month=5&year=2019',
                'https://www.timeanddate.com/weather/usa/' + city + '/historic?month=6&year=2019',
                'https://www.timeanddate.com/weather/usa/' + city + '/historic?month=7&year=2019',
                'https://www.timeanddate.com/weather/usa/' + city + '/historic?month=8&year=2019',
                'https://www.timeanddate.com/weather/usa/' + city + '/historic?month=9&year=2019',
                'https://www.timeanddate.com/weather/usa/' + city + '/historic?month=10&year=2019',
                'https://www.timeanddate.com/weather/usa/' + city + '/historic?month=11&year=2019',
                'https://www.timeanddate.com/weather/usa/' + city + '/historic?month=12&year=2019',]

    for list in url_list:
        driver.get(list)
        page_html = driver.page_source
        soup = BeautifulSoup(page_html, 'lxml')
        #Find the divs in div[id^='ws_'] where ^= represents 'starts with'
        for observation in soup.select('div[id^="ws_"]'):
            for metric in observation.select('div[class!="wicon"]'):
                if metric['class'][0]=='date':
                    day_data = day_data + '\n' + city + ',' + metric.text
                elif metric['class'][0] == 'time':
                    day_data = day_data + ',' + metric.text.replace(' ','')
                elif metric['class'][0] == 'tempLow':
                    day_data = day_data  + ',' + metric.text[3:5]
                elif metric['class'][0] == 'temp':
                    if metric.text == 'N/A':
                        day_data = day_data + ',' + 'NA'
                    else:
                        day_data = day_data  + ',' + metric.text[3:5]
                else:
                    day_data = day_data + ',' + 'NA'

        print(day_data)

headers = 'city,week_day,date,temp_low1,time1,temp_high1,NA1,NA2,' \
          'temp_low2,time2,temp_high2,NA3,NA4,' \
          'temp_low3,time3,temp_high3,NA5,NA6,' \
          'temp_low4,time4,temp_high4,NA7,NA8'
file = open(os.path.expanduser('city_weather_2019.csv'),'wb')
file.write(bytes(headers, encoding='ascii', errors='ignore'))
file.write(bytes(day_data, encoding='ascii', errors='ignore'))