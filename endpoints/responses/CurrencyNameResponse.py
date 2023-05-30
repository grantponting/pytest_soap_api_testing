from pytest_soap_api_testing.endpoints.baseResponse import baseResponse


class CurrencyNameResponse(baseResponse):
    def __init__(self, response):
        super().__init__(response)
        self.setNamespace("CurrencyNameResponse")

    def getResponseString(self):
        return self.root.find(".//" + self.getQualifiedTag("CurrencyNameResult"))
