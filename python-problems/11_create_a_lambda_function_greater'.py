"""
Description
Create a lambda function 'greater', which takes two arguments x and y and return x if x>y otherwise, y.

If x = 2 and y= 3, then the output should be 3.

Sample Input:
['9','3']

Sample Output:
﻿9
 """
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
a = int(input_list[0])
b = int(input_list[1])

greater =  lambda x,y: x if x>y else y

print(greater(a,b))
