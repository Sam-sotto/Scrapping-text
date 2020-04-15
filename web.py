from bs4 import BeautifulSoup
import requests

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.XpbpTPhKhPY')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id="seven-day-forecast-body")

#week2 = week.find_all(class_="tombstone-container")
items = week.find_all(class_="tombstone-container")

print(items[0].find(class_="period-name").get_text())


for item in items:
    print(item.get_text())