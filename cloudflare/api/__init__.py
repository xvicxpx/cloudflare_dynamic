from cloudflare.api.constants import ENDPOINT_URL
import os


class Endpoint:
    def __init__(self) -> None:
        auth_token = os.getenv("AUTH_TOKEN")
        self.headers = {
            "Authorization": f"Bearer {auth_token}",
            "Content-Type": "application/json",
        }

        self.endpoint = ENDPOINT_URL
