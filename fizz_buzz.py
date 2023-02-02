"""Реализуйте функцию fizz_buzz, которая возвращает строку с числами (через пробел) в диапазоне от begin до end включительно. При этом:

Если число делится без остатка на 3, то вместо него выводится слово Fizz
Если число делится без остатка на 5, то вместо него выводится слово Buzz
Если число делится без остатка и на 3, и на 5, то вместо числа выводится слово FizzBuzz
В остальных случаях в строку добавляется само число

Функция принимает два параметра (begin и end), определяющих начало и конец диапазона (включительно). 
Если диапазон пуст (в случае, когда begin > end), то функция возвращает пустую строку."""

import unittest


class TestFunction(unittest.TestCase):

    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(1, 5), '1 2 Fizz 4 Buzz')
        self.assertEqual(fizz_buzz(11, 20),
                         '11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz')
        self.assertEqual(fizz_buzz(1, 15), '1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz')
        self.assertEqual(fizz_buzz(20, 25), 'Buzz Fizz 22 23 Fizz Buzz')
        self.assertEqual(fizz_buzz(30, 35), 'FizzBuzz 31 32 Fizz 34 Buzz')


def fizz_buzz(begin, end):
    result = []

    for i in range(begin, end + 1):
        if i % 5 == 0 and i % 3 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(i))


if __name__ == '__main__':
    unittest.main()
