#  File: Horrible Tetris.py

#  Description: Crappy command prompt game of tetris

#  Name: Carlos Vazquez

#  Date Created: 10-03-23

#  Date Last Modified: 10-07-23

#  Notes: ***Run with .exe not in IDLE. ASCII color effects will not work in IDLE

import random
import piece
import copy
import os

### Add x to the vertical coordinates of a piece #############################################################
def add_to_coords_vert(piece, x, board):
    temp_coords = copy.deepcopy(piece.coords)

    for i in temp_coords:
        i[0] += x
        
    if(move_possible(board, temp_coords)):
      piece.coords = copy.deepcopy(temp_coords)
##############################################################################################################
      
### Add x to the horizontal coordinates of a piece ###########################################################
def add_to_coords_horiz(piece, x, board):
    temp_coords = copy.deepcopy(piece.coords)
    
    for i in temp_coords:
        i[1] += x

    left_bound = False
    right_bound = False
    for i in temp_coords:
      if(i[1] > 9):
        right_bound = True
      elif(i[1] < 0):
        left_bound = True

    if(left_bound):
      for i in temp_coords:
        i[1] += 1
    elif(right_bound):
      for i in temp_coords:
        i[1] -= 1

    if(move_possible(board, temp_coords)):
      piece.coords = copy.deepcopy(temp_coords)
##############################################################################################################

### Check if a move can be made without entering a filled tile ###############################################
def move_possible(board, temp_coords):
    possible = True
    for i in temp_coords:
      if(board[i[0]][i[1]] != 0):
        possible = False
    return possible
##############################################################################################################

### Clears the letters of a piece from the board #############################################################
def clear_piece(board, piece):
    for i in piece.returnCoords():
        board[i[0]][i[1]] = 0
##############################################################################################################

