
import random 
from replit import clear
from logo import logo

#Number of appemts depending on the difficulty 
easy_level_attemps = 10
hard_level_attemps = 5

#function to check if the users guess is to high, low or spot on
def check_answer(users_guess, random_number, turns):
  if users_guess < random_number:
    print("To low.")
    #minus an attempts every time the user guesses incorrectly 
    return turns - 1
  elif users_guess > random_number:
    print("to High.")
    #minus an attempts every time the user guesses incorrectly 
    return turns - 1
  else:
    print(f"Yes! you got it! the number was {random_number}")

#return the amount of attempts depending on the level the user chooses 
def set_difficulty():
  difficulty = input("choose a difficulty. Type 'easy' for 10 attempts or 'hard' for 5 attempts: ")
  if difficulty == "easy":
    return easy_level_attemps
  else:
    return hard_level_attemps

# the game function 
def game():
  #print logo
  print(logo)
  #begining text 
  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 and 100")
  #picking a random number from 1 - 100
  random_number = random.randint(1, 100)
  # setting turns to the level to the user picked 
  turns = set_difficulty()
  #giving users_guess a value outside the while loop 
  users_guess = 0 
  while users_guess != random_number:
    print(f"You have {turns} attempts remaining to guess the number.")
    #asking for the users guess
    users_guess = int(input("make a guess: "))
    #turns has the value of the Check answer function and its values
    turns = check_answer(users_guess, random_number, turns)
    # if turns = 0 then the user loses 
    if turns == 0:
      print(f"You've run out of guesses. You Lose! The number was {random_number}")
      return

game()

while input("Do you want to play again? Type 'y' or 'n': ") == "y":
	clear()
	game()
