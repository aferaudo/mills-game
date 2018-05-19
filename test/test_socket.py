from src.communication.mysocket import MySocket

PYTHON_PORT = 3033

python_socket = MySocket()

print("Invio la richiesta di connessione alla java interface")
python_socket.connect('localhost', PYTHON_PORT)

print("Connessione avvenuta con successo!")

print("Invio il messaggio..")
my_msg = b"black"
python_socket.my_send(my_msg)
print("Messaggio inviato con successo")

python_socket.safely_close()


