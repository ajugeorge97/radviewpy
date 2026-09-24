### Example Usage

example usage to delete all scans from the radview orthac contains scan-1 and scan-2

```python
from src.radviewclient import RadViewClient

if __name__ == "__main__":
    client = RadViewClient("radview-url")
    client.login("username", "password")
    print("Logged in successfully!")

    subjects = client.orthanc.subjects 

    for subject in subjects:
        print(f"subject id {subject.patient_id}")

        for experiment in subject.experiments:
            print(f"  Experiment: {experiment.description}")

            for scan in experiment.scans:
                print(f"    Scan: {scan.description}")
                if scan.description in ["scan-1","scan-2"]:
                    scan.delete()

    client.logout()

```
