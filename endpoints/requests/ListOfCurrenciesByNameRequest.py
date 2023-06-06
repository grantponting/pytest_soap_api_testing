from pytest_soap_api_testing.endpoints.BaseRequest import BaseRequest
from pytest_soap_api_testing.endpoints.responses.ListOfCurrenciesByNameResponse import (
    ListOfCurrenciesByNameResponse,
)
import requests


class ListOfCurrenciesByNameRequest(BaseRequest):
    def __init__(
        self,
        url="http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso",
        headers={"Content-Type": "text/xml; charset=utf-8"},
        body=None,
    ):
        super().__init__(url, headers, body)
        self.body = """<ListOfCurrenciesByName xmlns="http://www.oorsprong.org/websamples.countryinfo">
            </ListOfCurrenciesByName>"""
        self.build_body()

    def build_body(self):
        return super().build_body(self.body)

    def send_request(self) -> ListOfCurrenciesByNameResponse:
        response = requests.post(self.url, headers=self.headers, data=self.body)
        return ListOfCurrenciesByNameResponse(response)