### Rotates a piece clockwise ################################################################################
def rotate_piece(piece, board):
  temp_piece = copy.deepcopy(piece)

  for i in piece.returnCoords():
    board[i[0]][i[1]] = 0
  
  if(piece.name[0] == 'O'): ### O-piece does not rotate
    pass
  
  elif(piece.name[0] == 'I'): ### Rotate I-piece (2 orientations)
    if(piece.orientation == 1):
      anchor = temp_piece.coords[1]
      count = -1
      for i in temp_piece.coords:
        i[0] = anchor[0] + count
        i[1] = anchor[1]
        count += 1
      temp_piece.orientation = 2
      
    elif(piece.orientation == 2):
      anchor = temp_piece.coords[1]
      count = -1
      for i in temp_piece.coords:
        i[0] = anchor[0]
        i[1] = anchor[1] + count
        count += 1
      temp_piece.orientation = 1
      
  elif(piece.name[0] == 'Z'): ### Rotate Z-piece (2 orientations)
    if(piece.orientation == 1):
      anchor = temp_piece.coords[1]
      
      temp_piece.coords[0][0] = anchor[0] - 1
      temp_piece.coords[0][1] = anchor[1]
      temp_piece.coords[2][0] = anchor[0]
      temp_piece.coords[2][1] = anchor[1] - 1
      temp_piece.coords[3][0] = anchor[0] + 1
      temp_piece.coords[3][1] = anchor[1] - 1
    
      temp_piece.orientation = 2
      
    elif(piece.orientation == 2):
      anchor = temp_piece.coords[1]

      temp_piece.coords[0][0] = anchor[0]
      temp_piece.coords[0][1] = anchor[1] - 1
      temp_piece.coords[2][0] = anchor[0] + 1
      temp_piece.coords[2][1] = anchor[1]
      temp_piece.coords[3][0] = anchor[0] + 1
      temp_piece.coords[3][1] = anchor[1] + 1

      temp_piece.orientation = 1
      
  elif(piece.name[0] == 'S'): ### Rotate S-piece (2 orientations)
    if(piece.orientation == 1):
      anchor = temp_piece.coords[0]
      
      temp_piece.coords[1][0] = anchor[0] - 1
      temp_piece.coords[1][1] = anchor[1]
      temp_piece.coords[2][0] = anchor[0]
      temp_piece.coords[2][1] = anchor[1] + 1
      temp_piece.coords[3][0] = anchor[0] + 1
      temp_piece.coords[3][1] = anchor[1] + 1
    
      temp_piece.orientation = 2
      
    elif(piece.orientation == 2):
      anchor = temp_piece.coords[0]

      temp_piece.coords[1][0] = anchor[0]
      temp_piece.coords[1][1] = anchor[1] + 1
      temp_piece.coords[2][0] = anchor[0] + 1
      temp_piece.coords[2][1] = anchor[1]
      temp_piece.coords[3][0] = anchor[0] + 1
      temp_piece.coords[3][1] = anchor[1] - 1

      temp_piece.orientation = 1
      
  elif(piece.name[0] == 'T'): ### Rotate T-piece (4 orientations)
    if(piece.orientation == 1):
      anchor = temp_piece.coords[1]
      temp_piece.coords[0], temp_piece.coords[2] = temp_piece.coords[3].copy(), temp_piece.coords[0].copy()
      temp_piece.coords[3][0] = anchor[0] + 1
      temp_piece.coords[3][1] = anchor[1]
      temp_piece.orientation = 2

    elif(piece.orientation == 2):
      anchor = temp_piece.coords[1]
      temp_piece.coords[0], temp_piece.coords[2] = temp_piece.coords[3].copy(), temp_piece.coords[0].copy()
      temp_piece.coords[3][0] = anchor[0]
      temp_piece.coords[3][1] = anchor[1] - 1
      temp_piece.orientation = 3

    elif(piece.orientation == 3):
      anchor = temp_piece.coords[1]
      temp_piece.coords[0], temp_piece.coords[2] = temp_piece.coords[3].copy(), temp_piece.coords[0].copy()
      temp_piece.coords[3][0] = anchor[0] - 1
      temp_piece.coords[3][1] = anchor[1]
      temp_piece.orientation = 4
    elif(piece.orientation == 4):
      anchor = temp_piece.coords[1]
      temp_piece.coords[0], temp_piece.coords[2] = temp_piece.coords[3].copy(), temp_piece.coords[0].copy()
      temp_piece.coords[3][0] = anchor[0]
      temp_piece.coords[3][1] = anchor[1] + 1
      temp_piece.orientation = 1

  elif(piece.name[0] == 'J'): ### Rotate J-piece (4 orientations)
    if(piece.orientation == 1):
      anchor = temp_piece.coords[2]
      
      temp_piece.coords[0][0] = anchor[0] - 1
      temp_piece.coords[0][1] = anchor[1] + 1
      temp_piece.coords[1][0] = anchor[0] - 1
      temp_piece.coords[1][1] = anchor[1]
      temp_piece.coords[3][0] = anchor[0] + 1
      temp_piece.coords[3][1] = anchor[1]
    
      temp_piece.orientation = 2
      
    elif(piece.orientation == 2):
      anchor = temp_piece.coords[2]
      
      temp_piece.coords[0][0] = anchor[0] + 1
      temp_piece.coords[0][1] = anchor[1] + 1
      temp_piece.coords[1][0] = anchor[0] 
      temp_piece.coords[1][1] = anchor[1] + 1
      temp_piece.coords[3][0] = anchor[0] 
      temp_piece.coords[3][1] = anchor[1] - 1
    
      temp_piece.orientation = 3

    elif(piece.orientation == 3):
      anchor = temp_piece.coords[2]

      temp_piece.coords[0][0] = anchor[0] + 1
      temp_piece.coords[0][1] = anchor[1] - 1
      temp_piece.coords[1][0] = anchor[0] + 1
      temp_piece.coords[1][1] = anchor[1] 
      temp_piece.coords[3][0] = anchor[0] - 1
      temp_piece.coords[3][1] = anchor[1] 
    
      temp_piece.orientation = 4
      
    elif(piece.orientation == 4):
      anchor = temp_piece.coords[2]

      temp_piece.coords[0][0] = anchor[0] - 1
      temp_piece.coords[0][1] = anchor[1] - 1
      temp_piece.coords[1][0] = anchor[0]
      temp_piece.coords[1][1] = anchor[1] - 1
      temp_piece.coords[3][0] = anchor[0]
      temp_piece.coords[3][1] = anchor[1] + 1
    
      temp_piece.orientation = 1
  elif(piece.name[0] == 'L'): ### Rotate L-piece (4 orientations)
    if(piece.orientation == 1):
      anchor = temp_piece.coords[1]

      temp_piece.coords[0][0] = anchor[0] - 1
      temp_piece.coords[0][1] = anchor[1] 
      temp_piece.coords[2][0] = anchor[0] + 1
      temp_piece.coords[2][1] = anchor[1] 
      temp_piece.coords[3][0] = anchor[0] + 1
      temp_piece.coords[3][1] = anchor[1] + 1 

      temp_piece.orientation = 2
    elif(piece.orientation == 2):
      anchor = temp_piece.coords[1]

      temp_piece.coords[0][0] = anchor[0] 
      temp_piece.coords[0][1] = anchor[1] + 1
      temp_piece.coords[2][0] = anchor[0] 
      temp_piece.coords[2][1] = anchor[1] - 1
      temp_piece.coords[3][0] = anchor[0] + 1
      temp_piece.coords[3][1] = anchor[1] - 1

      temp_piece.orientation = 3
    elif(piece.orientation == 3):
      anchor = temp_piece.coords[1]

      temp_piece.coords[0][0] = anchor[0] - 1
      temp_piece.coords[0][1] = anchor[1]
      temp_piece.coords[2][0] = anchor[0] + 1 
      temp_piece.coords[2][1] = anchor[1]
      temp_piece.coords[3][0] = anchor[0] - 1
      temp_piece.coords[3][1] = anchor[1] - 1

      temp_piece.orientation = 4

    elif(piece.orientation == 4):
      anchor = temp_piece.coords[1]

      temp_piece.coords[0][0] = anchor[0] 
      temp_piece.coords[0][1] = anchor[1] - 1
      temp_piece.coords[2][0] = anchor[0] 
      temp_piece.coords[2][1] = anchor[1] + 1
      temp_piece.coords[3][0] = anchor[0] - 1
      temp_piece.coords[3][1] = anchor[1] + 1

      temp_piece.orientation = 1

      
  out_bounds_vert = False
  out_bounds_left = False
  out_bounds_right = False
  for i in temp_piece.coords:
    if(i[0] < 0):
      out_bounds_vert = True
    if(i[1] > 9):
      out_bounds_right = True
    elif(i[1] < 0):
      out_bounds_left = True

  infinite_loop = 0
  while(out_bounds_vert or out_bounds_left or out_bounds_right):
    for i in temp_piece.coords:
      if(i[0] < 0):
        add_to_coords_vert(temp_piece, 1, board)
      if(i[1] > 9):
        add_to_coords_horiz(temp_piece, -1, board)
      elif(i[1] < 0):
        add_to_coords_horiz(temp_piece, 1, board)
        
    out_bounds_vert = False
    out_bounds_left = False
    out_bounds_right = False  
    for i in temp_piece.coords:
      if(i[0] < 0):
        out_bounds_vert = True
      if(i[1] > 9):
        out_bounds_right = True
      elif(i[1] < 0):
        out_bounds_left = True
        
    infinite_loop += 1
    if(infinite_loop > 20):
        break

  if(move_possible(board, temp_piece.coords)):
      piece.coords = copy.deepcopy(temp_piece.coords)
      piece.orientation = temp_piece.orientation

  for i in piece.returnCoords():
      board[i[0]][i[1]] = piece.name[0]
