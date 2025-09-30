""" Boyer Moore voting algorithm -> given an array of size n find the element that appeasr more than n/2 times - assume such an element exists
approach -> keeep the candidate and a count , traverse the array -> if count = 0 pick current as candidate , else if current and candidate - increment count else document count - the cancidate and the end is the majrity element

"""

def majority_element(nums):
    count , candidate = 0 , None
    for num in nums:
        if count ==0:
            candidate = num
        count +=(1 if num == candidate else -1)
    return candidate

print(majority_element([3,2,3]))
print(majority_element([2,1,3,4,1,1,2,2,2]))
