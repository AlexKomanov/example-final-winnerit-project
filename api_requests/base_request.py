import requests
import allure
from typing import Optional, Dict


class BaseRequest:
    BASE_URL = "https://reqres.in"  # Replace with actual base URL

    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def get(self, params: Optional[Dict] = None, headers: Optional[Dict] = None) -> requests.Response:
        with allure.step(f"Performing GET request to {self.endpoint} with params={params} and headers={headers}"):
            url = f"{self.BASE_URL}/{self.endpoint}".rstrip('/')
            response = requests.get(url, params=params, headers=headers)
            allure.attach(url, 'Request URL', allure.attachment_type.TEXT)
            if params:
                allure.attach(str(params), 'Query Parameters', allure.attachment_type.TEXT)
            if headers:
                allure.attach(str(headers), 'Request Headers', allure.attachment_type.TEXT)
            return response

    def post(self, payload: Optional[Dict] = None, headers: Optional[Dict] = None) -> requests.Response:
        with allure.step(f"Performing POST request to {self.endpoint} with payload={payload} and headers={headers}"):
            url = f"{self.BASE_URL}/{self.endpoint}".rstrip('/')
            response = requests.post(url, json=payload, headers=headers)
            allure.attach(url, 'Request URL', allure.attachment_type.TEXT)
            if payload:
                allure.attach(str(payload), 'Request Payload', allure.attachment_type.TEXT)
            if headers:
                allure.attach(str(headers), 'Request Headers', allure.attachment_type.TEXT)
            return response

    def put(self, payload: Optional[Dict] = None, headers: Optional[Dict] = None) -> requests.Response:
        with allure.step(f"Performing PUT request to {self.endpoint} with payload={payload} and headers={headers}"):
            url = f"{self.BASE_URL}/{self.endpoint}".rstrip('/')
            response = requests.put(url, json=payload, headers=headers)
            allure.attach(url, 'Request URL', allure.attachment_type.TEXT)
            if payload:
                allure.attach(str(payload), 'Request Payload', allure.attachment_type.TEXT)
            if headers:
                allure.attach(str(headers), 'Request Headers', allure.attachment_type.TEXT)
            return response

    def delete(self, headers: Optional[Dict] = None) -> requests.Response:
        with allure.step(f"Performing DELETE request to {self.endpoint} with headers={headers}"):
            url = f"{self.BASE_URL}/{self.endpoint}".rstrip('/')
            response = requests.delete(url, headers=headers)
            allure.attach(url, 'Request URL', allure.attachment_type.TEXT)
            if headers:
                allure.attach(str(headers), 'Request Headers', allure.attachment_type.TEXT)
            return response