##############################################################################################################

### Reset piece coordinates ##################################################################################
def reset_piece(piece_to_reset):
  num = piece_to_reset.name[1]

  if(num == 1):
    reset = piece.Piece(('O', 1), [[0,3],[0,4],[1,3],[1,4]])
  elif(num == 2):
    reset = piece.Piece(('Z', 2), [[0,3],[0,4],[1,4],[1,5]])
  elif(num == 3):
    reset = piece.Piece(('S', 3), [[0,4],[0,5],[1,4],[1,3]])
  elif(num == 4):
    reset = piece.Piece(('T', 4), [[0,4],[1,4],[1,3],[1,5]])
  elif(num == 5):
    reset = piece.Piece(('I', 5), [[0,3],[0,4],[0,5],[0,6]])
  elif(num == 6):
    reset = piece.Piece(('J', 6), [[0,3],[1,3],[1,4],[1,5]])
  elif(num == 7):
    reset = piece.Piece(('L', 7), [[1,3],[1,4],[1,5],[0,5]])

  return copy.deepcopy(reset)
##############################################################################################################

### Inserts new piece ########################################################################################
def next_piece():

  num = random.randint(1, 7)

  if(num == 1):
    next_one = piece.Piece(('O', 1), [[0,3],[0,4],[1,3],[1,4]])
  elif(num == 2):
    next_one = piece.Piece(('Z', 2), [[0,3],[0,4],[1,4],[1,5]])
  elif(num == 3):
    next_one = piece.Piece(('S', 3), [[0,4],[0,5],[1,4],[1,3]])
  elif(num == 4):
    next_one = piece.Piece(('T', 4), [[0,4],[1,4],[1,3],[1,5]])
  elif(num == 5):
    next_one = piece.Piece(('I', 5), [[0,3],[0,4],[0,5],[0,6]])
  elif(num == 6):
    next_one = piece.Piece(('J', 6), [[0,3],[1,3],[1,4],[1,5]])
  elif(num == 7):
   next_one = piece.Piece(('L', 7), [[1,3],[1,4],[1,5],[0,5]])
  
  return copy.deepcopy(next_one)
##############################################################################################################

### Draw the current piece, next piece, hold piece on to their respective arrays #############################
def draw_pieces(piece, next_piece, hold_piece, board, hold_arr, next_arr):
  for i in piece.returnCoords():
    board[i[0]][i[1]] = piece.name[0]

  for i in next_piece.return_decor_coords():
      next_arr[i[0]][i[1]] = next_piece.name[0]

  if(hold_piece != 0):
      for i in hold_piece.return_decor_coords():
          hold_arr[i[0]][i[1]] = hold_piece.name[0]
