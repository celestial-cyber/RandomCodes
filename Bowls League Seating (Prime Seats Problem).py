# Problem: Bowls League - Prime Seats
#
# Problem Statement:
# In a league, there are H seats numbered from 1 to H.
# Only prime-numbered seats are valid for players.
# Players are seated at every P-th available prime seat.
# Find how many players are seated.
#
# Constraints:
# 1 ≤ H ≤ 10^6
# 1 ≤ P ≤ H
#
# Approach:
# - Use Sieve of Eratosthenes to count primes ≤ H.
# - The number of players = floor(total_primes / P).
#
# Example 1:
# Input: 30 2
# Primes ≤ 30 = [2,3,5,7,11,13,17,19,23,29] → 10 primes
# Every 2nd prime → 10//2 = 5 players
# Output: 5
#
# Example 2:
# Input: 50 5
# Primes ≤ 50 = 15 primes
# Every 5th prime → 15//5 = 3 players
# Output: 3

def sieve(n):
    prime=[1]*(n+1)
    prime[0]=prime[1]=0
    for i in range(2,int(n**0.5)+1):
        if prime[i]:
            for j in range(i*i,n+1,i):
                prime[j]=0
    return sum(prime)   # count of primes ≤ n

H,P = map(int,input().split())
prime_count = sieve(H)
print(prime_count // P)
