# Let me know the formula!
print("The r-ordered-sample without repetition are named PERMUTATIONS\n")
print("You know, the formula for permutation calculation is the following:\n")
print("P(n) = V(n, n) = n!\n")
print("Where n is the number of ELEMENTS in the SET, and R is the samples taken in the function\n")
print("///////////////////////////////\n")
print("///////////////////////////////\n")
print("///////////////////////////////\n")
print("///////////////////////////////\n")
print("NOW.... LET US CALCULATE!!!\n")

# CALCULATE!
n = int(input("How many ELEMENTS does the SET have?\n"))
factorial = 1

print("So... we want to calculate P(%(n)s) = %(n)s!\n" % { "n": n })

if n > 1:
   for i in range(1, n + 1):
       factorial = factorial * i

print("The total number of permutations is ", factorial)
