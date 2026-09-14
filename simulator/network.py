import os
import socket
import requests
from dotenv import load_dotenv


load_dotenv()


class ArcadeNetwork:

    def __init__(
        self,
        arcade_id="ARCADE-003",
        arcade_name="Main Arcade",
        software_version="0.1.0"
    ):
        self.server_url = os.getenv(
            "ARCADE_SERVER_URL",
            "https://api.sidebit.si"
        )

        self.api_key = os.getenv(
            "ARCADE_API_KEY",
            "0e02d5c201acb50c10e13a7736de1fd1cb27eff0bfe8847592a3f1a1a4c5779c"
        )

        self.arcade_id = arcade_id
        self.arcade_name = arcade_name
        self.software_version = software_version

    def get_local_ip(self):

        try:
            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_DGRAM
            )

            sock.connect(
                ("8.8.8.8", 80)
            )

            ip = sock.getsockname()[0]

            sock.close()

            return ip

        except Exception:
            return "127.0.0.1"

    def get_headers(self):

        return {
            "Content-Type": "application/json",
            "X-API-Key": self.api_key
        }

    def check_server(self):

        try:

            response = requests.get(
                f"{self.server_url}/api/arcades",
                headers=self.get_headers(),
                timeout=5
            )

            if response.status_code == 200:
                print("Server connection: OK")
                return True

            print(
                "Server returned:",
                response.status_code
            )

            return False

        except requests.RequestException as error:

            print(
                f"Server connection failed: {error}"
            )

            return False

    def register_arcade(self):

        data = {
            "arcade_id": self.arcade_id,
            "name": self.arcade_name,
            "software_version": self.software_version,
            "local_ip": self.get_local_ip()
        }

        try:

            print("HEARTBEAT URL:", f"{self.server_url}/api/arcades/heartbeat")

            response = requests.post(
                f"{self.server_url}/api/arcades/register",
                json=data,
                headers=self.get_headers(),
                timeout=5
            )

            if response.status_code in (200, 201):

                print(
                    "Arcade registered successfully."
                )

                return True

            print(
                "Registration failed:",
                response.status_code
            )

            print(response.text)

            return False

        except requests.RequestException as error:

            print(
                f"Registration error: {error}"
            )

            return False

    def send_heartbeat(
        self,
        temperature=45.0,
        cpu_usage=20,
        players=0,
        game=None
    ):

        data = {
            "arcade_id": self.arcade_id,
            "name": self.arcade_name,
            "software_version": self.software_version,
            "local_ip": self.get_local_ip(),

            "temperature": temperature,
            "cpu_usage": cpu_usage,
            "players": players,
            "game": game
        }

        try:

            response = requests.post(
                f"{self.server_url}/api/arcades/heartbeat",
                json=data,
                headers=self.get_headers(),
                timeout=5
            )

            if response.status_code in (200, 201):

                print(
                    f"State sent to server: {self.arcade_id}"
                )

                return True

            print(
                "Heartbeat failed:",
                response.status_code
            )

            print(response.text)

            return False

        except requests.RequestException as error:

            print(
                f"Heartbeat error: {error}"
            )

            return False

    def get_arcades(self):

        try:

            response = requests.get(
                f"{self.server_url}/api/arcades",
                headers=self.get_headers(),
                timeout=5
            )

            if response.status_code == 200:
                return response.json()

            print(
                "Failed to get arcades:",
                response.status_code
            )

            return []

        except requests.RequestException as error:

            print(
                f"Network error: {error}"
            )

            return []


if __name__ == "__main__":

    network = ArcadeNetwork()

    print("--------------------------------")
    print("ARCADE NETWORK CONNECTOR")
    print("--------------------------------")

    print("ID:", network.arcade_id)
    print("Name:", network.arcade_name)
    print("Version:", network.software_version)
    print("IP:", network.get_local_ip())
    print("Server:", network.server_url)

    print("--------------------------------")

    if network.check_server():

        network.register_arcade()

        arcades = network.get_arcades()

        print("Registered arcades:")

        for arcade in arcades:

            print(
                arcade.get("arcade_id"),
                arcade.get("name"),
                arcade.get("local_ip")
            )