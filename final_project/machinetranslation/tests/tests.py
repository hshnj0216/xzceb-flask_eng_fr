import unittest
from machinetranslation.translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french(None), 
        'Cannot translate null or empty text')
    
    def test_f2e(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english(None), 
        'Cannot translate null or empty text')

if __name__=='__main__':
    unittest.main()