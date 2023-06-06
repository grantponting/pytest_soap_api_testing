from pytest_soap_api_testing.endpoints.BaseResponse import BaseResponse


class ListOfCurrenciesByCodeResponse(BaseResponse):
    def __init__(self, response):
        super().__init__(response)
        self.set_namespace("ListOfCurrenciesByCodeResponse")

    def getAllCurrencies(self):
        return self.root.findall(".//" + self.get_qualified_tag("tCurrencies"))

    def getAllCurrencyNames(self):
        return self.root.findall(".//" + self.get_qualified_tag("sName"))

    def getAllCurrencyISOCodes(self):
        return self.root.findall(".//" + self.get_qualified_tag("sISOCode"))
