# Entry Point
from cloudflare.api.zone import Zone
from cloudflare.api.dns import DNS
import requests


def get_ip():
    r = requests.get("http://ifconfig.me")
    return r.text


def main():
    zone = Zone()
    zone_results = zone.get_zones(name="fleetfarm.us")
    zone_id = zone_results["r\esult"][0]["id"]

    dns = DNS(zone_id)

    dns_first_result = dns.list_dns_records(name="fleetfarm.us", type="A")["result"][0]

    # Checks if needs to even update the DNS record
    if dns_first_result["content"] == get_ip():
        return
    else:
        dns_identifier = dns_first_result["id"]

        dns.update_dns_record(
            identifier=dns_identifier,
            type="A",
            name="fleetfarm.us",
            content=get_ip(),
            ttl=1,
            proxied=True,
        )


if __name__ == "__main__":
    main()
