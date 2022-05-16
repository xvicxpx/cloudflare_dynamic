import requests
from cloudflare.api import Endpoint


class Zone(Endpoint):
    def get_zones(self, **keywords):

        r = requests.get(
            f"{self.endpoint}/zones", 
            headers=self.headers, 
            params=keywords
        )
        return r.json()
