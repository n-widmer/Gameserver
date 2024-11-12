# Gameserver
Here are the requirements provided by my Professor:

CS 35201 Computer Communication Networks
Fall 2024
Department of Computer Science
Kent State University
Homework 3 - Final
Sockets programming
Due date: December 4th
1. Using the code provided with the homework, and the pygame python library, continue
working on the client-server application of the “bucket catch” game.
2. The objective of the game is to collect as many falling objects as possible, similar to the
“bucket catch” game.
3. Rules of the game:
a. One bucket moves sideways (even up and down) to collect all falling objects.
b. Falling objects must be generated at random locations from the top of the screen
from the starting position on the X-axis.
c. Objects will fall faster as the game progresses.
d. Bucket also moves faster as the game progresses.
e. Player losses as soon as the first object touches the bottom of the screen.
4. A score must be displayed on the screen. No leaderboard is necessary.
5. GUI is not an important part of the homework, it is not necessary to implement any
visual elements outside of the basic elements to execute the game properly.
6. The server side will be in charge of displaying the game while the client side will be in
charge of the controls, you can set the controls to be with any keys from the keyboard,
preferable with the “WASD” or arrow keys.
7. Homework can be developed in pairs of two students, allowing for 2 people to work on
the 2 people’s project made specifically for 2 people and no less or more than 2 people.
8. The project will be evaluated during class time by the instructor and the grader together.
With students running the server and client side on two separate computers.
9. Project must be submitted to canvas as a .rar or .zip file containing all the source codes.
Evaluation table
Tasks Points - 20 total
Client-server connection established 3 pts
Client gets key input and sends it to server 3 pts
Server receives client data 3 pts
Server side uses threads to manage game
GUI and server
2 pts
Main bucket moves on the screen based on
client’s key press
2 pts
Objects are randomly generated on the
screen
1 pt
Objects fall at a faster speed as the game
progresses
1 pt
Bucket moves faster as the game
progresses
1 pt
Collision between “bucket” and falling
objects
1 pt
Game ends when 1st object reaches the
bottom of the screen
1 pt
Functional score board 1 pt
Game can be restarted once it finishes 1 pt
Additional notes:
a) The pygame and keyboard libraries must be installed alongside with python to
develop the game.
b) MacOS doesn’t support the “keyboard” library, use pynput instead.
c) You can use github to manage the development of the project.CS 35201 Computer Communication Networks
Fall 2024
Department of Computer Science
Kent State University
Homework 3 - Final
Sockets programming
Due date: December 4th
1. Using the code provided with the homework, and the pygame python library, continue
working on the client-server application of the “bucket catch” game.
2. The objective of the game is to collect as many falling objects as possible, similar to the
“bucket catch” game.
3. Rules of the game:
a. One bucket moves sideways (even up and down) to collect all falling objects.
b. Falling objects must be generated at random locations from the top of the screen
from the starting position on the X-axis.
c. Objects will fall faster as the game progresses.
d. Bucket also moves faster as the game progresses.
e. Player losses as soon as the first object touches the bottom of the screen.
4. A score must be displayed on the screen. No leaderboard is necessary.
5. GUI is not an important part of the homework, it is not necessary to implement any
visual elements outside of the basic elements to execute the game properly.
6. The server side will be in charge of displaying the game while the client side will be in
charge of the controls, you can set the controls to be with any keys from the keyboard,
preferable with the “WASD” or arrow keys.
7. Homework can be developed in pairs of two students, allowing for 2 people to work on
the 2 people’s project made specifically for 2 people and no less or more than 2 people.
8. The project will be evaluated during class time by the instructor and the grader together.
With students running the server and client side on two separate computers.
9. Project must be submitted to canvas as a .rar or .zip file containing all the source codes.
Evaluation table
Tasks Points - 20 total
Client-server connection established 3 pts
Client gets key input and sends it to server 3 pts
Server receives client data 3 pts
Server side uses threads to manage game
GUI and server
2 pts
Main bucket moves on the screen based on
client’s key press
2 pts
Objects are randomly generated on the
screen
1 pt
Objects fall at a faster speed as the game
progresses
1 pt
Bucket moves faster as the game
progresses
1 pt
Collision between “bucket” and falling
objects
1 pt
Game ends when 1st object reaches the
bottom of the screen
1 pt
Functional score board 1 pt
Game can be restarted once it finishes 1 pt
Additional notes:
a) The pygame and keyboard libraries must be installed alongside with python to
develop the game.
b) MacOS doesn’t support the “keyboard” library, use pynput instead.
c) You can use github to manage the development of the project.
