
import random
playerList = ['x','o'] 

board = [' 'for i in range(9)]

def printBoard(board):
  print('- - - - - - - - ') 
  for i in range(0,3):
    print(board[i] , end = ' | ' )
  print( )
  for i in range(3,6):
    print(board[i] , end = ' | ' )
  print( )
  for i in range(6,9):
    print(board[i] , end = ' | ' )
  print( )
  print('- - - - - - - - ')

def makeMove(board,player,position):
  board[position - 1] = player

def validMove(board,position):
  try:
    position = int(position)
  except:
    return False
  if (position < 1) or (position >9):
    return False
  if board[position-1] == " ":
    return True
  return False

def switchPlayer(player):
  if player == 'x':
    return 'o'
  return 'x'

def boardFull(board):
  if board.count(' ') > 0:
    return False
  return True

def askMove(board,player):
  userMove = ' '
  while (not validMove(board,userMove)):
    userMove = input(f'Player "{player}" make a valid move 1-9 :') 
  return int(userMove)

def personWon(board):
  for x in range(0,7,3):
    if (board[x] == board[x + 1] == board[x + 2]) and (board[x] != ' '):
      return board[x]
  for x in range(0,3):
    if (board[x] == board[x + 3] == board[x + 6]) and (board[x] != ' '):
      return board[x]
  if (board[0] == board[4] == board[8]) and (board[0] != ' '):
    return board[0]
  if (board[2] == board[4] == board[6]) and (board[2] != ' '):
    return board[2]
  return 'Yes'


player = random.choice(playerList)
keepPlaying = 'Yes'
printBoard(board) 
while keepPlaying == 'Yes':
  userMove = askMove(board,player)
  makeMove(board,player,userMove)
  printBoard(board)
  keepPlaying = personWon(board)
  if (keepPlaying == 'Yes'):
    if boardFull(board):
      keepPlaying = 'Tie'
  player = switchPlayer(player)
   

if keepPlaying == 'Tie':
  print(f'The match is a TIE') 
elif (keepPlaying == 'x'):
  print(f"Player 'X' have won the game. ") 
elif (keepPlaying == 'o'):
  print(f"Player 'O' have won the game. ")