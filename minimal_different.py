"""Напишите функцию diff, которая принимает два угла (int) и возвращает наименьшую разницу между ними."""

import unittest


class TestFunction(unittest.TestCase):

    def test_diff(self):
        self.assertEqual(diff(-135, 180), 45)
        self.assertEqual(diff(0, -550), 170)
        self.assertEqual(diff(120, 280), 160)
        self.assertEqual(diff(270, 0), 90)


def diff(x, y):
    first = 360 - abs(x - y) % 360
    second = abs(x - y) % 360
    return min(first, second)


if __name__ == '__main__':
    unittest.main()


