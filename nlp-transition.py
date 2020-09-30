# Exercise 3.8 from Stanford NLP textbook
# Write a program to compute unsmoothed unigrams & bigrams
# https://www.nltk.org/
# Basically a big transition matrix

import nltk

nltk.download('gutenberg')
nltk.corpus.gutenberg.fileids()
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
print(len(emma)) # should return 192427

# Figure out a way to access individual words
# Create a dictionary, where key = "[word1]-[word2]" for the count
# Create a access function, where if the pair returns nothing, create the key,
        # set value = 1

# Iterator solution, assumes bigrams
# from collections import defaultdict
# matrix = defaultdict()
# iterator1 = iter(nltk.corpus.gutenberg.words("austen-emma.txt"))
# iterator2 = iter(nltk.corpus.gutenberg.words("austen-emma.txt"))
# next(iterator2)
# for (w1, w2) in zip(iterator1, iterator2):
#   if 

NUM_GRAM = 3

matrix = {}
last_n = []

for word in nltk.corpus.gutenberg.words("austen-emma.txt"):
  last_n.append(word)
  if len(last_n) < NUM_GRAM + 1:
    continue
  last_n = last_n[1:]

  if tuple(last_n[:NUM_GRAM - 1]) not in matrix:
    matrix[tuple(last_n[:NUM_GRAM - 1])] = {}
  if last_n[-1] not in matrix[tuple(last_n[:NUM_GRAM - 1])]:
    matrix[tuple(last_n[:NUM_GRAM - 1])][last_n[-1]] = 0
  matrix[tuple(last_n[:NUM_GRAM - 1])][last_n[-1]] += 1
  
# Given two words? predict the third? using the matrix we have
# w1 = str, w2 = str, return w3 as str
# iterate over all keys, return list values from all matching w1, w2 pairs #BAD
# get values from n-1 grams, return list of counts for possible w3 #Good??
print(matrix)
