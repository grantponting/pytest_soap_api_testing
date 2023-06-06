from pytest_soap_api_testing.endpoints.BaseRequest import BaseRequest
from pytest_soap_api_testing.endpoints.responses.ListOfContinentsByCodeResponse import (
    ListOfContinentsByCodeResponse,
)
import requests


class ListOfContinentsByCodeRequest(BaseRequest):
    def __init__(
        self,
        url="http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso",
        headers={"Content-Type": "text/xml; charset=utf-8"},
        body=None,
    ):
        super().__init__(url, headers, body)
        self.body = """<ListOfContinentsByCode xmlns="http://www.oorsprong.org/websamples.countryinfo">
            </ListOfContinentsByCode>"""
        self.buildBody()

    def buildBody(self):
        return super().buildBody(self.body)

    def sendRequest(self) -> ListOfContinentsByCodeResponse:
        response = requests.post(self.url, headers=self.headers, data=self.body)
        return ListOfContinentsByCodeResponse(response)
