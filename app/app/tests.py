'''
Sample tests
'''
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    '''Test the Calc Module'''

    def test_add_num(self):
        ''' Test adding numbers together '''
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_num(self):
        ''' Test subtracting numbers '''
        res = calc.subtract(10, 6)

        self.assertEqual(res, 4)
