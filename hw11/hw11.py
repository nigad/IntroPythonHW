class Adventurer:
    # Purpose:
    #   Instantiates Adventurer object
    # Input Parameter(s):
    #   name - string name of Adventurer
    #   level - integer of what level Adventurer is
    #   strength - integer of what Adventurer's strength is
    #   power - integer of how much power Adventurer has
    # Return Value(s):
    #   None
    #==========================================
    def __init__(self, name, level, strength, speed, power):
        self.name = name
        self.level = level
        self.strength = strength
        self.speed = speed
        self.power = power
        self.HP = self.level * 6
        self.hidden = False

    # Purpose:
    #   Attacks another adventurer by deducting an amount of HP
    #   equivalent to the attacker's strength times 4 from the target
    # Input Parameter(s):
    #   target - the Adventurer object being attacked
    # Return Value(s):
    #   None
    #==========================================
    def attack(self, target):
        if target.hidden:
            print(self.name,  "can't see", target.name)
        else:
            target.HP -= self.strength + 4
            print(self.name, "attacks", target.name, "for", (self.strength + 4), "damage")

    # Purpose:
    #   Overloads < operator by comparing two Adventurer objects' HP
    # Input Parameter(s):
    #   other - the Adventurer object that which the comparison will occur
    # Return Value(s):
    #   Boolean value as to whether the Adventurer object that called the method
    #   has a lower HP than another Adventurer object
    #==========================================
    def __lt__(self,other):
        return self.HP < other.HP

    # Purpose:
    #   Overloads representation method for the Adventurer object
    # Input Parameter(s):
    #   None
    # Return Value(s):
    #   String telling Adventurer object's name and amount HP the object has
    #==========================================
    def __repr__(self):
        return self.name + " - HP: " + str(self.HP)


class Fighter(Adventurer):
    # Purpose:
    #   Instantiates Fighter object
    # Input Parameter(s):
    #   name - string name of Adventurer
    #   level - integer of what level Adventurer is
    #   strength - integer of what Adventurer's sttrength is
    #   power - integer of how much power Adventurer has
    # Return Value(s):
    #   None
    #==========================================
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP = self.level * 12

    # Purpose:
    #   Overloads Adventurer base class attack method, and attacks other
    #   Adventurer objects with specific attack that Fighter object does
    # Input Parameter(s):
    #   target - the Adventurer object being attacked
    # Return Value(s):
    #   None
    #==========================================
    def attack(self, target):
        if target.hidden:
            print(self.name,  "can't see", target.name)
        else:
            target.HP -= 2 * self.strength + 6
            print(self.name, "attacks", target.name, "for", (2 * self.strength + 6), "damage")

class Thief(Adventurer):
    # Purpose:
    #   Instantiates Thief object
    # Input Parameter(s):
    #   name - string name of Adventurer
    #   level - integer of what level Adventurer is
    #   strength - integer of what Adventurer's sttrength is
    #   power - integer of how much power Adventurer has
    # Return Value(s):
    #   None
    #==========================================
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP = self.level * 8
        self.hidden = True

    # Purpose:
    #   Overloads Adventurer base class attack method, and attacks other
    #   Adventurer objects with specific attack that Thief object does
    # Input Parameter(s):
    #   target - the Adventurer object being attacked
    # Return Value(s):
    #   None
    #==========================================
    def attack(self, target):
        if self.hidden == False:
                Adventurer.attack(self, target)
        else:
            if target.hidden and self.hidden and (self.speed < target.speed):
                print(self.name,  "can't see", target.name)
            else:
                target.HP -= (self.speed + self.level) * 5
                print(self.name, "sneak attacks", target.name, "for", ((self.speed + self.level) * 5), "damage")
                self.hidden = False
                target.hidden = False

class Wizard(Adventurer):
    # Purpose:
    #   Instantiates Wizard object
    # Input Parameter(s):
    #   name - string name of Adventurer
    #   level - integer of what level Adventurer is
    #   strength - integer of what Adventurer's sttrength is
    #   power - integer of how much power Adventurer has
    # Return Value(s):
    #   None
    #==========================================
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.fireballs_left = self.power

    # Purpose:
    #   Overloads Adventurer base class attack method, and attacks other
    #   Adventurer objects with specific attack that Wizard object does
    # Input Parameter(s):
    #   target - the Adventurer object being attacked
    # Return Value(s):
    #   None
    #==========================================
    def attack(self, target):
        if self.fireballs_left == 0:
            Adventurer.attack(self, target)
        else:
            if target.hidden:
                target.hidden = False
            target.HP -= self.level * 3
            self.fireballs_left -= 1
            print(self.name, "casts fireball on", target.name, "for", (self.level * 3), "damage")

# Purpose:
#   Makes two Adventurer objects duel each other until one has HP less than
#   or equal to 0. The one with HP less than or equal to 0 loses.
# Input Parameter(s):
#   adv1 - an dueler which is a Adventurer
#   adv2 - another dueler which is a Adventurer
# Return Value(s):
#   Boolean value as to whether adv1 won the duel
#==========================================
def duel(adv1, adv2):
    while adv1.HP > 0 and adv2.HP > 0:
        print(adv1)
        print(adv2)
        adv1.attack(adv2)
        if adv1.HP > 0 and adv2.HP > 0:
            adv2.attack(adv1)

    if adv1.HP <= 0 and adv2.HP > 0:
        print(adv1)
        print(adv2)
        print(adv2.name, "wins!")
        return False

    elif adv1.HP > 0 and adv2.HP <= 0:
        print(adv1)
        print(adv2)
        print(adv1.name, "wins!")
        return True

    elif adv1.HP <= 0 and adv2.HP <= 0:
        print(adv1)
        print(adv2)
        print("Everyone loses!")
        return False

# Purpose:
#   Makes a combination of Adventurer objects duel each other through  a specific
#   pairing process until only one Adventurer object has HP greater than 0
# Input Parameter(s):
#   adv_list - list of Adventurer objects
# Return Value(s):
#   Adventurer object that won the tournament
#==========================================
def tournament(adv_list):
    if len(adv_list) == 0:
        return None
    elif  len(adv_list) == 1:
        return adv_list[0]
    else:
        while len(adv_list) > 1:
            adv_list = sorted(adv_list)
            result = duel(adv_list[-2], adv_list[-1])

            if result == True:
                adv_list = adv_list[:-1]
            else:
                adv_list = adv_list[:-2] + [adv_list[-1]]

        return adv_list[0]
