import string
def is_upper(word):
	for letter in word:
		if letter not in string.ascii_uppercase:
			return False
	return True

print(is_upper('Thanks Geir'))
print(is_upper('LOL'))

# string.ascii_letters
# string.ascii_uppercase
# string.ascii_lowercase
# string.digits
# string.hexdigits
# string.octdigits
# string.punctuation
# string.printable
# string.whitespace