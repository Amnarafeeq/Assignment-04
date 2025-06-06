def sum(a, b, c):
    return a + b + c

def print_board(xState, zState):
    zero = "X" if xState[0] else ("O" if zState[0] else 0)
    one = "X" if xState[1] else ("O" if zState[1] else 1)
    two = "X" if xState[2] else ("O" if zState[2] else 2)
    three = "X" if xState[3] else ("O" if zState[3] else 3)
    four = "X" if xState[4] else ("O" if zState[4] else 4)
    five = "X" if xState[5] else ("O" if zState[5] else 5)
    six = "X" if xState[6] else ("O" if zState[6] else 6)
    seven = "X" if xState[7] else ("O" if zState[7] else 7)
    eight = "X" if xState[8] else ("O" if zState[8] else 8)

    print("\nCurrent Board:")
    print()
    print(f" {zero} | {one} | {two} ")
    print("---|---|---")
    print(f" {three} | {four} | {five} ")
    print("---|---|---")
    print(f" {six} | {seven} | {eight} ")
    print()

def check_winner(xState, zState):
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("🎉 Congratulations! Player 'X' wins the game!")
            return 1
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("🎉 Congratulations! Player 'O' wins the game!")
            return 0
    return -1

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    turn = 1
    print("🎮 Welcome to the Tic Tac Toe Game!")
    print("----------------------------------")
    print("Instructions:")
    print("Enter a number from 0 to 8 to mark your move on the board.")
    print("The positions are like this:")
    print(" 0 | 1 | 2 ")
    print("---|---|---")
    print(" 3 | 4 | 5 ")
    print("---|---|---")
    print(" 6 | 7 | 8 ")
    print("----------------------------------")

    while True:
        print_board(xState, zState)

        if turn == 1:
            print("🔵 Player 'X', it's your turn.")
            value = int(input("Enter your move (0-8): "))
            xState[value] = 1
        else:
            print("🟡 Player 'O', it's your turn.")
            value = int(input("Enter your move (0-8): "))
            zState[value] = 1

        cWin = check_winner(xState, zState)

        if cWin != -1:
            print("🏁 Game Over. Thanks for playing!")
            break

        if (xState.count(1) + zState.count(1)) == 9:
            print_board(xState, zState)
            print("🤝 It's a draw! Well played both players.")
            print("🏁 Game Over.")
            break

        turn = 1 - turn
