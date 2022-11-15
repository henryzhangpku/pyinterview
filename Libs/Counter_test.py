from collections import Counter
words = "if there was there was but if \
... there was not there was not".split()
print(words)
counts = Counter(words) #input as a list
print(counts)
print(counts.most_common(2))