import random
## Ayush Nigade
## nigad001

#==========================================
# Purpose:
#   Finds the first word in every sentence and groups all those words
#   a list. The words are in the order they are found.
# Input Parameter(s):
#   fname - The file that includes the text which is to be read
# Return Value(s):
#   Returns list of first words of all sentences within the given file.
#==========================================
def first_words(fname):
    file = open(fname)
    sentences = file.readlines()
    ls = []
    for sentence in sentences:
        words = sentence.split(" ")
        ls.append(words[0])
    file.close()
    return ls

#==========================================
# Purpose:
#   For every word in a text, finds every word that comes immediately after
#   it.
# Input Parameter(s):
#   fname - The file that includes the text which is to be read
# Return Value(s):
#   Returns dictionary which has words within the given list as keys and lists of
#   every word that comes immediately after each key in the file as values.
#==========================================
def next_words(fname):
    f = open(fname)
    contents = f.read()
    contents = contents.replace("\n", " ")
    words = contents.split(" ")
    dct = {}
    length = len(words)
    for i in range(length):
        ls = []
        j = i + 1
        if  words[i] != ".":
            if j < length:
                ls.append(words[j])

            if dct.get(words[i]) == None:
                dct[words[i]] = ls
            else:
                dct[words[i]] += ls
    f.close()
    return dct

#==========================================
# Purpose:
#   To print ten sentences based on a pattern. This pattern is based on
#   the grouping of each word with the words that come immediately
#   after itself and then using weighted randomization to choose the
#   words for each sentence.
# Input Parameter(s):
#   fname - The file that includes the text which is to be read
# Return Value(s):
#   None
#==========================================
def fanfic(fname):
    for i in range(10):
        first_word = random.choice(first_words(fname))
        related_words = next_words(fname)
        next_word = random.choice(related_words[first_word])
        sentence = first_word + " " + next_word + " "
        while next_word != ".":
            next_word = random.choice(related_words[next_word])
            if next_word != ".":
                sentence += next_word + " "
            else:
                sentence += next_word
        print(sentence)

#==========================================
# Purpose:
#   Finds the first word in every sentence and groups all those words
#   a list. The words are in the order they are found.
# Input Parameter(s):
#   directory - A nested dictionary representing a dictionary
# Return Value(s):
#   Returns list of first words of all sentences within the given file.
#==========================================
def total_txt_size(directory):
    sum = 0
    if type(directory) == dict:
        for an_inside in directory.items():
            if "." in an_inside[0]:
                if len(an_inside[0]) > 4 and an_inside[0][-4:] == ".txt":
                    sum += total_txt_size(an_inside[1])
            elif type(an_inside[1]) == dict:
                sum += total_txt_size(an_inside[1])
    else:
        return directory
    return sum
