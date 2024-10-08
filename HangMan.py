import random


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
#importing a dictionary soon
#word_list = ["aardvark", "baboon", "camel"]
#

with open ('Words_list.txt','r') as f:
  word = f.read()

chosen_word = random.choice(word)
print(f"answer : {chosen_word}")



display = []
for _ in range(0,len(chosen_word)):
    display += "_"
print(f"{display}")

End_Game = False
player_lives = 6


while not End_Game:
  guess = input("Guess a letter: ").lower()

  for position in range(0,len(chosen_word)):
      letter = chosen_word[position]
      if letter == guess:
          display[position] = letter

  if guess not in chosen_word:
     player_lives -= 1
     if player_lives == 0:
      End_Game = True
      print(f"You Lost!\nThe chosen word was {chosen_word}")

  print(f"{' '.join(display)}")            

  if "_" not in display:
    End_Game = True
    print("You Won!")

  print(stages[player_lives])