# Function to check if a number is prime
def prime(n):
    # A number is prime if it's > 1 and has no divisors other than 1 and itself
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

# Input N (limit)
N = int(input())

s = 0   # running sum of consecutive primes (starting from 2)
c = 0   # count of primes that can be expressed as such a sum

# Step through all numbers up to N
for i in range(2, N + 1):
    if prime(i):            # check if i is a prime
        s += i              # add this prime to the running sum
        if s > N:           # if sum exceeds N, no need to continue
            break
        if prime(s):        # check if the running sum itself is prime
            c += 1          # if yes, increase our count

# Final result
print(c)
