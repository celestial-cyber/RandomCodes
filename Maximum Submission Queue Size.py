"""
Problem:
---------
Steve makes N submissions at distinct timestamps. 
A submission made at time t removes any submission made exactly 5000 seconds before t. 
Find the maximum size of the submission queue at any point.

Input Format:
-------------
First line: N (number of submissions).
Second line: N space-separated integers (timestamps in ascending order).

Constraints:
------------
1 ≤ N ≤ 10^5
1 ≤ timestamps ≤ 10^9

Output Format:
--------------
An integer representing the maximum queue size.

Example 1:
----------
Input:
4
1000 6000 11000 16000

Process:
- At 1000: queue = {1000} → size = 1
- At 6000: removes 1000 (since 6000 - 5000 = 1000) → queue = {6000} → size = 1
- At 11000: removes 6000 (11000 - 5000 = 6000) → queue = {11000} → size = 1
- At 16000: removes 11000 (16000 - 5000 = 11000) → queue = {16000} → size = 1

Maximum size = 1

Output:
1

Example 2:
----------
Input:
3
1000 6000 11000

Process:
- At 1000: queue = {1000} → size = 1
- At 6000: removes 1000 → queue = {6000} → size = 1
- At 11000: removes 6000 → queue = {11000} → size = 1

Maximum size = 1

Output:
1
"""

# ----------------------
# Solution Logic:
# ----------------------
# 1. Keep track of all active submissions in a set.
# 2. For every new timestamp t:
#       - If (t - 5000) exists in the set, remove it
#       - Add the new submission t
#       - Update the maximum size of the set
# 3. The set size at each step = current queue size
# 4. The answer = maximum set size observed during the process.

# ----------------------
# Python Implementation:
# ----------------------

N = int(input())                       # Number of submissions
timestamps = list(map(int, input().split()))  # Timestamps (sorted, distinct)

active = set()    # to store current submissions
max_size = 0      # track maximum size of queue

for t in timestamps:
    # Step 1: Remove the submission exactly 5000 seconds before (if it exists)
    active.discard(t - 5000)  
    
    # Step 2: Add the current submission
    active.add(t)
    
    # Step 3: Update maximum queue size
    max_size = max(max_size, len(active))

# Final Answer
print(max_size)
