import random
import os
from socket import if_nameindex
c = 0
d = 0
def clear():
    os.system('clear')
def place_ship():
    return [random.randint(1,7),random.randint(1,7)]
def place_ships():
    return [random.randint(1,7),random.randint(1,7)]
def place_three():
    return [random.randint(1,7),random.randint(1,7)]
def play_game():
    board = [[" ", "A ", "B ", "C ", "D ", "E ", "F ", "G "],
             ["1", "--", "--", "--", "--", "--", "--", "--"],
             ["2", "--", "--", "--", "--", "--", "--", "--"],
             ["3", "--", "--", "--", "--", "--", "--", "--"],
             ["4", "--", "--", "--", "--", "--", "--", "--"],
             ["5", "--", "--", "--", "--", "--", "--", "--"],
             ["6", "--", "--", "--", "--", "--", "--", "--"],
             ["7", "--", "--", "--", "--", "--", "--", "--"]]

    for i in board:
        print(*i)
    ship1 = place_ship()
    ship2 = place_ship()
    ship3 = place_ship()
    ship4 = place_ship()
    ship_ones = [ship1,ship2,ship3,ship4]
    ship5 = place_ships()
    ship6 = place_ships()
    ship_twos = [ship5,ship6]
    ship7 = place_three()
    ships_left = 7
    while ships_left != 0:
        print('Enter the row number from 1-7: ')
        row = int(input())
        print('Enter the column number from 1-7: ')
        column = int(input())
        clear()
        if row > 0 and row < 8 and column > 0 and column < 8:
            if board[row][column] == "X" or board[row][column] == "00":
                board()
                print("\nYou have already shoot that place!\n")
                continue
            elif (row, column) == ship_ones:
                print('You sunk the ship! ')
                board[row][column] = "X"
                ships_left -= 1
            elif (row, column) == ship_twos:
                print('You hit the ship! ')
                board[row][column] = "X"
                c += 1
                if c == 2 or c == 4:
                    print('You sunk The ship!')
                    ships_left -= 1
            elif (row,column) == ship7:
                print('You hit the ship!')
                board[row,column] = "X"
                d += 1
                if d == 3:
                    print('You sunk the ship!')
                    ships_left -= 1
            else:
                board[row][column] = "00"
            for i in board:
                print(*i)
        else:
            print('Please, enter valid value: ')
            continue
a = []
play_game()