from config import BASE_URL
from utils.request import RequestClient


class AnimalLoader:
    def __init__(self):
        self.batch_size = 100
        self.request_client = RequestClient()

    def load_batches(self, animals):
        url = f"{BASE_URL}/home"
        for i in range(0, len(animals), self.batch_size):
            batch = animals[i:i + self.batch_size]
            _ = self.request_client.post(url, batch)
