# Problem Name: Galaxy Star Count

# Problem:
# A 3 × N grid of characters {'#', '*', '.'} represents galaxies ('#') and stars ('*').
# A galaxy is a connected component of '#' and '*' cells (connected horizontally or vertically).
# Count the number of stars in each galaxy.
#
# Input Format:
# First line: N (grid width)
# Second line: the 3 rows separated by commas, each with N characters
#
# Constraints:
# 1 ≤ N ≤ 100
#
# Output Format:
# Space-separated integers representing the number of stars in each galaxy
#
# Sample Input:
# 3
# #*#, *.*, #*#
#
# Sample Output:
# 4

from collections import deque

N = int(input())
rows = input().strip().split(',')
grid = [list(row.strip()) for row in rows]
visited = [[False]*N for _ in range(3)]

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    count = 0
    while q:
        x, y = q.popleft()
        if grid[x][y] == '*':
            count += 1
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 3 and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] in ('#','*'):
                visited[nx][ny] = True
                q.append((nx, ny))
    return count

res = []
for i in range(3):
    for j in range(N):
        if grid[i][j] in ('#','*') and not visited[i][j]:
            res.append(bfs(i,j))

print(*res)
