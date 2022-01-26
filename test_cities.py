import unittest
from city import city_country


class CityTest(unittest.TestCase):
    def test_city_country(self):
        formatted = city_country('Shenzhen', 'China')
        self.assertEqual(formatted, 'Shenzhen,China')


unittest.main()  # pycharm需注意运行方式
