from src.orthanc.scan import Scan
from src.orthanc.base import OrthancBase

class Experiment(OrthancBase):
    endpoint = "studies"
    
    def __init__(self, client, experiment_id):
        self.client = client
        self.id = experiment_id
        self._data = None

    @property
    def data(self):
        if self._data is None:
            response = self.client.session.get(f"{self.client.url}/studies/{self.id}")
            response.raise_for_status()
            self._data = response.json()

        return self._data

    @property
    def description(self):
        return self.data.get("MainDicomTags", {}).get("StudyDescription")

    @property
    def scans(self):
        series_ids = self.data.get("Series", [])

        return [Scan(self.client, series_id) for series_id in series_ids]
