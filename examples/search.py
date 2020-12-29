from wordsapy import Dictionary

dictionary = Dictionary(api_key='')

# More details: https://www.wordsapi.com/docs/#searching

search = dictionary.search(
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
    # random = 'true',
    limit = 200,
    page = 1
)

print('Total results: ' + str(search.total))
for word in search.data:
    print(word)