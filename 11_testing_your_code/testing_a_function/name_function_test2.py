import unittest
from name_function2 import get_formatted_name


class NameTestCase(unittest.TestCase):
    '''测试name_function2.py'''

    def test_first_last_name(self):
        '''能够正确的处理姓名吗'''
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')