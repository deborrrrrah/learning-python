import unittest
from classes import Price

class TestPrice(unittest.TestCase) :
    def setUp(self) :
        self.price = Price(303030)

    def test_price_to_string(self) :
        EXPECTED_RESULT = "Rp303030,00"
        self.assertEqual(self.price.to_string(), EXPECTED_RESULT)