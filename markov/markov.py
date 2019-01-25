from histograms import Dictogram
import random
from collections import deque
import re

def make_markov_model(data):
    markov_model = dict()

    for i in range(0, len(data) - 1):
        if data[i] in markov_model:
            markov_model[data[i]].update([data[i + 1]])
        else:
            markov_model[data[i]] = Dictogram([data[i + 1]])
    return markov_model

def make_higher_order_markov_model(order, data):
    markov_model = dict()

    for i in range(0, len(data) - order):
        window = tuple(data[i: i + order])
        if window in markov_model:
            markov_model[window].update(data[i + order])
        else:
            markov_model[window] = Dictogram(data[i + order])
    # print(markov_model)
    return markov_model

def generate_random_start(model):
    if 'END' in model:
        seed_word = 'END'
        while seed_word == 'END':
            seed_word = model['END'].return_weighted_random_word()
        return seed_word
    i = 0
    randint = random.randint(0, len(model.keys()) - 1)
    for key in model.keys():
        # print(key)
        if i == randint:
            return key
        i = i + 1

def generate_random_sentence(length, markov_model):
    current_word = generate_random_start(markov_model)
    sentence = [current_word]
    i = 0
    while (i < length - 1):
        current_dictogram = markov_model.get(current_word)
        random_weighted_word = current_dictogram.return_weighted_random_word()
        current_word = random_weighted_word
        sentence.append(current_word)
        i = i + 1
    sentence[0] = sentence[0].capitalize()
    return ' '.join(sentence) + '.'

# new method for higher order markov model?
def generate_higher_order_random_sentence(length, higher_order_markov_model):
    current_key = generate_random_start(higher_order_markov_model)
    current_word = higher_order_markov_model.get(current_key).return_weighted_random_word()
    sentence = [current_word]
    i = 0
    while (i < length - 1):
        current_dictogram = higher_order_markov_model.get(current_key)
        random_weighted_word = current_dictogram.return_weighted_random_word()
        current_word = random_weighted_word
        sentence.append(current_word)
        for key in higher_order_markov_model.keys():
            if current_word in higher_order_markov_model[key]:
                current_key = key
        i = i + 1
    sentence[0] = sentence[0].capitalize()
    return ' '.join(sentence) + '.'