from getpass import getpass as input
print('''
The game is Rock, Paper,Scissors
We have two players
Each player gets a prompt to put in their play
The game is over after a player wins three games
''')
winA=0
winB=0
while True:
  player_1= input(prompt= 'Player 1> ')
  player_2= input(prompt= 'Player 2> ')
  
  
  if player_1== 'R':
    if player_2== 'S':
      winA += 1
      print('Player 1 wins')
    elif player_2== 'P':
      winB += 1
      print('Player 2 wins')
    else:
      print('It is a draw')
  elif player_1== 'S':
    if player_2== 'P':
      winA += 1
      print('Player 1 wins')
    elif player_2== 'R':
      winB += 1
      print('Player 2 wins')
    else:
      print('It is a draw')
  elif player_1== 'P':
    if player_2== 'R':
      winA += 1
      print('Player 1 wins')
    elif player_2== 'S':
      winB += 1
      print('Player 2 wins')
    else:
      print('It is a draw')
  if winA==3 or winB==3:
    break
  else:
    continue
  exit()
else:
  print('The Game is Rock, Paper, Scissors! Get with it')