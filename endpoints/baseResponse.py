import xml.etree.ElementTree as ET
import io as io
from lxml import etree

class BaseResponse:
    """
    Base class for which all Responses will inherit
    """
    def __init__(self, response):
        self.response = response
        try:
            self.root = ET.fromstring(response.text)
        except ET.ParseError as parse_error:
            raise ValueError from parse_error
        self.namespace = None
        self.dtd = None

    def set_namespace(self, response_tag: str):
        """
        Sets the Namespace to use for each response
        """
        for elem in self.root.iter():
            if response_tag in elem.tag:
                self.namespace = elem.tag.split("}")[0].lstrip("{")
                break

    def get_qualified_tag(self, desired_tag: str, namespace: str =None):
        """
        Returns a qualified tag for the given tag string using the set 
            namespace for the response class
        """
        if namespace is None:
            namespace = self.namespace
        return f"{{{namespace}}}{desired_tag}"

    def verify_by_dtd(self):
        """
        Verifies the XML response by the self.dtd string for this response
        """
        utf8_parser = etree.XMLParser(encoding='utf-8')

        unicode_str = self.response.text
        s = unicode_str.encode('utf-8')
        print(s)
        tree = etree.fromstring(s, parser=utf8_parser)

        # Parse the DTD string
        try:
            dtd = etree.DTD(io.StringIO(self.dtd))
        except etree.DTDParseError as parse_error:
            raise ValueError from parse_error

        # Validate XML against DTD
        if not dtd.validate(tree):
            error_messages = [error.message for error in dtd.error_log]
            raise ValueError(f"DTD validation failed:\n{chr(10).join(error_messages)}")
        return True
