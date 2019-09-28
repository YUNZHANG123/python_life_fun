# Question: List all the prime numbers before a positive number
# input: num --> a positive number (if it is negative, it will become positive)
# output: list --> all the prime numbers before the input
# Purpose: practise the Python IO
# Sophia  20190914

#change the num to be positive
def abs():
    a = int(input())
    if a >= 0:
	    return a
    else:
	    return -a

#calculate all the prime num before the input
def sushu (num):
    for i in range (2,num):
        if num%i == 0:
           return(False) 
    else:
        return(True)
# add the prime numbers into a list
def uu():
    b = abs()
    ba=[]
    for i in range (2,b):
        if sushu(i):
            ba.append(i)
    return ba
		
if __name__ == "__main__":
    print(uu())