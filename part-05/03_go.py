def who_won(game_board: list):
    count_player_1 = 0
    count_player_2 = 0

    for row in game_board:
        count_player_1 += row.count(1)
        count_player_2 += row.count(2)
    
    if count_player_1 > count_player_2:
        return 1
    elif count_player_2 > count_player_1:
        return 2

    return 0



# Test
if __name__ == "__main__":
    # 1. Пример из задания: у игрока 2 больше фишек
    board1 = [
        [2, 0, 0, 0, 0],
        [0, 2, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 2, 1, 0],
        [0, 0, 0, 2, 2],
    ]
    print(who_won(board1))  # ожидается 2

    # 2. У игрока 1 больше фишек
    board2 = [
        [1, 1, 0],
        [0, 2, 1],
        [0, 0, 0],
    ]
    print(who_won(board2))  # ожидается 1

    # 3. Ничья: поровну фишек
    board3 = [
        [1, 2],
        [2, 1],
    ]
    print(who_won(board3))  # ожидается 0

    # 4. Пустое поле — тоже ничья
    board4 = [
        [0, 0, 0],
        [0, 0, 0],
    ]
    print(who_won(board4))  # ожидается 0

    # 5. Поле не квадратное (размер не ограничен)
    board5 = [
        [2, 2, 2, 2, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 1],
    ]
    print(who_won(board5))  # ожидается 2

    # 6. Только один игрок на поле
    board6 = [[1], [1], [0]]
    print(who_won(board6))  # ожидается 1

    # 7. Функция не должна менять исходное поле
    board7 = [[1, 2], [0, 2]]
    copy7 = [row[:] for row in board7]
    who_won(board7)
    print(board7 == copy7)  # ожидается True