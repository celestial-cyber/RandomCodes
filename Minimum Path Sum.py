"""Find the minimum cost to reach the bottom-right cell of an N ×N grid from the top-left, moving only right or down.

Input Format
First line: N. Next N lines: N integers (costs).
Constraints
1≤N≤100 0≤cost ≤109
Output Format
Minimum cost.
Sample Input 0
2
1 2
3 4
Sample Output 0
7
Sample Input 1
3
1 2 3
4 5 6
7 8 9
Sample Output 1
21
ChatGPT said:
This is a classic Dynamic Programming problem called Minimum Path Sum. Let’s solve it step by step.
Problem Understanding
You are given an N x N grid where each cell has a cost.
You start at the top-left (0,0) and want to reach the bottom-right (N-1, N-1) moving only right or down.
You need to find the minimum cost path.

Approach

We can solve this using Dynamic Programming:

Define DP Table:
Let dp[i][j] be the minimum cost to reach cell (i,j).

Recurrence Relation:

If you are at (i,j), you could have come from top (i-1,j) or left (i,j-1).

dp[i][j] = cost[i][j] + min(dp[i-1][j], dp[i][j-1])


For the first row, you can only come from the left.

For the first column, you can only come from above.

Initialization:

dp[0][0] = cost[0][0]
dp[0][j] = dp[0][j-1] + cost[0][j]  # first row
dp[i][0] = dp[i-1][0] + cost[i][0]  # first column


Answer:

dp[N-1][N-1] → minimum cost to reach bottom-right.

Python Code Example"""
# Read input
N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

# Initialize DP table
dp = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            dp[i][j] = cost[i][j]
        elif i == 0:
            dp[i][j] = dp[i][j-1] + cost[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + cost[i][j]
        else:
            dp[i][j] = cost[i][j] + min(dp[i-1][j], dp[i][j-1])

# Output the result
print(dp[N-1][N-1])

"""Explanation with Sample Input
Input:
2
1 2
3 4

DP Table:
1  3
4  7
Output: 7 ✅
Path: 1 → 2 → 4 (sum = 7)
Time and Space Complexity
Time Complexity: O(N^2)
Space Complexity: O(N^2) (can be optimized to O(N) using a single row if needed)"""
