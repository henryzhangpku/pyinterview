import random
all_words = "all the words in the world".split()
def get_random_word():
	return random.choice(all_words)

print(all_words)

def get_unique_words():
	words =set()
	for _ in range(1000):
		words.add(get_random_word()) #set.add

	return words

res=get_unique_words()
print(res)