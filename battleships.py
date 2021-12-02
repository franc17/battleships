#see the readme.md file for description and data from typing import Any, Union, Tuple, List

import random
from tkinter import *
from tkinter import ttk

shots = 0 #global variable to count the total number of shots

def ship_position(ship): #returns a list of tuples giving all coordinates of a ship
    ship_pos = [(ship[0], ship[1])]
    if ship[2] == True:
        for i in range(1, ship[3]):
            ship_pos.append((ship[0], ship[1] + i))
    elif ship[2] == False:
        for i in range(1, ship[3]):
            ship_pos.append((ship[0] + i, ship[1]))
    return ship_pos


def is_sunk(ship):
    if ship[3] == len(ship[4]):
        return True
    else:
        return False


def ship_type(ship):
    if ship[3] == 4:
        return "battleship"
    elif ship[3] == 3:
        return "cruiser"
    elif ship[3] == 2:
        return "destroyer"
    else:
        return "submarine"


def is_open_sea(row, column, fleet):
    if (row > 9 or row < 0) or (column > 9 or column < 0):
        return False
    else:
        for ship in fleet:
            ship_pos = ship_position(ship)
            for pos in ship_pos:
                if row == pos[0]:
                    if column == pos[1] or column == pos[1]+1 or column == pos[1]-1:
                        return False
                if row == pos[0]-1:
                    if column == pos[1] or column == pos[1] + 1 or column == pos[1] - 1:
                        return False
                if row == pos[0]+1:
                    if column == pos[1] or column == pos[1]+1 or column == pos[1]-1:
                        return False
    return True


def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    hits = set()
    tempship = (row, column, horizontal, length, hits)
    ok = True
    ship_pos = ship_position(tempship)
    for pos in ship_pos:
        if is_open_sea(pos[0], pos[1], fleet) == False:
            ok = False
    if ok == True:
        return True
    else:
        return False


def place_ship_at(row, column, horizontal, length, fleet):
    hits = set()
    new_ship = (row, column, horizontal, length, hits)
    fleet.append(new_ship)


def randomly_place_all_ships():
    fleet = []
    finished = False
    row = random.randint(0, 10)
    col = random.randint(0, 10)
    horiz = random.choice([True, False])

    #battleship
    while finished == False:
        if ok_to_place_ship_at(row, col, horiz, 4, fleet) == True:
            place_ship_at(row,col,horiz,3,fleet)
            finished = True
        else:
            row = random.randint(0, 10)
            col = random.randint(0, 10)
            horiz = random.choice([True, False])
    finished = False

    #re-randomize the values
    row = random.randint(0, 10)
    col = random.randint(0, 10)
    horiz = random.choice([True, False])

    #cruisers
    while finished == False:
        if ok_to_place_ship_at(row, col, horiz, 3, fleet) == True:
            place_ship_at(row,col,horiz,3,fleet)
            finished = True
        else:
            row = random.randint(0, 10)
            col = random.randint(0, 10)
            horiz = random.choice([True, False])
    finished = False
    # re-randomize the values
    row = random.randint(0, 10)
    col = random.randint(0, 10)
    horiz = random.choice([True, False])

    while finished == False:
        if ok_to_place_ship_at(row, col, horiz, 3, fleet) == True:
            place_ship_at(row,col,horiz,3,fleet)
            finished = True
        else:
            row = random.randint(0, 10)
            col = random.randint(0, 10)
            horiz = random.choice([True, False])
    finished = False

    # re-randomize the values
    row = random.randint(0, 10)
    col = random.randint(0, 10)
    horiz = random.choice([True, False])

    #destroyers
    while finished == False:
        if ok_to_place_ship_at(row, col, horiz, 2, fleet) == True:
            place_ship_at(row,col,horiz,2,fleet)
            finished = True
        else:
            row = random.randint(0, 10)
            col = random.randint(0, 10)
            horiz = random.choice([True, False])
    finished = False

    # re-randomize the values
    row = random.randint(0, 10)
    col = random.randint(0, 10)
    horiz = random.choice([True, False])

    while finished == False:
        if ok_to_place_ship_at(row, col, horiz, 2, fleet) == True:
            place_ship_at(row,col,horiz,2,fleet)
            finished = True
        else:
            row = random.randint(0, 10)
            col = random.randint(0, 10)
            horiz = random.choice([True, False])
    finished = False

    # re-randomize the values
    row = random.randint(0, 10)
    col = random.randint(0, 10)
    horiz = random.choice([True, False])

    while finished == False:
        if ok_to_place_ship_at(row, col, horiz, 2, fleet) == True:
            place_ship_at(row,col,horiz,2,fleet)
            finished = True
        else:
            row = random.randint(0, 10)
            col = random.randint(0, 10)
            horiz = random.choice([True, False])
    finished = False

    # re-randomize the values
    row = random.randint(0, 10)
    col = random.randint(0, 10)
    horiz = random.choice([True, False])

    #submarines
    while finished == False:
        if ok_to_place_ship_at(row, col, horiz, 1, fleet) == True:
            place_ship_at(row,col,horiz,1,fleet)
            finished = True
        else:
            row = random.randint(0, 10)
            col = random.randint(0, 10)
            horiz = random.choice([True, False])
    finished = False

    # re-randomize the values
    row = random.randint(0, 10)
    col = random.randint(0, 10)
    horiz = random.choice([True, False])

    while finished == False:
        if ok_to_place_ship_at(row, col, horiz, 1, fleet) == True:
            place_ship_at(row,col,horiz,1,fleet)
            finished = True
        else:
            row = random.randint(0, 10)
            col = random.randint(0, 10)
            horiz = random.choice([True, False])
    finished = False
    # re-randomize the values
    row = random.randint(0, 10)
    col = random.randint(0, 10)
    horiz = random.choice([True, False])

    while finished == False:
        if ok_to_place_ship_at(row, col, horiz, 1, fleet) == True:
            place_ship_at(row,col,horiz,1,fleet)
            finished = True
        else:
            row = random.randint(0, 10)
            col = random.randint(0, 10)
            horiz = random.choice([True, False])
    finished = False
    # re-randomize the values
    row = random.randint(0, 10)
    col = random.randint(0, 10)
    horiz = random.choice([True, False])

    while finished == False:
        if ok_to_place_ship_at(row, col, horiz, 1, fleet) == True:
            place_ship_at(row,col,horiz,1,fleet)
            finished = True
        else:
            row = random.randint(0, 10)
            col = random.randint(0, 10)
            horiz = random.choice([True, False])
    finished = False
    # re-randomize the values
    row = random.randint(0, 10)
    col = random.randint(0, 10)
    horiz = random.choice([True, False])

    return fleet


