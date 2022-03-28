class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def get_real(self):
        return self.real

    def get_imag(self):
        return self.imag

    def set_real(self, new_real):
        self.real = new_real

    def set_imag(self, new_imag):
        self.imag = new_imag

    def __str__(self):
        return str(self.real) + " + " + str(self.imag) + "i"

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real_num = (self.real * other.real) - (self.imag * other.imag)
        imag_num = (self.real * other.imag) + (self.imag * other.real)
        return Complex(real_num, imag_num)

    def __eq__(self, other):
        if (self.real == other.real) and (self.imag == other.imag):
            return True
        else:
            return False

# x = Complex(2.7,3)
# y = Complex(-4,0)
# z = Complex(0,-1.5)
#
# print(x.real)           # 2.7
# print(x.get_real())     # 2.7
# print(y.get_imag())     # 0
#
# x.set_real(6)
# z.set_imag(-2.5)
#
# print(x.real)           # 6
# print(x)                # 6 + 3i
# print(y)                # -4 + 0i
# print(z)                # 0 + -2.5i
# print(x+y)              # 2 + 3i
# print(z+y+x)            # 2 + 0.5i
# print(y*z)              # 0.0 + 10.0i
# print(x*z)              # 7.5 + -15.0i
# print(x*y+x*z)          # -16.5 + -27.0i
# print(x*(y+z))          # -16.5 + -27.0i
# print(x == y)           # False
# print(x*y+x*z == x*(y+z))   # True

class Employee:
    def __init__(self, file_row):
        row_entries = file_row.split(",")
        self.name = row_entries[0]
        self.position = row_entries[1]
        self.salary = float(row_entries[2])
        self.seniority = float(row_entries[3])
        self.value = float(row_entries[4])

    def __str__(self):
        return self.name + ", " + self.position

    def net_value(self):
        return self.value - self.salary

    def __lt__(self, other):
        return self.net_value() < other.net_value()

# emp1 = Employee('Milton,Underling,310423.01,5.0,22.99\n')
# emp2 = Employee('Bill,Boss,403567.34,5.0,519.35\n')
#
# print(emp1.name)            # Milton
# print(emp1.position)        # Underling
# print(emp1.salary)          # 310423.01
# print(emp1.seniority)       # 5.0
# print(emp1.value)           # 22.99
# print(emp1)                 # Milton, Underling
# print(emp1.net_value())     # -310400.02
# print(emp2.net_value())     # -403047.99
# print(emp1 < emp2)          # False
# print(emp2 < emp1)          # True

class Branch:
    def __init__(self, file_name):
        fp = open(file_name, "r")
        lines = fp.readlines()

        self.location = lines[0].split(",")[1]
        self.upkeep = float(lines[1].split(",")[1])

        lines = lines[3:]
        self.team = []
        for line in lines:
            self.team.append(Employee(line))

        fp.close()

    def __str__(self):
        to_print = ""
        num_emplyees = len(self.team)
        for i  in range(num_emplyees - 1):
            to_print += str(self.team[i]) + "\n"
        to_print += str(self.team[-1])
        return self.location + "\n" + to_print

    def profit(self):
        the_profit = 0
        for member in self.team:
            the_profit += member.net_value()
        the_profit -= self.upkeep
        return the_profit

    def __lt__(self, other):
        return self.profit() < other.profit()

    def cut(self, num):
        team_copy = sorted(self.team)
        self.team = team_copy[num:]

# branch2 = Branch('branch2.csv')
# print(branch2.location)         #Pawnee
# print(branch2.upkeep)           #98229.98
# print()
#
# print(branch2)
# ##                Pawnee
# ##                Ron, Efficiency Logistics Strategist
# ##                Leslie, Creative Evolution Strategist
# ##                Ann, Data Evolution Engineer
# ##                Mark, Operational Services Specialist
# ##                Tom, Creative Logistics Coordinator
# ##                April, Enterprise Services Consultant
# ##                Andy, Creative Logistics Specialist
# ##                Jerry, Enterprise Services Technician
# ##                Donna, Operational Innovation Engineer
#
# print()
# branch2.cut(7)
# print(branch2)
# ##                Pawnee
# ##                Leslie, Creative Evolution Strategist
# ##                Ann, Data Evolution Engineer
#
# print()
# print(branch2.profit())         #12577.81
# branch1 = Branch('branch1.csv')
# print(branch1.upkeep)           #57867.07
#
# print()
# print(branch1)
# ##                Scranton
# ##                Dwight, Efficiency Evolution Specialist
# ##                Jim, Data Innovation Specialist
# ##                Pam, Operational Analytics Technician
# ##                Ryan, Data Evolution Consultant
# ##                Stanley, Efficiency Logistics Technician
# ##                Michael, Enterprise Communications Technician
# ##                Kevin, Operational Services Technician
# ##                Meredith, Data Evolution Technician
# ##                Angela, Enterprise Communications Consultant
# ##                Oscar, Creative Innovation Coordinator
# ##                Phyllis, Enterprise Analytics Technician
# branch1.cut(8)
#
# print()
# print(branch1)
# ##                Scranton
# ##                Pam, Operational Analytics Technician
# ##                Michael, Enterprise Communications Technician
# ##                Stanley, Efficiency Logistics Technician

