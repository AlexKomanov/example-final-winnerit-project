from typing import Dict, Optional
from .base_request import BaseRequest


class UsersRequest(BaseRequest):
    def __init__(self):
        super().__init__("api/users")

    def list_users(self, page: Optional[int] = None) -> Dict:
        params = {"page": page} if page else None
        response = self.get(params=params)
        return response

    def create_user(self, name: str, job: str) -> Dict:
        payload = {
            "name": name,
            "job": job
        }
        response = self.post(payload=payload)
        return response 