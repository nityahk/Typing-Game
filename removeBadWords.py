with open('/Users/ben/Desktop/hello/newWords.txt', 'r+') as newfile:
    with open('/Users/ben/Desktop/hello/words.txt', 'r+') as oldFile:
        for word in oldFile.readlines():
            word = word.strip('\n')

            write = True

            if(len(word) <  1):
                write = False

            for letter in word:
                if(letter == '.' or letter == ',' or letter == '-' or letter == '\'' or letter == '&' or letter == '/'):
                    write = False

            for letter in word:
                if(letter == '0' or letter == '1' or letter == '2' or letter == '3' or letter == '4' or letter == '5' or letter == '6' or letter == '7' or letter == '8' or letter == '9'):
                    write = False

            count = 0;
            for letter in word:
                if(letter.isupper()):
                    count = count + 1

            if (count > 0):
                write = False

            if(write):
                newfile.write(word + '\n')

        with open('/Users/ben/Desktop/hello/wordlist.txt', 'r+') as wordlist:
            for word in newfile.readlines():
                newWord = word.lower()
                wordlist.write(newWord + '\n')



newfile.close()
oldFile.close()
