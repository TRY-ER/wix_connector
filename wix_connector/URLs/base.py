from pydantic import BaseModel
from typing import Optional


class BaseUrl(BaseModel):
    url: str
    request_type: str = "GET"
    description: str = ""
    example: str = ""

    def get_url(self,params: Optional[list] = None):
        try:
            print("formatted url >>", {self.url.format(*params)} if params else self.url)
            return self.url.format(*params) if params else self.url
        except Exception as e:
            print(f"Exception in formatting param: {params} , {e}") 



