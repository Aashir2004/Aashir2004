from random import randint
randnum = randint(0,100)


guess = int(input("Please guess the positive integer generated between 0 and 100: "))
tally = 1
while guess != randnum:
        if isinstance(guess, int):
            if guess > randnum and guess < 101:
                print("Lower\n")
                tally += 1
                guess = int(input("Please guess the positive integer generated between 0 and 100: "))
            elif guess < randnum and guess > -1:
                print('Higher\n')
                tally += 1
                guess = int(input("Please guess the positive integer generated between 0 and 100: "))
            elif guess == randnum:
                print('Correct\n')
                tally += 1
                guess = int(input("Please guess the positive integer generated between 0 and 100: "))
            elif guess < 0 or guess > 100:
                print("Error 404: Unknown Number entered\n")
                guess = int(input("Please guess the positive integer generated between 0 and 100: "))
        else:
            print("ERROR 404: Please enter an integer")
s = "Congratulations! You guessed the number correctly in "
z = " times!"
print("{}{}{}".format(s, tally, z))

