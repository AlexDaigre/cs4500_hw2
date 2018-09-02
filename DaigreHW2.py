# Alex Daigre
# Aug 27th, 2018
# cs4500
# Version: Python 3.7
# Description:
# External Files:
# Sources:
#   https://www.w3schools.com/python/python_classes.asp
#   https://stackoverflow.com/questions/11264684/flatten-list-of-lists/11264799
#   https://docs.python.org/3/library/enum.html
#   

import random
from enum import Enum

# The loop that is executed durring each turn of the game
def gameLoop(gameBoard):
    totalMoves = 0
    while gameBoard.isComplete =! false:
        newDirection =  rollDie()
        gameBoard.moveDirection(newDirection)
        totalMoves += 1
    return gameBoard, totalMoves

# Rolls a die and returns UL, ER, DL, or DR
def rollDie():
    return Direction(random.randint(1,4))

#Enum to represent the direction of movement on our board
class Direction(Enum):
    UL = 1
    ER = 2
    DL = 3
    DR = 4

# The class that determines how the game's board operatates
#  Stores the data on all nodes
class GameBoard:
    # 2D array representing the board. 0,0 starts at one as 
    # this is where the player begins.
    boardSpaces = [[1],[0,0],[0,0,0],[0,0,0,0],[0,0,0,0,0],[0,0,0,0,0,0]]
    MAXROW = 5
    currentRow = 0
    currentCollumn = 0

    # Itterate through all values in boardSpaces and check if they
    #  Have been reached at least once
    def isComplete():
        allSpacesVisited = true
        for subList in flattenedSpaces:
            for space in subList:
                if space <= 0:
                    allSpacesVisited = False
                    break
        return allSpacesVisited

    #Gets the average number of dots on the nodes
    def getAverageDots():
        totalDots = 0
        totalSpaces = 0
        for subList in flattenedSpaces:
            for space in subList:
                totalSpaces += 1
                totalDots += space
        return totalDots/totalSpaces

    #Gets the maximum number of dots on any one node
    def getMaxDots():
        maxDots = 0
        for subList in flattenedSpaces:
            for space in subList:
                if space > maxDots:
                    maxDots = space
        return maxDots
    
    # Gets the current position as a sigle number instead of a tuple
    getCurrentPositionAsNumber():

    # Get the value of the next position requested.
    # Check if that value is valid.
    # If not add one to current position and exit.
    # If change current position and add one to new position.
    def moveDirection(direction):
        newRow = currentRow
        newCollumn = currentCollumn

        # Find new row
        if direction == Direction.UL or direction == Direction.UR:
            newRow -= 1
        elif direction == Direction.DL or direction == Direction.DR:
            newRow += 1

        # Find new collumn. No change in collumn number on DL or UR.
        if direction == Direction.UL:
            newCollumn -= 1
        elif direction == Direction.DR:
            newCollumn += 1
        
        # Check if our location is out of bounds, if so add 1 to 
        #  current space and return.
        if newRow < 0 or newRow > 5:
            boardSpaces[currentRow][currentCollumn] += 1
            return
        elif newCollumn < 0 or newCollumn > newRow:
            boardSpaces[currentRow][currentCollumn] += 1
            return

        # Set new row and collumn and add to the new position
        currentRow = newRow
        currentCollumn = newCollumn
            boardSpaces[currentRow][currentCollumn] += 1
        return


print("a short explanation of the game, and what your simulation is doing \n")
gameBoard = GameBoard()
totalMoves = 0
gameBoard, totalMoves = gameLoop(gameBoard)