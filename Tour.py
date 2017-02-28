from Algorithm import *
from random import choice
board=[[False for i in range(8)] for j in range(8)]
moveList=[]
print("Enter Start Position separated by spaces")
startPos=[int(x) for x in input("").split()]

board[startPos[0]][startPos[1]]=True
currentPos=deepcopy(startPos)

while(not boardComplete(board)):
    moves=evalPossibilities(board,currentPos)
    moveValue=[]
    min=9
    for i in range(len(moves)) :
        moveValue.append(len(evalPossibilities(board,moves[i])))
    for i in moveValue:
        min = i if i<min else min
    moveList.append(currentPos)
    randomChoice=choice([i for i,x in enumerate(moveValue) if x==min])
    currentPos=moves[randomChoice]
    board[currentPos[0]][currentPos[1]] = True
    printPath(board,currentPos,moveList)
printPath(board,currentPos,moveList)