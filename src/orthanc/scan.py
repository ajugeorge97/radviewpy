from src.orthanc.base import OrthancBase

class Scan(OrthancBase):
    endpoint = "series"
    def __init__(self, client, scan_id):
        self.client = client
        self.id = scan_id
        self._data = None

    @property
    def data(self):
        if self._data is None:
            response = self.client.session.get(f"{self.client.url}/series/{self.id}")
            response.raise_for_status()
            self._data = response.json()

        return self._data

    @property
    def description(self):
        return self.data.get("MainDicomTags", {}).get("SeriesDescription")

    @property
    def modality(self):
        return self.data.get("MainDicomTags", {}).get("Modality")

    def delete(self):
        response = self.client.session.delete(f"{self.client.url}/series/{self.id}")
        response.raise_for_status()

        return True
