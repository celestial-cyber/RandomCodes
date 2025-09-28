# Question: String Transformation by Shifting Characters
#
# Problem Statement:
# Transform a string by replacing each character with the next character 
# in the alphabet (z becomes a) K times.
#
# Input Format:
# • First line: string (lowercase letters).
# • Second line: K.
#
# Constraints:
# • 1 ≤ string length ≤ 100
# • 1 ≤ K ≤ 10^9
#
# Output Format:
# • Transformed string.
#
# Approach:
# - Since alphabet has 26 letters, shifting by K is same as K % 26.
# - For each character:
#   - Convert to number using ord().
#   - Add shift and wrap with modulo 26.
#   - Convert back to character with chr().
#
# Sample Input 0:
# abc
# 2
# Sample Output 0:
# cde
#
# Sample Input 1:
# aaa
# 26
# Sample Output 1:
# aaa

s = input().strip()
k = int(input().strip())

shift = k % 26
result = []

for c in s:
    new_char = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
    result.append(new_char)

print("".join(result))
