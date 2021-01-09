#Sholeh Sepehri

def crossword(L):
  letterPos = 0 # letterPos keeps track of the position of a word's intersecting letter on the grid, which is used later to move a word up or to the left
  board = [[' '] * 20 for row in range(20)]
  firstword(board,L)
  first_word = firstword(board,L) # Updates crossword with what the first word of the List is
  first_word
  L = L[1:] # Ignores the first word in the list since it was already added in firstword(board,List)
  for word in L:
    for letter in range(len(word)): # Checks each letter in the word that is being iterated through in the previous loop
      if CheckingGrid(board,word[letter],word,letterPos) == True:
        break
      elif (letter==len(word)-1): # Checks if it is the last letter of the word and if it still was not added, it returns the following error message
        print(word,"cannot be placed") 
      letterPos += 1
    letterPos = 0 # Resets letterPos for the next word in the List
  printboard(board)


def printboard(b):
  print('_______________________________________')
  for row in range(len(b)):
    for col in range(len(b[row])):
      print(b[row][col], end = ' ') # Makes the 20x20 grid
    print()
  print('_______________________________________')


def firstword(board, List):
  lencol = len(board)
  lenrow = len(board[0])
  for word in List:
    lenword = len(word)
    if lenword > lencol:
      List.remove(word) # If the first word is too long, it removes that word from the list and tries to place the next "first" word onto the grid
      print(word, "cannot be placed" )
      return False
    for k in range(lenword):
      lencolumn= lencol//2 - lenword//2 + k # Finds the middle position in the grid
      board[lenrow//2][lencolumn] = word[k] # Places the first word in the middle of the grid
    return True


def CheckingGrid(board,letter,word,letterPos):
  for row in range(len(board)):
    for col in range(len(board[row])):
      if board[row][col] == letter: # Looks for an intersecting letter
        if checkvertical(board,word,row,col) == True:
          board = addvertical(board,word,row,col,letterPos) # Updates the board 
          return True
        if checkhorizontal(board,word,row,col) == True:
          board =addhorizontal(board,word,row,col,letterPos) # Updates the board
          return True
        

def checkvertical(board,word,row,col):
  count = 1 # A counter used to keep track of how many letters in the word can be placed legally onto a column on the grid
  lenword = len(word)
  try:
    if lenword + row > 20: # Checks to see if the lenght of the word fits onto the board
      return False
    for k in range(lenword):
      if (board[row+k][col] == ' ' or board[row+k][col] == word[k]) and (board[row-k][col] == ' ' or board[row-k][col] == word[k]): 
      # Line 68: Checks if a column is empty or if there is an intersection with a letter that is already on the grid
        if board[row-k][col-1] == ' ' and board[row-k][col+1] == ' ' and board[row+k][col+1] == ' ' and board[row+k][col-1] == ' ':
        # Line 70: For each empty spot in the column, it checks to see if the spots to the left and right of the empty spot are empty as well (Checks for legal adjancies)           
          count += 1
    if count == lenword: # Checks if all the letters were able to be placed legally on a column on the grid
      return True
  except:
    return False
  return False
  

def checkhorizontal(board,word,row,col):
  try:
    count1 = 1  # A counter used to keep of how many letters in the word can be placed legally onto a row on the grid
    lenword = len(word)
    if lenword + col  > 20: # Checks to see if the lenght of the word fits onto the board
      return False
    for k in range(lenword):
      if (board[row][col+k] == ' ' or board[row][col+k] == word[k]) and (board[row][col-k] == ' ' or board[row][col-k] == word[k]):
      # Line 87: Checks if a row is empty or if there is an intersection with a letter that is already on the grid
        if board[row-1][col-k] == ' ' and board[row+1][col-k] == ' ' and board[row+1][col+k] == ' ' and  board[row-1][col+k] == ' ' :
        # Line 89: For each empty spot in the row, checks to see if the stops to the top and bottom of the empty spot are empty as well (Checks for legal adjancies)                        
          count1 += 1
    if count1 == lenword: # Checks if all the letters were able to be legally placed on a row on the grid
      return True
  except:
    return False
  return False


def addvertical(board,word,row,col, letterPos):
  for k in range(len(word)):
    board[row + k- letterPos][col] = word[k] # Places the word on the board
  return board


def addhorizontal(board,word,row,col,letterPos):
  for k in range(len(word)):
    board[row][col + k - letterPos] = word[k] # Places the word on the board
  return board

# TEST CASES

print('List Test #1:')
L = ['rattlesnake','koala','rhinoceris','dinosaur','elephant','aardwolf','chimpanzee','dino','parrot','lamb','cat']
print(L)
print('_______________________________________')
crossword(L)
print('')
print('')


print('List Test #2:')
L1 = ['Wolfeschlegelsteinhausenbergerdorff','dylan', 'kami', 'deandra', 'maryam', 'jonathan', 'sam', 'richard','ethan', 'lorena', 'kyle', 'ben','andrew']
print(L1)
print('_______________________________________')
crossword(L1)
print('')
print('')


print('List Test #3:')
L2 = ['rosalina','rosalina','mario','luigi','waluigi','wario','kirby','daisy','peine']
print(L2)
print('_______________________________________')
crossword(L2)




