from pytest_soap_api_testing.endpoints.baseResponse import baseResponse


class ListOfContinentsByCodeResponse(baseResponse):
    def __init__(self, response):
        super().__init__(response)
        self.setNamespace("ListOfContinentsByCodeResponse")

    def getAllContinents(self):
        return self.root.findall(".//" + self.getQualifiedTag("tContinent"))

    def getAllContinentNames(self):
        return self.root.findall(".//" + self.getQualifiedTag("sName"))

    def getAllContinentCodes(self):
        return self.root.findall(".//" + self.getQualifiedTag("sCode"))
