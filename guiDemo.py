import pygame
import threading
from time import sleep
import random
easy = list()
medium = list()
difficult = list()

pygame.init()

# Program Variables
runProgram = True # will keep the program running as long 
difficulty = 0
time = True
totalWords = 0

## Game States
SPLASH = 0
RESULTS = 1
IN_GAME = 2

gameState = SPLASH

## Window Variables
WIDTH = 1000
HEIGHT = 700
SIZE = (WIDTH, HEIGHT)
TITLE = "Untitled Typing Game"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()
refresh_rate = 60
display_clock = 0

# Asset Variables

## Fonts
splash_font = pygame.font.Font("guiAssets/Ubuntu-Bold.ttf", 60)
button_font = pygame.font.Font("guiAssets/Ubuntu-Regular.ttf", 60)
default_font = pygame.font.Font("guiAssets/Ubuntu-Regular.ttf", 30)

## Colors
COL_BLACK = (0, 0, 0)
COL_RED = (255, 0, 0)
COL_GREEN = (0, 255, 0)
COL_ORANGE = (255, 162, 0)

# Helper Functions
def updateScreen():
    pygame.display.flip()
    clock.tick(refresh_rate)

def displayText(xpos, ypos, font, color, printedtext):
    first_text = font.render(printedtext, 1, color)
    textW = first_text.get_width()
    screen.blit(first_text, [xpos - textW/2, ypos])

def displayButton(xpos, ypos, displayedText, color):
    
    # Draws the button
    pygame.draw.rect(screen, color, (xpos, ypos, 500, 100))

    button_text = button_font.render(displayedText, 1, COL_BLACK)
    screen.blit(button_text, [xpos+200, ypos+10])

def checkClick(xpos, ypos):
    mousePos = pygame.mouse.get_pos()
    mouseClick = pygame.mouse.get_pressed()

    return xpos <= mousePos[0] <= xpos+500 and ypos <= mousePos[1] <= ypos+100 and mouseClick[0] == 1

# Game Functions

def timerFunction():
    print("\nTimes up!!")
    print("\nPress Enter to see your results!")
    global time
    time = False

def displayResults():
    print("Your Words Per minute for this test is: " + str(totalWords))
    if(totalWords == 66):
        print("Execute order 66!")
    elif(totalWords > 50):
        print("You are an octopus!")
    elif(totalWords > 40):
        print("Fast you are")
    elif(totalWords>30):
        print("Not bad kid")
    elif(totalWords>20):
        print("I guess your ok with being average")
    elif(totalWords>10):
        print("Is that the best you can do?")
    else:
        print("Bonehead!")

def runGame(choice):
    #represents the list that will contain the elements for the current game
    gameList = list()
    if choice == 0:  # if the choice is 1, then will run the game on easy difficulty
        gameList = easy
    elif choice == 1:
        gameList = medium
    elif choice == 2:
        gameList = difficult
    else:
        print("Error when selecting difficulty")  # Debugging tool
    isFirst = True
    while(time):
        randNum = random.randint(0,len(gameList)-1)
        print(gameList[randNum], end = " ")
        if isFirst == True:
            print("\nPlease enter the word above and press Enter:", end = " ")
            isFirst = False
        word = input()
        while word != gameList[randNum] and time:
            word = input("Please enter the word " + gameList[randNum] + ": ")
        global totalWords
        if(word == gameList[randNum] and time):
            totalWords += 1

def runMainGame():
    #opens the file and reads in the content from them

    file1 = open("WordList.txt", "r")
    for line in file1.readlines():
        #print(line.split("\t")[1])
        if(line.split("\t")[1].strip() == "Easy"):
            easy.append(line.split("\t")[0])
        if(line.split("\t")[1].strip() == "Medium"):
            medium.append(line.split("\t")[0])
        if(line.split("\t")[1].strip() == "Hard"):
            difficult.append(line.split("\t")[0])
    file1.close()

    #defines the timer objects that will execute the displayResults once something happens
    timer = threading.Timer(10.0, timerFunction)
    timer.start()
    
    runGame(difficult)
    displayResults()

    exit()

# MAIN 
while runProgram:
    # Handling Logic for game state events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runProgram = False
    
    # Logic for game states
    if gameState == SPLASH: # Logic for the title screen
 
        pygame.Surface.fill(screen, COL_BLACK)
        displayText(SIZE[0]/2, 200, splash_font, COL_RED, "Untitled Typing Game")
        
        ## Easy Button
        displayButton(SIZE[0]/2 - 250, 300, "EASY", COL_GREEN)

        if (checkClick(SIZE[0]/2 - 250, 300)):
            gameState = IN_GAME
            difficulty = 0
            print("You pressed the easy button")

        ## Medium Button

        displayButton(SIZE[0]/2 - 250, 425, "MEDIUM", COL_ORANGE)

        if (checkClick(SIZE[0]/2 - 250, 425)):
            gameState = IN_GAME
            difficulty = 1
            print("You pressed the medium button")
        
        ## Hard Button

        displayButton(SIZE[0]/2 - 250, 550, "HARD", COL_RED)

        if (checkClick(SIZE[0]/2 - 250, 550)):
            gameState = IN_GAME
            difficulty = 2
            print("You pressed the hard button")

    elif gameState == IN_GAME: # Logic for in-game        
        pygame.Surface.fill(screen, COL_BLACK)
        pygame.draw.line(screen, COL_RED, (100, 300), (900, 300), 5)
        displayText(500, 600, default_font, COL_RED, "Type the words that appear above into the console")
        
        runMainGame()

    # Screen Projection Logic
    updateScreen()

pygame.quit()
