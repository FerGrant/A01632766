""
Create a function that takes a number as an argument and returns "even" for even numbers and "odd" for odd numbers.
""
def isEvenOrOdd(num):
	if num & 1:
		return "odd"
	else:
		return "even"
