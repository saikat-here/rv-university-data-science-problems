"""
Description
You are given a list of string elements and asked to return a list which contains each element of the string in title case or in other words first character of the string would be in upper case and remaining all characters in lower case

Sample Input:
['VARMA', 'raj', 'Gupta', 'SaNdeeP']

Sample Output
['Varma', 'Raj', 'Gupta', 'Sandeep']
"""

import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

for i in range(len(input_list)):
    input_list[i] = input_list[i][0].upper() + input_list[i][1:].lower()
    
print(input_list)
