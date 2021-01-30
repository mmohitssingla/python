from random import shuffle


def modify(word):
    new_word = list(word)
    shuffle(new_word)
    return ''.join(new_word)


words = ['apple', 'grapes', 'banana', 'pineapple', 'mango']
new_words = []

# for word in words:
#     new_words.append(modify(word))
#
# print(new_words)

print(list(map(modify, words)))
