# https://simple.wikipedia.org/wiki/Flesch_Reading_Ease
# http://www.readabilityformulas.com/flesch-reading-ease-readability-formula.php
'''

How to use the scale:

90-100 : Very Easy
80-89 : Easy
70-79 : Fairly Easy
60-69 : Standard
50-59 : Fairly Difficult
30-49 : Difficult
0-29 : Very Confusing

'''

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

def sentence_length(phrase):
    n = []
    phrase = phrase.split('.')
    clean_message = ''.join(phrase)
    for w in clean_message.split(' '):
        n.append(len(w))
    return np.mean(n)



def LEXIE(phrase):
    meansyll = np.mean(syllcount(phrase))
    sl = sentence_length(phrase)
    score = 206.835 - (1.015*sl)-(84.6*meansyll)
    return score


while True:
    phrase = input('phrase: ')
    print('The Flesch Readability Score is: ' + str(LEXIE(phrase)))
