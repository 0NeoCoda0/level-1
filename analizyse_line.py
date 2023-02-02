"""В рамках этого испытания вы реализуете небольшой набор функций, работающих с отрезками прямых на двухмерной плоскости. 
Отрезок в нашем случае будет кодироваться в виде пары пар и выглядеть как-то так: ((x1, y1), (x2, y2)) (вложенные пары — это концы отрезка). 
Вам нужно реализовать четыре функции:

is_degenerated() должна возвращать истину, если отрезок вырожден в точку (начало и конец совпадают);
is_vertical() должна возвращать "истину", если отрезок — вертикальный;
is_horizontal() должна возвращать "истину", если отрезок — горизонтальный;
is_inclined() должна возвращать "истину", если отрезок — наклонный (не вертикальный и не горизонтальный)."""

import unittest


class TestFunction(unittest.TestCase):

    def test_line_analyze(self):
        self.assertEqual(is_degenerated([4, 4], [4, 4]), True)
        self.assertEqual(is_degenerated([0, 3], [1, 4]), False)
        self.assertEqual(is_vertical([2, 3], [2, 10]), True)
        self.assertEqual(is_vertical([3, 12], [5, 2]), False)
        self.assertEqual(is_horizontal([23, 5], [4, 5]), True)
        self.assertEqual(is_horizontal([3, 3], [8, 1]), False)
        self.assertEqual(is_inclined([3, 4], [8, 12]), True)
        self.assertEqual(is_inclined([3, 2], [3, 1]), False)


def is_degenerated(begin, end):
    return begin == end

def is_vertical(begin, end):
    return begin[0] == end[0]

def is_horizontal(begin, end):
    return begin[1] == end[1]

def is_inclined(begin, end):
    return begin[1] != end[1] and begin[0] != end[0]
 
if __name__ == '__main__':
    unittest.main()
