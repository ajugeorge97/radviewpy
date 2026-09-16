import requests
from src.orthanc.orthanc_client import OrthancClient

class RadViewClient:
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
        self.orthanc = OrthancClient(session=self.session,url = self.url)

    def login(self, username, password):
        response = self.session.post(
            f"{self.url}/api/auth/login",
            json={
                "username": username,
                "password": password,
            },
        )
        response.raise_for_status()

        data = response.json()
        token = data["token"]

        self.session.headers.update({"Authorization": f"Bearer {token}"})
        
    def logout(self):
        response = self.session.post(
            f"{self.url}/api/auth/logout",
        )
        response.raise_for_status()
