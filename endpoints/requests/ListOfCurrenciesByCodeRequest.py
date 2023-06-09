from pytest_soap_api_testing.endpoints.BaseRequest import BaseRequest
from pytest_soap_api_testing.endpoints.responses.ListOfCurrenciesByCodeResponse import (
    ListOfCurrenciesByCodeResponse,
)
import requests


class ListOfCurrenciesByCodeRequest(BaseRequest):
    def __init__(
        self,
        url="http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso",
        headers={"Content-Type": "text/xml; charset=utf-8"},
        body=None,
    ):
        super().__init__(url, headers, body)
        self.body = """<ListOfCurrenciesByCode xmlns="http://www.oorsprong.org/websamples.countryinfo">
            </ListOfCurrenciesByCode>"""
        self.build_body()

    def build_body(self):
        return super().build_body(self.body)

    def send_request(self) -> ListOfCurrenciesByCodeResponse:
        response = requests.post(self.url, headers=self.headers, data=self.body)
        return ListOfCurrenciesByCodeResponse(response)
