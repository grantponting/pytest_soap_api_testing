from ..endpoints.requests.ListOfCurrenciesByNameRequest import (
    ListOfCurrenciesByNameRequest,
)
from ..endpoints.requests.ListOfCurrenciesByCodeRequest import (
    ListOfCurrenciesByCodeRequest,
)
import xml.etree.ElementTree as ET
import pytest


def test_list_of_currencies_by_name():
    response = ListOfCurrenciesByNameRequest().sendRequest()

    currencies_names = []
    for currency in response.getAllCurrencies():
        name_element = currency.find(response.getQualifiedTag("sName"))
        currencies_names.append(name_element.text)

    assert sorted(currencies_names) == currencies_names


def test_list_of_currencies_by_code():
    response = ListOfCurrenciesByCodeRequest().sendRequest()

    currency_codes = []
    for continent in response.getAllCurrencies():
        code_element = continent.find(response.getQualifiedTag("sISOCode"))
        currency_codes.append(code_element.text)

    assert sorted(currency_codes) == currency_codes
