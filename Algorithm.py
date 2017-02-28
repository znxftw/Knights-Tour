from copy import deepcopy
from math import floor
def evalPossibilities(board,currentPos):
    possibleSquares=[]
    #Direct exit if not legal square
    if floor(currentPos[0] / 8) != 0 or floor(currentPos[1] / 8) != 0:
        return []
    # All possible +-2,+-1 combinations

    possibleSquares.extend((currentPos[0] + x, currentPos[1] + y) for x in (1, -1) for y in (-2, 2))
    possibleSquares.extend((currentPos[0] + x, currentPos[1] + y) for y in (1, -1) for x in (-2, 2))
    #Eliminate illegal squares

    for i in deepcopy(possibleSquares):
        if floor(i[0]/8)!=0 or floor(i[1]/8)!=0:
            possibleSquares.remove(i)
    checkBoard(board,possibleSquares)
    return possibleSquares

def checkBoard(board,possibleSquares):
    for i in deepcopy(possibleSquares):
        x,y=i
        if board[x][y] is True :
            possibleSquares.remove(i)

def boardComplete(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] is False:
                return False
    return True

def printPath(board,currentPos,moveList):
    for i in range(8):
        for j in range(8):
            if board[i][j] is True:
                if (i,j) in moveList:
                    print(moveList.index((i,j))+1,"\t",end='')
                else:
                    print("O\t",end='')
            else:
                print("-\t",end='')
        print("\n")
    print("\n\n")