from src.orthanc.base import OrthancBase

class Scan(OrthancBase):
    endpoint = "series"
    def __init__(self, client, scan_id):
        self.client = client
        self.id = scan_id
        self._data = None

    @property
    def description(self):
        return self.data.get("MainDicomTags", {}).get("SeriesDescription")

    @property
    def modality(self):
        return self.data.get("MainDicomTags", {}).get("Modality")
