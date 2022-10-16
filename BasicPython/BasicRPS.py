from getpass import getpass as input
print('''
The game is Rock, Paper,Scissors
We have two players
Each player gets a prompt to put in their 
''')
player_1= input(prompt= 'Player 1> ')
player_2= input(prompt= 'Player 2> ')


if player_1== 'R':
  if player_2== 'S':
    print('Player 2 loses')
  elif player_2== 'P':
    print('Player 2 wins')
  else:
    print('It is a draw')
elif player_1== 'S':
  if player_2== 'P':
    print('Player 2 loses')
  elif player_2== 'R':
    print('Player 2 wins')
  else:
    print('It is a draw')
elif player_1== 'P':
  if player_2== 'R':
    print('Player 2 loses')
  elif player_2== 'S':
    print('Player 2 wins')
  else:
    print('It is a draw')
else:
  print('The Game is Rock, Paper, Scissors! Get with it')