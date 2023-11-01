"""
Description
Convert a list ['Pythons syntax is easy to learn', 'Pythons syntax is very clear'] to a string using ‘&’. The sample output of this string will be:
Pythons syntax is easy to learn & Pythons syntax is very clear

Note that there is a space on both sides of '&' (as usual in English sentences).
"""
import ast,sys
input_str = (sys.stdin.read()).split(',')

string_1 = f"{input_str[0]} & {input_str[1]}"
print(string_1)
