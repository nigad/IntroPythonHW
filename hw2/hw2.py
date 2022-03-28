#Name: Ayush Nigade

#==========================================
# Purpose:
#   Computes contracted distance between two objects from the
#   reference frame
# Input Parameter(s):
#   dist - The original distance between two objects
#   speed - The speed at we are traveling relative to two objects
# Return Value(s):
#   Returns contracted distance between two objects from the
#   reference frame
#==========================================
def length_contract(dist, speed):
    return dist  * (1 - ((speed ** 2) / (3 * 10 ** 8) ** 2)) ** 0.5

#==========================================
# Purpose:
#   Computes time required to travel a segment as seen by stationary
#   person in years. Also computes time required to traverse segment
#   as seen by traverser.
# Input Parameter(s):
#   speed - traverser's average speed in run
# Return Value(s):
#   Returns time required to traverse segment as seen by traverser
#==========================================
def bessel_run(speed):
    distance = 12 * (3.086 * 10 **16)
    seconds_in_year = 31557600
    print((distance / speed) / seconds_in_year)
    return (length_contract(distance, speed) / speed) / seconds_in_year

#==========================================
# Purpose:
#   This function prints "Who needs loops?" 100 times by calling a
#   function 5 times that calls another function 5 times that prints
#   "Who needs loops?" 4 times
# Input Parameter(s):
#   None
# Return Value(s):
#   None
#==========================================
def print_100():
    print_call()
    print_call()
    print_call()
    print_call()
    print_call()


#==========================================
# Purpose:
#   This function's purpose is to call a function 5 times. That function
#   that is called 5 times prints "Who needs loops?" 4 times.
# Input Parameter(s):
#   None
# Return Value(s):
#   None
#==========================================
def print_call():
    print_it()
    print_it()
    print_it()
    print_it()
    print_it()

#==========================================
# Purpose:
#   The purpose of this function is to print "Who needs loops?"
#   four times.
# Input Parameter(s):
#   None
# Return Value(s):
#   None
#==========================================
def print_it():
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
