from wordsapy import Dictionary

dictionary = Dictionary(api_key='')

# More details: https://www.wordsapi.com/docs/#get-word-details

# Definitions
results = dictionary.definitions('example')
for result in results:
    print('Definition: ' + result.definition)
    print('Part of speech: ' + result.partOfSpeech)

# Synonyms
synonyms = dictionary.synonyms('example')
print('Synonyms:' + ', '.join(synonyms))

# Antonyms
antonyms = dictionary.synonyms('true')
print('Synonyms:' + ', '.join(antonyms))

# Examples
examples = dictionary.examples('example')
print('Synonyms:' + ', '.join(examples))

# For more options see the link above