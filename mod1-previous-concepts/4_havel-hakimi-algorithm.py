from utils import to_int

print("You are about to witness the power of the Havel-Hakimi algorithm...\n")
print("Enter your sequence of numbers, separated by spaces\n")

seq = input("What is the sequence?\n").split()
mapped = list(map(to_int, seq))


print("Final sequence", list(mapped))