##############################################################################################################

### Check if board is too high to add new piece ##############################################################
def board_too_high(board):
  check = False
  if( not (board[0][3] == 0 and board[0][4] == 0 and board[0][5] == 0 and board[0][6] == 0)):
    check = True
  if( not (board[1][3] == 0 and board[1][4] == 0 and board[1][5] == 0)):
    check = True

  return check
##############################################################################################################

### Check if board has full line #############################################################################
def full_line_present(board):
  for row in board:
    if(0 not in row):
      return True

  return False
##############################################################################################################

### Rotate piece clockwise, rewrite previous position ########################################################
def rotate(board, piece):
  for i in piece.returnCoords():
    board[i[0]][i[1]] = 0

  rotate_piece()

  for i in piece.returnCoords():
    board[i[0]][i[1]] = piece.name[0]
##############################################################################################################

### Check if board all clear, add points if so ###############################################################
def check_all_clear(board):
    global score
    global all_clear

    all_clear = False
    
    empty_line = [0,0,0,0,0,0,0,0,0,0]
    clear = True
    for row in board:
        if(row != empty_line):
            clear = False

    if(clear):
        score += 1000
        all_clear = True
    
### Remove full line and add empty lines to top ##############################################################
def remove_full_lines(board):
  global score
  global tetris
  global line_clear
  line_clear = [False, 0]
  tetris = False
  
  count = 0
  while(full_line_present(board)):
    for row in board:
      if(0 not in row):
        board.remove(row)
        count += 1

  if(count == 4):
      score += 500
      tetris = True
  elif(count > 0):
      line_clear = [True, count]
      score += 100 * count
      
  for i in range(count):
    board.insert(0, [0,0,0,0,0,0,0,0,0,0])
##############################################################################################################

### Drops piece, rewrites previous position with zeros #######################################################
def drop_piece(board, piece):

  for i in piece.returnCoords():
    board[i[0]][i[1]] = 0

  add_to_coords_vert(piece, collision(board, piece), board)

  for i in piece.returnCoords():
    board[i[0]][i[1]] = piece.name[0]
#############################################################################################################  
  
### Count the number of units you can drop before collision #################################################
def collision(board, piece):
  lowest = piece.lowestColumns()
  counts = []
  for i in lowest:
    counts.append(0)

  for i in range(len(lowest)):
    for row in range(len(board)):
      if(row > lowest[i][0]):
        if(board[row][lowest[i][1]] == 0):
          counts[i] += 1
        else:
          break
  return min(counts)

##############################################################################################################
  
### Move Piece Right #########################################################################################
def move_right(board, piece):
  for i in piece.returnCoords():
    board[i[0]][i[1]] = 0

  add_to_coords_horiz(piece, 1, board)

  for i in piece.returnCoords():
    board[i[0]][i[1]] = piece.name[0]
  
##############################################################################################################

### Move Piece Left #########################################################################################
def move_left(board, piece):
  for i in piece.returnCoords():
    board[i[0]][i[1]] = 0

  add_to_coords_horiz(piece, -1, board)

  for i in piece.returnCoords():
    board[i[0]][i[1]] = piece.name[0]
  
##############################################################################################################
    
### Updates leaderboard based on current player score ##########################################################
def update_leaderboard(leaders):
    global new_leader
    global score
    space = ' '
    w = '\33[37m'
    black = '\33[30m'
    r = '\33[31m'
    y = '\33[33m'
    g = '\33[32m'
    c = '\33[36m'
    b = '\33[34m'
    m = '\33[35m'

    top_5 = False
    for player in leaders:
        if(score > player[0]):
            top_5 = True
            new_leader[0] = True

    if(not top_5):
        return

    line1 = f'{r}  _{y}___{g}_  {c}   {b}   {m}   {r}   {y}   {g}   {c}   {b} __{m}   {r}   {y}__'
    line2 = f'{m} {r}/ _{y}__/{g}__ {c} __{b}_  {m}___{r} __{y}___{g}___{c} _/{b} /_{m}___{r} / {y}/'
    line3 = f'{m}/ {r}/__{y}/ _{g} \/{c} _ {b}\/ {m}_ `{r}/ _{y}_/ {g}_ `{c}/ _{b}_(_{m}-</{r}_/ '
    line4 = f'{m}\__{r}_/\{y}___{g}/_/{c}/_/{b}\_,{m} /_{r}/  {y}\_,{g}_/\{c}__/{b}___{m}(_){r}  '
    line5 = f'             {c} /_{b}__/                      '
    print(f'{line1:^175}')
    print(f'{line2:^180}')
    print(f'{line3:^175}')
    print(f'{line4:^175}')
    print(f'{line5:^115}')
    print()
    line6 = f'{c}You made it on the leaderboard!'
    line7 = f'{c}Please enter your name\n\n   {w}'
    line8 = f'{w}Name must be 10 characters or less\n'
    print(f'{line6:^110}')
    user_name = input(f'{line7:^120}')

    while(len(user_name) > 10):
        
        print(f'{line8:^110}')
        user_name = input(f'{line7:^120}')
    print()
    
    leaders.append([score, user_name])
    leaders.sort()
    leaders.reverse()
    leaders.pop()
    new_leader[1] = leaders.index([score, user_name])

    f = open("Leaderboard.txt", "w")

    new_leaderboard = ''
    for player in leaders:
        for val in player:
            new_leaderboard += str(val) + ','
            
    f = open("Leaderboard.txt", "w")
    f.write(new_leaderboard[:len(new_leaderboard)-1])
    f.close()
    
