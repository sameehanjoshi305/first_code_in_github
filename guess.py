import random
guessTaken=0

print ("Hello I am sameehan who are you")
myName=input ()
number= random.randint (1, 20)
print("Guess the number and try your luck Mr. " +  myName)
for guessTaken in range(1,4):
    guessedNumber = int(input())
    if(guessedNumber > number):
        print("Well " + myName + ", you guessd it high!!")
    elif(guessedNumber < number):
        print("Well " + myName + ", you guessed it low!!")
    else:
        print("Hurray!! "+ myName +", you guessed it right.")
        break

if(guessTaken == 3):
    print("you lost boi")


    
