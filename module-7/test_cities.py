#Scott Anderson Module 7.2 Assignment

import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")

if __name__ == '__main__':
    unittest.main()

