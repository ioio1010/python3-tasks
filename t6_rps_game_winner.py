class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(players):
    HAND_MOVES = ["R", "P", "S"]

    result = None

    if len(players) > 2:
        raise WrongNumberOfPlayersError

    p1_move = players[0][1]
    p2_move = players[1][1]

    if p1_move not in HAND_MOVES or p2_move not in HAND_MOVES:
        raise NoSuchStrategyError

    if p1_move == 'P':
        result = players[1] if p2_move == 'S' else players[0]
    elif p1_move == 'S':
        result = players[0] if p2_move == 'P' else players[1]
    elif p1_move == 'R':
        result = players[0] if p2_move == 'S' else players[1]
    elif p1_move == p2_move:
        result = players[0]

    print("players: " + str(players) + " | result: " + " ".join(result))

    return result


rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])
rps_game_winner([['player1', 'P'], ['player2', 'A']])
rps_game_winner([['player1', 'P'], ['player2', 'S']])
rps_game_winner([['player1', 'P'], ['player2', 'R']])
rps_game_winner([['player1', 'S'], ['player2', 'P']])
rps_game_winner([['player1', 'S'], ['player2', 'R']])
rps_game_winner([['player1', 'R'], ['player2', 'S']])
rps_game_winner([['player1', 'R'], ['player2', 'P']])
rps_game_winner([['player1', 'P'], ['player2', 'P']])
