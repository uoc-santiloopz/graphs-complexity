from factorial import factorial
from logs import letUsCalculate


# Let me know the formula!
print("The r-unordered-sample without repetition are named COMBINATIONS\n")
print("You know, the formula for combinations calculation is the following:\n")
print("C(n, r) = (n, r) = (n r)\n")
letUsCalculate()


# CALCULATE!
n = int(input("How many ELEMENTS does the SET have?\n"))
s = int(input("How many SAMPLES do we take?\n"))
diff = n - s

print("So... we want to calculate C(%(n)s, %(s)s) = %(n)s!/(%(n)s - %(s)s)! * %(s)s)!\n" % {"n": n, "s": s})

numerator = factorial(n)

denominator = factorial(s) * factorial(diff)

res = numerator / denominator

print("The total number of permutations is ", int(res))
