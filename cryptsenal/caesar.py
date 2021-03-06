"""
description: caesar cipher
author: ao wang
date: june 16, 2020
"""
from cryptsenal.cipher import Cipher
import random


class Caesar(Cipher):
    """The Caesar Cipher class

    :param text: the plain/cipher text
    :type text: str
    :param key: the cipher key
    :type key: int
    """

    def __init__(self, text, key):
        super().__init__(text, key)

    def __str__(self):
        return "Text: {}, Key: {}".format(self.text, self.key)

    def encrypt(self):
        """Encrypts the plain text into cipher text

        :returns: the encrypted plain text
        :rtype: str
        """
        arr = self.removePunctuation()
        arr = [self.intToChar(self.charToInt(char) + self.key) for char in arr]
        return "".join(arr)

    def decrypt(self):
        """Decrypts the cipher text into plain text

        :returns: the decrypted cipher text
        :rtype: str
        """
        self.setKey(26-self.key)
        return self.encrypt()

    def getKey(self):
        return key

    def setKey(self, key):
        self.key = key


def random_key():
    return random.randint(1, 25)


if __name__ == "__main__":
    msg = """JQRRG, JQRRG, TGKVGT, JQRRG, JQRRG, TGKVGT,YGPP, GT HCGNNV FCPP 
    UEJTGKV GTHCGNNV GT KP FGP ITCDGPHTGUUGP KJP FKG TCDGPHCGNNV GT KP FGP 
    UWORHFCPP OCEJV FGT TGKVGT RNWORUJWORVA FWORVAJWORVA FWORVA UCV QP C 
    YCNNJWORVA FWORVA JCF C ITGCV HCNNCNN VJG MKPIU JQTUGU CPF CNN VJG MKPIU
    OGPEQWNFPV RWV JWORVA VQIGVJGT CICKP"""
    for i in range(1, 26):
        print("key: {}, msg: {}".format(i, Caesar(msg, i).encrypt()))
