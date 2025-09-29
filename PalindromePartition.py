import sys

def min_pal_partitions(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    dp = [0] * n
    pal = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i] = i + 1
        for j in range(i + 1):
            if s[i] == s[j] and (i - j <= 1 or pal[j+1][i-1]):
                pal[j][i] = True
                dp[i] = 1 if j == 0 else min(dp[i], dp[j-1] + 1)
    return dp[-1]

if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    if not data:
        sys.exit(0)
    s = data[0]
    print(min_pal_partitions(s))
