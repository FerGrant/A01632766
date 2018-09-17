""
Create a function that takes an integer and returns the factorial of that integer.
That is, the integer multiplied by all positive lower integers.
""

def factorial(num):
	nums = 1
	while num >= 1:
		nums = nums * num
		num = num - 1
	return nums
