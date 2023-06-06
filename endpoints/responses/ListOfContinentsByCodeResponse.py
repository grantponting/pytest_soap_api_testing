from pytest_soap_api_testing.endpoints.BaseResponse import BaseResponse


class ListOfContinentsByCodeResponse(BaseResponse):
    def __init__(self, response):
        super().__init__(response)
        self.set_namespace("ListOfContinentsByCodeResponse")

    def getAllContinents(self):
        return self.root.findall(".//" + self.get_qualified_tag("tContinent"))

    def getAllContinentNames(self):
        return self.root.findall(".//" + self.get_qualified_tag("sName"))

    def getAllContinentCodes(self):
        return self.root.findall(".//" + self.get_qualified_tag("sCode"))
