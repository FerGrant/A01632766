"
Create a function that takes a string and returns the number (count) of vowels contained within it.
"
def count_vowels(txt):
	count = 0
	vowels = "aeiou"
	for letter in txt:
			if letter in vowels:
				count += 1
	return count
