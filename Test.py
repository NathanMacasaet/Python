print("Welcome to Treasure Island!\nYour mission is to find the treasure\n")

print("You are stranded on the island with no food and water\n")
movement = input("Do you go North into the forest or head South into the desert\nType 'North' or 'South'\n").lower()

# first Movement into the game
if movement == "north":
    forest = input("You have encountered a wild animal.\nType Y to fight the wild animal or Type N to keep moving through the forest.").lower()
elif movement == "south":
    desert = input("You start to hallucinate.\nYou see a sand village and a glass of water.\nDo you drink the water or walk towards the village.\nPlease Type 'Water' or 'Village'\n").lower()

if forest == "y":
    print("You lost fighting the grizzly bear and died. ✞")
elif forest == "n":
    movement2 = input("An indigenous tribe Uru-Eu-Wau-Wau is chasing you and throwing their spears at you.\nThere is a river in front of you, do you dive in or keep running\nPlease Type 'Diving' or 'Running'\n").lower()

if movement2 == "dive" or movement2 == "diving":
    movement3 = input("As the tribe shoots their spears at you through the river water you successfully escape.\n You are now located at the bottom of the river located near the mountains.\nDo you head South and hunt for food or continue your journey North.\n").lower()
elif movement2 == "running" or movement2 == "run":
    print("You were unable to outrun the tribe Uru-Eu-Wau-Wau and got hit with a spear through your chest.")

if movement3 == "north":
    print("Congratulations You have found the hidden treasure!!! 💎💎💎")
elif movement3 == "south":
    print("You head south which brings you to the desert.\nYou are hungry and dehydrated.\nUnfortunately, you did not survive. :((")

if desert == "water":
    print("You get closer and closer to the water and take a drink.\nYou die of dehydration as it was all an illusion.\n")
elif desert == "village":
    village = input("You arrive at the village and see Three huts. \nRed hut \nYellow hut \nBlack hut\n").lower()

if village == "red" or village == "red hut":
    print("You step into the hut, and it goes on fire. \nYou are trapped and died ✞\n")
elif village == "yellow" or village == "yellow hut":
    mountain = input("You are transported on top of the mountains.\n Do you go glide to the bottom heading South or glide heading North\n Please Type 'North' Or 'South'\n").lower()
elif village == "black" or village == "black hut":
    print("A sniper was waiting for you on the opposite hut and shot you through the heart.\nYou are Dead ✞\n")

if mountain == "north":
    print("You land and feel something weird underneath your feet.\n You start to Dig and keep digging\nCongratulations You have found the hidden treasure!!! 💎💎💎")
elif mountain == "south":
    spider = input("You land South... Home of the Giant tarantula 25Ft tall.\nDo you Fight The Giant spider or accept your death\n Type 'Fight' or 'Accept'\n").lower()

if spider == "fight" or spider == "accept":
    print("Both options lead to DEATH ✞")
