def rotate(nums, k):
    n= len(nums)
    k%=n ##Reduces k modulo n. If k is larger than n, rotating by k is the same as rotating by k % n.
##Note: if n == 0 this will raise an error, so in practice you might want to add if n == 0: return before this line.
    def rev(i, j):
        while i < j:
            nums[i], nums[j]=nums[j],nums[i]
            i+=1;j-=1
    rev(0 , n-1) ##Reverse the entire array. This step turns the array into its full reverse.
    rev(0 , k-1)
    rev(k , n-1)

arr=[1,2,3,4,5,6,7]
rotate(arr,3)
print(arr)

"""Reverse the first k elements (which, after the full reverse, correspond to the last k elements of the original array).

rev(k, n-1)
Reverse the remaining n-k elements (which correspond to the first n-k elements of the original array).
Step-by-step trace for your example arr = [1,2,3,4,5,6,7] and k = 3
Start: [1, 2, 3, 4, 5, 6, 7]
After n = 7 and k %= n → k = 3.
First rev(0,6) — reverse entire array
swap 0 & 6: [7,2,3,4,5,6,1]
swap 1 & 5: [7,6,3,4,5,2,1]
swap 2 & 4: [7,6,5,4,3,2,1]
stop (i == j) → result: [7,6,5,4,3,2,1]
Second rev(0,2) — reverse first k elements
subarray before: [7,6,5] → after reversing → [5,6,7]
array becomes: [5,6,7,4,3,2,1]
Third rev(3,6) — reverse from index k to end
subarray before: [4,3,2,1] → after reversing → [1,2,3,4]
final array: [5,6,7,1,2,3,4]
This final array is the input rotated right by 3 positions.
Complexity and notes
Time complexity: O(n), because each element is moved a constant number of times.
Space complexity: O(1) additional memory, in-place.
Edge cases: if k == 0 nothing changes. If n == 0 add a guard if n == 0: return. Negative k is not handled by this code."""

"""Why the 3-step reversal works
Think of the array as two parts after rotation:
The last k elements [5,6,7] should come to the front.
The first n−k elements [1,2,3,4] should move to the back.
So the target order is:
[last k elements] + [first n-k elements]
Trick: Using Reversal to Achieve Rotation
Reverse the whole array
[1,2,3,4,5,6,7] → [7,6,5,4,3,2,1]
Now the desired two groups are in place, but each group is reversed.
Group 1: [7,6,5] (these are the last 3 from original, reversed)
Group 2: [4,3,2,1] (the first 4 from original, reversed)
Reverse the first k elements[7,6,5] → [5,6,7]

This restores Group 1 (the last k elements) into the correct order.
Reverse the remaining n−k elements[4,3,2,1] → [1,2,3,4]
This restores Group 2 (the first n−k elements) into the correct order.
Final result: [5,6,7,1,2,3,4]. ✅"""
