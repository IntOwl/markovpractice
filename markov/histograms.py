import random

class Dictogram(dict):
    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(Dictogram, self).__init__ # what does this do?
        self.types = 0 # number of distinct item types in histogram
        self.tokens = 0 # total count of all item tokens in histogram
        if iterable and isinstance(iterable, (list, tuple)):
            self.update(iterable)
        else:
            self[iterable] = 1
            self.types += 1
            self.tokens += 1
    
    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        # currently splitting input from make_higher_order_markov_model into individual chars, instead of full strings
        for item in iterable:
            # if the item is in the dictionary, then increment tokens and item
            if item in self:
                self[item] += 1
                self.tokens += 1
            # if item is not in the dictionary, then create place for item and increment type and tokens
            else:
                self[item] = 1
                self.types += 1
                self.tokens += 1
                # there will always be one type per item, makes sense

    def count(self, item):
        if item in self:
            return self[item]
        return 0

    def return_random_word(self):
        random_key = random.randint(0, self.keys().__len__)
        return self[random_key]

    def return_weighted_random_word(self):
        random_index = random.randint(0, self.tokens - 1)
        index = 0
        list_of_keys = self.keys()
        for key in list_of_keys:
            index += self[key]
            if (index > random_index):
                return key
