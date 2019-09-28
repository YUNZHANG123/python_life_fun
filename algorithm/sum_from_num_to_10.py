# Question:Calculate the summation from a number(smaller than 10) to 10
# Input: num --> any number between 0 to 10
# Output: num --> the summation from input to 10
# Purpose: practise the Python IO
# Sophia  20190914

def func1(num):
    result = 0;
    while True:
        # The number has to be smaller than 10, otherwise the function will break.
        if num > 10:
            break
        # starting calculate --> num + (num+1) + (num + 2) +...+10
        result = result + num
        num = num +1
    return result


num = int(input())
print(func1(num))