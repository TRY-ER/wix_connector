from pydantic import (BaseModel,
                     root_validator)
from abc import ABC, abstractmethod
from wix_connector.client import DataClient
from wix_connector.URLs.data.collections import (InsertDataUrl,
                                                 UpdateDataUrl,
                                                 SaveDataUrl,
                                                 GetDataUrl,
                                                 RemoveDataUrl,
                                                 QueryDataUrl)

class BaseDataHandler(BaseModel, ABC):
    client: DataClient 

    def insert_data(self, data:dict):
        url = InsertDataUrl
        response = self.client.post(url=url,
                         data=data)
        return response

    def update_data(self, data:dict, id: str):
        url = UpdateDataUrl
        response = self.client.put(url=url,
                         data=data,
                         params=[id])
        return response
    
    def save_data(self, data:dict):
        "this inserts if data doesn't exist if it exists if updates it"
        url = SaveDataUrl
        response = self.client.post(url=url,
                                    data=data)
        return response 

    def get_data(self, table_name: str, id: str):
        url = GetDataUrl
        response = self.client.get(url=url,
                                   params=[id,table_name])
        return response

    def remove_data(self, table_name: str, id: str):
        url = RemoveDataUrl
        response = self.client.delete(url=url,
                                      params=[id, table_name])
        return response 

    def query_data(self, query_dict: dict):
        url = QueryDataUrl
        response = self.client.post(url=url,
                                    data=query_dict)
        return response 

    