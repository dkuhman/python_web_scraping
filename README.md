# Web Scraping in Python
## python_web_scraping
This repository houses miscellaneous web scraping scripts written in Python. Brief descriptions of each script are listed below; navigate to
individual project folders to view each script.


## Scrape the current weather
### get_weather.py
**What it does:** This script runs from the command window. It prompts the user for a U.S. city name and returns the city's current temperature.
The script does not assume valid input. 

**Modules used:** urllib, BeautifulSoup

**What I learned:** This was my first web scraping script, so I learned a lot about BeautifulSoup (primarily by reading through its 
documentation). 

---

## Scrape daily weather details from each day of 2019 in a list of cities
### city_weather_scrape_2019.py

**What it does:** This script uses timeanddate.com to scrape weather information (high and low temperatures) from a list of cities
from four observations on each day of 2019. After the scrape, the script saves weather data to a .csv file in the same path as the script.

**Output data file:** city_weather_2019.csv 

**Modules used:** urllib, BeautifulSoup, selenium, os. 

**What I learned:** This was my first time using selenium. I incorporated selenium because the page was loading too slowly, causing bs4
to miss the divs needed for the scrape (likely due to slow javascript code). This was also my first time running conditional statements 
based on CSS attributes. 

**Bonus:** The repository contains an R script that will tidy the output data file and create a ridgeline plot grouped by city. See example figure below:

<img href='/alabama_weather/compare_weather.png' style='width:50%'>

---

## Scrape the NHL leaderboard
### nhl_scrape.py

**What it does:** This script scrapes NHL leaderboard data (player name, team, position, goals, assissts, points, etc.) from ESPN.com. 
 After the scrape, the script saves weather data to a .csv file in the same path as the script.

**Output data file:** nhl_leaders.csv 

**Modules used:** urllib, BeautifulSoup, os

**What I learned:** This was my first time scraping table contents from a web page. 

---
