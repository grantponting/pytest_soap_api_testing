from pytest_soap_api_testing.endpoints.BaseResponse import BaseResponse


class ListOfContinentsByNameResponse(BaseResponse):
    def __init__(self, response):
        super().__init__(response)
        self.set_namespace("ListOfContinentsByNameResponse")

    def getAllContinents(self):
        return self.root.findall(".//" + self.get_qualified_tag("tContinent"))

    def getAllContinentNames(self):
        return self.root.findall(".//" + self.get_qualified_tag("sName"))

    def getAllContinentCodes(self):
        return self.root.findall(".//" + self.get_qualified_tag("sCode"))
