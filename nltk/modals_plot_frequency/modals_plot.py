'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

Created on 9 janv. 2016

@author: combo

'''
import nltk
from numpy import arange
from matplotlib import pyplot


colors = 'rgbcmyk' # red, green, blue, cyan, magenta, yellow, black 

def bar_char(categories, words, counts):
    "Plot a bar chart showing counts for each word by category"
    ind = arange(len(words))
    width = 1 / (len(categories) + 1)
    bar_groups = []
    for c in range(len(categories)):
        bars = pyplot.bar(ind+c*width, counts[categories[c]], width, color=colors[c % len(colors)])
        bar_groups.append(bars)
    pyplot.xticks(ind+width, words)
    pyplot.legend([b[0] for b in bar_groups], categories, loc = 'upper left')
    pyplot.ylabel('Frequency')
    pyplot.title('Frequency of six modal verbs bay genre')
    pyplot.show()

genres = ['news', 'religion', 'hobbies', 'government','adventure']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfdist = nltk.ConditionalFreqDist(
                                  (genre, word)
                                  for genre in genres
                                  for word in nltk.corpus.brown.words(categories = genre)
                                  if word in modals
                                  )
counts = {}
for genre in genres:
    counts[genre] = [cfdist[genre][word] for word in modals]
bar_char(genres, modals, counts)  
