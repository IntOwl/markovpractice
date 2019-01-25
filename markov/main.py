import histograms

import markov

data = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']

model = markov.make_higher_order_markov_model(3, data)

# for key in model.keys():
    # print(key)
    # print(model[key])

start = markov.generate_random_start(model)

# print(start)

sentence = markov.generate_higher_order_random_sentence(8, model)

print(sentence)
