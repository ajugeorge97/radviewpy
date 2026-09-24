# radviewpy

Python client helpers for RadView and its Orthanc API.

## Installation

Install the project from this checkout:

```bash
pip install .
```

For development, install it in editable mode:

```bash
pip install -e .
```

## Example Usage

Example usage to delete all scans from the RadView Orthanc instance that contain
`scan-1` or `scan-2`:

```python
from radviewclient import RadViewClient

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
