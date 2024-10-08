import random

Rock = '''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_/
'''

Paper = ''' 
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_| 
'''

Scissors = ''' 
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ /
|___/\___|_|___/___/\___/|_|  |___/
'''
item = [Rock, Paper, Scissors]

choice = int(input(print("Type 0 for 'ROCK', 1 for 'PAPER' 2 for 'SCISSORS'.\n")).lower())
print(f"You Choose:\n{item[choice]}")

computer = random.randint(0, 2)
print(f"Computer Choose: \n{item[computer]}")

#More if and elif statements to make game proper 
if choice == 0 and computer == 2:
    print("You Win!")
elif computer > choice:
    print("You Lose :((")
elif computer == choice:
    print("Draw!")
else:
    print("You typed an invalid number, you lose :((")