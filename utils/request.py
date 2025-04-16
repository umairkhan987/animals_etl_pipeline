import requests
from tenacity import retry, stop_after_attempt, wait_exponential, \
    retry_if_exception_type, RetryError


class RequestClient:

    def __init__(self):
        self.exceptions_code = (500, 502, 503, 504)

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type(requests.exceptions.RequestException)
    )
    def _get(self, url: str, params: dict):
        response = requests.get(url, params=params)
        if response.status_code in self.exceptions_code:
            raise requests.exceptions.HTTPError(f"Retrying due to {response.status_code}")
        return self._parse_response(response)

    def _post(self, url: str, body):
        response = requests.post(url, json=body)
        if response.status_code in self.exceptions_code:
            raise requests.exceptions.HTTPError(f"Retrying due to {response.status_code}")
        return self._parse_response(response)

    def get(self, url: str, params: dict):
        try:
            return self._get(url, params)
        except RetryError as e:
            print(f"Request failed after retries: {e}")
        except Exception as e:
            print(f"Error: {e}")
            return {}

    def post(self, url: str, body):
        try:
            return self._post(url, body)
        except RetryError as e:
            print(f"Request failed after retries: {e}")
        except Exception as e:
            print(f"Error: {e}")
        return {}

    def _parse_response(self, response):
        status_code = response.status_code
        if status_code in (200, 201):
            return response.json()
        if status_code not in self.exceptions_code:
            raise Exception(f"Unexpected status code: {status_code}")
