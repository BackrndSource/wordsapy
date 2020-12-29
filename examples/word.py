from wordsapy import Dictionary

dictionary = Dictionary(api_key='')

# More details: https://www.wordsapi.com/docs/#words

word = dictionary.word('example')

print('Word: ' + str(word))
# or
print('Word: ' + word.word)

if hasattr(word, 'results'):
    for result in word.results:
        print('Definition: ' + result.definition)
        print('Part of speech: ' + result.partOfSpeech)

if hasattr(word, 'syllables'):
    print('Syllables: ' + str(word.syllables.count))
    print(', '.join(word.syllables.list))

if hasattr(word, 'pronunciation'):
    if hasattr(word.pronunciation, 'all'):
        print('Pronunciations: ')
        print(', '.join(word.pronunciation.all))

