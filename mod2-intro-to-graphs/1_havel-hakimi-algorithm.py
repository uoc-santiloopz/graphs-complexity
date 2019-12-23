from shared.utils import sequence_is_graphic, to_int


print("You are about to witness the power of the Havel-Hakimi algorithm...\n")
print("Enter your sequence of numbers, separated by spaces\n")

# ask for the space separated list
seqInput = input("What is the sequence?\n").split()

# map the list into integers and sort it
intSeq = list(map(to_int, seqInput))

if sequence_is_graphic(intSeq):
    print("Bingo! Your sequence is graphic ^^")
else:
    print("BOOOP, Your sequence is NOOOT graphic")
