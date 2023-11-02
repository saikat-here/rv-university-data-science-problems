"""
Description
Let’s say you have two lists, A and B. Identify the elements which are common in the two lists, A and B and return them in a sorted manner. For example 


Sample Input :

A = [5,1,3,4,4,5,6,7]

B = [3,3,5,5, 1 ,7 ,2]


Sample Output:

[1,3,5,7]


If you observe the sample output here, you can see that:

Though value 5 is repeated twice in both lists, in the final output, it is present only once.
The values are returned in a sorted manner with values increasing.
"""
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
list_1 = input_list[0]
list_2 = input_list[1]

set1 = set(list_1)
set2 = set(list_2)
answer= list(set1 & set2)

print(answer)
