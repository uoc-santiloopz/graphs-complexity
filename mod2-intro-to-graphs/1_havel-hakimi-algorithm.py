from shared.utils import to_int

print("You are about to witness the power of the Havel-Hakimi algorithm...\n")
print("Enter your sequence of numbers, separated by spaces\n")

# variable to store the final result
graphical_seq = False
# ask for the space separated list
seq = input("What is the sequence?\n").split()
# map the list into integers and sort it
intSeq = list(map(to_int, seq))
sortedIntSeq = sorted(intSeq, reverse=True)

maxDegree = max(sortedIntSeq)
degLength = len(sortedIntSeq)

print(sortedIntSeq)
# if maxDegree <= (degLength - 1):
#     for i in range(1, degLength):
#         print(i)
# else:
#     print("The sequence is not graphical\n")

# Havel-Hakimi algorithm, determines weather a sequence of numbers can be
# the degrees of the edges of a simple graph
def sequence_is_graphic(seq):

    # Perform operations until one of the stopping conditions is met

    # sort the sequence
    sortedIntSeq = sorted(seq, reverse=True)

    # check if all elements are equal to 0
    if sortedIntSeq[0] == 0 and sortedIntSeq[len(sortedIntSeq)-1] == 0:
        return True

    # store the first element in a variable and delete it from the list
    firstEl = sortedIntSeq[0]
    sortedIntSeq = sortedIntSeq[:1]

    # check if there are elements left of the list
    if len(firstEl) > len(sortedIntSeq):
        return False

    # substract the first element from the
