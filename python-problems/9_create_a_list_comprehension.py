"""
Description
You are given an integer 'n' as the input. Create a list comprehension containing the squares of the integers from 1 till n^2 (including 1 and n), and print the list. 

For example, if the input is 4, the output should be a list as follows:
[1, 4, 9, 16]

The input integer 'n' is stored in the variable 'n'. 
"""
import ast, sys
n = int(input())

my_list = [i*i for i in range(1, n+1)]
print(my_list)
