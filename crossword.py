import sys; args = sys.argv[1:]
#myLines = open(args[0], "r").read().splitlines()
import time 
import math
import random 

case = args[2]
size = args[0]
numOfBlocks = int(args[1])
seedstrings = []
x=3
while len(args) > x:
    ind = args[x].index("x")
    nextind = ind + 1
    while args[x][nextind].isnumeric():
        nextind += 1
    seedstrings.append((int(args[x][1:ind]),int(args[x][ind+1:nextind]),args[x][0],args[x][nextind:].upper()))
    x = x + 1

x = size.index("x")
height = int(size[:x])
width = int(size[x+1:])

def read():
    with open(case) as f:
        line_list = [line.strip() for line in f]
    return line_list

file = read()

def generateBoard():
    board = ""
    for i in range (0,height):
        for j in range (0,width):
            board = board + "-"
    return board

theboard = generateBoard()

def boardprint(board):
    state = ""
    for i in range (0,height):
        for j in range (0,width):
            state = state + board[i*width+j]
        state = state + "\n"
    print(state)

def goal(board):
    count = 0 
    for x in board:
        if x == "#":
            count = count + 1
    if count != numOfBlocks:
        return False
    return True 

def placeSeedStrings(board):
    for row,column,orientation,word in seedstrings:
        if orientation == "H":
            board = board[:row*width+column] + word + board[row*width+column+len(word):]
        elif orientation == "V":
            count = len(word)
            for x in range (0,count):
                board = board[:(row+x)*width+column] + word[x] + board[(row+x)*width+column+1:]
    return board

theboard = placeSeedStrings(theboard)

def findRowCol(index):
    return index // width, index % width

def findInv(var):
    row,col = findRowCol(var)
    newrow = height - row-1
    newcol = width-col-1
    return newrow*width + newcol 

def checkLeft(state,var):
    row,col = findRowCol(var)
    if col - 3 < 0:
        return False
    if "#" in state[row*width+col-3:var]:
        return False 
    return True

def checkRight(state,var):
    row,col = findRowCol(var)
    if col + 3 > width-1:
        return False
    if "#" in state[var+1:row*width+col+4]:
        return False 
    return True

def checkUp(state,var):
    row,col = findRowCol(var)
    if row - 3 < 0 :
        return False
    for x in range (1,4):
        if "#" == state[(row-x)*width+col]:
            return False 
    return True

def checkDown(state,var):
    row,col = findRowCol(var)
    if row + 3 > height - 1:
        return False
    for x in range (1,4):
        if "#" == state[(row+x)*width+col]:
            return False 
    return True 

def leftside(state,var):
    row,col = findRowCol(var)
    if col - 3 < 0:
        return True
    if "-" == state[var-1]:
        if "#" in state[var-3:var-1]:
            return False
    return True

def rightside(state,var):
    row,col = findRowCol(var)
    if col - 3 < 0:
        return True
    if "-" == state[var+1]:
        if "#" in state[var+2:var+4]:
            return False
    return True

def upside(state,var):
    row,col = findRowCol(var)
    if row - 3 < 0 :
        return True
    if state[var+width] == "-":
        for x in range (2,4):
            if "#" == state[(row-x)*width+col]:
                return False 
    return True

def downside(state,var):
    row,col = findRowCol(var)
    if row + 3 > height - 1:
        return True
    if state[var+width] == "-":
        for x in range (2,4):
            if "#" == state[(row+x)*width+col]:
                return False 
    return True

def checkAround(state,var):
    count = 0
    if leftside(state,var) and rightside(state,var) and upside(state,var) and downside(state,var):
        if checkLeft(state,var):
            count += 1 
        if checkRight(state,var):
            count += 1
        if checkUp(state,var):
            count += 1
        if checkDown(state,var):
            count += 1
        if count > 2:
            return True
    return False

def checkSpace(board,space):
    

def checkDisconnected(board):

    return True

def get_nextun(state):
    row = 


    return row

def get_sorted(state,var):
    coloptions = []
    for x in range (0,width):
        ind = var * width + x
        flip = findInv(ind)
        if state[flip] == "-":
            if checkAround(state,var) and checkAround(state,flip):
                coloptions.append(x) 
    return coloptions 

def solve(board):
    if height * width % 2 == 1 and numOfBlocks % 2 == 1:
        index = height*width//2
        newboard = board[:index] + "#" + board[index+1:]
        boardprint(newboard)
        return csp_backtracking(newboard)
    else:
        return csp_backtracking(board)

def csp_backtracking(thestate):
    if goal(thestate):
        return thestate
    var = get_nextun(thestate)
    for val in get_sorted(thestate,var):
        ind = var*width + val
        inv = findInv(ind)
        newstate = thestate[:ind] + "#" + thestate[ind+1:]
        newstate = newstate[:inv] + "#" + newstate[inv+1:]
        result = csp_backtracking(newstate)
        if result is not None:
            return result
    return None

x = solve(theboard)
count = 0
while x == None:
    count+=1
    x = csp_backtracking(theboard)
    
boardprint(x)
print(x)

# Joaquim Das, 3, 2022
