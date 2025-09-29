# Question Name: Rock Sample Classification
#
# Description:
# Juan classifies rock samples by their size (in ppm) into R ranges.
# Given S sample sizes and R ranges (each with a min and max),
# determine how many samples fall into each range.
#
# Input:
# - First line: S (number of samples), R (number of ranges).
# - Second line: S space-separated integers (sample sizes).
# - Next R lines: two integers (min and max of range).
#
# Output:
# - R space-separated integers, each representing the count of samples in the corresponding range.
#
# Constraints:
# - 1 ≤ S ≤ 10^6
# - 1 ≤ R ≤ 100
# - 1 ≤ min, max, sample size ≤ 10^9
#
# Method to Solve:
# 1. Sort the list of sample sizes.
# 2. For each range [min, max]:
#    - Use binary search (bisect_left and bisect_right) to find how many samples
#      fall between min and max (inclusive).
#    - Count = right_index - left_index.
# 3. Print the counts space-separated.
#
# Complexity:
# - Sorting: O(S log S)
# - Each range query: O(log S)
# - Total: O(S log S + R log S), efficient for large input sizes.
# Sample Input 0:
# 5 2
# 345 604 811 300 350
# 300 700
# 701 900
#
# Sample Output 0:
# 4 1
#
# Sample Input 1:
# 4 2
# 50 60 70 80
# 0 60
# 61 100

import bisect
S, R= map(int , input().split())
samples = list (map(int , input().split()))

samples.sort()

results =[]
for _ in range(R):
    low , high= map(int , input().split())
    left = bisect.bisect_left(samples,low)
    right = bisect.bisect_right(samples , high)
    results.append(str(right-left))

print(" " . join(results))



































#
# Sample Output 1:
# 2 2
