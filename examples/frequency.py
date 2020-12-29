from wordsapy import Dictionary

dictionary = Dictionary(api_key='')

# More details: https://www.wordsapi.com/docs/#frequency

frequency = dictionary.frequency('wind')

if hasattr(frequency, 'zipf'):
    print('Zipf: ' + frequency.zipf)

if hasattr(frequency, 'perMillion'):
    print('Per million: ' + frequency.perMillion)

if hasattr(frequency, 'diversity'):
    print('Diversity: ' + frequency.diversity)