##############################################################################################################
    
### Display current Leaderboard, takes a list of lists #######################################################
def display_leaderboard(leaders):
    space = ' '
    cyan = '\33[36m'
    red = '\33[31m'
    white = '\33[37m'
    yellow = '\33[33m'

    ranks = ['1ST', '2ND', '3RD', '4TH', '5TH']

    print()
    if(not new_leader[0]):
        line = f'{red}{space:>8}SCORE{space:>9}NAME'
        print(f'{line:^110}\n')
        for i in range(5):
            line = f'{white}{ranks[i]}{space:>3}{leaders[i][0]:>7}{space:>3}{leaders[i][1]:>10}'
            print(f'{line:^110}')
    else:
        line = f'{red}{space:>8}SCORE{space:>9}NAME'
        print(f'{line:^110}\n')
        for i in range(5):
            if(i != new_leader[1]):
                line = f'{white}{ranks[i]}{space:>3}{leaders[i][0]:>7}{space:>3}{leaders[i][1]:>10}'
            else:
                line = f'{yellow}{ranks[i]}{space:>3}{leaders[i][0]:>7}{space:>3}{leaders[i][1]:>10}'
            print(f'{line:^110}')
    
##############################################################################################################

### Rewrite board to have game over message ##################################################################
def game_over_board(board):
    for i in range(6):
        board[7][2+i] = ''
        board[8][2+i] = ''
        board[9][2+i] = ''
        board[10][2+i] = ''
        
    board[7][2] = '1'
    board[8][2] = '2'
    board[9][2] = '3'
    board[10][2] = '1'
##############################################################################################################
    
### Displays left board including hold, score ################################################################
def display_left(board, hold_arr, i):
    global score
    global decor_array_row
    space = ' '
    white = '\33[37m'
    cyan = '\33[36m'
    black = '\33[30m'
    yellow = '\33[33m'
    magenta = '\33[35m'
    green = '\33[32m'
    red = '\33[31m'
    blue = '\33[34m'
    
    if(i == 0):
      print(f'{space:>32}| {white}HOLD{space:>4}{cyan}|', end = '')
    elif(1 <= i <= 2):
      print(f'{space:>32}{cyan}| ', end = '')
      for hold_item in hold_arr[decor_array_row]:
          if(hold_item == 'O'):
            print(f'{yellow}{hold_item:^2}', end = '')
          elif(hold_item == 'Z'):
            print(f'{red}{hold_item:^2}', end = '')
          elif(hold_item == 'S'):
            print(f'{green}{hold_item:^2}', end = '')
          elif(hold_item == 'T'):
            print(f'{magenta}{hold_item:^2}', end = '')
          elif(hold_item == 'I'):
            print(f'{cyan}{hold_item:^2}', end = '')
          elif(hold_item == 'J'):
            print(f'{blue}{hold_item:^2}', end = '')
          elif(hold_item == 'L'):
            print(f'{white}{hold_item:^2}', end = '')
          elif(hold_item == 0):
            print(f'{black}{hold_item:^2}', end = '')
      print(f'{cyan}|', end = '')
    elif(i == 3):
      print(f'{space:>32}----------|', end = '')
    elif(i == 6 or i == 9):
        print(f'{space:>32}{cyan}----------{cyan}|', end = '')
    elif(i == 7):
        print(f'{space:>32}{cyan}| {white}SCORE{space:>3}{cyan}|', end = '')
    elif(i == 8):
        num_zeroes = 7 - len(str(score))
        zero = '0'
        print(f'{space:>32}{cyan}| {red}{zero*num_zeroes}{white}{score}{cyan} |', end = '')
    else:
        print(f'{space:>42}|', end = '')
