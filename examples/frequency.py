from wordsapy import Dictionary

dictionary = Dictionary(api_key='')

# More details: https://www.wordsapi.com/docs/#frequency

frequency = dictionary.frequency('wind')

if hasattr(frequency, 'zipf'):
    print('Zipf: ' + str(frequency.zipf))

if hasattr(frequency, 'perMillion'):
    print('Per million: ' + str(frequency.perMillion))

if hasattr(frequency, 'diversity'):
    print('Diversity: ' + str(frequency.diversity))