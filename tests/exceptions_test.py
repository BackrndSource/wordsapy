from unittest import TestCase
from wordsapy import Dictionary, WordsapyException

class WordsapyExceptionApiKeyTests(TestCase):
    def test_exception_blank_api_key(self):
        dictionary = Dictionary(api_key='')
        try:
            dictionary.word('example')
        except WordsapyException as exception:
            self.assertTrue(isinstance(exception, WordsapyException))
            self.assertEqual(exception.args[0], 'API key not found.')

class WordsapyExceptionBadQueriesTests(TestCase):
    def setUp(self):
        self.dictionary = Dictionary()

    def test_exception_word_not_found(self):
        try:
            self.dictionary.word('sfsfsd\'s$%$cscs)(da\"sdsgsdgvv')
        except WordsapyException as exception:
            self.assertTrue(isinstance(exception, WordsapyException))
            self.assertEqual(exception.args[0], 'word not found')
         
