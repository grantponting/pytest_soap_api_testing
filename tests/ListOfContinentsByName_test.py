from ..endpoints.requests.ListOfContinentsByNameRequest import ListOfContinentsByNameRequest
import xml.etree.ElementTree as ET
import pytest

def test_list_of_continents_by_name():
    response = ListOfContinentsByNameRequest().sendRequest()
    
    # Iterate over the root element's children
    for continent in response.getAllContinents():
        name_element = continent.find(response.getQualifiedTag('sName'))
        code_element = continent.find(response.getQualifiedTag('sCode'))
        print("Continent name:", name_element.text)
        print("Continent Code: " + code_element.text)
