from ..endpoints.requests.CurrencyNameRequest import (
    CurrencyNameRequest,
)
import xml.etree.ElementTree as ET
import pytest


def test_currency_name():
    response = CurrencyNameRequest("USD").sendRequest()

    assert response.verifyByDTD()
    assert response.getResponseString().text == "Dollars"
