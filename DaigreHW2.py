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
#   https://stackoverflow.com/questions/25902690/typeerror-init-takes-0-positional-arguments-but-1-was-given
#   https://docs.python.org/3/tutorial/classes.html
#   

import random
from enum import Enum

# The loop that is executed durring each turn of the game
def gameLoop(gameBoard):
    while gameBoard.isComplete() != True:
        newDirection =  rollDie()
        gameBoard.moveDirection(newDirection)
    return gameBoard

# Rolls a die and returns UL, ER, DL, or DR
def rollDie():
    return Direction(random.randint(1,4))

#Enum to represent the direction of movement on our board
class Direction(Enum):
    UL = 1
    UR = 2
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

    movesLog = ""

    def __init__(self):
        startPosition = self.getCurrentPositionAsNumber() 
        self.logMoveData(f"{startPosition}, ")

    # Itterate through all values in boardSpaces and check if they
    #  Have been reached at least once
    def isComplete(self):
        allSpacesVisited = True
        for subList in self.boardSpaces:
            for space in subList:
                if space <= 0:
                    allSpacesVisited = False
                    break
        if allSpacesVisited == True:
            lastposition = self.getCurrentPositionAsNumber()
            self.logMoveData(f"{lastposition}.\n")
        return allSpacesVisited

    # Gets the average number of dots on the nodes.
    def getAverageDots(self):
        totalDots = 0
        totalSpaces = 0
        for subList in self.boardSpaces:
            for space in subList:
                totalSpaces += 1
                totalDots += space
        return totalDots/totalSpaces

    # Gets the maximum number of dots on any one node.
    def getMaxDots(self):
        maxDots = 0
        for subList in self.boardSpaces:
            for space in subList:
                if space > maxDots:
                    maxDots = space
        return maxDots

    # Gets the total number of moves performed on the board.
    # This is equal to dots -1 as the board starts with 1 dot.
    def getTotalMoves(self):
        totalMoves = -1
        for subList in self.boardSpaces:
            for space in subList:
                    totalMoves += space
        return maxDots
    
    # Gets the current position as a sigle number instead of a tuple
    def getCurrentPositionAsNumber(self):
        boardNumbers = [[1],[2,3],[4,5,6],[7,8,9,10],[11,12,13,14,15],[16,17,18,19,20,21]]
        return boardNumbers[self.currentRow][self.currentCollumn]

    def logMoveData(self, dataToLog):
        print(dataToLog, end = "")
        self.movesLog += dataToLog

    # Get the value of the next position requested.
    # Check if that value is valid.
    # If not add one to current position and exit.
    # If change current position and add one to new position.
    def moveDirection(self, direction):
        newRow = self.currentRow
        newCollumn = self.currentCollumn

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
            self.boardSpaces[self.currentRow][self.currentCollumn] += 1
            currentPosition = self.getCurrentPositionAsNumber()
            self.logMoveData(f"{currentPosition}, ")
            return
        elif newCollumn < 0 or newCollumn > newRow:
            self.boardSpaces[self.currentRow][self.currentCollumn] += 1
            currentPosition = self.getCurrentPositionAsNumber()
            self.logMoveData(f"{currentPosition}, ")
            return

        # Set new row and collumn and add to the new position
        self.currentRow = newRow
        self.currentCollumn = newCollumn
        self.boardSpaces[self.currentRow][self.currentCollumn] += 1
        currentPosition = self.getCurrentPositionAsNumber()
        self.logMoveData(f"{currentPosition}, ")
        return


print("a short explanation of the game, and what your simulation is doing \n")
gameBoard = GameBoard()
totalMoves = 0
gameBoard = gameLoop(gameBoard)