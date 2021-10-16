import pygame
pygame.init()

# Program Variables
runProgram = True # will keep the program running as long 

## Game States
SPLASH = 0
DIFF_SELECT = 1
HELP = 2
IN_GAME = 3

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

## Colors
COL_BLACK = (0, 0, 0)

# Helper Functions
def updateScreen():
    pygame.display.flip()
    clock.tick(refresh_rate)


# Main
while runProgram:
    # Handling Logic for game state events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runProgram = False
    
    # Logic for game states
    if gameState == SPLASH: # Logic for the title screen
        # Perfoming Logic
        pass
        # Drawing To Screen 
        pygame.Surface.fill(screen, COL_BLACK)

    elif gameState == DIFF_SELECT: # Logic for the difficulty select screen
        pass
    elif gameState == HELP: # Logic for the help screen
        pass
    elif gameState == IN_GAME: # Logic for in-game
        pass

    # Screen Projection Logic
    updateScreen()

pygame.quit()


