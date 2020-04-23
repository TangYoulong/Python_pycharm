import unittest
from city_functions2 import city_country_population

class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        msg = city_country_population("santiago","chile")
        self.assertEqual(msg,"Santiago,Chile")
    def test_city_country_population(self):
        msg2 = city_country_population("santiago","chile","population=50000")
        self.assertEqual(msg2,"Santiago,Chile-population=50000")

