"""
description: abstract base class to extend to all other cipher classes
author: ao wang
date: june 16, 2020
"""


import abc
import string


class Cipher(metaclass=abc.ABCMeta):
    """An abstract base cipher class 

    :param text: plain/cipher text
    :type text: str
    """

    def __init__(self, text):
        self.text = text

    @abc.abstractmethod
    def encrypt(self):
        pass

    @abc.abstractmethod
    def decrypt(self):
        pass

    def removePunctuation(self):
        """Removes punctuation from the plain text

        :returns: the plain text with only alphanumeric characters
        :rtype: str
        """
        return self.text.translate(str.maketrans('', '', string.punctuation + " "))

    def intToChar(self, num):
        num %= 26
        arr = [chr(ord('A')+i) for i in range(26)]
        return arr[num]

    def charToInt(self, char):
        char = char.upper()
        arr = {chr(ord('A')+i): i for i in range(26)}
        return arr[char]

    def getText(self):
        return self.text

    def setText(self, text):
        self.text = text
