#assign difficuly to words

import random

with open('words.txt', 'r+') as newfile:
    with open('wordlist.txt', 'r+') as wordlist:
        for word in newfile.readlines():
            n = random.randrange(0,20)
            if(n == 0):
                difficulty = 0
                if(len(word) < 7):
                    difficulty = 0
                elif(len(word) > 7 and len(word) < 12):
                    difficulty = 1
                else:
                    difficulty = 2

                line = word.strip('\n') + '\t' + str(difficulty) + '\n'
                wordlist.write(line)
