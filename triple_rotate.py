"""В этом испытании вы будете работать с "тройками" — кортежами из трёх элементов. 
Вам предстоит реализовать две функции, которые "вращают" тройку влево и вправо. Как это выглядит, вы можете понять из пары примеров:

triple = ('A', 'B', 'C')
rotate_left(triple)  # ('B', 'C', 'A')
rotate_right(triple)  # ('C', 'A', 'B')"""

import unittest


class TestFunction(unittest.TestCase):

    def test_rotate_triple(self):
        triple = ('A', 'B', 'C')
        self.assertEqual(rotate_left(triple), ('B', 'C', 'A'))
        triple_2 = ('B', 'C', 'D', 'A')
        self.assertEqual(rotate_left(triple_2), ('C', 'D', 'A', 'B'))
        self.assertEqual(rotate_right(triple), ('C', 'A', 'B'))


def rotate_left(triple):
    result = triple[1:] + (triple[0],)
    return result


def rotate_right(triple):
    result = (triple[-1],) + triple[:-1]
    return result


if __name__ == '__main__':
    unittest.main()
