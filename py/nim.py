# nim.py
# Shana Elizabeth Henry
# CSCI 77800 Fall 2022
# collaborators: None
# consulted: Google

print(
    "Let's play Nim!  This version you have 12 stones to begin and the last player to take a stone wins!  You can remove between 1 and 3 stones.\n"
)


def getStones(curStones):
    global stones

    print("How many stones would you like to take? ", end='')
    take = int(input())
#this code helps if the user enters a number outside of 1 or 3, but if the user enters a character not a number then it produces an error. Next level would be to give an error message, but not end the program.
    if (take < 1 or take > 3):
        print("Number must be between 1 and 3.\n")
        getStones(curStones)
        return

    stones = curStones - take
    print(f'You take {take} stones.')
    print(f'{stones} stones remaining.\n')


def compTurn(curStones):
    global stones

    take = curStones % 4
    stones = curStones - take
    print(f'Computer takes {take} stones.')
    print(f'{stones} stones remaining.\n')


stones = 12
while (stones > 0):
    getStones(stones)
    compTurn(stones)

print("Computer wins!")
