import xml.etree.ElementTree as ET


class baseResponse:
    def __init__(self, response):
        self.response = response
        self.root = ET.fromstring(response.text)
        self.namespace = None

    def setNamespace(self, responseTag):
        for elem in self.root.iter():
            if responseTag in elem.tag:
                self.namespace = elem.tag.split("}")[0].lstrip("{")
                break

    def getQualifiedTag(self, desiredTag, namespace=None):
        if namespace == None:
            namespace = self.namespace
        return f"{{{namespace}}}{desiredTag}"
