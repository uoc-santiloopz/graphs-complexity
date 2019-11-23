from logs import letUsCalculate

# Let me know the formula!
print("You know, the formula for a r-ordered-sample with repetition is the following:\n")
print("VR(n,r) = n^r\n")
letUsCalculate()


# CALCULATE!
n = input("How many ELEMENTS does the SET have?\n")
r = input("How many samples are taken?\n")
print("So... we want to calculate VR(%(n)s, %(r)s) = %(n)s^%(r)s\n" % { "n": n, "r": r})

print("The result is ", pow(int(n), int(r)), "   OOOLRAIT :)\n")