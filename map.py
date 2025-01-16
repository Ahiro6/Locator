import folium
from pathlib import Path
from geocode import GeoCode
from bs4 import BeautifulSoup
import re

class Mapping:

    def __init__(self):
        
        self.maps = folium.Map(location=[-26.2041, 28.0473], zoom_start=6, min_zoom=2.5)
        self.lg = folium.FeatureGroup(name="Coordinates")
        self.maps.add_child(self.lg)            
        
        if Path("templates/partials/Map.html").is_file():
            with open("templates/partials/Map.html", "r") as f:
                html_content = f.read()

            soup = BeautifulSoup(html_content, 'html.parser')
            
            script = soup.find_all('script')[-1]

            coords = re.findall(r'L\.circleMarker\(\s*\[([^]]+)\]', script.string)
            names = re.findall(r'<div id="html_[a-f0-9]+"[^>]*>([^<]+)</div>', script.string)

            for i in range(len(coords)):
                lat, lng = map(float, coords[i].split(','))
                cm = folium.CircleMarker(location=(lat, lng), radius=10, fill_opacity=0.8, fill_color="red", color="blue", popup=names[i])
                self.lg.add_child(cm)

        self.maps.save("templates/partials/Map.html")


    def createMarker(self, loc, name):
        self.lg.add_child(folium.CircleMarker(location=(loc.location.latitude, loc.location.longitude), radius=10, fill_opacity=0.8, fill_color="red", color="blue", popup=name))
        
        self.maps.save("templates/partials/Map.html")
