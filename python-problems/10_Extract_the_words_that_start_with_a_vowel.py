"""
Description
Extract the words that start with a vowel from a list input_list=[wood, old, apple, big, item, euphoria] using list comprehensions.

Sample Input:
['wood','old','apple','big','item','euphoria']

Sample Output:
﻿['old', 'apple', 'item', 'euphoria']
 """
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

list_vowel = [ word for word in input_list if word[0].upper()  in ["A","E","I","O","U"]]

print(list_vowel)
