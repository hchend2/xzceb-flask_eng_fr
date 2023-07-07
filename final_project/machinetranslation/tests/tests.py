import unittest

from translator import english_to_french
from translator import french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test(sefl):
        sefl.assertEqual(english_to_french("Hello"), "Bonjour")
        sefl.assertNotEqual(english_to_french("Tank you"), "Moi")


class TestFrenchToEnglish(unittest.TestCase):
    def test(sefl):
        sefl.assertEqual(french_to_english("Bonjour"), "Hello")
        sefl.assertNotEqual(french_to_english("Dieu"), "Me")
