# Question: calculate the sum of three prime numbers after a number 
# input: a --> a positive number 
# output: a num --> the sum of three prime numbers after the input
# Purpose: practise the Python IO
# Sophia  20190914

def is_sushu(a):
    for i in range(2,a): #TO dicide if it is a prime number
        if a%i == 0:
            return False
    else:
        return True

def sushu():
    num = int(input())
    sushu_list = []
    ba=0
    count=0
    while count < 3: #only the three prime numbers after the input
        if is_sushu(ba + num):
            sushu_list.append(ba+num)
            count = count + 1
        ba = ba + 1  
    return sushu_list

def cal_result(sushu_list):
    result = 0
    for sushu in sushu_list:
        result = result + sushu #calculate the sum 
    return result
	
if __name__ == "__main__":
    print(cal_result(sushu()))