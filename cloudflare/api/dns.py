from cloudflare.api import Endpoint
import requests


class DNS(Endpoint):
    def __init__(self, zone_id) -> None:
        super().__init__()
        self.zone_id = zone_id

    def list_dns_records(self, **keywords):
        url = f"{self.endpoint}/zones/{self.zone_id}/dns_records"

        r = requests.get(url, params=keywords, headers=self.headers)
        return r.json()

    def update_dns_record(self, identifier, type, name, content, ttl=1, proxied=False):
        r = requests.put(
            url=f"{self.endpoint}/zones/{self.zone_id}/dns_records/{identifier}",
            headers=self.headers,
            json={
                "type": type,
                "name": name,
                "content": content,
                "ttl": ttl,
                "proxied": proxied,
            },
        )

        if r.json()["success"]:
            return True
        else:
            raise Exception(r.json())
