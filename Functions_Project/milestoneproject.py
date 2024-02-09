# This is the milestone project

test_board = ['#','X','O','X','O','X','O','X','O','X']
def displayboard(board):
     
     print(board[7] +'|' + board[8] +'|' + board[9]) 
     print(board[3] +'|' + board[5] +'|' + board[6])
     print(board[1] +'|' + board[2] +'|' + board[3])


print(displayboard(test_board))

def player_input():
     marker = ''
     while marker != 'X' and marker != 'O':
          marker = input('Player 1 choose between X or O: ')
     player1 = marker
     if player1 == 'X':
        player2 = 'O'
     else:
          player2 = 'X'
     return (player1,player2)

print(player_input())

def place_marker(board, marker, position):
     while marker not in range(0,9) and marker == int:
          position = int(input('Enter your desired position: '))
          board[position] = marker
print(place_marker(test_board,'$',7))

work_board = displayboard(test_board)
test_place_marker = place_marker(test_board,'$',7)
print(work_board)
print(test_place_marker)