from bs4 import BeautifulSoup
import requests

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.XpbpTPhKhPY')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id="seven-day-forecast-body")

items = week.find_all(class_="tombstone-container")

for item in items:
    print(item.get_text())
