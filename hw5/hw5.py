import random
#==========================================
# Purpose:
#   Given 3 lists representing 3 types of college students, finds if
#   there are any students that are in all 3 lists, and then returns
#   a list of those students.
# Input Parameter(s):
#   grades - list of students who get the best grades
#   life - list of students who have social life
#   sleep - list of students who get a healthy amount of sleep
# Return Value:
#   Returns list of students who are in all three lists: grades, life, and
#   sleep
#==========================================
def wizards(grades, life, sleep):
    wizards = []
    arr = []
    if (len(life) > (len(grades) and len(sleep))):
        arr = life
    elif (len(grades)> (len(life) and len(sleep))):
        arr = grades
    else:
        arr = sleep
    for student in arr:
        if (student in grades) and (student in life) and (student in sleep):
            wizards.append(student)
    return wizards

#==========================================
# Purpose:
#   Runs a tic tac toe game where computer plays itself
# Input Parameter(s):
#   None
# Return Value:
#   Returns who won the tic tac toe game
#==========================================
def tic_tac_toe():
    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    rand = random.random()
    if random.random() >= .5:
        do_move(board, "O")
    else:
        do_move(board, "X")
    while winner(board) == "-":
        x_moves = board.count("X")
        o_moves = board.count("O")
        if x_moves > o_moves:
            do_move(board, "O")
        else:
            do_move(board, "X")
    return winner(board)

#==========================================
# Purpose:
#   Given a list representing a tic tac board and a string representing
#   the type of player, a move is played for the specific player on the
#   tic tac toe board
# Input Parameter(s):
#   board - list representing tic tac toe board
#   player - string representing type of player
# Return Value:
#   None
#==========================================
def do_move(board, player):
    move = random.choice(open_slots(board))
    board[move] = player

#==========================================
# Purpose:
#   Given a list repesenting a tic tac toe board game, finds all
#   open spots on board
# Input Parameter(s):
#   board - list repreenting tic tac toe board
# Return Value:
#   Returns list of indeces for open spots on tic tac toe board
#==========================================
def open_slots(board):
    open_spaces = []
    for i in range(0, 9):
        if board[i] == "-":
            open_spaces.append(i)
    return open_spaces

#==========================================
# Purpose:
#   Given a list representing board of tic tac toe game find out
#   whether someone won
# Input Parameter(s):
#   board - list representing board of tic tac toe game
# Return Value:
#   Returns string letter representing who has one if anyone has won
#==========================================
def winner(board):
    v1 = [board[0], board[3], board[6]]
    v2 = [board[1], board[4], board[7]]
    v3 = [board[2], board[5], board[8]]
    d1 = [board[0], board[4], board[8]]
    d2 = [board[2], board[4], board[6]]
    rows = [board[0:3], board[3:6], board[6:], v1, v2, v3, d1, d2]

    for row in rows:
        result = three_in_row(row)
        if result == "X":
            return "X"
        elif result == "O":
            return "O"
    if (board.count("-") > 0):
        return "-"
    else:
        return "D"

#==========================================
# Purpose:
#   Given a list representing a row in tic tac toe board find if all spots
#   in row are covered by one player
# Input Parameter(s):
#   three_spots - list representing row in tic tac toe board
# Return Value:
#   Returns string letter representing who has won if anyone has won
#==========================================
def three_in_row(three_spots):
    if (("X" in three_spots) and ("O" not in three_spots) and ("-" not in three_spots)):
        return "X"
    elif (("O" in three_spots) and ("X" not in three_spots) and ("-" not in three_spots)):
        return "O"
    else:
        return "D"


#==========================================
# Purpose:
#   Given number of tic tac toe games to play, runs the given
#   nunber of tic tac games and tallies how many times who has won
# Input Parameter(s):
#   n - number of tic tac toe games to run
# Return Value:
#   None
#==========================================
def play_games(n):
    x_wins = 0
    o_wins = 0
    draws = 0
    for i in range (0, n):
        winner = tic_tac_toe()
        if winner == "X":
            x_wins += 1
        elif winner == "O":
            o_wins += 1
        else:
            draws += 1
    print("X wins:", x_wins)
    print("O wins:", o_wins)
    print("Draws:", draws)
