class OrthancBase:
    endpoint = None

    def __init__(self, client, resource_id):
        self.client = client
        self.id = resource_id
        self._data = None

    @property
    def data(self):
        if self._data is None:
            response = self.client.session.get(
                f"{self.client.url}/{self.endpoint}/{self.id}"
            )
            response.raise_for_status()
            self._data = response.json()

        return self._data

    def delete(self):
        response = self.client.session.delete(
            f"{self.client.url}/{self.endpoint}/{self.id}"
        )
        response.raise_for_status()
        return True
