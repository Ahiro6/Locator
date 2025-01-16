from bs4 import BeautifulSoup
import re

with open("templates/partials/Map.html", "r") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

map_div = soup.find('div', class_='folium-map')
lat = float(map_div.get('data-lat', 0))
lng = float(map_div.get('data-lng', 0))
zoom = int(map_div.get('data-zoom', 10))

script = soup.find_all('script')[-1]

coords = re.findall(r'L\.circleMarker\(\s*\[([^]]+)\]', script.string)
names = re.findall(r'<div id="html_[a-f0-9]+"[^>]*>([^<]+)</div>', script.string)