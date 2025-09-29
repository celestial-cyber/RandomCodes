import sys

def knapsack(N, W, items):
    dp = [0] * (W + 1)
    for wt, val in items:
        for w in range(W, wt - 1, -1):  # go backwards
            dp[w] = max(dp[w], dp[w - wt] + val)
    return dp[W]

if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    N, W = map(int, data[:2])
    items = [(int(data[i]), int(data[i+1])) for i in range(2, 2*N+2, 2)]
    print(knapsack(N, W, items))
