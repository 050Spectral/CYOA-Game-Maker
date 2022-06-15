class Choices:
    # Constructer class
    #optons is an array so that I can check if the input matches up
    def __init__(self, senario, id, options):
        self.senario = senario
        self.id = id
        self.options = options

    def inputChecker(self, userInput):
        for i in range(len(self.options)):
            if(userInput == self.options[i]):
                return True
        return False

# Create the stages here
# Format: (description, id[name of the room], options)
mainPathStart = Choices("You find yourself walking down a dirt road\n"
                        "There's a fork in the road\n"
                        "Do you go left or right? Type: [left1/right1]\n"
                        "> ", "mainPathStart", ["left1", "right1"])

left1 = Choices("You choose to go left\n"
                "> ", "left1", ["placeholder"])
right1 = Choices("You choose to go right\n"
                "> ", "right1", ["placeholder"])

placeholder = Choices("This is a test", "placeholder", ["nothing"])