import sys

if __name__ == '__main__':
	limit = int(sys.argv[1])

def is_divisble(a,b):
	"""checks if 2 numbers are divisible by each"""
	if a%b==0:
		return True
	else:
		return False
def fizzbuzz(limit):
	"""prints fizbuzz, fizz or buzz or x depending upon if divisble ny 15, 5 ,3 or not divisible by them"""
	for x in range(1, limit+1):
		if is_divisble(x,15):
			print 'fizzbuzz'
		elif is_divisble(x,5):
			print 'fizz'
		elif is_divisble(x,3):
			print 'buzz'
		else:
			print x

fizzbuzz(limit)


