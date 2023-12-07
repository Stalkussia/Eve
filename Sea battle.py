import random
import os

def clear():
    os.system('clear')
def play_game():
    board = [[" ", "A ", "B ", "C ", "D ", "E ", "F ", "G "," "],
             ["1", "--", "--", "--", "--", "--", "--", "--"," "],
             ["2", "--", "--", "--", "--", "--", "--", "--"," "],
             ["3", "--", "--", "--", "--", "--", "--", "--"," "],
             ["4", "--", "--", "--", "--", "--", "--", "--"," "],
             ["5", "--", "--", "--", "--", "--", "--", "--"," "],
             ["6", "--", "--", "--", "--", "--", "--", "--"," "],
             ["7", "--", "--", "--", "--", "--", "--", "--"," "],
             [" ", "  ", "  ", "  ", "  ", "  ", "  ", "  "," "]]

    for i in board:
        print(*i)
    
    def place_ships():
        ships_left = 7
        dir = random.randint(0,1)
        if dir == 0:
            dir = [random.randint(1,5), random.randint(1,7)]
            three1 = dir[0],dir[1]
            three2 = dir[0]+1,dir[1]
            three3 = dir[0]+2,dir[1]
            col = (three1,three2,three3),(dir[0]-1,dir[1]),(dir[0]-1,dir[1]+1),(dir[0]-1,dir[1]-1),(dir[0],dir[1]-1),(dir[0],dir[1]+1),(dir[0]+1,dir[1]-1),(dir[0]+1,dir[1]+1),(dir[0]+2,dir[1]-1),(dir[0]+2,dir[1]+1),(dir[0]+3,dir[1]-1),(dir[0]+3,dir[1]),(dir[0]+3,dir[1]+1)
            col1 = str(col)
        else:
            dir = [random.randint(1,7), random.randint(1,5)]
            three1 = dir[0],dir[1]
            three2 = dir[0],dir[1]+1
            three3 = dir[0],dir[1]+2
            col = (three1,three2,three3),(dir[0]+ 1, dir[1]), (dir[0]-1,dir[1]),(dir[0],dir[1]-1),(dir[0]-1,dir[1]+1),(dir[0]-1, dir[1]+2),(dir[0]+ 1, dir[1]+2),(dir[0]-1,dir[1]-1),(dir[0]+1,dir[1]-1),(dir[0]+1,dir[1]+1),(dir[0],dir[1]+3),(dir[0]-1,dir[1]+3),(dir[0]+1,dir[1]+3)
            col1 = str(col)
        dir = random.randint(0,1)
        if dir == 0:
            dir = [random.randint(1,6), random.randint(1,7)]
            two1 = dir[0],dir[1]
            pik1 = str(two1)
            two2 = dir[0],dir[1]+1
            pik2 = str(two2)
            coll = (two1,two2),(dir[0]-1,dir[1]-1),(dir[0]-1,dir[1]),(dir[0]-1,dir[1]+1),(dir[0]-1,dir[1]+2),(dir[0]+1,dir[1]-1),(dir[0]+1,dir[1]),(dir[0]+1,dir[1]+1),(dir[0]+1,dir[1]+2),(dir[0],dir[1]-1),(dir[0],dir[1]+2)
            coll1 = str(coll)
        elif dir == 1:
            dir = [random.randint(1,7), random.randint(1,6)]
            two1 = dir[0],dir[1]
            pik1 = str(two1)
            two2 = dir[0]+1,dir[1]
            pik2 = str(two2)
            coll = (two1,two2),(dir[0]-1,dir[1]-1),(dir[0],dir[1]-1),(dir[0]+1,dir[1]-1),(dir[0]+2,dir[1]-1),(dir[0]-1,dir[1]+1),(dir[0],dir[1]+1),(dir[0]+1,dir[1]+1),(dir[0]+2,dir[1]+1),(dir[0]-1,dir[1]),(dir[0]+2,dir[1])
            coll1 = str(coll)
        dir = random.randint(0,1)
        if dir == 0:
            dir = [random.randint(1,6), random.randint(1,7)]
            two3 = dir[0],dir[1]
            pik3 = str(two3)
            two4 = dir[0],dir[1]+1
            pik4 = str(two4)
            coll = (two1,two2),(dir[0]-1,dir[1]-1),(dir[0]-1,dir[1]),(dir[0]-1,dir[1]+1),(dir[0]-1,dir[1]+2),(dir[0]+1,dir[1]-1),(dir[0]+1,dir[1]),(dir[0]+1,dir[1]+1),(dir[0]+1,dir[1]+2),(dir[0],dir[1]-1),(dir[0],dir[1]+2)
            coll1 = str(coll)
        else:
            dir = [random.randint(1,7), random.randint(1,6)]
            two3 = dir[0],dir[1]
            pik3 = str(two3)
            two4 = dir[0]+1,dir[1]
            pik4 = str(two4)
            coll = (two1,two2),(dir[0]-1,dir[1]-1),(dir[0],dir[1]-1),(dir[0]+1,dir[1]-1),(dir[0]+2,dir[1]-1),(dir[0]-1,dir[1]+1),(dir[0],dir[1]+1),(dir[0]+1,dir[1]+1),(dir[0]+2,dir[1]+1),(dir[0]-1,dir[1]),(dir[0]+2,dir[1])
            coll1 = str(coll)

        ship1 = random.randint(1,7),random.randint(1,7)
        one1 = str(ship1)
        ship2 = random.randint(1,7),random.randint(1,7)
        one2 = str(ship2)
        ship3 = random.randint(1,7),random.randint(1,7)
        one3 = str(ship3)
        ship4 = random.randint(1,7),random.randint(1,7)
        one4 = str(ship4)
            
        while two1 == two3 or two1 == two4 or two2 == two3 or two2 == two4 or col1.count(pik1)==1 or col1.count(pik2)==1 or col1.count(pik3)==1 or col1.count(pik4)==1 or coll1.count(one1)==1 or coll1.count(one2)==1 or coll1.count(one3)==1 or coll1.count(one4)==1 or col1.count(one1)==1 or col1.count(one2)==1 or col1.count(one3)==1 or col1.count(one4)==1:
            place_ships()
        

        c = 0
        d = 0

        while ships_left != 0:
            try:
                row = int(input('Enter the row number from 1-7: '))
                column = int(input('Enter the column number from 1-7: '))
                clear()
            except ValueError:
                print('Enter valid value! ')
                continue
            if row > 0 and row < 8 and column > 0 and column < 8:
                if board[row][column] == "XX" or board[row][column] == "00":
                    print("\nYou have already shoot that place!\n")
                    continue
                elif (row, column) == ship1 or (row, column) == ship2 or (row, column) == ship3 or (row, column) == ship4:
                    print("You sunk the ship! ")
                    board[row][column] = "XX"
                    ships_left -= 1
                elif (row, column) == two1 or (row, column) == two2 or (row, column) == two3 or (row, column) == two4:
                    print("You hit the ship! ")
                    board[row][column] = "XX"
                    c += 1
                    if c == 2 or c == 4:
                        print('You sunk The ship!')
                        ships_left -= 1
                elif (row,column) == three1 or (row,column) == three2 or (row,column) == three3:
                    print('You hit the ship!')
                    board[row][column] = "XX"
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
            if ships_left == 0:
                break
    place_ships()
play_game()

