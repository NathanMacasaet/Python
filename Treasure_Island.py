print('''

  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----/
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \//    " |   "    \_____,' | ~~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\ " __,---._  "  "   "  /~~~ |
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/     ___  `---  ---  - - ' ,--.     ___        |~ |
 |~   \      ,'~~|  "  (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~|
 | ~~ ~|__,-'~~~~~\    \/"/\     "  "   "    /~ ~~   O ~ ~~`-.__/~ ~ |
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~NATE~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------/
 \_/__________________________________________________________________/


 ''')
print("Welcome to Treasure Island!\nYour mission is to find the treasure\n")


print("You are stranded in the island with no food and water\n")
movement = input("Do you go North into the forest or head South into the desert\nType North or South\n").lower()

#first Movement into the game
if movement == "north":
    forest= input(print("You have encountered a wild animal.\nType Y to fight the wild animal or Type N to keep moving through the forest.")).lower()
elif movement == "south":
    desert = input(print ("You start to hallucinate.\nYou see a sand village and a glass of water.\nDo you drink the water or walk towards the village.\nPlease Type 'Water' or 'Village'\n")).lower()

if forest == "y":
    print("You lost fighting the grizzley bear and died. ✞")
elif forest == "n":
    movement2 = input(print("An indigenous tribe Uru-Eu-Wau-Wau is chasing you and throwing their spears at you.\nThere is a river in front of you, do you dive in or keep running\nPlease Type 'Diving' or 'Running\n")).lower()

if movement2 == "Dive" or "Diving":
    movement3 = input(print("As the tribe shoots their spears at you through the river water you successfully escape.\n You are now located at the bottom of the river located near the mountains.\nDo you head South and hunt for food or continue your journey North.\n")).lower()
elif movement2 == "Running" or "Run":
    print("You were unable to outrun the tribe Uru-Eu-Wau-Wau and got hit with a spear through your chest.")

if movement3 == "North":
    print("Congratulations You have found the hidden treasure!!! 💎💎💎")
elif movement3 == "South":
    print("You head south which brings you to the desert.\nYou are hungry and dehydrated.\nUnfortuantly you did not Survive. :((")

if desert == "Water" or "water":
    print("You get closer and closer to the water, and take a drink.\nYou die of dyhydration as it was all an illusion.\n")
elif desert == "Village" or "village":
    village = input("You arrive at the village and see Three huts. \nRed hut \nYellow hut \nBlack hut\n").lower()

if village == "Red" or "Red hut":
    print("You step into the hut, and it goes on fire. \nYou are trapped and died ✞\n")
elif village == "Yellow" or "Yellow hut":
    mountain = input(print("You are transported on top of the mountains.\n Do you go glide to the bottom heading South or glide heading North\n Please Type 'North' Or 'South'\n")).lower()
elif village == "Black" or "Black hut":
    print("A sniper was waiting for you on the opposite hut and shot you through the heart.\nYou are Dead ✞\n")

if mountain == "North":
    print("You land and feel something weird underneath your feet.\n You start to Dig and keep digging\nCongratulations You have found the hidden treasure!!! 💎💎💎")
elif mountain == "South":
   spider = input(print("You land South... Home of the Giant tarantula 25Ft tall.\nDo you Fight The Giant spider or accecpt your death\n Type 'Fight' or 'Accecpt'\n")).lower()

if spider == "fight" or "accecpt":
    print("Both options lead to DEATH ✞")