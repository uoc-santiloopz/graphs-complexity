from shared.utils import to_int

print("You are about to witness the power of the Havel-Hakimi algorithm...\n")
print("Enter your sequence of numbers, separated by spaces\n")

# variable to store the final result
graphical_seq = False
# ask for the space separated list
seq = input("What is the sequence?\n").split()
# map the list into integers and sort it
mapped = list(map(to_int, seq))
mapped.sort()

maxDegree = max(mapped)
degLength = len(mapped)

if maxDegree <= (degLength - 1):
    for i in range(1, degLength):
        print(i)
else:
    print("The sequence is not graphical\n")
