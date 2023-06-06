from pytest_soap_api_testing.endpoints.BaseRequest import BaseRequest
from pytest_soap_api_testing.endpoints.responses.ListOfContinentsByNameResponse import (
    ListOfContinentsByNameResponse,
)
import requests


class ListOfContinentsByNameRequest(BaseRequest):
    def __init__(
        self,
        url="http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso",
        headers={"Content-Type": "text/xml; charset=utf-8"},
        body=None,
    ):
        super().__init__(url, headers, body)
        self.body = """<ListOfContinentsByName xmlns="http://www.oorsprong.org/websamples.countryinfo">
            </ListOfContinentsByName>"""
        self.build_body()

    def build_body(self):
        return super().build_body(self.body)

    def send_request(self) -> ListOfContinentsByNameResponse:
        response = requests.post(self.url, headers=self.headers, data=self.body)
        return ListOfContinentsByNameResponse(response)
