board = list(range(1, 10))

def game_field():
    print("-------------")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-------------")

def take_input(token_X_or_O):
    while True:
        value = input("Выберите ячейку для   " + token_X_or_O + "  ?")
        if not value in "1,2,3,4,5,6,7,8,9":
            print("Введите номер ячейки от 1 до 9!!!")
            print("---------------------------------")
            continue
        value = int(value)
        if str(board[value - 1]) in "XO":
            print("Ячейка уже занята! Выберите другую!")
            print("-----------------------------------")
            continue
        else:
            board[value - 1] = token_X_or_O
            break

def check_win():
    win_cords = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    for each in win_cords:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[0] - 1]
    else:
        return False

def main():
    counter = 0
    while True:
        game_field()
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        if counter > 3:
            win = check_win()
            if win:
                game_field()
                print("Выиграл игрок    " + win,  "  !")
                break
        counter += 1
        if counter > 8:
            game_field()
            print("Ничья!!!")
            break

main()