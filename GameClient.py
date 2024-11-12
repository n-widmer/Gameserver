from pynput.keyboard import Listener
import socket
import time


#global vairables to be used through both methods
client_socket = None
quit_flag = False

def on_press(key):
    global client_socket
    global quit_flag

    try:
    #check if user wants to exit game (with 'q')
        if key.char == 'q':
            quit_flag = True
            return False
        

        #print statements are for debugging purposes
        elif key.char == 'a':
            #print("key 'a' pressed") 
            client_socket.send('a'.encode())
        elif key.char == 'd':
            #print("key 'd' pressed")
            client_socket.send('d'.encode())
        elif key.char == 's':
            #print("key 's' pressed")
            client_socket.send('s'.encode())
        elif key.char == 'w':
            #print("key 'w' pressed")
            client_socket.send('w'.encode())
        time.sleep(0.1)
    except AttributeError:
        pass #ignore any other key inputs



def client_program():
    global client_socket
    global quit_flag


    print("trying to connect to server")
    host = "10.95.10.244"
    port = 5001   # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    print("waiting for keyboard input")
   
   #start listening for keyboard input
    with Listener(on_press=on_press) as listener:
        while not quit_flag:
            listener.join()


    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()