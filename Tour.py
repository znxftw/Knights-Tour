from Algorithm import *
from random import choice

#Initialize entire board to 'not tread'
board=[[False for i in range(8)] for j in range(8)]
moveList=[]
print("Enter Start Position separated by spaces")
startPos=[int(x) for x in input("").split()]

board[startPos[0]][startPos[1]]=True
currentPos=deepcopy(startPos)
#As long as the tour isn't complete
while(not boardComplete(board)):
    #Get a list of possible moves and see how many positions a given move produces
    moves=evalPossibilities(board,currentPos)
    moveValue=[]
    min=9
    for i in range(len(moves)) :
        moveValue.append(len(evalPossibilities(board,moves[i])))
    #Find lowest, select random, move to that square
    for i in moveValue:
        min = i if i<min else min
    moveList.append(currentPos)
    randomChoice=choice([i for i,x in enumerate(moveValue) if x==min])
    currentPos=moves[randomChoice]
    board[currentPos[0]][currentPos[1]] = True
    printPath(board,currentPos,moveList)
moveList.append(currentPos)
printPath(board,currentPos,moveList)