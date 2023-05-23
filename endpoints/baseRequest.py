class baseRequest:
    def __init__(
        self,
        url="http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso",
        headers={"Content-Type": "text/xml; charset=utf-8"},
        body=None,
    ):
        self.url = url
        self.headers = headers
        self.body = body

    def buildBody(self, xml_request):
        xml_soap_wrapper = """<?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            {request}
        </soap:Body>
        </soap:Envelope>""".format(
            request=xml_request
        )
        self.body = xml_soap_wrapper

    def sendRequest(self):
        return
