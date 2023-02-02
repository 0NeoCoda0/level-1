"""Вам предстоит написать программу, которая шифрует сообщения по следующему алгоритму: она берёт текст и переставляет в нём каждые два подряд идущих символа.

Если количество символов нечётное, то последний символ остаётся на своём месте"""

import unittest


class TestFunction(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(encrypt("attack"), "taatkc")
        self.assertEqual(encrypt("go!"), "og!")


def encrypt(text):
    new_text = ''
    for i in range(len(text) - 1):
        if i % 2 == 0:
            new_text += text[i + 1]
            new_text += text[i]
    if len(text) % 2 != 0:
        new_text += text[-1]
    return new_text


if __name__ == '__main__':
    unittest.main()
