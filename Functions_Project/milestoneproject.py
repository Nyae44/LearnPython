# This is the milestone project

test_board = ['#','X','O','X','O','X','O','X','O','X']
# Function that prints out the board
from IPython.display import clear_output
def displayboard(board):
     clear_output()
     print(board[7] +'|' + board[8] +'|' + board[9]) 
     print(board[3] +'|' + board[5] +'|' + board[6])
     print(board[1] +'|' + board[2] +'|' + board[3])


print(displayboard(test_board))

# Function that takes player input 
def player_input():
     marker = ''
     while marker != 'X' and marker != 'O':
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
          return 'Player1 goes first'
     else:
          return 'Player2 goes first'
     
# Function to check if board is empty
def space_check(board, position):
     return board[position] == ' '

# Function to check if space is full
def full_board_check():
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

# Align 