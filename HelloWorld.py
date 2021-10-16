import threading
from time import sleep
import random
easy = list()
medium = list()
difficult = list()

#opens the file and reads in the content from them

file1 = open("WordList.txt", "r")
for line in file1.readlines():
    #print(line.split("\t")[1])
    if(line.split("\t")[1].strip() == "Easy"):
        easy.append(line.split("\t")[0])
    if(line.split("\t")[1].strip() == "Medium"):
        medium.append(line.split("\t")[0])
    if(line.split("\t")[1].strip() == "Difficult"):
        difficult.append(line.split("\t")[0])
file1.close()



time = True
totalWords = 0


def timerFunction():
    print("\nTimes up!!")
    print("\nPress Enter to see your results!")
    global time
    time = False

#defines the timer objects that will execute the displayResults once something happens
timer = threading.Timer(60.0, timerFunction)
timer.start()

#All game related info is below
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
#asks the user what difficulty the thing is going to be /
userDifficulty = input("Please enter your difficulty: \n0) Easy \n1) Medium \n2) Hard\n")
'''
while(not(userDifficulty.isnumeric())):
    userDifficulty = input("Please enter a number: ")
while(not(int(userDifficulty) == 0 or int(userDifficulty) == 1 or int(userDifficulty) == 2)):
    userDifficulty = input("Please enter a valid difficulty: ")
    if(not(userDifficulty.isnumeric())):
        print("Please enter a number")
    print(userDifficulty)
'''
runGame(int(userDifficulty))

#end of new stuff
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
displayResults()


exit()