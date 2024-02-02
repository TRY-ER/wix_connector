from pydantic import BaseModel


class BaseUrl(BaseModel):
    url: str
    request_type: str = "GET"
    description: str = ""
    example: str = ""

    def get_url(self,param: str | None = None):
        try:
            return self.url.format(param) if param else self.url
        except Exception as e:
            print(f"Exception in formatting param: {param}") 



