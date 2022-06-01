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
    zone_id = zone_results["result"][0]["id"]

    dns = DNS(zone_id)

    dns_first_result = dns.list_dns_records(name="fleetfarm.us", type="A")["result"][0]

    print(f"Current IP is: {get_ip()}")

    # Checks if needs to even update the DNS record
    if dns_first_result["content"] == get_ip():
        print("IP Address Does Not Need To Be Updated")
        return
    else:
        print(f'IP Address Updated From {dns_first_result["content"]} to {get_ip()}')

        dns_identifier = dns_first_result["id"]

        dns.update_dns_record(
            identifier=dns_identifier,
            type="A",
            name="fleetfarm.us",
            content=get_ip(),
            ttl=1,
            proxied=True,
        )

        print("Updating Completed")


if __name__ == "__main__":
    print("Updating DNS address")
    main()
