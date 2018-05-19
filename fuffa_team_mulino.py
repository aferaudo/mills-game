import sys, getopt


def main(argv):
    # prendiamo in ingresso da terminale il colore del giocatore
    our_color = None
    try:
        opts, args = getopt.getopt(argv, "wbh")
    except getopt.GetoptError:
        print('usage: fuffa_team_mulino.py -w (player white) -o (player black)')
        sys.exit(2)
    if len(opts) != 1:
        print('usage: fuffa_team_mulino.py -w (player white) -b (player black)')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('usage: fuffa_team_mulino.py -w (player white) -b (player black)')
            sys.exit()
        elif opt == '-w':
            our_color = 'W'
        elif opt == '-b':
            our_color = 'B'
    if our_color is None:
        print('please specify a player\nusage: fuffa_team_mulino.py -w (player white) -o (player black)')
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
