import random
num=random.randint(1,100)
user=int(input("Guess the number:\nEnter -1 to stop:"))
guesses=1
while(user!=-1):
    if(user==num):
        print(f"A perfect Guess!\n You took {guesses} guesses")
        break
    elif(user>num):
        user=int(input("Lower number please: "))
    else:
        user=int(input("Higher number please: "))
    guesses+=1
