import numpy as np
import re
import string
from nltk.corpus import cmudict
d = cmudict.dict()


def nsyl(word):
  return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]


def syllcount(phrase):
    n = []
    phrase = [x for x in phrase if x not in string.punctuation]
    clean_message = ''.join(phrase)
    for w in clean_message.split(' '):
        n.append(nsyl(w)[0])
    return n

def word_length(phrase):
    n = []
    phrase = [x for x in phrase if x not in string.punctuation]
    clean_message = ''.join(phrase)
    for w in clean_message.split(' '):
        n.append(len(w))
    return n


while True:
    phrase = input('phrase: ')
    meansyll = np.mean(syllcount(phrase))
    meanwordlen = np.mean(word_length(phrase))
    print(syllcount(phrase))
    print('average number of sylables: ' + str(meansyll))
    print('average word length: ' + str(meanwordlen))
    print('the number of words are: ' + str(len(phrase)))
    score = (meanwordlen*meansyll)
    print('the altarac score is: ' + str(score))
