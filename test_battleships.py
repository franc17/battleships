import pytest
from battleships import *

def test_is_sunk1():
    testship = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    testship2 = (4, 6, True, 4, ())
    testship3 = (7, 7, False, 2, {(7,7)})
    testfleet = [testship, testship2]
    assert is_sunk(testship) == True
    assert is_sunk(testship2) == False
    assert is_sunk(testship3) == False
    assert is_sunk(testfleet[0]) == True



def test_ship_type1():
    #need to check that ship of length 4 produces 'battleship' string
    testship = (0, 0, True, 4, set())
    testship2 = (5, 5, True, 3, set())
    testship3 = (9, 1, True, 2, set())
    testship4 = (7, 1, False, 1, set())
    testfleet = [testship, testship2, testship3, testship4]
    assert ship_type(testship) == "battleship"
    assert ship_type(testship2) == "cruiser"
    assert ship_type(testship3) == "destroyer"
    assert ship_type(testship4) == "submarine"
    assert ship_type(testfleet[1]) == "cruiser"

def test_is_open_sea1():
    #need to test that a given coord doesn't appear in any ship tuples or adjacent to any ship tuples
    testship = (0, 0, True, 4, set())
    testship2 = (5, 5, True, 3, set())
    testfleet = [testship, testship2]
    assert is_open_sea(0, 0, testfleet) == False
    assert is_open_sea(4, 4, testfleet) == False
    assert is_open_sea(6, 1, testfleet) == True
    assert is_open_sea(0, 1, testfleet) == False
    assert is_open_sea(10, 5, testfleet) == False
    assert is_open_sea(2, 15, testfleet) == False


def test_ok_to_place_ship_at1():
    #checks all the coordinates of a given ship to check they satisfy is_open_sea == True
    testship = (0, 0, True, 4, set())
    testship2 = (5, 5, True, 3, set())
    testfleet = [testship, testship2]
    assert ok_to_place_ship_at(5, 0, False, 3, testfleet) == True
    assert ok_to_place_ship_at(8, 7, True, 5, testfleet) ==  False
    assert ok_to_place_ship_at(9, 0, False, 3, testfleet) == False
    assert ok_to_place_ship_at(2, 6, False, 5, testfleet) == False
    assert ok_to_place_ship_at(5, 0, False, 2, testfleet) == True


def test_place_ship_at1():
    #test that the ship is added to the fleet correctly
    testship = (0, 0, True, 4, set())
    testship2 = (5, 5, True, 3, set())
    testfleet = [testship, testship2]
    place_ship_at(5, 0, False, 3, testfleet)
    assert testfleet[2] == (5, 0, False, 3, set())
    assert len(testfleet) == 3
    assert testfleet[1] == (5, 5, True, 3, set())
    assert testfleet[0] == (0, 0, True, 4, set())
    assert testfleet[2][0] == 5


def test_check_if_hits1():
    #compare a given coord against the coords in fleet
    testship = (0, 0, True, 4, set())
    testship2 = (5, 5, True, 3, set())
    testfleet = [testship, testship2]
    assert check_if_hits(0, 3, testfleet) == True
    assert check_if_hits(4, 4, testfleet) == False
    assert check_if_hits(0, 2, testfleet) == True
    assert check_if_hits(10, 10, testfleet) == False
    assert check_if_hits(5, 6, testfleet) == True


def test_hit1():
    #testing that the return tuple is correct
    testship = (0, 0, True, 4, set())
    testship2 = (5, 5, True, 3, set())
    testship3 = (7, 3, False, 3, {(8,3)})
    testfleet = [testship, testship2, testship3]
    returnfleet = hit(0, 3, testfleet)
    returnfleet2 = hit(9, 3, testfleet)
    assert returnfleet == ([testship, testship2, testship3], testship)
    assert returnfleet[1] == testship
    assert testship3[4] == {(8,3), (9,3)}
    assert testship[4] == {(0,3)}
    assert returnfleet2[1] == testship3


def test_are_unsunk_ships_left1():
    #check the ship tuples for no. of sunk coords equalling length
    testship = (0, 0, True, 4, ((0,0), (0,1), (0,2), (0,3)))
    testship2 = (5, 5, True, 3, set())
    testfleet = [testship, testship2]
    testfleet2 = [testship]
    assert are_unsunk_ships_left(testfleet) == True
    assert len(testfleet) == 2
    assert len(testship[4]) == testship[3]
    assert len(testship2[4]) != testship2[3]
    assert are_unsunk_ships_left(testfleet2) == False

    
