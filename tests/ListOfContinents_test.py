from ..endpoints.requests.ListOfContinentsByNameRequest import (
    ListOfContinentsByNameRequest,
)
from ..endpoints.requests.ListOfContinentsByCodeRequest import (
    ListOfContinentsByCodeRequest,
)
import xml.etree.ElementTree as ET
import pytest


def test_list_of_continents_by_name():
    response = ListOfContinentsByNameRequest().send_request()

    continent_names = []
    for continent in response.getAllContinents():
        name_element = continent.find(response.get_qualified_tag("sName"))
        continent_names.append(name_element.text)

    assert sorted(continent_names) == continent_names


def test_list_of_continents_by_code():
    response = ListOfContinentsByCodeRequest().send_request()

    continent_codes = []
    for continent in response.getAllContinents():
        code_element = continent.find(response.get_qualified_tag("sCode"))
        continent_codes.append(code_element.text)

    assert sorted(continent_codes) == continent_codes
