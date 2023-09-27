import socket
from _thread import *   #agar kita dapat memproses banyak client
from player import Player
import pickle   #agar data antar client tetap sama

server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((server, port))
s.listen(2)
print("Waiting for a connection, Server Started")


players = [Player(0,0,50,50,(255,0,0)), Player(100,100, 50,50, (0,0,255))]  #buat player

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]  #kirim data ke player 1
                else:
                    reply = players[1]  #kirim data ke player 2
                
            conn.sendall(pickle.dumps(reply))   #kirim data player
        except:
            break
        
    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1