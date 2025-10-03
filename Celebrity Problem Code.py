"""Find the row with the maximum number of 1s in a boolean sorted row matrix.

Celebrity problem (who is known by everyone but knows no one).

The input format and constraints you pasted match the celebrity problem, not the "maximum number of 1s" problem. Let me separate them and solve both so you’re clear.

✅ Problem 1: First row with maximum number of 1s

Each row is sorted (so all 0s come before 1s).

We want the index of the first row with the maximum number of 1s.

Efficient Approach (O(n + m)):

Start at the top-right corner of the matrix.

If you see a 1, move left.

If you see a 0, move down.

Keep track of the row where you moved leftmost (that row has maximum 1s).

Example:
Matrix:
0 0 1 1
0 1 1 1
0 0 0 1
Start at (0,3). → 1 → move left.

At (0,2). → 1 → move left.

At (0,1). → 0 → move down.

Row 1 has more 1s. Answer = row 1.

✅ Problem 2: Celebrity Problem
Matrix M, where M[i][j] = 1 means i knows j.
Celebrity = A person known by everyone but knows no one.
Constraint M[i][i] = 0 ensures no self-knowledge.
Algorithm (O(N)):
Start with two pointers a=0, b=N-1.
f M[a][b] == 1 → a cannot be celebrity → a++.Else → b cannot be celebrity → b--.
At the end, a will be the candidate.
Verify:
Row of a must be all 0s.
Column of a must be all 1s (except diagonal).
If both true → a is celebrity. Otherwise → no celebrity (-1).
⚡ Example Input:
4
0 1 1 0
0 0 1 0
0 0 0 0
0 1 1 0
Candidate after elimination = 2.

Row 2 = all 0s ✅"""

def findCelebrity(M, N):
    # Step 1: Find candidate using elimination
    a, b = 0, N - 1
    while a < b:
        if M[a][b] == 1:
            # a knows b → a cannot be celebrity
            a += 1
        else:
            # a does not know b → b cannot be celebrity
            b -= 1

    candidate = a

    # Step 2: Verify candidate
    for i in range(N):
        if i != candidate:
            # candidate should not know i, and everyone should know candidate
            if M[candidate][i] == 1 or M[i][candidate] == 0:
                return -1
    return candidate


# ---------- Input ----------
N = int(input().strip())
M = []
for _ in range(N):
    M.append(list(map(int, input().split())))

print(findCelebrity(M, N))




Column 2 = all 1s except self ✅
Answer = 2."""
