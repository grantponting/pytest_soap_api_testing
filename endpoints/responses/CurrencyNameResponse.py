from pytest_soap_api_testing.endpoints.BaseResponse import BaseResponse


class CurrencyNameResponse(BaseResponse):
    def __init__(self, response):
        super().__init__(response)
        self.setNamespace("CurrencyNameResponse")
        self.dtd = """<!ELEMENT Envelope (soap:Body)>
        <!ELEMENT Body (m:CurrencyNameResponse)>
        <!ELEMENT CurrencyNameResponse (m:CurrencyNameResult)>
        <!ELEMENT CurrencyNameResult (#PCDATA)>

        <!ATTLIST Envelope xmlns:soap CDATA #IMPLIED>
        <!ATTLIST CurrencyNameResponse xmlns:m CDATA #IMPLIED>
        """

    def getResponseString(self):
        return self.root.find(".//" + self.getQualifiedTag("CurrencyNameResult"))
