import pytest
from classes import Price

class TestPrice() :
    def test_price_to_string(self) :
        price = Price(303030)
        EXPECTED_RESULT = "Rp303030,00"
        assert price.to_string() == EXPECTED_RESULT

    def test_price_add(self) :
        price = Price(303030)
        price.add(70)
        EXPECTED_RESULT = 303101
        assert price.get_price() == EXPECTED_RESULT