import unittest

from translator import english_to_french, french_to_english

class TestSquare(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
        self.assertNotEqual(english_to_french('none'), 'Bonjour')
        self.assertNotEqual(english_to_french(0), 0)
        
class TestDouble(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')
        self.assertNotEqual(french_to_english('none'), 'Hello')
        self.assertNotEqual(french_to_english(0), 0)

unittest.main()