"""Algorithm

Observation:

Each row is sorted (0 … 0 1 … 1).

So if we find the first 1 in a row, the number of 1s = M - index_of_first_1.

Approach 1 (Binary Search, O(N log M))

For each row, use binary search to find the first 1.

Compute count of 1s.

Keep track of max count and row index.

Approach 2 (Optimized, O(N + M))

Start from top-right corner of the matrix.

If we see 1, move left (this row may have more 1s).

If we see 0, move down.

Track the row index where we moved leftmost → that row has maximum 1s.

👉 We’ll use Approach 2 because it’s faster.

🔹 Time Complexity

Each step moves either left or down, at most N + M steps.

So complexity = O(N + M).

Space = O(1)."""

🔹 Python Code (Optimized O(N+M))
def rowWithMaxOnes(matrix, N, M):
    # Start from top-right corner
    row, col = 0, M - 1
    max_row = -1

    while row < N and col >= 0:
        if matrix[row][col] == 1:
            max_row = row   # update row (this row has more 1s)
            col -= 1        # move left
        else:
            row += 1        # move down
    
    return max_row


# -------- Input --------
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# Convert into 2D matrix
matrix = []
for i in range(N):
    matrix.append(arr[i*M:(i+1)*M])

print(rowWithMaxOnes(matrix, N, M))

🔹 Example Run

"""Input

2 4
0 0 1 1
1 1 1 1


Step

Start at (0,3) = 1 → move left → (0,2) = 1 → left → (0,1) = 0 → down → row=1

Row 1 has more 1s → answer = 1

Output

1"""