class Company:
    def __init__(self, name, branches):
        self.name = name
        self.branches = branches

    def __str__(self):
        all_branch_names = ""
        num_branches = len(self.branches)
        for i in range(num_branches):
            if i < (num_branches - 1):
                all_branch_names += str(self.branches[i]) + "\n" + "\n"
            else:
                all_branch_names += str(self.branches[i])
        return self.name + "\n" + "\n" + all_branch_names

    def synergize(self):
        worst_profit = float("inf")
        most_inneficient_branch = 0

        for branch in self.branches:
            branch_profit = branch.profit()
            if branch_profit < worst_profit:
                worst_profit = branch_profit
                most_inneficient_branch = branch
        num_half_team = int(len(most_inneficient_branch.team)/2)
        most_inneficient_branch.cut(num_half_team)

# b1 = Branch('branch1.csv')
# b2 = Branch('branch2.csv')
# b3 = Branch('branch3.csv')
# b4 = Branch('branch4.csv')
# hs = Company('Synergistic Management Solutions',[b1,b2,b3,b4])
# print(hs.name)           #Synergistic Management Solutions
#
# print()
# print(hs)
# ##                    Synergistic Management Solutions
# ##
# ##                    Scranton
# ##                    Dwight, Efficiency Evolution Specialist
# ##                    Jim, Data Innovation Specialist
# ##                    Pam, Operational Analytics Technician
# ##                    Ryan, Data Evolution Consultant
# ##                    Stanley, Efficiency Logistics Technician
# ##                    Michael, Enterprise Communications Technician
# ##                    Kevin, Operational Services Technician
# ##                    Meredith, Data Evolution Technician
# ##                    Angela, Enterprise Communications Consultant
# ##                    Oscar, Creative Innovation Coordinator
# ##                    Phyllis, Enterprise Analytics Technician
# ##
# ##                    Pawnee
# ##                    Ron, Efficiency Logistics Strategist
# ##                    Leslie, Creative Evolution Strategist
# ##                    Ann, Data Evolution Engineer
# ##                    Mark, Operational Services Specialist
# ##                    Tom, Creative Logistics Coordinator
# ##                    April, Enterprise Services Consultant
# ##                    Andy, Creative Logistics Specialist
# ##                    Jerry, Enterprise Services Technician
# ##                    Donna, Operational Innovation Engineer
# ##
# ##                    Greendale
# ##                    Britta, Enterprise Services Coordinator
# ##                    Abed, Operational Services Strategist
# ##                    Troy, Efficiency Innovation Coordinator
# ##                    Annie, Efficiency Innovation Consultant
# ##                    Shirley, Enterprise Innovation Engineer
# ##                    Pierce, Enterprise Evolution Specialist
# ##                    Ben, Enterprise Communications Consultant
# ##                    Jeff, Brand Logistics Specialist
# ##                    Craig, Enterprise Communications Engineer
# ##
# ##                    Ambiguous
# ##                    J.D., Efficiency Analytics Coordinator
# ##                    Turk, Efficiency Innovation Technician
# ##                    Elliot, Data Innovation Specialist
# ##                    Perry, Efficiency Evolution Technician
# ##                    Bob, Enterprise Logistics Engineer
# ##                    Carla, Brand Services Technician
# ##                    Janitor, Efficiency Evolution Coordinator
#
# print()
# hs.synergize()
# print()
#
# print(hs)
# ##                    Synergistic Management Solutions
# ##
# ##                    Greendale
# ##                    Ben, Enterprise Communications Consultant
# ##                    Craig, Enterprise Communications Engineer
# ##                    Britta, Enterprise Services Coordinator
# ##                    Pierce, Enterprise Evolution Specialist
# ##                    Jeff, Brand Logistics Specialist
# ##
# ##                    Pawnee
# ##                    Ron, Efficiency Logistics Strategist
# ##                    Leslie, Creative Evolution Strategist
# ##                    Ann, Data Evolution Engineer
# ##                    Mark, Operational Services Specialist
# ##                    Tom, Creative Logistics Coordinator
# ##                    April, Enterprise Services Consultant
# ##                    Andy, Creative Logistics Specialist
# ##                    Jerry, Enterprise Services Technician
# ##                    Donna, Operational Innovation Engineer
# ##
# ##                    Scranton
# ##                    Dwight, Efficiency Evolution Specialist
# ##                    Jim, Data Innovation Specialist
# ##                    Pam, Operational Analytics Technician
# ##                    Ryan, Data Evolution Consultant
# ##                    Stanley, Efficiency Logistics Technician
# ##                    Michael, Enterprise Communications Technician
# ##                    Kevin, Operational Services Technician
# ##                    Meredith, Data Evolution Technician
# ##                    Angela, Enterprise Communications Consultant
# ##                    Oscar, Creative Innovation Coordinator
# ##                    Phyllis, Enterprise Analytics Technician
# ##
# ##                    Ambiguous
# ##                    J.D., Efficiency Analytics Coordinator
# ##                    Turk, Efficiency Innovation Technician
# ##                    Elliot, Data Innovation Specialist
# ##                    Perry, Efficiency Evolution Technician
# ##                    Bob, Enterprise Logistics Engineer
# ##                    Carla, Brand Services Technician
# ##                    Janitor, Efficiency Evolution Coordinator
#
# print()
# hs.synergize()
# print()
#
# print(hs)
# ##                    Synergistic Management Solutions
# ##
# ##                    Pawnee
# ##                    Jerry, Enterprise Services Technician
# ##                    Ron, Efficiency Logistics Strategist
# ##                    Andy, Creative Logistics Specialist
# ##                    Leslie, Creative Evolution Strategist
# ##                    Ann, Data Evolution Engineer
# ##
# ##                    Scranton
# ##                    Dwight, Efficiency Evolution Specialist
# ##                    Jim, Data Innovation Specialist
# ##                    Pam, Operational Analytics Technician
# ##                    Ryan, Data Evolution Consultant
# ##                    Stanley, Efficiency Logistics Technician
# ##                    Michael, Enterprise Communications Technician
# ##                    Kevin, Operational Services Technician
# ##                    Meredith, Data Evolution Technician
# ##                    Angela, Enterprise Communications Consultant
# ##                    Oscar, Creative Innovation Coordinator
# ##                    Phyllis, Enterprise Analytics Technician
# ##
# ##                    Ambiguous
# ##                    J.D., Efficiency Analytics Coordinator
# ##                    Turk, Efficiency Innovation Technician
# ##                    Elliot, Data Innovation Specialist
# ##                    Perry, Efficiency Evolution Technician
# ##                    Bob, Enterprise Logistics Engineer
# ##                    Carla, Brand Services Technician
# ##                    Janitor, Efficiency Evolution Coordinator
# ##
# ##                    Greendale
# ##                    Ben, Enterprise Communications Consultant
# ##                    Craig, Enterprise Communications Engineer
# ##                    Britta, Enterprise Services Coordinator
# ##                    Pierce, Enterprise Evolution Specialist
# ##                    Jeff, Brand Logistics Specialist
#
# print()
# hs.synergize()
# print()
#
# print(hs)
# ##                    Synergistic Management Solutions
# ##
# ##                    Scranton
# ##                    Meredith, Data Evolution Technician
# ##                    Kevin, Operational Services Technician
# ##                    Phyllis, Enterprise Analytics Technician
# ##                    Pam, Operational Analytics Technician
# ##                    Michael, Enterprise Communications Technician
# ##                    Stanley, Efficiency Logistics Technician
# ##
# ##                    Ambiguous
# ##                    J.D., Efficiency Analytics Coordinator
# ##                    Turk, Efficiency Innovation Technician
# ##                    Elliot, Data Innovation Specialist
# ##                    Perry, Efficiency Evolution Technician
# ##                    Bob, Enterprise Logistics Engineer
# ##                    Carla, Brand Services Technician
# ##                    Janitor, Efficiency Evolution Coordinator
# ##
# ##                    Greendale
# ##                    Ben, Enterprise Communications Consultant
# ##                    Craig, Enterprise Communications Engineer
# ##                    Britta, Enterprise Services Coordinator
# ##                    Pierce, Enterprise Evolution Specialist
# ##                    Jeff, Brand Logistics Specialist
# ##
# ##                    Pawnee
# ##                    Jerry, Enterprise Services Technician
# ##                    Ron, Efficiency Logistics Strategist
# ##                    Andy, Creative Logistics Specialist
# ##                    Leslie, Creative Evolution Strategist
# ##                    Ann, Data Evolution Engineer
