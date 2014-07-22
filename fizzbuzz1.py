x=int(raw_input("Enter a number: "))
print "Fizz buzz counting up to %d" %(x)
n=1
while n<=x:
	if n%3==0 and n%5==0:
		print "fizz buzz"
	elif n%3==0:
		print "fizz"
	elif n%5==0:
		print "buzz"
	else:
		print n,
	n+=1
