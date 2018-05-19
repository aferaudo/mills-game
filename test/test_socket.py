from src.communication.mysocket import MySocket
from src.MillsGame import MillsGame

PYTHON_PORT = 3033

python_socket = MySocket()


print("Invio la richiesta di connessione alla java interface")
python_socket.connect('localhost', PYTHON_PORT)
print("Connessione avvenuta con successo!")

print("Invio giocatore scelto..")
our_color = "white"
python_socket.my_send(my_msg.encode("UTF-8"))
print("Messaggio inviato con successo")

millsGame = MillsGame()
current_state = millsGame.initial

print("Attendo lo stato iniziale")
state_board = python_socket.receive()
print(state_board)

python_socket.safely_close()
