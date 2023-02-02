"""Написать функцию возвращающую квадратный корень числа"""

import unittest


class TestFunction(unittest.TestCase):

    def test_sqrt(self):
        self.assertEqual(sqrt(25), 5)


def sqrt(x):
    return x ** 0.5


if __name__ == '__main__':
    unittest.main()
