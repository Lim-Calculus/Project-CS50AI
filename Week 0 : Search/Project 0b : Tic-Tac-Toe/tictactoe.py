import math
import copy
import time
##from filewriter import *
### state=board
X = "X" 
O = "O"
positive_infinity=float("inf")
negative_infinity=float("-inf")
Xwin=1
Owin=-1
Draw=0
EMPTY = None

start_time = time.time()



###Initial State of the game = EMPTY
def initial_state():
    board =[[[],[],[]],[[],[],[]],[[],[],[]]]
    board[0][0]=EMPTY
    board[0][1]=EMPTY
    board[0][2]=EMPTY
    board[1][0]=EMPTY
    board[1][1]=EMPTY
    board[1][2]=EMPTY
    board[2][0]=EMPTY
    board[2][1]=EMPTY
    board[2][2]=EMPTY
    return board


    ##return [[EMPTY, EMPTY, EMPTY],
            ##[EMPTY, EMPTY, EMPTY],
            ##[EMPTY, EMPTY, EMPTY]]

#### Determine which player to play
def player(board):
    ##### If the game is initial state, then X start first
    if board == initial_state():  
        return X

    Xturn = 0
    Oturn = 0 
    for turn in board: ## Using list.count() function we are able to count the number of element inside the list
        Xturn = Xturn+ turn.count(X) ## Xcount= Xcount+1
        ##To check number of X player's turn                      
        Oturn = Oturn+ turn.count(O)  ## Ocount=Ocount+1
          ## To check number of O player's turn
    if Xturn == Oturn: 
    ## If number of turn of X = number of turn of O then will be X turn, else will be O's turn
        return X
    else:
        return O
    #print(f"Xturn : ", Xturn)
    #print(f"Oturn : ", Oturn)
### Action(s) 
def actions(board): ###Return all possible moves / All possible states
   
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY: ## If board is empty then append to positive moves list[]
                possible_moves.append([i, j])
    return possible_moves

## Resuts(s,a)=return the state for the output results
def result(board, action):
   
    boardcopy = copy.deepcopy(board)
    ##print(boardcopy) ##Deep copy creates a copy without changing the state
    try:
        if boardcopy[action[0]][action[1]] != EMPTY:
            raise IndexError
        else:
            boardcopy[action[0]][action[1]] = player(boardcopy)
         
            return boardcopy
          
    except IndexError:
       print('OCCUPIED!')

## Check winner(s)
def winner(board):
    
     # Checks diagonals for O player
    if board[0][0]==O and board[1][0]==O and  board[2][0] ==O:
        return O #
    if board[0][1]==O and board[1][1]==O  and board[2][1]==O:
        return O #
    if board[0][2]==O and board[1][2]==O and board[2][2]==O:
        return O #
    if board[0][0]==O and board[0][1]==O and board[0][2]==O:
        return O #
    if board[1][0]==O and board[1][1]==O and board[1][2]==O:
        return O #
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O #
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O #
    if board[2][0]== O and board[2][1]==O and board[2][2]==O:
        return O #
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O #


# Checks diagonals for X player
    if board[0][0]==X and board[1][0]==X and  board[2][0] ==X:
        return X #
    if board[0][1]==X and board[1][1]==X and board[2][1]==X:
        return X #
    if board[0][2]==X and board[1][2]==X and board[2][2]==X:
        return X #
    if board[0][0]==X and board[0][1]==X and board[0][2]==X:
        return X #
    if board[1][0]==X and board[1][1]==X and board[1][2]==X:
        return X #
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X #
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:#
        return X
    if board[2][0]== X and board[2][1]==X and board[2][2]==X:
        return X #
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:#
        return X
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X

# No winner/tie
    return None


def terminal(board):
   
    # Checks if board is full or if there is a winner
    empty_counter = 0
    for row in board:
        empty_counter += row.count(EMPTY)
    if empty_counter == 0:
        return True
    elif winner(board) is not None:
        return True
    else:
        return False


def utility(board):
    
    ### Check who is the winner and return their numerical value
    if winner(board) == X:
        ##print("AI Computing time : %s seconds ---" % (time.time() - start_time))
       ## filewrite(board,utility)
        return Xwin
        
        
    elif winner(board) == O:
        ##print("AI Computing time : %s seconds ---" % (time.time() - start_time))
        ##filewrite(board,utility)
        return Owin
    else:
       ## filewrite(board,utility)
        ##print("AI Computing time : %s seconds ---" % (time.time() - start_time))
        return Draw
    
#Minimax algorithm
###Alpha beta pruning
def minimax(board):
    
    if terminal(board):
        return utility(board)
    
    alpha = negative_infinity
    beta = positive_infinity
    current_player=player(board)

   
    if current_player==X:
        v = negative_infinity

        for action in actions(board):
            max_value = max(v,minimax_value(result(board, action),False, alpha, beta))

            alpha = max(v, max_value)

            if max_value > v:
                v = max_value
                best_move = action

    elif current_player==O:
        v = positive_infinity

        for action in actions(board):
            min_value =min(v, minimax_value(result(board, action), True, alpha, beta))

            beta = min(v, min_value)

            if min_value < v:
                v = min_value
                best_move = action
    if v==1:
        print(f"X player has more advantages, V={v},Alpha={alpha}, Beta={beta}\n")     
    elif v==-1:
        print(f"O player has more advantages,V={v},Alpha={alpha}, Beta={beta}\n")   
    else:
        print(f"Highly possible end in tie if you make the right move, think carefully,  V= {v}, Alpha={alpha},Beta={beta}\n") ##Analysis of the game 
        
    print(f"AI analyze the best_move for player {player(board)}={best_move}")
   
    return best_move

def minimax_value(board, IsMaximizing, alpha, beta):
    if terminal(board):
        return utility(board)

    if IsMaximizing is True:
        v = negative_infinity

        for action in actions(board):
            v = max(v, minimax_value(result(board, action), False, alpha, beta))

            alpha = max(alpha, v)

            if beta<=alpha:
                break

        return v
    elif IsMaximizing is not True:
        v = positive_infinity

        for action in actions(board):
            v= min(v, minimax_value(result(board, action), True, alpha, beta))
            beta = min(beta, v)

            if beta<=alpha:
                break

        return v
