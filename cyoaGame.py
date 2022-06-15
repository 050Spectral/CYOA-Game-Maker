# Get the possible paths from cyoaSenarios
# import the needed function and assign variables to it
import cyoaSenarios
from cyoaSenarios import Choices
c = Choices
s = cyoaSenarios

# Dictionary that converts string into object so that function will register
convert = {"mainPathStart" : s.mainPathStart, "left1" : s.left1, "right1" : s.right1, "placeholder" : s.placeholder}

# Setup
userInput = input(convert["mainPathStart"].senario)
# !!Have to check for input MANUALLY


# main gameplay loop
end = False
while not end:
    # makes a copy of userInput's information so that later on I can check it
    checkFor = userInput
    userInput = input(convert[userInput].senario)

    # checkFor is used in place of userInput because userInput is always changing while checkFor keeps the previous senario
    # Checks whether the input matches the choices or not
    # You CAN'T backtrack
    while (not c.inputChecker(convert[checkFor], userInput)):
        print("That is not valid, type something else: \n")
        userInput = input(convert[checkFor].senario)

