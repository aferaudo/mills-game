# util for printing colored string
class bcolors:
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    HILIHGT = '\033[41m'
    WHITE = '\033[93m'
    BLACK = '\033[91m'

# take an index occupied by some player and colors it
def print_colored(linea):
    new_line = ''
    for c in linea:
        if c == 'W':
            new_line += bcolors.WHITE + c + bcolors.END
        elif c == 'B':
            new_line += bcolors.BLACK + c + bcolors.END
        else:
            new_line += c

    print(new_line)



def display(game, state):
    print_colored(state.board[0] + "(00)----------------------" + state.board[1] + "(01)----------------------" + state.board[2] + "(02)")
    print_colored("|                           |                           |")
    print_colored("|       " + state.board[3] + "(03)--------------" + state.board[4] + "(04)--------------" + state.board[5] + "(05)     |")
    print_colored("|       |                   |                    |      |")
    print_colored("|       |                   |                    |      |")
    print_colored("|       |        " + state.board[6] + "(06)-----" + state.board[7] + "(07)-----" + state.board[8] + "(08)       |      |")
    print_colored("|       |         |                   |          |      |")
    print_colored("|       |         |                   |          |      |")
    print_colored(state.board[9] + "(09)---" + state.board[10] + "(10)----" + state.board[11] + "(11)               " + state.board[12] + "(12)----" +
          state.board[13] + "(13)---" + state.board[14] + "(14)")
    print_colored("|       |         |                   |          |      |")
    print_colored("|       |         |                   |          |      |")
    print_colored("|       |        " + state.board[15] + "(15)-----" + state.board[16] + "(16)-----" + state.board[17] + "(17)       |      |")
    print_colored("|       |                   |                    |      |")
    print_colored("|       |                   |                    |      |")
    print_colored("|       " + state.board[18] + "(18)--------------" + state.board[19] + "(19)--------------" + state.board[20] + "(20)     |")
    print_colored("|                           |                           |")
    print_colored("|                           |                           |")
    print_colored(state.board[21] + "(21)----------------------" + state.board[22] + "(22)----------------------" + state.board[23] + "(23)")
