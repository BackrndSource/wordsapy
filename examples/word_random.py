from wordsapy import Dictionary

dictionary = Dictionary(api_key='')

# More details: https://www.wordsapi.com/docs/#random-words

word = dictionary.random(
    letterPattern = '^a.{4}$',
    # letters = 6,
    # lettersMin = 2,
    # lettersMax = 7,
    # pronunciationPattern = '.*æm$',
    # sounds = 5,
    # soundsMin = 3,
    # soundsMax = 5,
    # partOfSpeech = 'verb',
    # hasDetails = 'typeOf',
)

print('Word: ' + str(word))

# Retrieve a word in the same way as dictionary.word()
# See examples/word.py