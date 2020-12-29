from unittest import TestCase
from wordsapy import Dictionary, WordsapyException

class WordsapyExceptionApiKeyTests(TestCase):
    def setUp(self):
        self.dictionary = Dictionary(api_key='')

    def test_exception_blank_api_key(self):
        self.dictionary.api_key = ''
        try:
            self.dictionary.word('example')
        except WordsapyException as exception:
            self.assertTrue(isinstance(exception, WordsapyException))
            self.assertEqual(exception.args[0], 'API key not found.')
    
    def test_exception_not_valid_api_key(self):
        self.dictionary.api_key = 'xxvvvvxxxxxxxxxxxxxxxxx'
        try:
            self.dictionary.word('example')
        except WordsapyException as exception:
            self.assertTrue(isinstance(exception, WordsapyException))
            self.assertEqual(exception.args[0], 'You are not subscribed to this API.')

class WordsapyExceptionTests(TestCase):
    def setUp(self):
        self.dictionary = Dictionary()

    def test_exception_word_not_found(self):
        try:
            self.dictionary.word('sfsfsd\'s$%$cscs)(da\"sdsgsdgvv')
        except WordsapyException as exception:
            self.assertTrue(isinstance(exception, WordsapyException))
            self.assertEqual(exception.args[0], 'word not found')
         