##############################################################################################################
### Display right board including next piece, special scores ###################################################
def display_right(board, next_arr, i):
    global score
    global decor_array_row
    global tetris
    global all_clear
    global line_clear
    
    space = ' '
    white = '\33[37m'
    cyan = '\33[36m'
    black = '\33[30m'
    yellow = '\33[33m'
    magenta = '\33[35m'
    green = '\33[32m'
    red = '\33[31m'
    blue = '\33[34m'
    
    if(i == 0):
      print(f'{cyan}|{white}{space:>1}NEXT{space:>4}{cyan}|')
    elif(1 <= i <= 2):
      print(f'{cyan}| ', end = '')
      for next_item in next_arr[decor_array_row]:
          if(next_item == 'O'):
            print(f'{yellow}{next_item:^2}', end = '')
          elif(next_item == 'Z'):
            print(f'{red}{next_item:^2}', end = '')
          elif(next_item == 'S'):
            print(f'{green}{next_item:^2}', end = '')
          elif(next_item == 'T'):
            print(f'{magenta}{next_item:^2}', end = '')
          elif(next_item == 'I'):
            print(f'{cyan}{next_item:^2}', end = '')
          elif(next_item == 'J'):
            print(f'{blue}{next_item:^2}', end = '')
          elif(next_item == 'L'):
            print(f'{white}{next_item:^2}', end = '')
          elif(next_item == 0):
            print(f'{black}{next_item:^2}', end = '')
      decor_array_row += 1
      print(f'{cyan}|')
    elif(i == 3):
      print(f'{cyan}|----------')
    elif(i == 7):
        if(tetris and all_clear):
            print(f'{cyan}|  {white}~{red}T{yellow}e{green}t{cyan}r{blue}i{magenta}s {white}and {red}A{yellow}l{green}l{cyan}-{blue}c{magenta}l{red}e{yellow}a{green}r{cyan}!{white}~')
        elif(tetris):
            print(f'{cyan}|  {white}~{red}T{yellow}e{green}t{cyan}r{blue}i{magenta}s{red}!{white}~')
        elif(all_clear):
            print(f'{cyan}|  {white}~{red}A{yellow}l{green}l{cyan}-{blue}c{magenta}l{red}e{yellow}a{green}r{cyan}!{white}~')
        elif(line_clear[0]):
            print(f'{cyan}|  {white}-{cyan}Line Clear X {line_clear[1]}{white}-')
        else:
            print(f'{cyan}|')
    elif(i == 8):
        if(tetris and all_clear):
            a = '1500pts'
            print(f'{cyan}|  {white}{a:^23}')
        elif(tetris):
            b = '500pts'
            print(f'{cyan}|  {white}{b:^9}')
        elif(all_clear):
            c = '1000pts'
            print(f'{cyan}|  {white}{c:^12}')
        elif(line_clear[0]):
            d = str(line_clear[1] * 100) + 'pts'
            print(f'{cyan}|  {white}{d:^16}')
        else:
            print(f'{cyan}|')
    else:
      print(f'{cyan}|')

##############################################################################################################

### Displays board in string format ##########################################################################
def display_board(board, next_arr, hold_arr):
  global score
  global decor_array_row
  space = ' '
  white = '\33[37m'
  cyan = '\33[36m'
  black = '\33[30m'
  yellow = '\33[33m'
  magenta = '\33[35m'
  green = '\33[32m'
  red = '\33[31m'
  blue = '\33[34m'

  decor_array_row = 0  
  print(f'{space:>32}{cyan}------------------------------------------')
  for i in range(len(board)):
      
    display_left(board, hold_arr, i)
    
    for q in range(len(board[i])):
      item = board[i][q]
      if(item == 'O'):
        print(f'{yellow}{item:^2}', end = '')
      elif(item == 'Z'):
        print(f'{red}{item:^2}', end = '')
      elif(item == 'S'):
        print(f'{green}{item:^2}', end = '')
      elif(item == 'T'):
        print(f'{magenta}{item:^2}', end = '')
      elif(item == 'I'):
        print(f'{cyan}{item:^2}', end = '')
      elif(item == 'J'):
        print(f'{blue}{item:^2}', end = '')
      elif(item == 'L'):
        print(f'{white}{item:^2}', end = '')
      elif(item == 0):
        print(f'{black}{item:^2}', end = '')
      elif(item == '1'):
        print(f'{red}----------- ', end = '')
      elif(item == '2'):
        print(f'{red}| G A M E | ', end = '')
      elif(item == '3'):
        print(f'{red}| O V E R | ', end = '')
        
    display_right(board, next_arr, i)
    
  print(f'{space:>42}{cyan}----------------------')
  print()

##############################################################################################################

