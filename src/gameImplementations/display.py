

def display(game, state):
    print(state.board[0] + "(00)----------------------" + state.board[1] + "(01)----------------------" + state.board[2] + "(02)");
    print("|                           |                           |");
    print("|       " + state.board[8] + "(08)--------------" + state.board[9] + "(09)--------------" + state.board[10] + "(10)     |");
    print("|       |                   |                    |      |");
    print("|       |                   |                    |      |");
    print("|       |        " + state.board[16] + "(16)-----" + state.board[17] + "(17)-----" + state.board[18] + "(18)       |      |");
    print("|       |         |                   |          |      |");
    print("|       |         |                   |          |      |");
    print(state.board[3] + "(03)---" + state.board[11] + "(11)----" + state.board[19] + "(19)               " + state.board[20] + "(20)----" +
          state.board[12] + "(12)---" + state.board[4] + "(04)");
    print("|       |         |                   |          |      |");
    print("|       |         |                   |          |      |");
    print("|       |        " + state.board[21] + "(21)-----" + state.board[22] + "(22)-----" + state.board[23] + "(23)       |      |");
    print("|       |                   |                    |      |");
    print("|       |                   |                    |      |");
    print("|       " + state.board[13] + "(13)--------------" + state.board[14] + "(14)--------------" + state.board[15] + "(15)     |");
    print("|                           |                           |");
    print("|                           |                           |");
    print(state.board[5] + "(05)----------------------" + state.board[6] + "(06)----------------------" + state.board[7] + "(07)");
