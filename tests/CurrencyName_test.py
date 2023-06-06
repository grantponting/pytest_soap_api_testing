from ..endpoints.requests.CurrencyNameRequest import (
    CurrencyNameRequest,
)
import xml.etree.ElementTree as ET
import pytest


def test_currency_name():
    response = CurrencyNameRequest("USD").send_request()

    assert response.verify_by_dtd()
    assert response.getResponseString().text == "Dollars"
