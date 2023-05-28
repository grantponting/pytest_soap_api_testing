from pytest_soap_api_testing.endpoints.baseRequest import baseRequest
from pytest_soap_api_testing.endpoints.responses.ListOfCurrenciesByNameResponse import (
    ListOfCurrenciesByNameResponse,
)
import requests


class ListOfCurrenciesByNameRequest(baseRequest):
    def __init__(
        self,
        url="http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso",
        headers={"Content-Type": "text/xml; charset=utf-8"},
        body=None,
    ):
        super().__init__(url, headers, body)
        self.body = """<ListOfCurrenciesByName xmlns="http://www.oorsprong.org/websamples.countryinfo">
            </ListOfCurrenciesByName>"""
        self.buildBody()

    def buildBody(self):
        return super().buildBody(self.body)

    def sendRequest(self) -> ListOfCurrenciesByNameResponse:
        response = requests.post(self.url, headers=self.headers, data=self.body)
        return ListOfCurrenciesByNameResponse(response)
