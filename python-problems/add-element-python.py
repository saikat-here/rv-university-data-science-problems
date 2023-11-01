"""
Description
Add the element ‘Python’ to a tuple input_tuple = ('Monty Python', 'British', 1969). Since tuples are immutable, one way to do this is to convert the tuple to a list, add the element, and convert it back to a tuple.



Sample Input:

('Monty Python', 'British', 1969)



Sample Output:

﻿('Monty Python', 'British', 1969, 'Python')
 """
import ast,sys
input_str = sys.stdin.read()
input_tuple = ast.literal_eval(input_str)

temp_list = list(input_tuple)
temp_list.append("Python")
tuple_2 = tuple(temp_list)

print(tuple_2)