### Displays title in ascii format ###########################################################################
def display_title():
  white = '\33[37m'
  cyan = '\33[36m'
  black = '\33[30m'
  yellow = '\33[33m'
  magenta = '\33[35m'
  green = '\33[32m'
  red = '\33[31m'
  blue = '\33[34m'
  
  print(f'{white}TTTTTTTTTTTTTTTTTTTTTTT                         tttt                              iiii                   ')
  print(f'{white}T{magenta}:::::::::::::::::::::{white}T                      ttt{red}:::{white}t                             i{cyan}::::{white}i                  ')
  print(f'{white}T{magenta}:::::::::::::::::::::{white}T                      t{red}:::::{white}t                              iiii                   ')
  print(f'{white}T{magenta}:::::{white}TT{magenta}:::::::{white}TT{magenta}:::::{white}T                      t{red}:::::{white}t                                                     ')
  print(f'{white}TTTTTT  T{magenta}:::::{white}T  TTTTTTeeeeeeeeeeee    ttttttt{red}:::::{white}ttttttt   rrrrr   rrrrrrrrr  iiiiiii     ssssssssss   ')
  print(f'        {white}T{magenta}:::::{white}T      ee{yellow}::::::::::::{white}ee  t{red}:::::::::::::::::{white}t   r{blue}::::{white}rrr{blue}:::::::::{white}r i{cyan}:::::{white}i   ss{green}::::::::::{white}s  ')
  print(f'        {white}T{magenta}:::::{white}T     e{yellow}::::::{white}eeeee{yellow}:::::{white}eet{red}:::::::::::::::::{white}t   r{blue}:::::::::::::::::{white}r i{cyan}::::{white}i ss{green}:::::::::::::{white}s ')
  print(f'        {white}T{magenta}:::::{white}T    e{yellow}::::::{white}e     e{yellow}:::::{white}etttttt{red}:::::::{white}tttttt   rr{blue}::::::{white}rrrrr{blue}::::::{white}ri{cyan}::::{white}i s{green}::::::{white}ssss{green}:::::{white}s')
  print(f'        {white}T{magenta}:::::{white}T    e{yellow}:::::::{white}eeeee{yellow}::::::{white}e      t{red}:::::{white}t          r{blue}:::::{white}r     r{blue}:::::{white}ri{cyan}::::{white}i  s{green}:::::{white}s  ssssss ')
  print(f'        {white}T{magenta}:::::{white}T    e{yellow}:::::::::::::::::{white}e       t{red}:::::{white}t          r{blue}:::::{white}r     rrrrrrri{cyan}::::{white}i    s{green}::::::{white}s      ')
  print(f'        {white}T{magenta}:::::{white}T    e{yellow}::::::{white}eeeeeeeeeee        t{red}:::::{white}t          r{blue}:::::{white}r            i{cyan}::::{white}i       s{green}::::::{white}s   ')
  print(f'        {white}T{magenta}:::::{white}T    e{yellow}:::::::{white}e                 t{red}:::::{white}t    ttttttr{blue}:::::{white}r            i{cyan}::::{white}i ssssss   s{green}:::::{white}s ')
  print(f'      {white}TT{magenta}:::::::{white}TT  e{yellow}::::::::{white}e                t{red}::::::{white}tttt{red}:::::{white}tr{blue}:::::{white}r           i{cyan}::::::{white}is{green}:::::{white}ssss{green}::::::{white}s')
  print(f'      {white}T{magenta}:::::::::{white}T   e{yellow}::::::::{white}eeeeeeee        tt{red}::::::::::::::{white}tr{blue}:::::{white}r           i{cyan}::::::{white}is{green}::::::::::::::{white}s ')
  print(f'      {white}T{magenta}:::::::::{white}T    ee{yellow}:::::::::::::{white}e          tt{red}:::::::::::{white}ttr{blue}:::::{white}r           i{cyan}::::::{white}i s{green}:::::::::::{white}ss  ')
  print(f'      {white}TTTTTTTTTTT      {white}eeeeeeeeeeeeee            ttttttttttt  rrrrrrr           iiiiiiii  sssssssssss    ')
  print()
  print()
  
##############################################################################################################

### Displays menu in string format ###########################################################################
def display_menu():
  cyan = '\33[36m'
  white = '\33[37m'

  s = f'{cyan} - - - - - - {white}(1) Start Game (1){cyan} - - - - - -'
  i = f'{cyan} - - - - - - {white}(2) Instructions (2){cyan} - - - - - -'
  l = f'{cyan} - - - - - - {white}(3) Leaderboard (3){cyan} - - - - - -'
  e = f'{cyan} - - - - - - {white}(4) Exit Game (3){cyan} - - - - - -'
  space = ''
  print(f'{s:^120}')
  print(f'{i:^120}')
  print(f'{l:^120}')
  print(f'{e:^120}')

##############################################################################################################
##############################################################################################################

# initialize variables
space = ' '
user_in = ''
white = '\33[37m'