def check_if_hits(row, column, fleet):
    hit = False
    check_hit = (row, column)
    for ship in fleet:
        ship_pos = ship_position(ship)
        for pos in ship_pos:
            if check_hit == pos:
                hit = True
    if hit == True:
        return True
    else:
        return False


def hit(row, column, fleet):
    check_hit = (row, column)
    for ship in fleet:
        ship_pos = ship_position(ship)
        for pos in ship_pos:
            if check_hit == pos:
                ship[4].add(check_hit)
                if ship[3] == len(ship[4]):
                    print("You sank a " + ship_type(ship))
                if are_unsunk_ships_left(fleet) == False:
                    print("You win! Total shots = " + str(shots))
                return (fleet, ship)



def are_unsunk_ships_left(fleet):
    sunk_count = 0
    for ship in fleet:
        if is_sunk(ship) == True:
            sunk_count +=1
    if len(fleet) == sunk_count:
        return False
    else:
        return True


#the following 3 functions are all needed for createbuttons()
def labelx(t, c, r, b):
    ttk.Label(b, text=t).grid(column=c, row=r, sticky=W, padx=5)

def labely(t, c, r, b):
    ttk.Label(b, text=t).grid(column=c, row=r, sticky=W)

def shoot(r, c, fleet, b):
    global shots
    if check_if_hits(r, c, fleet) == True:
        print("You hit!")
        hit(r, c, fleet) #the hit function then deals with checking if a ship has been sunk and communicating that
        b.configure(bg="green")
        shots +=1
    else:
        print("You missed")
        b.configure(bg="red")
        shots += 1



def createbuttons(board, tempfleet): #this creates the axis and the button grid
    for i in range(0, 10):
        labelx(i, i + 2, 1, board)

    for j in range(0, 10):
        labely(j, 1, j + 2, board)

    for i in range(2, 12):
        for j in range(2, 12):
            btn = Button(board)
            btn.config(width=3, command=lambda r=i-2, c=j-2, fleet=tempfleet, b=btn: shoot(r, c, fleet, b)) #this feeds the button corrdinates into shoot() when the button is clicked
            btn.grid(column=i, row=j)


def quitter(): #this is needed for the quit button
    sys.exit()

def main():

    current_fleet = randomly_place_all_ships()

    #the following sets up the board
    root = Tk()
    title = ttk.Label(root)
    title.configure(text="Battleships", anchor="center")
    title.grid(column = 1, row = 1)
    subtitle = ttk.Label(root)
    subtitle.configure(text="Click on a square to shoot!", anchor="center")
    subtitle.grid(column=1, row=2)

    board = ttk.Frame(root, padding="5 5 5 5")
    board.grid(column=1, row=3, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    #each square is a button, created using loops
    createbuttons(board, current_fleet)

    #this creates the lower portion of the board and the quit button
    scores = ttk.Frame(root, padding="5 5 5 5")
    scores.grid(column=1, row=4, sticky=(W, E))
    quit_button = Button(scores)
    quit_button.configure(text="Quit", bg="red", command=quitter)
    quit_button.grid(column=1, row=1)


    root.mainloop()

if __name__ == '__main__': #keep this in
   main()
