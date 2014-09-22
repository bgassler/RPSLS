# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

#This functions converts the names to their corresponding numbers and returns the number
def name_to_number(name):
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print "please pick an appropriate choice"
        return
        
    return number
    

#This function converts the number to its corresponding name and returns the name
def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        return
    
    return name 
    
#This function determines and prints the winner of the game
def rpsls(player_choice): 

    # print a blank line to separate consecutive games
    print "\n"
    
    
    
    print "Player chooses " + player_choice
    
    computer_number = random.randrange(0, 5, 1)
    computer_choice = number_to_name(computer_number)
    print "Computer chooses " + computer_choice
    
    player_number = name_to_number(player_choice)
    
    diff = player_number - computer_number
    if diff == 0:
        print "Player and Computer tie!"
    elif diff > 0:
        if diff in (1, 2):
            print "Player wins!"
        elif diff > 2:
            print "Computer wins!"
    elif diff < 0:
        diff = diff + 5
        if diff in (1,2):
            print "Player wins!"
        elif diff > 2:
            print "Computer wins"
        

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

x = random.randrange(0, 5, 1)
#print x



# always remember to check your completed program against the grading rubric


