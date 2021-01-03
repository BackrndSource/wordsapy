from .wordsapy import WordsapyClient

class Dictionary(WordsapyClient):
    _urls = {
        'word': '',
        'definitions': 'definitions',
        'synonyms': 'synonyms',
        'antonyms': 'antonyms',
        'examples': 'examples',
        'typeof': 'typeof',
        'hastypes': 'hastypes',
        'partof': 'partof',
        'hasparts': 'hasparts',
        'instanceof': 'instanceof',
        'hasinstances': 'hasinstances',
        'similarto': 'similarto',
        'also': 'also',
        'entails': 'entails',
        'memberof': 'memberof',
        'hasmembers': 'hasmembers',
        'substanceof': 'substanceof',
        'hassubstances': 'hassubstances',
        'incategory': 'incategory',
        'hascategories': 'hascategories',
        'usageof': 'usageof',
        'hasusages': 'hasusages',
        'inregion': 'inregion',
        'regionof': 'regionof',
        'pertainsto': 'pertainsto',
        'rhymes': 'rhymes',
        'frequency': 'frequency',
        'search': ''

    }
    
    def word(self, word):
        '''
        Retrieve all details of a word.
        Unless you ask for specific details of word, the results of a call to the Words api will return 
        everything known about a word, grouped by definition.
        '''
        return self._get(self._urls['word'], word)
        
    def definitions(self, word):
        '''
        The meaning of the word, including its part of speech.
        '''
        return self._get(self._urls['definitions'], word, 'definitions')
    
    def synonyms(self, word):
        '''
        Words that can be interchanged for the original word in the same context.
        '''
        return self._get(self._urls['synonyms'], word, 'synonyms')
    
    def antonyms(self, word):
        '''
        Words that have the opposite context of the original word.
        '''
        return self._get(self._urls['antonyms'], word, 'antonyms')
    
    def examples(self, word):
        '''
        Example sentences using the word.
        '''
        return self._get(self._urls['examples'], word, 'examples')
    
    def typeof(self, word):
        '''
        Words that are more generic than the original word. Also known as hypernyms.
        For example, a hatchback is a type of car.
        '''
        return self._get(self._urls['typeof'], word, 'typeOf')
    
    def hastypes(self, word):
        '''
        Words that are more specific than the original word. Also known as hyponyms.
        For example, purple has types violet, lavender, mauve, etc.
        '''
        return self._get(self._urls['hastypes'], word, 'hasTypes')
    
    def partof(self, word):
        '''
        The larger whole to which this word belongs. Also known as holonyms.
        For example, a finger is part of a hand, a glove, a paw, etc.
        '''
        return self._get(self._urls['partof'], word, 'partOf')
    
    def hasparts(self, word):
        '''
        Words that are part of the original word. Also known as meronyms.
        For example, a building has parts such as roofing, plumbing etc.
        '''
        return self._get(self._urls['hasparts'], word, 'hasParts')
    
    def instanceof(self, word):
        '''
        Words that the original word is an example of.
        For example, Einstein is an instance of a physicist.
        '''
        return self._get(self._urls['instanceof'], word, 'instanceOf')
    
    def hasinstances(self, word):
        '''
        Words that are examples of the original word.
        For example, president has instances such as theodore roosevelt, van buren, etc.
        '''
        return self._get(self._urls['hasinstances'], word, 'hasInstances')
    
    def similarto(self, word):
        '''
        Words that similar to the original word, but are not synonyms.
        For example, red is similar to bloody.
        '''
        return self._get(self._urls['similarto'], word, 'similarTo')
    
    def also(self, word):
        '''
        Phrases to which the original word belongs.
        For example, bump is used in the phrase bump off.
        '''
        return self._get(self._urls['also'], word, 'also')
    
    def entails(self, word):
        '''
        Words that are implied by the original word. Usually used for verbs.
        For example, rub entails touch.
        '''
        return self._get(self._urls['entails'], word, 'entails')
    
    def memberof(self, word):
        '''
        A group to which the original word belongs.
        For example, dory is a member of the family zeidae.
        '''
        return self._get(self._urls['memberof'], word, 'memberOf')
    
    def hasmembers(self, word):
        '''
        Words that belong to the group defined by the original word.
        For example, a cult has members called cultists.
        '''
        return self._get(self._urls['hasmembers'], word, 'hasMembers')
    
    def substanceof(self, word):
        '''
        Substances to which the original word is a part of.
        For example, water is a substance of sweat.
        '''
        return self._get(self._urls['substanceof'], word, 'substanceOf')
    
    def hassubstances(self, word):
        '''
        Substances that are part of the original word.
        For example, wood has a substance called lignin.
        '''
        return self._get(self._urls['hassubstances'], word, 'hasSubstances')
    
    def incategory(self, word):
        '''
        The domain category to which the original word belongs.
        For example, chaotic is in category physics.
        '''
        return self._get(self._urls['incategory'], word, 'inCategory')
    
    def hascategories(self, word):
        '''
        Categories of the original word.
        For example, math has categories such as algebra, imaginary, numerical analysis, etc.
        '''
        return self._get(self._urls['hascategories'], word, 'hasCategories')
    
    def usageof(self, word):
        '''
        Words that the original word is a domain usage of.
        For example, advil is a useage of the trademark, etc.
        '''
        return self._get(self._urls['usageof'], word, 'usageOf')
    
    def hasusages(self, word):
        '''
        Words that are examples of the domain the original word defines.
        For example, colloquialism is a domain that includes examples like big deal, blue moon, etc.
        '''
        return self._get(self._urls['hasusages'], word, 'hasUsages')
    
    def inregion(self, word):
        '''
        Regions where the word is used.
        For example, chips is used in region Britain.
        '''
        return self._get(self._urls['inregion'], word, 'inRegion')
    
    def regionof(self, word):
        '''
        A region where words are used.
        For example, Canada is the region of pogey.
        '''
        return self._get(self._urls['regionof'], word, 'regionOf')
    
    def pertainsto(self, word):
        '''
        Words to which the original word is relevant.
        For example, .22-caliber pertains to caliber.
        '''
        return self._get(self._urls['pertainsto'], word, 'pertainsTo')

    def rhymes(self, word):
        '''
        Retrieve rhymes of a word.
        More details: https://www.wordsapi.com/docs/#rhymes
        '''
        return self._get(self._urls['rhymes'], word, 'rhymes')

    def frequency(self, word):
        '''
        Retrieve details about the frequency of use of a word.
        More details: https://www.wordsapi.com/docs/#frequency
        '''
        return self._get(self._urls['frequency'], word, 'frequency')

    def search(self, **kwargs):
        '''
        Retrieve details about the frequency of use of a word.
        More details: https://www.wordsapi.com/docs/#search
        '''
        if 'random' in kwargs and kwargs['random'] == 'true':
            return self.random(**kwargs)
                
        return self._get(self._urls['search'], results_key='results', params=kwargs)
    
    def random(self, **kwargs):
        '''
        Retrieve details about the frequency of use of a word.
        More details: https://www.wordsapi.com/docs/#search
        '''
        kwargs['random'] = 'true'
        return self._get(self._urls['search'], results_key=0, params=kwargs)


        