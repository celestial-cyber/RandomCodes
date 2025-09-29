# Problem Name: Compare Bank Interest Slabs

# Problem:
# Compare interest rates offered by two banks over a tenure T.
# Each bank provides multiple slabs with different periods and rates.
# Determine which bank offers better returns using compound interest.
# 
# Input Format:
# First line: T (tenure in years)
# Second line: N1 (number of slabs for Bank A)
# Next N1 lines: period and rate for Bank A
# Next line: N2 (number of slabs for Bank B)
# Next N2 lines: period and rate for Bank B
#
# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ N1,N2 ≤ 10
# 1 ≤ period ≤ T
# 0.1 ≤ rate ≤ 100.0
#
# Output Format:
# "Bank A" or "Bank B" depending on which gives higher compound interest.
#
# Sample Input:
# 5
# 2
# 2 5.0
# 3 6.0
# 1
# 5 5.5
#
# Sample Output:
# Bank A

T = int(input())

N1 = int(input())
bankA = [tuple(map(float, input().split())) for _ in range(N1)]

N2 = int(input())
bankB = [tuple(map(float, input().split())) for _ in range(N2)]

def calc_amount(slabs):
    amt = 1.0
    years_passed = 0
    for period, rate in slabs:
        period = int(period)
        if years_passed + period > T:
            period = T - years_passed
        amt *= (1 + rate/100) ** period
        years_passed += period
        if years_passed >= T:
            break
    return amt

amtA = calc_amount(bankA)
amtB = calc_amount(bankB)

if abs(amtA - amtB) < 1e-6:
    print("Bank A")  # tie-breaker to Bank A if both give same amount
elif amtA > amtB:
    print("Bank A")
else:
    print("Bank B")
