
import random
ran= random.randrange(50,200)
print("The random number is between 50-200 and you have 5 chances to guess the correct random number:")
for i in range(5):
    guess=int(input("enter your guess: "))
    if(ran==guess):
        print("WELL DONE!!")
        print("You took ",i," chance to guess the random number")
        break
    elif((guess>ran and guess<ran+5)or(guess>=ran-5 and guess<ran)):
        print("OOH.SO CLOSE")
    else:
        print("INCORRECT GUESS")


print("the random number was: ",ran)




