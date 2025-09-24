# Question Name: Digit String Encryption
#
# Description:
# John encrypts a number string by applying a sequence of actions (I for increment, D for decrement)
# to each digit in the string. If incrementing goes beyond 9, it wraps around to 0.
# If decrementing goes below 0, it wraps around to 9.
#
# Input:
# - First line: string of digits.
# - Second line: string of actions (I or D), same length as the digit string.
#
# Output:
# - The encrypted number string.
#
# Method to Solve:
# 1. Read the digit string and actions string.
# 2. For each digit and its corresponding action:
#    - If action = 'I', increment digit by 1 (wrap using % 10).
#    - If action = 'D', decrement digit by 1 (wrap using % 10).
# 3. Build the result string from modified digits.
# 4. Print the encrypted string.
#
# Sample Input 0:
# 123
# IDD
#
# Sample Output 0:
# 212
#
# Sample Input 1:
# 456
# DDD
#
# Sample Output 1:
# 345
#
# Extra Test Case (wrap-around check):
# Input:
# 908

def encrypt_number(digits, actions):
    result = []
    for d , a in zip (digits, actions):
        num = int(d)
        if a =='I':
            num = (num + 1) %10 #wrap around after 9 -> 0
        elif a =='0':
            num = (num-1)%10
        result.append(str(num))
    return ' '.join(result)

digits = input().strip()
actions= input().strip()































# IDD
# Output:
# 097
