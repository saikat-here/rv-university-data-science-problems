"""
Description
Write a code to check if the string in input_str starts with a vowel or not. Print capital YES or NO.

For example, if input_str = 'analytics' then, your output should print 'YES'.

Sample Input:
alpha


Sample Output:
YES
"""
import ast,sys
input_str = sys.stdin.read()

if input_str[0].upper() in ["A","E","I","O","U"]:
    print("YES")
else:
    print("NO")
