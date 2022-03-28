#   Name: Ayush

#==========================================
# Purpose:
#   Finds out what the sound of bark is based on weight of dog
# Input Parameter(s):
#   weight - the weight of a dog
# Return Value(s):
#   Returns string representing dog's bark
#==========================================
def sound(weight):
    if weight < 13:
        return "Yip"
    elif 13 < weight <= 30:
        return "Ruff"
    elif 31 <= weight <= 70:
        return "Bark"
    else:
        return "Boof"
#==========================================
# Purpose:
#   To give a problem and three solutions to the problem to choose
#   from. You HAVE to choose one of the three options.
# Input Parameter(s):
#   text - the problem that person who runs function has to solve
#   option1 - one of the three solutions to the problem in text
#   option2 - one of the three solutions to the problem in text
#   option3 - one of the three solutions to the problem in text
# Return Value(s):
#   Returns number 1, 2, or 3 depending on which solution choice is
#   chosen by the person who runs the function
#==========================================
def choice(text, option1, option2, option3):
    print(text)
    print( "1. ", option1)
    print( "2. ", option2)
    print( "3. ", option3)
    decision = input("Choose 1, 2, or 3:  ")
    while (decision != "1") and (decision !=  "2") and (decision !=  "3"):
        print ("Invalid choice")
        decision = input("Choose 1, 2, or 3: ")
    return decision

#==========================================
# Purpose:
#   To run a text adventure in which the person running the
#   function may or may not end up in a good ending for the
#   adventure. Sidenote, could be done with nodes but forgot how to....
# Input Parameter(s):
#   None
# Return Value(s):
#   Returns True or False boolean value based on whether the
#   person running the program ends the adventure in a good (True)
#   or bad (False) ending
#==========================================
def adventure():
    currentState = 1
    chosen = int(choice(" ", " ", " ", " "))

    if (chosen == 2):
        chosen = int(choice(" ", " ", " ", " "))
        if chosen == 2 or chosen == 3:
            currentState = 4
        else:
            return False

    elif (chosen == 3):
        chosen = int(choice(" ", " ", " ", " "))
        if (chosen == 2):
            currentState = 4
        elif (chosen == 3):
            currentState = 5
        else:
            return False

    else:
        return False

    if (currentState == 4):
        chosen = int(choice(" ", " ", " ", " "))
        if (chosen != 2):
            if (chosen == 1):
                return True
            else:
                return False
        else:
            currentState = 5

    if (currentState == 5):
            if(int(choice(" ", " ", " ", " ")) == 2):
                return False
            else:
                return True
