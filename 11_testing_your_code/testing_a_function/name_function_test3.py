import unittest
from name_function3 import get_formatted_name


class NameTestCase(unittest.TestCase):
    '''测试name_function2.py'''

    def test_first_last_name(self):
        '''能够正确的处理姓名吗'''
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    def test_first_last_middle_name(self):
        '''能够处理包含middle中间名的情况吗'''
        formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')



