# Problem Statement:
# Given a list of digits (0-9), convert each digit to its textual representation
# (e.g., 1 → "one") and count unordered pairs of digits whose sum of vowels
# in their text equals a given digit D.
#
# Input Format:
# - First line: N (number of digits)
# - Second line: N space-separated digits (0-9)
# - Third line: D (target sum of vowels)
#
# Constraints:
# 1 ≤ N ≤ 100
# 0 ≤ D ≤ 10
#
# Output Format:
# - Number of unordered pairs meeting the vowel sum condition
#
# Sample Input 0:
# 4
# 1 2 3 4
# 3
# Sample Output 0:
# 3
#
# Sample Input 1:
# 3
# 7 8 9
# 3
# Sample Output 1:
# 0
#
# Solution Approach:
# 1. Map each digit to its English word.
# 2. Count the vowels in each word (a, e, i, o, u).
# 3. For each unordered pair of digits, check if the sum of their vowel counts equals D.
# 4. Count all pairs that satisfy this condition.
#
# Example:
# Digits = [1,2,3,4]
# Words = ["one","two","three","four"]
# Vowel counts = [2,1,2,2]
# Pairs with sum = 3: (1,2),(2,3),(2,4) → total 3 pairs

digit_words={
    0:"zero", 1:"one", 2:"two", 3:"three",4:"four",
    5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"
    }

def count_vowels(word):
    vowels= set("aeiou")
    return sum(1 for ch in word if ch in vowels)

N = int(input().strip())
digits=list(map(int ,input().split()))
D=int(input().strip())

vowel_counts=[count_vowels(digit_words[d]) for d in digits]

count =0
for i in range(N):
    for i in range(N):
        for j in range(i+1, N):
            if vowel_counts[i]+vowel_counts[j]==D:
                count+=1
print(count)







































#
# Python Implementation:
