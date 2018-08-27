""
Create a function that takes a list of numbers and returns the sum of the two lowest positive numbers.
""

def sum_two_smallest_nums(lst):
	lst = [item for item in lst if item >= 0]
	i=min(lst)
	lst.remove(i)
	j=min(lst)
	return i+j
