#SY ExTC
#Experiment No. 7
#10 points

#Dipika Tele
#Apr 20
#Given a non negative integer A, print all the pairs of integers(a,b) such that
#a and b are positive integers
#a<=b and
#a^2 + b^2 = A
#0 <= A
#A<=1000

#Problem statement is pretty clear, We just need to find such pairs who satisfies the Pythagoras theorem up-to that number.
#The idea is to put two nested loops and print those numbers whose squared sum is equal to the given number.



while (1):
	A=int(input('Enter the non-negative integer: '))
	if A<0 or A>1000:
		print('Invalid Input. Enter Again.')
	else:
		break
b=1
while b<A:
	for a in range(b+1):
		if a==0:
			continue
		if ((a**2 + b**2)==A):
			print('({},{})'.format(a,b))
	b=b+1
pythonassignment3.py
Displaying pythonassignment3.py.
