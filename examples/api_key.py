# Define your api key as an environment variable
import os 


os.environ['WORDS_API_KEY'] = 'your_api_key'
# ----------------------------------------------
# Or use the Dictionary class
from wordsapy import Dictionary


dictionary = Dictionary(api_key='your_api_key')
# or
dictionary = Dictionary()
dictionary.api_key = 'your_api_key'
# ----------------------------------------------
# Or the WordsapyClient class
from wordsapy import WordsapyClient


client = WordsapyClient(api_key='your_api_key')
# or
client = WordsapyClient()
client.api_key = 'your_api_key'
# ----------------------------------------------
# when using any of these classes the api key 
# will be defined as an environment variable, 
# so with doing it only once is more than enough