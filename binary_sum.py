"""Реализуйте функцию binary_sum(), которая принимает на вход два двоичных числа (в виде строк) и возвращает их сумму. 
Результат (вычисленная сумма) также должен быть бинарным числом в виде строки"""

import unittest

class TestFunction(unittest.TestCase):
    
    def test_binary_sum(self):
        self.assertEqual(binary_sum('10','1'),'11')
        self.assertEqual(binary_sum('1101','101'),'10010')
#----------------
def binary_sum(first, second):
    first = int(('0b' + first), 2)
    second = int(('0b' + second), 2)
    result = str(bin(first + second))[2:]
    return result 
#----------------
if __name__ == "__main__":
    unittest.main()

