 #----------------Global Variables------------------

board=['-','-','-',
       '-','-','-',
       '-','-','-',]


 #------Lets us know if the  game is over yet--------
game_still_going=True

#------Tells us who the winner is---------------------
winner=None

#------------Tells us who the current player is-------
current_player="x"


#---------------------functions------------------------


#-------------play tic tac toe-------------------------
def play_game() :

#-------------display initial game board---------------
  display_board() 

  while game_still_going:
#-------------handle a currently active player---------
    handle_turn(current_player)

#-------------check if the game is over----------------  
    check_if_gameover()
#--------------flip a player after a step-------------   
    flip_player()

#-------------print the winner-----------------------
  if winner== "x" or winner== "0":
    print(winner+" won")
  elif winner==None:
    print("tie") 


def display_board():
  print("\n")
  print("\n")
  print(board[0]+" | "+board[1]+" | "+board[2]+"     1 | 2 | 3 ")
  print(board[3]+" | "+board[4]+" | "+board[5]+"     4 | 5 | 6 ")
  print(board[6]+" | "+board[7]+" | "+board[8]+"     7 | 8 | 9 ")




#-------------- handle a single player-----------------
def handle_turn(player):

#---------------get position from player---------------  
  print(player+",s turn")
  position=input("chose a position from 1-9 : ")
 # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:

    # Make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    # Get correct index in our board list
    position = int(position) - 1

    # Then also make sure the spot is available on the board
    if board[position] == '-':
      valid = True
    else:
      print("You can't go there. Go again.")

  # Put the game piece on the board
  board[position] = player

  # Show the game board
  display_board()




#-----------check if the game is over---------------

def check_if_gameover():
  check_if_win()
  check_if_tie()
  return


#-------checking the winner conditions------

def check_if_win():


  ###setup global variables
  global winner
  ##check Row
  row_winner=check_row()
  ##check columb
  columb_winner=check_columb()
  ##check diagonal
  diagonal_winner=check_diagonal()


  if row_winner:
    winner=row_winner

  elif columb_winner:
    winner=columb_winner

  elif diagonal_winner:     
    winner=diagonal_winner

  else :
    winner=None  


def check_row():

#---------set global variables-----------------------------------

  global game_still_going

  ###--------------------check if rows are equal----------


  row1=board[0]==board[1]==board[2] !='-'
  row2=board[3]==board[4]==board[5] !='-'
  row3=board[6]==board[7]==board[8] !='-'


  if row1 or row2 or row3:
    game_still_going=False
  if row1:
    return board[0] 
  elif row2:
    return board[3]
  elif row3:
    return board[6]
  else :
    return None  

       

  

####----------------------------checking columbs------------------------------

def check_columb():

  global game_still_going

  columb1=board[0]==board[3]==board[6] !='-'
  columb2=board[1]==board[4]==board[7] !='-'
  columb3=board[2]==board[5]==board[8] !='-'


  if columb1 or columb2 or columb3:
      game_still_going=False
  if columb1:
    return board[0] 
  elif columb2:
    return board[1]
  elif columb3:
    return board[2] 
  else :
    return  None



#----------------check diagonal----------------------

def check_diagonal():

  global game_still_going
  
  diagonal1=board[0]==board[4]==board[8] !='-'
  diagonal2=board[6]==board[4]==board[2] !='-'
  


  if diagonal1 or diagonal2 :
    game_still_going=False
  if diagonal1:
    return board[0] 
  elif diagonal2:
    return board[6]
  else:
    return None  
 

  


#------------------check if tie-------------------

def check_if_tie():
  # Set global variables
  global game_still_going
  # If board is full
  if '-' not in board:
    game_still_going = False
    return True
  # Else there is no tie
  else:
    return False
  

 


def  flip_player():

  global current_player

  if current_player=='x':
    current_player='0'
  elif current_player=='0':
    current_player='x'  

  

# ------------ Start Execution -------------
# Play a game of tic tac toe
play_game()


 




  

