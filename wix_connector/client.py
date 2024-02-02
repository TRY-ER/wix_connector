from pydantic import (BaseModel,
                     root_validator)
from abc import ABC, abstractmethod
import requests
from wix_connector.URLs.base import BaseUrl


class BaseClientResponse(BaseModel, ABC):
    status_code: int
    response: dict

class BaseClient(BaseModel, ABC): 
    authorization: str 
    content_type: str = "application/json"

    @abstractmethod
    def get(self, url: str, **kwargs) -> BaseClientResponse:
        pass

    @abstractmethod
    def post(self, url: str, data: dict, **kwargs) -> BaseClientResponse:
        pass

class DataClient(BaseClient):     
    wix_site_id: str

    @root_validator(pre=True)
    def form_header(cls, values):
        values["headers"] = {"Authorization": values["authorization"],
                             "Content-Type": values["content_type"],
                             "wix-site-id": values["wix_site_id"]}
        return values


    def get(self, url: BaseUrl, param: str | None = None):
        if url.request_type == "GET":
            response = requests.get(BaseUrl.get_url(param=param) if param else BaseUrl.get_url(), headers=self.headers)
            return BaseClientResponse(status_code=response.status_code, response=response.json())
        else:
            raise ValueError(f"Invalid request type for this method: {url.request_type}")

    def post(self, url: BaseUrl, data: dict, **kwargs):
        if url.request_type == "POST":
            response = requests.post(BaseUrl.get_url(), json=data, headers=self.headers)
            return BaseClientResponse(status_code=response.status_code, response=response.json())
        else:
            raise ValueError(f"Invalid request type for this method: {url.request_type}")

    def put(self, url: BaseUrl, data: dict, param: str | None = None):
        if url.request_type == "PUT": 
            response = requests.put(BaseUrl.get_url(param=param) if param else BaseUrl.get_url(), headers=self.headers) 
            return BaseClientResponse(status_code=response.status_code, response=response.json())
        else:
            raise ValueError(f"Invalid request type for this method: {url.request_type}")

    def delete(self, url: BaseUrl, data: dict, param: str | None = None):
        if url.request_type == "DELETE": 
            response = requests.delete(BaseUrl.get_url(param=param) if param else BaseUrl.get_url(),headers=self.headers) 
            return BaseClientResponse(status_code=response.status_code, response=response.json())
        else:
            raise ValueError(f"Invalid request type for this method: {url.request_type}")




class AccountClient(BaseClient):
    wix_account_id: str

    @root_validator(pre=True)
    def form_header(cls, values):
        values["headers"] = {"Authorization": values["authorization"],
                             "Content-Type": values["content_type"],
                             "wix-account-id": values["wix_account_id"]}
        return values

    def get(self, url: str, **kwargs):
        pass

    def post(self, url: str, data: dict, **kwargs):
        pass