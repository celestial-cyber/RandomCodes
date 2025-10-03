def triplet_sum(arr,n,x):
    arr.sort()

    for i in range(n-2):
        l, r=i+1, n-1
        while l< r:
            total= arr[i]+arr[l]+arr[r]
            if total==x:
                return 1
            elif total<x:
                l+=1
            else:
                r-=1
    return 0

n,x= map(int , input().split())
arr=list(map(int , input().split()))

print(triplet_sum(arr,n,x))
