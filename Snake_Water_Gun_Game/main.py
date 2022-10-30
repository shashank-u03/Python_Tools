import random
from re import T

def game(a,b): # here a is computer
    if(a=='s'):
        if(b=='w'):
            return True
        if(b=='g'):
            return False
        else:
            return None
    
    if(a=='w'):
        if(b=='s'):
            return False
        if(b=='g'):
            return True
        else:
            return None
    
    if(a=='g'):
        if(b=='s'):
            return True
        if(b=='w'):
            return False
        if(b=='g'):
            return None


print("Computer Turn: Snake(s) Water(w) or Gun(g)?")
randNo=random.randint(1,3)
# print(randNo)

if randNo==1:
    comp = 's'
elif randNo==2:
    comp = 'w'
else:
    comp='g'

b=input("Your Turn: Snake(s) Water(w) or Gun(g)?")

ans=game(comp,b)
if(ans==True):
    print("You lose")
elif(ans==False):
    print("You won")
else:
    print("No one win")