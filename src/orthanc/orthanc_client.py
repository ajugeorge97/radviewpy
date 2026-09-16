import requests
from src.orthanc.subjects import Subject

class OrthancClient:
    def __init__(self,session,url):
        self.session = session
        self.url = f"{url.rstrip('/')}/orthanc"
        
    @property
    def subjects(self):
        response = self.session.get(
            f"{self.url}/patients",
            params={"expand": "true"},
        )
        response.raise_for_status()

        return [
            Subject(self, data)
            for data in response.json()
        ]
        
    
    # def get_patients(self):
    #     response = self.session.get(
    #         f"{self.url}/patients",
    #         params={"expand": "true"}
    #     )
    #     response.raise_for_status()

    #     return response.json()

    # def get_studies(self):
    #     response = self.session.get(f"{self.url}/studies")
    #     response.raise_for_status()

    #     return response.json()
    # def delete_studies(self,series_id):
    #     response = self.session.delete(f"{self.url}/series/{series_id}")
    #     response.raise_for_status()

    #     return response
