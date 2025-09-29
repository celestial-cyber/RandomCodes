# Problem: Range Sum and Update Queries
#
# Problem Statement:
# Given an array of N integers, perform Q queries of two types:
# 1. "sum l r"   -> print the sum of elements from index l to r (1-based indexing).
# 2. "update i v" -> update the element at index i to value v.
#
# Constraints:
# 1 ≤ N, Q ≤ 10^5
# 1 ≤ l ≤ r ≤ N
# 1 ≤ index ≤ N
# -10^9 ≤ value, array elements ≤ 10^9
#
# Approach:
# - Use a Fenwick Tree (Binary Indexed Tree) for O(log N) updates and prefix sums.
# - For "sum l r", compute prefix(r) - prefix(l-1).
# - For "update i v", adjust difference and update Fenwick Tree.
#
# Example:
# Input:
# 5 2
# 1 2 3 4 5
# sum 1 3
# update 2 10
#
# Output:
# 6

class FenwickTree:
    def __init__(self, n):
        self.tree = [0]*(n+1)
        self.n = n

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

N, Q = map(int, input().split())
arr = [0] + list(map(int, input().split()))  # 1-based indexing

fenwick = FenwickTree(N)
for i in range(1, N+1):
    fenwick.update(i, arr[i])

for _ in range(Q):
    query = input().split()
    if query[0] == "sum":
        l, r = map(int, query[1:])
        print(fenwick.query(r) - fenwick.query(l-1))
    else:  # update
        idx, val = int(query[1]), int(query[2])
        delta = val - arr[idx]
        arr[idx] = val
        fenwick.update(idx, delta)
