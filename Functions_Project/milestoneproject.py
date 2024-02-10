# This is the milestone project

test_board = ['#','X','O','X','O','X','O','X','O','X']
# Function that prints out the board
def displayboard(board):
     print('\n'*100)
     print(board[7] +'|' + board[8] +'|' + board[9]) 
     print(board[3] +'|' + board[5] +'|' + board[6])
     print(board[1] +'|' + board[2] +'|' + board[3])


print(displayboard(test_board))

# Function that takes player input 
def player_input():
     marker = ''
     while not (marker == 'X' or marker == 'O'):
          marker = input('Player 1 choose between X or O: ')
     if marker == 'X':
          return ('X', 'O')
     else:
          return ('O', 'X')

print(player_input())

# Function that takes board list object and assigns it to the board
def place_marker(board, marker, position):
     board[position] = marker

work_board = displayboard(test_board)
test_place_marker = place_marker(test_board,'$',7)
print(work_board)
print(test_place_marker)

# Function to check winner 
def win_check(board, mark):
     """
     if mark == 'X' or 'O'and board[7]==board[8]==board[9]:
          return True
     elif mark == 'X' or 'O' and board[4]==board[5]==board[6]:
          return True
     elif mark == 'X' or 'O' and board[1]==board[2]==board[3]:
          return True
     return False

     """
     return ((board[7] == mark and board[8] == mark and board[9] == mark)or
        (board[4] == mark and board[5] == mark and board[6] == mark)or
        (board[1] == mark and board[2] == mark and board[3] == mark)or
        (board[1] == mark and board[4] == mark and board[7] == mark)or
        (board[2] == mark and board[5] == mark and board[8] == mark)or
        (board[3] == mark and board[6] == mark and board[9] == mark)or
        (board[1] == mark and board[5] == mark and board[9] == mark)or
        (board[7] == mark and board[5] == mark and board[3] == mark))
     
import random
def choose_first():
     who_goes_first = random.randint(0,1)
     if who_goes_first == 0:
          return 'Player 1'
     else:
          return 'Player 2'
     
# Function to check if board is empty
def space_check(board, position):
     return board[position] == ' '

# Function to check if space is full
def full_board_check(test_board):
     for i in range(1,10):
          if space_check(test_board, i):
               return False
     return True

# 
def player_choice(board):
     """
        next_position = 0
     while board[next_position] in range(1,9):
          next_position = int(input('Enter your next position(1-9): ')) 
     space_check(board,next_position)
     """
     next_position = 0
     while next_position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
          position = int(input('Enter your next position(1-9): '))
     
     return position
          
  

def replay():
     choice = input('Do you want play again? Yes or No')
     return choice == 'Yes'

# Align everythin to make the function work

print('Tic Tac Toe game')

while True:
     # Set everything up(Board, who goes next, choose marker)
     the_board = ['']
     
     player1_marker, player2_marker = player_input()
     turn = choose_first()
     print(f'{turn} will go first')
     play_game = input('Ready to play?(y or n)')
     if play_game == 'y':
          game_on = True
     else:
          game_on = False
     # Game play 
     while game_on:
          if turn == 'Player 1':
               # show the board
               displayboard(the_board)
               # Choose a position
               position = player_choice(the_board)
               # Place a marker on the position they chose
               place_marker(the_board,player1_marker,position)
               
               # Check if they won
               if win_check(the_board,player1_marker):
                    displayboard(the_board)
                    print('PLAYER 1 HAS WON !!!!')
                    game_on = False
               else:
                    if full_board_check(the_board):
                         displayboard(the_board)
                         print('TIE GAME!!')
                         game_on = False
                    else:
                         turn == 'Player 2'
                         
          else:
                displayboard(the_board)
               # Choose a position
                position = player_choice(the_board)
               # Place a marker on the position they chose
          place_marker(the_board,player1_marker,position)

               # Check if they won
          if win_check(the_board,player2_marker):
                    displayboard(the_board)
                    print('PLAYER 2 HAS WON !!!!')
                    game_on = False
          else:
                    if full_board_check(the_board):
                         displayboard(the_board)
                         print('TIE GAME!!')
                         game_on = False
                    else:
                         turn == 'Player 2'
                         
               
               # Or check if there is a tie 
               
               
               # No tie, no win then next player's turn
               
     
     if not replay():
          break