from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


class GeoCode:
    def __init__(self):
        self.locator = Nominatim(user_agent="test")
        self.geocode = RateLimiter(self.locator.geocode, min_delay_seconds = 1,   return_value_on_exception = None)
        self.location = None

    def locate(self, place):
        self.location = self.locator.geocode(place)
