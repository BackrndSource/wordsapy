# Wordsapy
![Build Status](https://api.travis-ci.org/backrndsource/wordsapy.svg?branch=master)

Wordsapy is a python integration for the [WordsAPI](https://www.wordsapi.com/), that allows developers to retrieve information about English words like a dictionary.

## Install

> Wordsapy is available on the Python Package Index (PyPI):
https://pypi.python.org/pypi/wordsapy

You can install wordsapy using pip.

```bash
$ pip install wordsapy
```

## Usages

In order to use WordsAPI you need an API Key.

> Get you Free API Key: https://rapidapi.com/dpventures/api/wordsapi/pricing


### Setting your API Key

Initialize a `Dictionary` object and set your API Key.

```python
from wordsapy import Dictionary


dictionary = Dictionary(api_key='your_api_key')
```

In this way the API Key will be defined as an environment variable, so with doing it only once is more than enough.
Alternatively, you can export your API key as an environment variable.

```bash
$ export WORDS_API_KEY='your_api_key'
```
See [examples/api_key.py](https://github.com/BackrndSource/wordsapy/blob/master/examples/api_key.py) for other examples.

### Making queries

Once done, you can use the `Dictionary` object instance to perform queries. 

Most methods of the `Dictionary` class have the same name as WordsAPI endpoints.

> Check out the API Documentation: https://www.wordsapi.com/docs/

Assuming that the API Key is already defined as an environment variable, we retrieve the definitions of the word: *example*.

```python
from wordsapy import Dictionary


dictionary = Dictionary()
results = dictionary.definitions('example')
for result in results:
    print('Definition: ' + result.definition)
    print('Part of speech: ' + result.partOfSpeech)
```

All responses will return a `DictObj` object or a `list` object. All `dict` objects in the response will be transformed into `DictObj`. You can access to the data of a `DictObj` object as you would with a `dict` object, or do it through the attributes. An example to illustrate this:

```python
dictionary = Dictionary()
word = dictionary.word('example')

# It is the same::
for word['results'][0]['definition']
for word.results[0]['definition']
for word['results'][0].definition
for word.results.[0].definition # I love this one

# DictObj is iterable:
for key, value in word.items():
    print(key)
    print(value)
```



## Examples

All usage examples can be found in the [/examples](https://github.com/BackrndSource/wordsapy/blob/master/examples) folder of the project

## Tests

You can run the tests via the command line. Your API Key must have been exported as an environment variable. 

Place your terminal at the root of the project and run the following command.

```bash
$ python -m unittest discover tests "*_test.py"
```

## Greetings

[@AnthonyBloomer](https://github.com/AnthonyBloomer) by [tmdbv3api](https://github.com/AnthonyBloomer/tmdbv3api), with which I learned how to create a python interface for an API. The wordsapy structure is based on his library.