from unittest import TestCase
from wordsapy import Dictionary, WordsapyDict

class DictionaryTests(TestCase):
    def setUp(self):
        self.dictionary = Dictionary()

    def test_get_word(self):
        word = self.dictionary.word('example')
        self.assertTrue(isinstance(word, WordsapyDict))
        
        self.assertTrue(hasattr(word, 'word'))
        self.assertEqual(word.word, 'example')

        self.assertTrue(hasattr(word, 'results'))
        self.assertTrue(isinstance(word.results, list))
        self.assertGreater(len(word.results), 0)
        for result in word.results:
            self.assertTrue(isinstance(result, WordsapyDict))
            self.assertTrue(hasattr(result, 'definition'))
            self.assertTrue(isinstance(result.definition, str))
            self.assertTrue(hasattr(result, 'partOfSpeech'))
            self.assertTrue(isinstance(result.partOfSpeech, str))
            self.assertTrue(hasattr(result, 'synonyms'))
            self.assertTrue(isinstance(result.synonyms, list))
            self.assertTrue(hasattr(result, 'typeOf'))
            self.assertTrue(isinstance(result.typeOf, list))
            if hasattr(result, 'derivation'):
                self.assertTrue(isinstance(result.derivation, list))
        
        self.assertTrue(hasattr(word, 'syllables'))
        self.assertTrue(isinstance(word.syllables, WordsapyDict))
        self.assertTrue(hasattr(word.syllables, 'count'))
        self.assertTrue(isinstance(word.syllables.count, int))
        self.assertTrue(hasattr(word.syllables, 'list'))
        self.assertTrue(isinstance(word.syllables.list, list))
            
        self.assertTrue(hasattr(word, 'pronunciation'))
        self.assertTrue(isinstance(word.syllables, WordsapyDict))

    def test_get_definitions(self):
        definitions = self.dictionary.definitions('example')
        self.assertTrue(isinstance(definitions, list))
        self.assertGreater(len(definitions), 0)
        for definition in definitions:
            self.assertTrue(isinstance(definition, WordsapyDict))
            self.assertTrue(hasattr(definition, 'definition'))
            self.assertTrue(hasattr(definition, 'partOfSpeech'))
    
    def test_get_synonyms(self):
        synonyms = self.dictionary.synonyms('example')
        self.assertTrue(isinstance(synonyms, list))
        self.assertGreater(len(synonyms), 0)
        self.assertIn('exemplar', synonyms)
        for synonym in synonyms:
            self.assertTrue(isinstance(synonym, str))

    def test_get_antonyms(self):
        antonyms = self.dictionary.antonyms('true')
        self.assertTrue(isinstance(antonyms, list))
        self.assertGreater(len(antonyms), 0)
        self.assertIn('false', antonyms)
        for antonym in antonyms:
            self.assertTrue(isinstance(antonym, str))

    def test_get_examples(self):
        examples = self.dictionary.examples('example')
        self.assertTrue(isinstance(examples, list))
        self.assertGreater(len(examples), 0)
        self.assertIn('I profited from his example', examples)
        for example in examples:
            self.assertTrue(isinstance(example, str))

    def test_get_typeof(self):
        typeof = self.dictionary.typeof('example')
        self.assertTrue(isinstance(typeof, list))
        self.assertGreater(len(typeof), 0)
        self.assertIn('representation', typeof)
        for item in typeof:
            self.assertTrue(isinstance(item, str))

    def test_get_hastypes(self):
        hastypes = self.dictionary.hastypes('example')
        self.assertTrue(isinstance(hastypes, list))
        self.assertGreater(len(hastypes), 0)
        self.assertIn('prefiguration', hastypes)
        for item in hastypes:
            self.assertTrue(isinstance(item, str))

    def test_get_partof(self):
        partof = self.dictionary.partof('arm')
        self.assertTrue(isinstance(partof, list))
        self.assertGreater(len(partof), 0)
        self.assertIn('human', partof)
        for item in partof:
            self.assertTrue(isinstance(item, str))

    def test_get_hasparts(self):
        hasparts = self.dictionary.hasparts('human')
        self.assertTrue(isinstance(hasparts, list))
        self.assertGreater(len(hasparts), 0)
        self.assertIn('arm', hasparts)
        for item in hasparts:
            self.assertTrue(isinstance(item, str))

    def test_get_instanceof(self):
        instanceof = self.dictionary.instanceof('einstein')
        self.assertTrue(isinstance(instanceof, list))
        self.assertGreater(len(instanceof), 0)
        self.assertIn('physicist', instanceof)
        for item in instanceof:
            self.assertTrue(isinstance(item, str))

    def test_get_hasinstances(self):
        hasinstances = self.dictionary.hasinstances('physicist')
        self.assertTrue(isinstance(hasinstances, list))
        self.assertGreater(len(hasinstances), 0)
        self.assertIn('einstein', hasinstances)
        for item in hasinstances:
            self.assertTrue(isinstance(item, str))

    def test_get_similarto(self):
        similarto = self.dictionary.similarto('hungry')
        self.assertTrue(isinstance(similarto, list))
        self.assertGreater(len(similarto), 0)
        self.assertIn('empty', similarto)
        for item in similarto:
            self.assertTrue(isinstance(item, str))

    def test_get_also(self):
        also = self.dictionary.also('true')
        self.assertTrue(isinstance(also, list))
        self.assertGreater(len(also), 0)
        self.assertIn('honest', also)
        for item in also:
            self.assertTrue(isinstance(item, str))

    def test_get_entails(self):
        entails = self.dictionary.entails('rub')
        self.assertTrue(isinstance(entails, list))
        self.assertGreater(len(entails), 0)
        self.assertIn('touch', entails)
        for item in entails:
            self.assertTrue(isinstance(item, str))

    def test_get_memberof(self):
        memberof = self.dictionary.memberof('galaxy')
        self.assertTrue(isinstance(memberof, list))
        self.assertGreater(len(memberof), 0)
        self.assertIn('cosmos', memberof)
        for item in memberof:
            self.assertTrue(isinstance(item, str))

    def test_get_hasmembers(self):
        hasmembers = self.dictionary.hasmembers('cosmos')
        self.assertTrue(isinstance(hasmembers, list))
        self.assertGreater(len(hasmembers), 0)
        self.assertIn('galaxy', hasmembers)
        for item in hasmembers:
            self.assertTrue(isinstance(item, str))

    def test_get_substanceof(self):
        substanceof = self.dictionary.substanceof('hydrogen')
        self.assertTrue(isinstance(substanceof, list))
        self.assertGreater(len(substanceof), 0)
        self.assertIn('water', substanceof)
        for item in substanceof:
            self.assertTrue(isinstance(item, str))

    def test_get_hassubstances(self):
        hassubstances = self.dictionary.hassubstances('water')
        self.assertTrue(isinstance(hassubstances, list))
        self.assertGreater(len(hassubstances), 0)
        self.assertIn('hydrogen', hassubstances)
        for item in hassubstances:
            self.assertTrue(isinstance(item, str))

    def test_get_incategory(self):
        incategory = self.dictionary.incategory('chaotic')
        self.assertTrue(isinstance(incategory, list))
        self.assertGreater(len(incategory), 0)
        self.assertIn('physics', incategory)
        for item in incategory:
            self.assertTrue(isinstance(item, str))

    def test_get_hascategories(self):
        hascategories = self.dictionary.hascategories('physics')
        self.assertTrue(isinstance(hascategories, list))
        self.assertGreater(len(hascategories), 0)
        self.assertIn('chaotic', hascategories)
        for item in hascategories:
            self.assertTrue(isinstance(item, str))

    def test_get_usageof(self):
        usageof = self.dictionary.usageof('advil')
        self.assertTrue(isinstance(usageof, list))
        self.assertGreater(len(usageof), 0)
        self.assertIn('trade name', usageof)
        for item in usageof:
            self.assertTrue(isinstance(item, str))

    def test_get_hasusages(self):
        hasusages = self.dictionary.hasusages('colloquialism')
        self.assertTrue(isinstance(hasusages, list))
        self.assertGreater(len(hasusages), 0)
        self.assertIn('way', hasusages)
        for item in hasusages:
            self.assertTrue(isinstance(item, str))

    def test_get_inregion(self):
        inregion = self.dictionary.inregion('chips')
        self.assertTrue(isinstance(inregion, list))
        self.assertGreater(len(inregion), 0)
        self.assertIn('britain', inregion)
        for item in inregion:
            self.assertTrue(isinstance(item, str))

    def test_get_regionof(self):
        regionof = self.dictionary.regionof('spain')
        self.assertTrue(isinstance(regionof, list))
        self.assertGreater(len(regionof), 0)
        self.assertIn('paella', regionof)
        for item in regionof:
            self.assertTrue(isinstance(item, str))

    def test_get_pertainsto(self):
        pertainsto = self.dictionary.pertainsto('.22-caliber')
        self.assertTrue(isinstance(pertainsto, list))
        self.assertGreater(len(pertainsto), 0)
        self.assertIn('caliber', pertainsto)
        for item in pertainsto:
            self.assertTrue(isinstance(item, str))

    def test_get_rhymes(self):
        rhymes = self.dictionary.rhymes('wind')
        self.assertTrue(isinstance(rhymes, WordsapyDict))
        self.assertTrue(hasattr(rhymes, 'all'))
        self.assertTrue(hasattr(rhymes, 'noun'))
        self.assertTrue(hasattr(rhymes, 'verb'))
        self.assertTrue(isinstance(rhymes.all, list))
        self.assertGreater(len(rhymes.all), 0)
        self.assertIn('abscind', rhymes.all)
        for item in rhymes.all:
            self.assertTrue(isinstance(item, str))
        self.assertTrue(isinstance(rhymes.noun, list))
        self.assertGreater(len(rhymes.noun), 0)
        self.assertIn('downwind', rhymes.noun)
        for item in rhymes.noun:
            self.assertTrue(isinstance(item, str))
        self.assertTrue(isinstance(rhymes.verb, list))
        self.assertGreater(len(rhymes.verb), 0)
        self.assertIn('affined', rhymes.verb)
        for item in rhymes.verb:
            self.assertTrue(isinstance(item, str))

    def test_get_frequency(self):
        frequency = self.dictionary.frequency('example')
        self.assertTrue(isinstance(frequency, WordsapyDict))
        self.assertTrue(hasattr(frequency, 'zipf'))
        self.assertTrue(hasattr(frequency, 'perMillion'))
        self.assertTrue(hasattr(frequency, 'diversity'))
        self.assertTrue(isinstance(frequency.zipf, float))
        self.assertTrue(isinstance(frequency.perMillion, float))
        self.assertTrue(isinstance(frequency.diversity, float))

    def test_search_letter_pattern(self):
        search = self.dictionary.search(
            letterPattern = '^a.{4}$',
            limit = 50,
            page = 1
        )
        self.assertTrue(hasattr(search, 'data'))
        self.assertTrue(isinstance(search.data, list))
        self.assertEqual(len(search.data), 50)
        for word in search.data:
            self.assertTrue(isinstance(word, str))
        self.assertTrue(hasattr(search, 'total'))
        self.assertTrue(isinstance(search.total, int))
        self.assertGreater(search.total, 0)

    def test_search_letters(self):
        search = self.dictionary.search(
            letters = 6,
            limit = 50,
            page = 1
        )
        self.assertTrue(hasattr(search, 'data'))
        self.assertTrue(isinstance(search.data, list))
        self.assertEqual(len(search.data), 50)
        for word in search.data:
            self.assertTrue(isinstance(word, str))
            self.assertEqual(len(word.replace(' ' ,'')), 6)
        self.assertTrue(hasattr(search, 'total'))
        self.assertTrue(isinstance(search.total, int))
        self.assertGreater(search.total, 0)

    def test_search_letters_min(self):
        search = self.dictionary.search(
            lettersMin = 9,
            limit = 50,
            page = 1
        )
        self.assertTrue(hasattr(search, 'data'))
        self.assertTrue(isinstance(search.data, list))
        self.assertEqual(len(search.data), 50)
        for word in search.data:
            self.assertTrue(isinstance(word, str))
            self.assertGreaterEqual(len(word.replace(' ' ,'')), 9)
        self.assertTrue(hasattr(search, 'total'))
        self.assertTrue(isinstance(search.total, int))
        self.assertGreater(search.total, 0)

    def test_search_letters_max(self):
        search = self.dictionary.search(
            lettersMax = 6,
            limit = 50,
            page = 1
        )
        self.assertTrue(hasattr(search, 'data'))
        self.assertTrue(isinstance(search.data, list))
        self.assertEqual(len(search.data), 50)
        for word in search.data:
            self.assertTrue(isinstance(word, str))
            self.assertLessEqual(len(word.replace(' ' ,'')), 6)
        self.assertTrue(hasattr(search, 'total'))
        self.assertTrue(isinstance(search.total, int))
        self.assertGreater(search.total, 0)

    def test_search_pronunciation_pattern(self):
        search = self.dictionary.search(
            pronunciationPattern = '.*æm$',
            limit = 50,
            page = 1
        )
        self.assertTrue(hasattr(search, 'data'))
        self.assertTrue(isinstance(search.data, list))
        self.assertEqual(len(search.data), 50)
        for word in search.data:
            self.assertTrue(isinstance(word, str))
        self.assertTrue(hasattr(search, 'total'))
        self.assertTrue(isinstance(search.total, int))
        self.assertGreater(search.total, 0)

    def test_search_sounds(self):
        search = self.dictionary.search(
            sounds = 5,
            limit = 50,
            page = 1
        )
        self.assertTrue(hasattr(search, 'data'))
        self.assertTrue(isinstance(search.data, list))
        self.assertEqual(len(search.data), 50)
        for word in search.data:
            self.assertTrue(isinstance(word, str))
        self.assertTrue(hasattr(search, 'total'))
        self.assertTrue(isinstance(search.total, int))
        self.assertGreater(search.total, 0)

    def test_search_sounds_min(self):
        search = self.dictionary.search(
            soundsMin = 3,
            limit = 50,
            page = 1
        )
        self.assertTrue(hasattr(search, 'data'))
        self.assertTrue(isinstance(search.data, list))
        self.assertEqual(len(search.data), 50)
        for word in search.data:
            self.assertTrue(isinstance(word, str))
        self.assertTrue(hasattr(search, 'total'))
        self.assertTrue(isinstance(search.total, int))
        self.assertGreater(search.total, 0)

    def test_search_sounds_max(self):
        search = self.dictionary.search(
            soundsMax = 5,
            limit = 50,
            page = 1
        )
        self.assertTrue(hasattr(search, 'data'))
        self.assertTrue(isinstance(search.data, list))
        self.assertEqual(len(search.data), 50)
        for word in search.data:
            self.assertTrue(isinstance(word, str))
        self.assertTrue(hasattr(search, 'total'))
        self.assertTrue(isinstance(search.total, int))
        self.assertGreater(search.total, 0)

    def test_search_part_of_speech(self):
        search = self.dictionary.search(
            partOfSpeech = 'verb',
            limit = 50,
            page = 1
        )
        self.assertTrue(hasattr(search, 'data'))
        self.assertTrue(isinstance(search.data, list))
        self.assertEqual(len(search.data), 50)
        for word in search.data:
            self.assertTrue(isinstance(word, str))
        self.assertTrue(hasattr(search, 'total'))
        self.assertTrue(isinstance(search.total, int))
        self.assertGreater(search.total, 0)

    def test_search_has_details(self):
        search = self.dictionary.search(
            hasDetails = 'typeOf',
            limit = 50,
            page = 1
        )
        self.assertTrue(hasattr(search, 'data'))
        self.assertTrue(isinstance(search.data, list))
        self.assertEqual(len(search.data), 50)
        for word in search.data:
            self.assertTrue(isinstance(word, str))
        self.assertTrue(hasattr(search, 'total'))
        self.assertTrue(isinstance(search.total, int))
        self.assertGreater(search.total, 0)
    
    def test_search_random(self):
        search = self.dictionary.search(
            letters = 6,
            random = 'true',
            limit = 50,
            page = 1
        )
        self.assertTrue(isinstance(search, WordsapyDict))
        self.assertTrue(hasattr(search, 'word'))
        self.assertEqual(len(search.word.replace(' ' ,'')), 6)

    def test_random(self):
        search = self.dictionary.random()
        self.assertTrue(isinstance(search, WordsapyDict))
        self.assertTrue(hasattr(search, 'word'))

    def test_random_letters(self):
        search = self.dictionary.random(letters=6)
        self.assertTrue(isinstance(search, WordsapyDict))
        self.assertTrue(hasattr(search, 'word'))
        self.assertEqual(len(search.word.replace(' ' ,'')), 6)