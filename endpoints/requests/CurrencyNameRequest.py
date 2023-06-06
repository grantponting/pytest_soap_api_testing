from pytest_soap_api_testing.endpoints.BaseRequest import BaseRequest
from pytest_soap_api_testing.endpoints.responses.CurrencyNameResponse import (
    CurrencyNameResponse,
)
import requests


class CurrencyNameRequest(BaseRequest):
    def __init__(
        self,
        currencyCode,
        url="http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso",
        headers={"Content-Type": "text/xml; charset=utf-8"},
        body=None,
    ):
        super().__init__(url, headers, body)
        self.body = """<CurrencyName xmlns="http://www.oorsprong.org/websamples.countryinfo">
                <sCurrencyISOCode>{code}</sCurrencyISOCode>
            </CurrencyName>""".format(
            code=currencyCode
        )
        self.build_body()

    def build_body(self):
        return super().build_body(self.body)

    def send_request(self) -> CurrencyNameResponse:
        response = requests.post(self.url, headers=self.headers, data=self.body)
        return CurrencyNameResponse(response)
