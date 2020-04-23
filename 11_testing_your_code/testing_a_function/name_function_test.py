import unittest
from name_function import get_formatted_name
from city_functions import city_country


class NameTestCase(unittest.TestCase):
    '''测试类'''
    # def __init__(self):

    def test_first_last_name(self):
        '''能够正确的处理姓名吗'''
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_city_country(self):
        """定义一个用于测试city_country方法的测试方法"""
        city_name = city_country('santiago','chile')
        print(city_name)
        self.assertEqual(city_name,"Santiago,Chile")
        # print("1")

