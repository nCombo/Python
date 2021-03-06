'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

Created on 9 janv. 2016

@author: combo
'''
import nltk
from matplotlib import use, pyplot
from numpy import arange

colors = 'rgbcmyk' # red, green, blue, cyan, magenta, yellow, black 

def bar_char(categories, words, counts):
    "Plot a bar chart showing counts for each word by category"
    ind = arange(len(words))
    width = 1 / (len(categories) + 1)
    bar_groups = []
    use('agg')
    for c in range(len(categories)):
        bars = pyplot.bar(ind+c*width, counts[categories[c]], width, color=colors[c % len(colors)])
        bar_groups.append(bars)
        
    pyplot.xticks(ind+width, words)
    pyplot.legend([b[0] for b in bar_groups], categories, loc = 'upper left')
    pyplot.ylabel('Frequency')
    pyplot.title('Frequency of six modal verbs bay genre')
    #pyplot.show()
    pyplot.savefig('modals_frequency.png') # we use pyplot.savefig() instead of pyplot.show() to save frequency
    print('Content-Type: text/html')
    print('<html><body>')
    print('<img src="modals.png"/>')
    print('</body></html>')

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



