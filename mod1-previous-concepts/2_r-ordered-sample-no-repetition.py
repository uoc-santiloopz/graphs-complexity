from factorial import factorial
from logs import letUsCalculate

# Let me know the formula!
print("The r-ordered-sample without repetition are named PERMUTATIONS\n")
print("You know, the formula for permutation calculation is the following:\n")
print("P(n) = V(n, n) = n!\n")
letUsCalculate()


# CALCULATE!
n = int(input("How many ELEMENTS does the SET have?\n"))
s = int(input("How many SAMPLES do we take?\n"))
diff = n - s

print("So... we want to calculate P(%(n)s) = %(n)s!/(%(n)s - %(s)s)!\n" % {"n": n, "s": s})

numerator = factorial(n)

denominator = factorial(diff)

res = numerator / denominator

print("The total number of permutations is ", int(res))
