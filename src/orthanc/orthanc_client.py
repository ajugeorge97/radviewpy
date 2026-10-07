from pathlib import Path

from orthanc.subjects import Subject

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

    def upload_file(self, file_path):
        path = Path(file_path)
        if not path.is_file():
            raise FileNotFoundError(f"Upload file does not exist: {path}")

        with path.open("rb") as dicom_file:
            response = self.session.post(
                f"{self.url}/instances",
                data=dicom_file,
                headers={"Content-Type": "application/dicom"},
            )
        response.raise_for_status()
        return response.json()

    def upload_dir(self, directory_path, recursive=True):
        path = Path(directory_path)
        if not path.exists():
            raise FileNotFoundError(f"Upload directory does not exist: {path}")
        if not path.is_dir():
            raise NotADirectoryError(f"Upload path is not a directory: {path}")

        files = path.rglob("*") if recursive else path.glob("*")
        results = []
        for file_path in sorted(files):
            if file_path.is_file():
                results.append({
                    "file": str(file_path),
                    "response": self.upload_file(file_path),
                })

        return results
