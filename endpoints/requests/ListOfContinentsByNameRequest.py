from pytest_soap_api_testing.endpoints.baseRequest import baseRequest
from pytest_soap_api_testing.endpoints.responses.ListOfContinentsByNameResponse import (
    ListOfContinentsByNameResponse,
)
import requests


class ListOfContinentsByNameRequest(baseRequest):
    def __init__(
        self,
        url="http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso",
        headers={"Content-Type": "text/xml; charset=utf-8"},
        body=None,
    ):
        super().__init__(url, headers, body)
        self.body = """<ListOfContinentsByName xmlns="http://www.oorsprong.org/websamples.countryinfo">
            </ListOfContinentsByName>"""
        self.buildBody()

    def buildBody(self):
        return super().buildBody(self.body)

    def sendRequest(self) -> ListOfContinentsByNameResponse:
        response = requests.post(self.url, headers=self.headers, data=self.body)
        return ListOfContinentsByNameResponse(response)
