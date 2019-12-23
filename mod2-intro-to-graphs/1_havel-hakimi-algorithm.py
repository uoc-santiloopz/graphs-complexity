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

    # check if there is some edge with a degree exceeding the total number of edges minus 1
    if max(seq) > len(seq) - 1:
        return False

    # Perform operations until one of the stopping conditions is met

    # sort the sequence
    sorted_int_seq = sorted(seq, reverse=True)

    # check if all elements are equal to 0
    if sorted_int_seq[0] == 0 and sorted_int_seq[len(sorted_int_seq)-1] == 0:
        return True

    # store the first element in a variable and delete it from the list
    first_el = sorted_int_seq[0]
    sorted_int_seq = sorted_int_seq[:1]

    # check if there are elements left of the list
    if len(first_el) > len(sorted_int_seq):
        return False

    # subtract the first element from the
    for i in range(first_el):
        sorted_int_seq[i] -= 1

        if sorted_int_seq[i] < 0:
            return False

    sequence_is_graphic(sorted_int_seq)
