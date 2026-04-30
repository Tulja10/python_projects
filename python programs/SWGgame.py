# SNAKE WATER GUN ......
# PLAY AND HAVE FUN......

'''
snake : -1
water : 0
gun : 1
'''

import random
computer= random.choice([0,-1,1])
userstr=input("Enter your choice (s/w/g): ")
dict={"s":-1,"w":0,"g":1}
revdict={0:"Water",1:"Gun",-1:"Snake"}
usernum=dict[userstr]
print(f"Computer chose {revdict[computer]}")
print(f"You chose {revdict[usernum]}")

if(computer==usernum):
    print("Its a tie..better luck next time")
else:
    if(computer==-1 and usernum==1):
        print("You Win")
    elif(computer==-1 and usernum==0):
        print("You Lose")
    elif(computer==1 and usernum==-1):
        print("You Lose")
    elif(computer==1 and usernum==0):
        print("You Win")
    elif(computer==0 and usernum==-1):
        print("You Win")
    elif(computer==0 and usernum==1):
        print("You Lose")
    elif(computer==-1 and usernum==1):
        print("You Lose")
    else:
        print("ERROR!!")