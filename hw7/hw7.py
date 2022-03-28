import random
#==========================================
# Purpose:
#   Computes and comes up with a list of numbers from n to 1 using
#   the Collatz Conjecture
# Input Parameter(s):
#   n - number that is used in the Collatz Cojecture to create the list
# Return Value(s):
#   Returns a list representing a collatz sequence
#==========================================
def collatz(n):
    if n == 1:
        return [n]
    elif n % 2 == 0:
        return [n]  + collatz(n // 2)
    else:
        return [n] + collatz((3 * n) + 1)

#==========================================
# Purpose:
#   Finds the minimum number in a list of numbers
# Input Parameter(s):
#   num_list - a list which will be searched for what its minimum value is
# Return Value(s):
#   Returns a number representing the given list's minimum value
#==========================================
def find_min(num_list):
    if len(num_list)  == 1:
        return num_list[0]
    else:
        if num_list[1] < num_list[0]:
            return find_min(num_list[1:])
        else:
            return find_min([num_list[0]] + num_list[2:])

#==========================================
# Purpose:
#   Runs a tic tac toe game where computer plays itself and the O
#   wins or there is a draw; those are the only two winner results in
#   this function
# Input Parameter(s):
#   None
# Return Value:
#   Returns who won the tic tac toe game
#==========================================
def tic_tac_toe():
    board = ["-"] * 9
    if random.random() >= 0.5:
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
    if player == "X":
        move = random.choice(open_slots(board))
        board[move] = player
    else:
        open_spaces = open_slots(board)
        lowest_state = 2
        best_spot = 0
        for spot in open_spaces:
            board_copy = board[:]
            board_copy[spot] = player
            state_possibility = force_win(board_copy)
            if state_possibility < lowest_state:
                lowest_state = state_possibility
                best_spot = spot
        board[best_spot] = player


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

#==========================================
# Purpose:
#   Given list representing tic-tac-toe board, finds state representing
#   who (if any) has won
# Input Parameter(s):
#   board - a list representation of a tic-tac-toe board
# Return Value:
#   Returns the current state of the board
#==========================================
def force_win(board):
    who_won = winner(board)
    if who_won != "-":
        if who_won == "X":
            return 1
        elif who_won == "O":
            return -1
        else:
            return 0
    else:
        x_moves = board.count("X")
        o_moves = board.count("O")
        if x_moves > o_moves:
            lowest_state = 2
            open_spaces = open_slots(board)
            for spot in open_spaces:
                board_copy = board[:]
                board_copy[spot] = "O"
                state_possibility = force_win(board_copy)
                if state_possibility < lowest_state:
                    lowest_state = state_possibility
            return lowest_state
        else:
            highest_state = -2
            open_spaces = open_slots(board)
            for spot in open_spaces:
                board_copy = board[:]
                board_copy[spot] = "X"
                state_possibility = force_win(board_copy)
                if state_possibility > highest_state:
                    highest_state = state_possibility
            return highest_state
