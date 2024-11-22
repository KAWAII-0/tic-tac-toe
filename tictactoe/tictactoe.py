"""
Tic Tac Toe Player
"""

import math
import copy
import random 
# which player starts firts with thier symbol 
playerX = True
PlayerO = False
X = "X"
O = "O"
EMPTY = None

# dimensions 
colSize = 3
rowSize = 3

# actions and board

'''
board = [   ["X", "O", "X"],
            ["O", "X", "O"],
            ["X", "O", EMPTY]]
'''

def initial_state():
    """
    Returns starting state of the board.
    """
    global playerXactions, playerOactions
    playerXactions = []
    playerOactions = []
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCounter = sum(i.count(X) for i in board)
    oCounter = sum(i.count(O) for i in board)

    if xCounter <= oCounter:
        return X
    else:
        return O

    raise Exception("unable to select player")


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()
    for i in range(rowSize):
        for j in range(colSize):
            if board[i][j] != EMPTY:
                continue
            else: 
                possibleActions.add((i,j))
    print("Empty spots on board: ")
    print(possibleActions)
    return possibleActions
  


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action == None:
        raise Exception("Action is none!")
    i, j = action
    print(f"action : {action}, i: {i}, j: {j}") 
    currentPlayer = player(board)
    actionBoard = copy.deepcopy(board)
    if actionBoard[i][j] == EMPTY:
        actionBoard[i][j] = currentPlayer
        print(actionBoard)
        return actionBoard
    
    else:
        raise Exception("Please choose a move that is not taken!")

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winCondition = [
        # rows
        [(0, 0), (0, 1), (0, 2)], 
        [(1, 0), (1, 1), (1, 2)],  
        [(2, 0), (2, 1), (2, 2)],  
        
        # columns 
        [(0, 0), (1, 0), (2, 0)],  
        [(0, 1), (1, 1), (2, 1)],  
        [(0, 2), (1, 2), (2, 2)],  
        
        # diagonals
        [(0, 0), (1, 1), (2, 2)],  
        [(0, 2), (1, 1), (2, 0)]   
    ]
    for condition in winCondition:
        if board[condition[0][0]][condition[0][1]] == board[condition[1][0]][condition[1][1]] == board[condition[2][0]][condition[2][1]] != EMPTY:
            return board[condition[0][0]][condition[0][1]]
    print("No one won")
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for i in board:
            if None in i:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    checkWinner = winner(board)
    if checkWinner == X:

        return 1
    elif checkWinner == O:

        return -1
    else:

        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board. -- FOR NOW RANDOM TO TEST OTHER FUNCTIONS..
    """
    if terminal(board):
        return utility(board), None

    currentPlayer = player(board)
    bestMove = None

    if currentPlayer == X:
        highScore = float('-inf')
    else:
        highScore = float('inf')

    for move in actions(board):
        minimaxBoard = result(board, move)
        score,_ = minimax(minimaxBoard)
        if currentPlayer == X:
            if score > highScore:
                highScore = score
                bestMove = move
        else:
            if score < highScore:
                highScore = score
                bestMove = move
 

    return highScore, bestMove