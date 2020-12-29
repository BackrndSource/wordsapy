from wordsapy import Dictionary

dictionary = Dictionary(api_key='')

# More details: https://www.wordsapi.com/docs/#rhymes

rhymes = dictionary.rhymes('wind')

if hasattr(rhymes, 'all'):
    print('All rhymes: ' + ', '.join(rhymes.all))

if hasattr(rhymes, 'noun'):
    print('Noun rhymes: ' + ', '.join(rhymes.all))

if hasattr(rhymes, 'verb'):
    print('Verb rhymes: ' + ', '.join(rhymes.all))