import turtle, sys

t = turtle.Turtle()

pos = turtle.Turtle()

sc = turtle.Screen()

sc.bgcolor("black")

turn = -1

origin = [0,0]
up_left = [-120,120]
up_center = [-40,120]
up_right = [40,120]
middle_left = [-120,40]
middle_center = [-40,40]
middle_right = [40,40]
down_left = [-120,-40]
down_center = [-40,-40]
down_right = [40,-40]

global wait
wait = False

grid_pos = [origin,up_left,up_center,up_right,middle_left,middle_center,middle_right,down_left,down_center,down_right]

def grid():
  tic=[1,2,3]
  tac=[4,5,6]
  toe=[7,8,9]
  global grid
  grid = [tic, tac, toe]
#Restart grid value
  for b in range(3):
    for a in range(3):
      grid[b][a] = "none"
  return grid

def t_place(degree, advance=0):
  t.color("white")
  t.pu()
  t.seth(degree)
  t.fd(advance)
  
def draw_grid():
  t.pu()
  t.pensize(5)
  t.color("white")
  t.right(90)
  
  t.goto(40,120)
  t.pd()
  t.fd(240)
  
  t.pu()
  t.goto(-40,120)
  t.pd()
  t.fd(240)

  t.right(90)
  
  t.pu()
  t.goto(120,40)
  t.pd()
  t.fd(240)
  
  t.pu()
  t.goto(120,-40)
  t.pd()
  t.fd(240)
  t.ht()

  for i in range(1,10):
    t.pu()
    t.goto(grid_pos[i])
    t_place(315,56.57)
    t.write(str(i),align='center')

def draw_changeGrid(PInput, PName):
  def draw_X(Pinput):
# Rajouter l'emplacement auto (PInput)
    t.pu()
    t.goto(grid_pos[Pinput])
    
    t_place(315,11.5)
    t.pd()
    t.fd(90)
   
    t_place(90, 63.64)
    t.left(135)
    t.pd()
    t.fd(90)
  def draw_O(Pinput):
    t.pu()
    t.goto(grid_pos[Pinput])

    t_place(315,90)
    t.pd()
    t.seth(45)
    t.circle(31.82)
  
  if (PName == "X"):
    draw_X(PInput)
  elif (PName == "O"):
    draw_O(PInput)
  end_game(grid)
    
def changeGrid(playerInput, playerName):
  int(playerInput)
  str(playerName)
  repeat_turn = 1
  if(bool(int(playerInput)) == True):
    if (playerInput == 1):
      if(grid[0][0] == "none"):
        grid[0][0] = playerName
        draw_changeGrid(playerInput,playerName)
      else:
       print("Already occupied") 
       repeat_turn = -1
    elif (playerInput == 2):
      if(grid[0][1] == "none"):
        grid[0][1] = playerName
        draw_changeGrid(playerInput,playerName)
      else:
        print("Already occupied")
        repeat_turn = -1  
    elif (playerInput == 3):
      if(grid[0][2] == "none"):
        grid[0][2] = playerName
        draw_changeGrid(playerInput,playerName)
      else:
        print("Already occupied")
        repeat_turn = -1  
    elif (playerInput == 4):
      if(grid[1][0] == "none"):
        grid[1][0] = playerName
        draw_changeGrid(playerInput,playerName)
      else:
        print("Already occupied")
        repeat_turn = -1  
    elif (playerInput == 5):
      if(grid[1][1] == "none"):
        grid[1][1] = playerName
        draw_changeGrid(playerInput,playerName)
      else:
        print("Already occupied")
        repeat_turn = -1  
    elif (playerInput == 6):
      if(grid[1][2] == "none"):
        grid[1][2] = playerName
        draw_changeGrid(playerInput,playerName)
      else:
        print("Already occupied")
        repeat_turn = -1  
    elif (playerInput == 7):
      if(grid[2][0] == "none"):
        grid[2][0] = playerName
        draw_changeGrid(playerInput,playerName)
      else:
        print("Already occupied")
        repeat_turn = -1  
    elif (playerInput == 8):
      if(grid[2][1] == "none"):
        grid[2][1] = playerName
        draw_changeGrid(playerInput,playerName)
      else:
        print("Already occupied")
        repeat_turn = -1    
    elif (playerInput == 9):
      if(grid[2][2] == "none"):
        grid[2][2] = playerName
        draw_changeGrid(playerInput,playerName)
      else:
        print("Already occupied")

  elif (bool(int(playerInput)) == False):
    print("Try again!")

  print(grid)
  return repeat_turn

def click(x,y):
  global wait
  if not wait:
    wait = True
    case_selected(x,y)
  else:
    print("Wait!")

def case_selected(x,y):
  a = 0
  for i in range(1,10):
    if grid_pos[i][0] < x < grid_pos[i][0] + 78 and grid_pos[i][1] > y > grid_pos[i][1] - 78:
      global turn
      if(turn == 1):
        Name = "O"
      else:
        Name = "X"
      turn = turn * -1
      changeGrid(i, Name)
      print(i)
      a -= 1
    else:
      a += 1
      if a == 9:
        print("\033[1;31;40m")
        print("Please, click on a case in the grid.")
        print("\033[0;37;48m")
  
    
#End Game
def end_game(check_grid):
  global wait
  wait = False
  #End Game|O winner
  for i in range(3):
    if(check_grid[i][0] == check_grid[i][1] == check_grid[i][2] == "O"):
      print("O wins!")
      endgame('O')
    else:
      i += 1  
  for i in range(3):
    if(check_grid[0][i] == check_grid[1][i] == check_grid[2][i] == "O"):
      print("O wins!")
      endgame('O')    
    else:
      i += 1  
  if(check_grid[0][0] == check_grid[1][1] == check_grid[2][2] == "O"): 
    print("O wins!")
    endgame('O')
  elif(check_grid[0][2] == check_grid[1][1] == check_grid[2][0] == "O"): 
    print("O wins!")
    endgame('O')    
  #End Game|X winner
  for i in range(3):
    if(check_grid[i][0] == check_grid[i][1] == check_grid[i][2] == "X"):
      print("X wins!")
      endgame('X')      
    else:
      i += 1  
  for i in range(3):
    if(check_grid[0][i] == check_grid[1][i] == check_grid[2][i] == "X"):
      print("X wins!")
      endgame('X')
    else:
      i += 1  
  if(check_grid[0][0] == check_grid[1][1] == check_grid[2][2] == "X"): 
    print("X wins!")
    endgame('X')
  elif(check_grid[0][2] == check_grid[1][1] == check_grid[2][0] == "X"): 
    print("X wins!")
    endgame('X')
#End Game|No winner    
  elif(check_grid[0][0] != "none" and check_grid[0][1] != "none" and check_grid[0][2] != "none" and check_grid[1][0] != "none" and check_grid[1][1] != "none" and check_grid[1][2] != "none" and check_grid[2][0] != "none" and check_grid[2][1] != "none" and check_grid[2][2] != "none"):
    print("Nobody wins")
    endgame('Nobody')
#End Game|Not finish yet
  else:
    print("")
    pass

def endgame(winner):
  if winner == "Nobody":
    sc.textinput("Equality", f"{winner} wons.")
  else:
    sc.textinput("NEW Champion!", f"{winner} wons.")
  sys.exit()
  
end = False
draw_grid()
grid = grid()

sc.onclick(click)
turtle.mainloop()
