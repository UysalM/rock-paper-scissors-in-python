import random

computer_option = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0
while player_score < 3 and computer_score < 3:
  computer_hand = random.choice(computer_option)
  player_hand = input('Enter your choice(rock/paper/scissors): ')
  print(f'you chose {player_hand}, computer chose {computer_hand}')
  
  if player_hand == computer_hand:
    print(f"Both chose {player_hand}, it's a tie.")
  elif player_hand == 'rock':
    if computer_hand == 'scissors':
      print("Rock smashes scissors, player wins")
      player_score += 1
      print("Player score = " + str(player_score))
    else:
      print("Paper covers rock, computer wins")
      computer_score += 1
      print("Computer score = " + str(computer_score))
  elif player_hand == 'paper':
    if computer_hand == 'rock':
      print("Paper covers rock, player wins")
      player_score += 1
      print("Player score = " + str(player_score))
    else:
      print("Scissors cut paper, computer wins")
      computer_score += 1
      print("Computer score = " + str(computer_score))
  elif player_hand == 'scissors':
    if computer_hand == 'paper':
      print("Scissors cut paper, player wins")
      player_score += 1
      print("Player score = " + str(player_score))
    else:
      print("Rock smashes scissors, computer wins")
      computer_score += 1
      print("Computer score = " + str(computer_score))