import folium
from geocode import GeoCode

class Mapping:

    def __init__(self):
        
        self.maps = folium.Map(location=[-26.2041, 28.0473], zoom_start=6, tiles="Stamen Terrain", min_zoom=2.5)
        self.lg = folium.FeatureGroup(name="Coordinates")
        self.maps.add_child(self.lg)

    def createMarker(self, loc, name):
        self.lg.add_child(folium.CircleMarker(location=(loc.location.latitude, loc.location.longitude), radius=10, fill_opacity=0.8, fill_color="red", color="blue", popup=name))
        
        self.maps.save("templates/partials/Map.html")
