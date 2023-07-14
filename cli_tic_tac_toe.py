from os import system


player_1 = "❌"
player_2 = "⭕"
theBoard = {
    'a': ' ', 'b': ' ', 'c': ' ',
    'd': ' ', 'e': ' ', 'f': ' ',
    'g': ' ', 'h': ' ', 'i': ' '
}

moves = 0
total_moves = 9


def check_input_and_add_value(field, player):
    global moves
    move_is_valid = None
    fields = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    check_input = len(field) == 1 and field in fields

    if check_input:
        check_if_subwrited = player_1 not in theBoard[field] and player_2 not in theBoard[field]

        if player == player_1 and check_if_subwrited:
            theBoard[field] = player_1
            move_is_valid = True
            moves += 1

        elif player == player_2 and check_if_subwrited:
            theBoard[field] = player_2
            move_is_valid = True
            moves += 1

    system('cls')
    return move_is_valid


def unpacket(board):
    a, b, c, *_ = board.values()  # 1º Line
    _, _, _, d, e, f, *_ = board.values()  # 2º Line
    *_, g, h, i = board.values()  # 3º Line
    return a, b, c, d, e, f, g, h, i


def print_Board(board):
    a, b, c, d, e, f, g, h, i = unpacket(board)
    add_line = '-' * moves
    print(f'{moves=}\n')
    print(f' {a=} || {b=} || {c=}')
    print(f'---------------------{add_line}')
    print(f' {d=} || {e=} || {f=}')
    print(f'---------------------{add_line}')
    print(f' {g=} || {h=} || {i=}')
    print()


def who_won(board):
    a, b, c, d, e, f, g, h, i = unpacket(board)

    result = "Draw!"
    flag = 1

    check_fields_completed = [
        [a, b, c],
        [a, d, g],
        [d, e, f],
        [g, h, i],
        [c, f, i],
        [b, e, h],
        [a, e, i],
        [c, e, g]
    ]

    for complet_line in check_fields_completed:

        if ' ' not in complet_line:
            players = [player_1, player_2]

            for player in players:
                if complet_line.count(player) == len(complet_line):
                    if player == player_2:
                        flag += 1
                    result = f'Player {str(flag)} is the Winner 🏆.\n'
    return result


def check_the_winner(who_won):
    check_moves_result = who_won
    if check_moves_result != "Draw!":
        check_ok = 0
    else:
        check_ok = 1
    return check_ok


def is_draw(board):
    if ' ' not in board.values():
        print_Board(board)
        print("Draw!")
        exit(0)


def game_over(check_player_moving, flag):
    result = who_won(theBoard)
    flag = check_the_winner(who_won=result)
    if check_player_moving == True and flag == 0:
        print_Board(theBoard)
        print(result)
        exit(0)


def checks(field, player):
    check_player_moving = check_input_and_add_value(field, player)
    game_over(check_player_moving, flag_of_winner)


if __name__ == "__main__":
    try:
        flag_of_winner = 1

        while True:
            print_Board(theBoard)
            field_first_player = input("[Player 1] Chose a field: ")
            checks(field_first_player, player_1)
            is_draw(theBoard)

            print_Board(theBoard)
            field_second_player = input("[Player 2] Chose a field: ")
            checks(field_second_player, player_2)
            is_draw(theBoard)

    except KeyboardInterrupt:
        print('\n\nCtrl + C ---> Finished game')
