#-------------------------------------------------------------------------------  
#--- Given: Two positive integers a and b (a<b<10000).
#--- Return: The sum of all odd integers from a through b, inclusively
#--- 
#--- Code written by: Edgar Garriga				edgargarriga.com
#-------------------------------------------------------------------------------
#we define the function. We don't check the PRECOND a<b<10000
def sumOdd (a,b):
	#create a var to save the sum
	result=0
	#loop from A to B
	for num in range(a, b):
		if (num % 2 != 0): #odd
			#if it's odd, add to the sum
			result= result + num
	#return the value
	return result
#we define the value of A and B
a= 5
b= 120
assert(a<b<1000) # check the precondition 
#we call the function and print the result
print "The sum of odds numbers from {} to {} is {}".format(a,b,sumOdd(a,b))
