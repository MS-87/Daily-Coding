"""
05/23/2018
FooBar challenge:
Write a function called FooBar that takes input integer n and prints all the numbers from 1 up to n in a new line.
If the number is divisible by 3 then print "Foo",
if the number is divisible by 5 then print "Bar"
and if the number is divisible by both 3 and 5, print "FooBar".
Otherwise just print the number.
"""


def foobar(t):
	"""
	Given a number, determines if it is divisible by 3, 5, or both
	then prints the appropriate texts
	"""
	foo = t % 3
	bar = t % 5
	x = 0  # determine if new line has to be done

	if not foo:
		print('Foo', end="")
		x = 1
	if not bar:
		print('Bar', end="")
		x = 1

	if x:
		print('')


def iterate(upper=100):
	"""
	receive a number, this is your upper limit
	iterate through all numbers up to arg
	"""

	for i in range(1, upper + 1):
		print(i)
		foobar(i)


number = int(input("Select # to foobar up to: "))

iterate(number)
