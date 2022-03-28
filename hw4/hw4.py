# Problem A: find_password
#==========================================
# Purpose:
#   Given an encrypted file, tries every possible four letter lowercase
#   password for that file until one works, and then returns the password.
# Input Parameter(s):
#   filename is a string representing the name of the encrypted file.
#   The file must be in the same folder as this script.
# Return Value:
#   Returns the password that successfully decrypts the given file
#==========================================

def find_password(filename):
    fp = open(filename)
    data = fp.read()

    #TODO: Try all possible four letter passwords, not just 'pwnd'
    password = None
    for letter1 in range(97, 123):
        for letter2 in range(97, 123):
            for letter3 in range(97, 123):
                for letter4 in range(97, 123):
                    password = chr(letter1) + chr(letter2) + chr(letter3) + chr(letter4)
                    if decrypt(data, password):
                        return password


# Problem B: count_primes
#==========================================
# Purpose:
#   Prints out all prime numbers between low and high, inclusve, and
#   returns a count of how many there were.
# Input Parameter(s):
#   low is a positive integer
#   high is a positive integer, which should be >= low
# Return Value:
#   Returns the number of prime numbers between low and high, inclusive
#==========================================
def count_primes(low, high):
    num_primes = 0
    if (low > high) or (low < 1) or (high < 1):
        return num_primes

    high += 1
    for i in range(low, high):
        if (is_prime(i)):
            print(i, "is prime")
            num_primes += 1
    return num_primes


#==========================================
# Purpose:
#   Finds out whether a number is a prime number
# Input Parameter(s):
#   num - the integer which needs to be checked for if it is prime
# Return Value:
#   Returns truce or false boolean value based on whether num is prime
#==========================================
def is_prime(num):
    if (num > 1):
        square_root_num = int(num**0.5) + 1
        for i in range(2, square_root_num):
            if (num % i == 0):
                return False
        return True
    else:
        return False


# Problem C: population
#==========================================
# Purpose:
#   Simulates the population of smallfish, middlefish, and bigfish over time
# Input Parameter(s):
#   small is an integer, the initial number of smallfish in the lake
#   middle is an integer, the initial number of middlefish in the lake
#   big is an integer, the initial number of bigfish in the lake
# Return Value:
#   Returns the number of weeks required for one of the populations to
#   fall below 10, or 100 if the populations are all still >= 10 after
#   100 weeks
#==========================================
def population(small, middle, big):
    for week in range(1, 101):
        if ((small >= 10) and (middle >= 10) and (big >= 10)):
            small_change = 0.1 * small - 0.0002 * small * middle
            middle_change = -0.05 * middle + 0.0001 * small * middle - 0.00025 * middle * big
            big_change = -0.1 * big + 0.0002 * middle * big

            small += small_change
            middle += middle_change
            big += big_change

            print("Week", week, "-", "Small:", int(small), "Middle:", int(middle), "Big:", int(big))
        else:
            return week - 1

    return 100


#DO NOT EDIT ANYTHING BELOW THIS LINE
#Below are helper functions used for decrypting the text files.
#You don't have to understand how any of these work.

# decrypt
#==========================================
# Purpose:
#   Check whether the password is correct for a given encrypted
#   file, and print out the decrypted contents if it is.
# Input Parameter(s):
#   data is a string, representing the contents of an encrypted file.
#   password is a four letter lowercase string, representing the password
#   used to encrypt/decrypt the file contents.
# Return Value:
#   Returns True if the password is correct and the file contents
#   were printed.  Returns False and prints nothing otherwise.
#==========================================
def decrypt(data, password):
    data = data.split('\n')
    if encode(password) == int(data[0]):
        print(vigenere(data[1],password))
        return True
    return False

# encode
#==========================================
# Purpose:
#   Turn a password into a ~9 digit number
# Input Parameter(s):
#   key is a four letter string representing a password
# Return Value:
#   Returns a number between 0 and 547120140, using modular exponentiation
#   to make it difficult to reverse engineer the password from the number.
#==========================================
def encode(key):
    total = 0
    for ltr in key:
        total += ord(ltr)
        total *= 123
    return pow(total,2011,547120141)

# vigenere
#==========================================
# Purpose:
#   Decipher a message using the Vigenere cipher
# Input Parameter(s):
#   msg a string, representing the encrypted message
#   key is a four letter string, representing the cipher key
# Return Value:
#   Returns a string representing the deciphered text
#==========================================
def vigenere(msg,key):
    i = 0
    out_msg = ''
    for ltr in msg:
        out_msg += chr((ord(ltr)-ord(key[i]))%28 +97)
        i = (i+1)%len(key)
    return out_msg.replace('{',' ').replace('|','.')
