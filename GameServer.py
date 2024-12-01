#Author: Nick Widmer
#Date: 11/10/24
#Class: CCN

import threading #This allows for concurrent execution of game and server
import pygame  
from pygame.locals import *  #Allows for game to be made
import socket    #Allows for basic networking features
import sys   
import random   
import os 



gameWidth = 800
gameHeight = 600

pixel = 64

# spawn the image at a random location on the screen
bitcoinXPos = random.randint(0, (gameWidth - pixel))
bitcoinYPos = 0 - pixel

bucketXPos = (gameWidth / 2) - (pixel / 2)
bucketYPos = gameHeight - pixel

score = 0
score_increment = 1

start_time = 0

bucketSpeedChange = 20

#runs game loop and updates display
def GameThread():
    pygame.init()
    pygame.font.init()

    global gameWidth
    global gameHeight
    global bitcoinXPos
    global bitcoinYPos
    global bucketXPos
    global bucketYPos
    global score 
    global score_increment
    global start_time
    global bucketSpeedChange

    # Set the screen bounds
    screen = pygame.display.set_mode((gameWidth, gameHeight))

    pygame.display.set_caption('Money Heist by Nick Widmer')

    backgroundImg = pygame.image.load("./assets/background.png") 
    backgroundImg = pygame.transform.scale(backgroundImg, (gameWidth, gameHeight))

    bucketImg = pygame.image.load("./assets/bucket.png")
    bucketImg = pygame.transform.scale(bucketImg, (100, 100))


    gameIcon = pygame.image.load("./assets/bitcoin.png")
    pygame.display.set_icon(gameIcon)


    # Set initially to 0
    bucketXPosChange = 0


    # Method for setting bucketImage at specific coordinates
    def player(x, y):
        # Paste image to the screen
        screen.blit(bucketImg, (x, y))

    # load the image =
    bitcoinImage = pygame.image.load("./assets/bitcoin.png")
    bitcoinImage = pygame.transform.scale(bitcoinImage, (pixel, pixel))


    # To set the speed of the bitcoinImage when falling
    bitcoinYPosChange = 2
    bitcoinXPosChange = 2


    # Function definition for setting image at a particular coord
    def bitCoin(x, y):
        # Paste bitcoin to screen
        screen.blit(bitcoinImage, (x, y))
    
    def haveCollided():
        global bitcoinYPos, bitcoinXPos
        if bucketYPos < (bitcoinYPos + pixel):

            if ((bucketXPos > bitcoinXPos and bucketXPos < (bitcoinXPos + pixel)) or 
                ((bucketXPos + pixel) > bitcoinXPos and (bucketXPos + pixel) < (bitcoinXPos + pixel))):
                bitcoinYPos = 0 - pixel
                bitcoinXPos = random.randint(0, (gameWidth - pixel))
                return True
            
        return False

    clock = pygame.time.Clock()

    if start_time is None:
        start_time = pygame.time.get_ticks()


    last_speed_increase_time = 0
    running = True
    while running:
        # Paste background to window
        
        screen.blit(backgroundImg, (0,0))
        global score

        #set global font
        font = pygame.font.Font('assets/Geist_Mono,Mulish/Geist_Mono/GeistMono-VariableFont_wght.ttf', 36)

        
        #calculate time since game has started
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

        #formatting
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        time_text = f"{minutes:02}:{seconds:02}"

        #display the time on screen
        time_surface = font.render(f'Time: {time_text}', True, (255, 255, 255))
        screen.blit(time_surface, ((gameWidth - 270), 10))
        
        #render the score on the screen
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #update speed of bitcoin and bucket every 10 sec
        if elapsed_time - last_speed_increase_time >= 10:
            bitcoinYPosChange += 1
            bucketSpeedChange += 5
            last_speed_increase_time = elapsed_time


        if bucketXPos >= (gameWidth - pixel):
            bucketXPos = (gameWidth - pixel)

        if bucketXPos <= 0:
            bucketXPos = 0

        if bitcoinYPos >= gameHeight:
            font_gameover =  pygame.font.Font('assets/Geist_Mono,Mulish/Geist_Mono/GeistMono-VariableFont_wght.ttf', 64)
            gameOver_text = font_gameover.render("GAME OVER!", True, (255, 0, 0))
            screen.blit(gameOver_text, (gameWidth / 2 - 200, gameHeight / 2 - 50))
            pygame.display.update()
            pygame.time.wait(2000)
            running = False
            continue


        bucketXPos += bucketXPosChange
        bitcoinYPos += bitcoinYPosChange

        player(bucketXPos, (bucketYPos - 60))
        bitCoin(bitcoinXPos, bitcoinYPos)
        if haveCollided():
            score += score_increment

        

        pygame.display.update()
        clock.tick(60)



        

# pygame.quit()


def ServerThread():
    global bucketYPos
    global bucketXPos
    global bucketSpeedChange

    # get the hostname
    host = socket.gethostbyname(socket.gethostname())
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    host = s.getsockname()[0]
    s.close()
    print(host)
    port = 6999  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
    print("Server enabled...")
    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))    
    while True:        
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        
        print("from connected user: " + str(data))
        if(data == 'w'):
            bucketYPos -= bucketSpeedChange
        if(data == 's'):
            bucketYPos += bucketSpeedChange
        if(data == 'a'):
            bucketXPos -= bucketSpeedChange
        if(data == 'd'):
            bucketXPos += bucketSpeedChange
    conn.close()  # close the connection


def main():
    #start server thread
    t1 = threading.Thread(target=ServerThread, args=[])
    #t2 = threading.Thread(target=GameThread, args=[])
    t1.start()
    #t2.start()

    GameThread()

    #run game loop on main thread

if __name__ == "__main__":
     main()

