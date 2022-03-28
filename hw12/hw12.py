import tkinter as tk
import random

#FIRST: Implement and test your Pokemon class below
class Pokemon:
    def __init__(self, dex_num, name, catch_rate, speed):
        self.name = name
        self.dex_num = dex_num
        self.catch_rate = catch_rate
        self.speed = speed

    def __str__(self):
        return self.name

    print("Implement this and then remove this print statement")


#NEXT: Complete the class definition provided below
class SafariSimulator(tk.Frame):
    def __init__(self, master=None):
        print("In SafariSimulator init")
        fp = open("pokedex.csv")
        lines = fp.readlines()
        self.pokemons = {}
        for i in range(1, len(lines)):
            values = lines[i].split(",")
            pokemon = Pokemon(values[0], values[1], values[2], values[3])
            self.pokemons[values[0]] = pokemon
        self.safari_balls = 30
        self.caught_pokemons = []

        #Read in the data file from pokedex.csv at some point here
        #It's up to you how you store and handle the data
        #(e.g., list, dictionary, etc.),
        #but you must use your Pokemon class in some capacity

        #Initialize any instance variables you want to keep track of
        self.current_Pokemon_dex = 0
        self.probability = 0
        #DO NOT MODIFY: These lines set window parameters and create widgets
        tk.Frame.__init__(self, master)
        master.minsize(width=275, height=350)
        master.maxsize(width=275, height=350)
        master.title("Safari Zone Simulator")
        self.pack()
        self.createWidgets()
        self.nextPokemon()
        #Call nextPokemon() method here to initialize your first random pokemon


    def createWidgets(self):
        print("In createWidgets")
        #See the image in the instructions for the general layout required
        #You need to create an additional "throwButton"
        self.throwButton = tk.Button(self)
        self.throwButton["command"] = self.throwBall
        self.safari_balls = 30
        self.throwButton["text"] = "Throw Safari Ball (" + str(self.safari_balls) + " left)"
        self.throwButton.pack()


        #"Run Away" button has been completed for you as an example:
        self.runButton = tk.Button(self)
        self.runButton["text"] = "Run Away"
        self.runButton["command"] = self.nextPokemon
        self.runButton.pack()

        #A label for status messages has been completed for you as an example:
        self.messageLabel = tk.Label(bg="grey")
        self.messageLabel.pack(fill="x", padx=5, pady=5)

        #You need to create two additional labels:
        #Complete and pack the pokemonImageLabel here.
        #file_string = str(current_Pokemon_dex) + ".gif"
        #img = tk.PhotoImage(file = file_string)
        self.pokemonImageLabel = tk.Label()
        self.pokemonImageLabel.pack()

        self.catchProbLabel = tk.Label()
        self.catchProbLabel.pack()

    def nextPokemon(self):
        print("In nextPokemon")

        #This method must:
            #Choose a random pokemon
            #Get the info for the appropriate pokemon
            #Ensure text in messageLabel and catchProbLabel matches the pokemon
            #Change the pokemonImageLabel to show the right pokemon

        #Hint: to see how to create an image, look at the documentation
        #for the PhotoImage/Label classes in tkinter.

        #Once you generate a PhotoImage object, it can be displayed
        #by setting self.pokemonImageLabel["image"] to it

        #Note: the PhotoImage object MUST be stored as an instance
        #variable for some object (you can just set it to self.photo).
        #Not doing this will, for weird memory reasons, cause the image
        #to not be displayed.
        rand_pokemon = random.choice(list(self.pokemons.values()))
        self.current_Pokemon_dex = rand_pokemon.dex_num
        print("Dex current: "+ self.current_Pokemon_dex)
        self.messageLabel["text"] = "You encounter a wild " + rand_pokemon.name

        self.probability = min((int(rand_pokemon.catch_rate) + 1) , 151) / 499.5
        self.catchProbLabel["text"] = "Your chance of catching it is " + str(round(self.probability * 100)) + "%!"

        file_string = "sprites\\" + str(self.current_Pokemon_dex) + ".gif"
        self.img = tk.PhotoImage(file = file_string)
        self.pokemonImageLabel["image"] = self.img

    def throwBall(self):
        print("In throwBall")

        #This method must:

            #Decrement the number of balls remaining
            #Try to catch the pokemon
            #Check to see if endAdventure() should be called

        #To determine whether or not a pokemon is caught, generate a random
        #number between 0 and 1, using random.random().  If this number is
        #less than min((catchRate+1), 151) / 449.5, then it is caught.
        #catchRate is the integer in the Catch Rate column in pokedex.csv,
        #for whatever pokemon is being targetted.

        #Don't forget to update the throwButton's text to reflect one
        #less Safari Ball (even if the pokemon is not caught, it still
        #wastes a ball).

        #If the pokemon is not caught, you must change the messageLabel
        #text to "Aargh! It escaped!"

        #Don't forget to call nextPokemon to generate a new pokemon
        #if this one is caught.
        temp_num = random.random()
        print(temp_num, self.probability)
        if temp_num < self.probability:
            self.caught_pokemons.append(self.pokemons[self.current_Pokemon_dex])
            print(self.caught_pokemons)
            self.safari_balls -= 1
            if 0 >= self.safari_balls:
                self.endAdventure()
            self.throwButton["text"] = "Throw Safari Ball (" + str(self.safari_balls) + " left)"
            self.nextPokemon()
        else:
            self.safari_balls -= 1
            self.messageLabel["text"] = "Aargh! It escaped"
            self.throwButton["text"] = "Throw Safari Ball (" + str(self.safari_balls) + " left)"
            print("escaped")
            if 0 >= self.safari_balls:
                self.endAdventure()

    def endAdventure(self):
        print("In endAdventure")

        #This method must:

            #Display adventure completion message
            #List captured pokemon

        #Hint: to remove a widget from the layout, you can call the
        #pack_forget() method.

        #For example, self.pokemonImageLabel.pack_forget() removes
        #the pokemon image.
        self.messageLabel["text"] = "You’re out of balls, I hope you had fun!"
        self.throwButton.pack_forget()
        self.runButton.pack_forget()
        self.pokemonImageLabel.pack_forget()
        self.catchProbLabel.pack_forget()

        list_caught_ones = ""
        num_caught = 0
        for caught_one in self.caught_pokemons:
            list_caught_ones = list_caught_ones + caught_one.name + "\n"
            num_caught += 1
        list_caught_ones = list_caught_ones[:-2]
        self.gameResultLabel = tk.Label()
        if num_caught > 0:
            self.gameResultLabel["text"] = "You caught " + str(num_caught) + " Pokemon:\n" + list_caught_ones
        else:
            self.gameResultLabel["text"] = "Oops, you caught 0 Pokemon."
        self.gameResultLabel.pack()




#DO NOT MODIFY: These lines start your app
app = SafariSimulator(tk.Tk())
app.mainloop()
