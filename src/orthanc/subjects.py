from orthanc.experiment import Experiment
from orthanc.base import OrthancBase

class Subject(OrthancBase):
    endpoint = "patients"
    def __init__(self, client, data):
        self.client = client
        self._data = data

    @property
    def id(self):
        return self.data["ID"]

    @property
    def patient_id(self):
        return self.data.get("MainDicomTags", {}).get("PatientID")

    @property
    def name(self):
        return self.data.get("MainDicomTags", {}).get("PatientName")

    @property
    def experiments(self):
        response = self.client.session.get(f"{self.client.url}/patients/{self.id}")
        response.raise_for_status()

        study_ids = response.json().get("Studies", [])

        return [Experiment(self.client, study_id) for study_id in study_ids]
