def play_turn(game_board: list, x: int, y: int, piece: str):
    size = len(game_board)
    if (0 <= y < size and 0 <= x < size) and game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    return False


# Test
if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    game_board2 = [['O', '', 'O'], ['X', '', 'X'], ['X', '', '']]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)
    print(play_turn(game_board2, 3, 0, "X"))
    print(game_board2)