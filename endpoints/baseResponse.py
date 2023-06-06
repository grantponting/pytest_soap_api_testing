import xml.etree.ElementTree as ET
import io as io
from lxml import etree


class BaseResponse:
    def __init__(self, response):
        self.response = response
        try:
            self.root = ET.fromstring(response.text)
        except ET.ParseError as e:
            raise ValueError(f"Invalid XML: {str(e)}")
        self.namespace = None
        self.dtd = None

    def setNamespace(self, responseTag):
        for elem in self.root.iter():
            if responseTag in elem.tag:
                self.namespace = elem.tag.split("}")[0].lstrip("{")
                break

    def getQualifiedTag(self, desiredTag, namespace=None):
        if namespace == None:
            namespace = self.namespace
        return f"{{{namespace}}}{desiredTag}"
    

    # def parse_from_unicode(unicode_str):
    #     s = unicode_str.encode('utf-8')
    #     return etree.fromstring(s, parser=utf8_parser)

    def verifyByDTD(self):
        utf8_parser = etree.XMLParser(encoding='utf-8')

        unicode_str = self.response.text
        s = unicode_str.encode('utf-8')
        print(s)
        tree = etree.fromstring(s, parser=utf8_parser)
        # Parse the DTD string
        try:
            dtd = etree.DTD(io.StringIO(self.dtd))
        except etree.DTDParseError as e:
            raise ValueError(f"Invalid DTD: {str(e)}")

        # Validate XML against DTD
        if not dtd.validate(tree):
            error_messages = [error.message for error in dtd.error_log]
            raise ValueError(f"DTD validation failed:\n{chr(10).join(error_messages)}")
        return True
