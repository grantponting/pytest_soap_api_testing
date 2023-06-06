from pytest_soap_api_testing.endpoints.BaseResponse import BaseResponse


class ListOfCurrenciesByNameResponse(BaseResponse):
    def __init__(self, response):
        super().__init__(response)
        self.setNamespace("ListOfCurrenciesByNameResponse")

    def getAllCurrencies(self):
        return self.root.findall(".//" + self.getQualifiedTag("tCurrencies"))

    def getAllCurrencyNames(self):
        return self.root.findall(".//" + self.getQualifiedTag("sName"))

    def getAllCurrencyISOCodes(self):
        return self.root.findall(".//" + self.getQualifiedTag("sISOCode"))
