import unittest

from translator import english_to_french
from translator import french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(sefl):
        sefl.assertEqual(english_to_french("Hello"), "Bonjour")
        

class TestEnglishToFrench(unittest.TestCase):
    def test2(sefl):
        sefl.assertNotEqual(english_to_french("Tank you"), "Moi")


class TestFrenchToEnglish(unittest.TestCase):
    def test1(sefl):
        sefl.assertEqual(french_to_english("Bonjour"), "Hello")


class TestFrenchToEnglish(unittest.TestCase):
    def test2(sefl):
        sefl.assertNotEqual(french_to_english("Dieu"), "Me")


if __name__ == "__main__":
    unittest.main()