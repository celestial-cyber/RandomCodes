# Problem Restated:
# You’re given an array of N integers (which can be positive, negative, or zero). 
# You need to find the maximum sum of any contiguous subarray. 
#
# Approach (Kadane’s Algorithm):
# 1. Initialize two variables:
#    max_so_far = first element of the array. 
#    current_sum = first element of the array. 
#    These keep track of the best subarray found so far and the current running sum. 
# 2. Traverse the array from the second element onward:
#    - Update current_sum = max(current_element, current_sum + current_element). 
#    - Update max_so_far = max(max_so_far, current_sum). 
# 3. At the end, max_so_far holds the maximum subarray sum. 
#
# Edge Case:
# If all numbers are negative, the standard version that resets current_sum to 0 would give wrong output. 
# To handle this, initialize max_so_far and current_sum with the first element instead of -infinity or 0. 
#
# Complexity:
# Time: O(N).  Space: O(1).
#
# Sample Input 0:
# 3
# -1 -2 -3
# Sample Output 0:
# -1
#
# Sample Input 1:
# 4
# 1 2 3 4
# Sample Output 1:
# 10




def max_subarray_sum(arr):
    max_so_far=arr[0]
    current_sum=arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum+arr[i[])
        max_so_far = max(max_so_far, current_sum)

    return max_so_far

n= int(input())
arr= list(map(int , input().split()))

print(max_subarray_sum(arr))