global score
score = 0
global tetris
tetris = False
global all_clear
all_clear = False
global line_clear
line_clear = [False, 0]
global new_leader
new_leader = [False, None]
game_played = False

# read leaderboard file
f = open("Leaderboard.txt", "r")
temp = f.read().split(',')
f.close()
leader_list = []
    
for i in range(0, len(temp), 2):
    leader_list.append([int(temp[i]), temp[i + 1]])

# display menu, take menu input
display_title()
display_menu()

menu_input = input(f'{white}')
while(not (menu_input == '1' or menu_input == '2' or menu_input == '3' or menu_input == '4')):
    print(f'{white}{space:>38}Valid inputs are: "1", "2", "3", "4"')
    menu_input = input(f'{white}')

while(menu_input == '2' or menu_input == '3'):
  os.system('cls')
  if(menu_input == '2'):
      print(f'{white}{space:>47}Instructions:')
      print(f'{white}{space:>22}Input "a", "d", to shift the piece left, or right respectively.')
      print(f'{white}{space:>24}Input "h" to switch the current piece with the held piece')
      print(f'{white}{space:>27}Press the enter key with no input to drop the piece.')
      print(f'{white}{space:>20}Lines will disappear once there are no gaps along the horizontal.')
      print(f'{white}{space:>20}When the height of the board obstructs a piece, the game is over.')
      print(f'{white}{space:>16}At any point after starting the game, you may input "end" to end the game.')
  elif(menu_input == '3'):
      display_leaderboard(leader_list)
  
  print()
  back = input(f'{white}{space:>41}Enter anything to go back\n')
  print()
  print()
  os.system('cls')
  display_title()
  display_menu()
  menu_input = input(f'{white}')

# create boards, initialize pieces, display board
if(menu_input == '1'):
  os.system('cls')
  brd = [[0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0]]

  hold_array = [[0,0,0,0],
                [0,0,0,0]]
  
  next_array = [[0,0,0,0],
                [0,0,0,0]]
  
  current_piece = next_piece()
  next_one = next_piece()
  hold_piece = 0

  draw_pieces(current_piece, next_one, hold_piece, brd, hold_array, next_array)
  display_board(brd, next_array, hold_array)
  
  # Enter game loop
  while(user_in.lower() != 'end'):
    game_played = True
    user_in = input(f'{white}')

    while(not (user_in.lower() == 'w' or user_in.lower() == 'a' or user_in.lower() == 'd' or user_in.lower() == 'end' or user_in == '' or user_in.lower() == 'r' or user_in.lower() == 'h')):
      print(f'{white}{space:>31}Valid inputs are: "a", "d", "r", "", or "end"')
      user_in = input(f'{white}')

    # Take non-drop input, loop until drop
    hold_not_used = True
    while(not (user_in == '' or user_in.lower() == 'end')):
      if(user_in.lower() == 'd'):
        move_right(brd, current_piece)
      elif(user_in.lower() == 'a'):
        move_left(brd, current_piece)
      elif(user_in.lower() == 'r'):
        rotate_piece(current_piece, brd)
      elif(user_in.lower() == 'h' and hold_not_used):
        clear_piece(brd, current_piece)
        if(hold_piece == 0):
            hold_piece = reset_piece(current_piece)
            current_piece = copy.deepcopy(next_one)
        else:
            current_piece = reset_piece(current_piece)
            current_piece, hold_piece = copy.deepcopy(hold_piece), copy.deepcopy(current_piece)
        hold_not_used = False

      hold_array = [[0,0,0,0],
                    [0,0,0,0]]
  
      next_array = [[0,0,0,0],
                    [0,0,0,0]]
      os.system('cls')
      draw_pieces(current_piece, next_one, hold_piece, brd, hold_array, next_array)
      display_board(brd, next_array, hold_array)
      user_in = input(f'{white}')
      
    if(user_in.lower() == 'end'):
      break
    
    drop_piece(brd, current_piece)
    score += 40
    remove_full_lines(brd)
    check_all_clear(brd)
    
    if(board_too_high(brd)):
      break

    current_piece = copy.deepcopy(next_one)
    next_one = next_piece()

    hold_array = [[0,0,0,0],
                  [0,0,0,0]]
  
    next_array = [[0,0,0,0],
                  [0,0,0,0]]
    os.system('cls')
    draw_pieces(current_piece, next_one, hold_piece, brd, hold_array, next_array)
    display_board(brd, next_array, hold_array)

# post-game things: game over screen, leaderboard
if(game_played):
    game_over_board(brd)
    os.system('cls')
    display_board(brd, next_array, hold_array)
    line = 'Enter anything to view leaderboard\n'
    print(f'{white}{line:^105}')
    pause = input(f'')
    update_leaderboard(leader_list)
    display_leaderboard(leader_list)
    pause = input('')
