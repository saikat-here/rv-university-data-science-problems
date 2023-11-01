"""
Description
Split the string input_str = 'Kumar_Ravi_003' to the person's second name, first name and unique customer code. In this example, second_name= 'Kumar', first_name= 'Ravi', customer_code = '003'.

A sample output of the input 'Kumar_Ravi_003' is:

Ravi
Kumar
003
 

Note that you need to print in the order first name, last name and customer code.
"""

import ast,sys
input_str = sys.stdin.read()
splt = input_str.split("_")
first_name = splt[1]
second_name = splt[0]
customer_code = splt[2]
print(first_name)
print(second_name)
print(customer_code)
