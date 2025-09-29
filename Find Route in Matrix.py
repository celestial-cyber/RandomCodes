# Question: Route Finder in Matrix
#
# Problem Statement:
# Given an N × N matrix, find a continuous route from A[0][0] = 'A' 
# to destination 'D', avoiding hurdles (S, L, W, T). 
# Mark the route cells with 'R'. You can move up, down, left, or right.
#
# Input Format:
# • First line: N
# • Next N lines: N characters each (A, D, S, L, W, T, M)
#
# Constraints:
# • 2 ≤ N ≤ 10
#
# Output Format:
# • N lines of matrix with route marked as 'R'
#
# Approach:
# - Use DFS to explore paths from (0,0).
# - Avoid blocked cells (S, L, W, T).
# - Stop when destination 'D' is found.
# - Mark visited path as 'R' in final output.
#
# Sample Input 0:
# 2
# AW
# TD
# Sample Output 0:
# RW
# TD
#
# Sample Input 1:
# 2
# AM
# TD
# Sample Output 1:
# RR
# TD

N = int(input().strip())
grid = [list(input().strip()) for _ in range(N)]

blocked = {'S', 'L', 'W', 'T'}
dirs = [(-1,0), (1,0), (0,-1), (0,1)]
path = []

def dfs(x, y, visited):
    if grid[x][y] == 'D':
        return True
    visited.add((x, y))
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited and grid[nx][ny] not in blocked:
            path.append((nx, ny))
            if dfs(nx, ny, visited):
                return True
            path.pop()
    return False

path.append((0, 0))
dfs(0, 0, set())

for x, y in path:
    if grid[x][y] != 'D':
        grid[x][y] = 'R'

for row in grid:
    print(''.join(row))
