"""how to solve this problem Problem
Submissions
Leaderboard
Discussions
Find the length of the longest common subsequence between two strings.
Input Format
Two strings (lowercase letters).
Constraints
1≤string length ≤ 1000
Output Format
Length of the longest common subsequence.
Sample Input 0
ABC
DEF
Sample Output 0
0
Sample Input 1
AAA
AAA
Sample Output 1
3


Problem Understanding
You are given two strings, and you need to find the length of the longest subsequence that appears in both strings.
Subsequence: A sequence that can be derived from another sequence by deleting some elements without changing the order.
Example:
ABC and AC → LCS = AC → length = 2
AAA and AAA → LCS = AAA → length = 3

Approach
We can solve this using Dynamic Programming.
Define DP Table:
Let dp[i][j] be the length of LCS of the first i characters of string A and first j characters of string B.
Recurrence Relation:
If characters match:
dp[i][j] = dp[i-1][j-1] + 1
If characters do not match:
dp[i][j] = max(dp[i-1][j], dp[i][j-1])

Initialization:
dp[0][*] = 0 and dp[*][0] = 0 because LCS with an empty string is 0.

Answer:
The length of LCS is dp[len(A)][len(B)]."""

# Read input
A = input().strip()
B = input().strip()

# Initialize DP table
n = len(A)
m = len(B)
dp = [[0] * (m + 1) for _ in range(n + 1)]

# Fill DP table
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# Output the result
print(dp[n][m])

        
