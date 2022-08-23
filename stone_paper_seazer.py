from playsound import playsound
import random
def gameWin(comp, you):
    if comp == you:
        return None
    elif comp== 'r':
        if  you=='s':
            return False
        elif you=='p':
            return True
    elif comp== 'p':
        if  you=='r':
            return False
        elif you=='s':
            return True
    elif comp== 's':
        if  you=='p':
            return False
        elif you=='r':
            return True



print("comp Turn: Rock(r) Paper(p) or scissor(s)")
randNo = random.randint(1, 3)
if randNo == 1 :
    comp = 'r'
elif randNo == 2 :
    comp = 'p'
elif randNo == 3 :
    comp = 's'
you = input("your Turn: Rock(r) Paper(p) or scissor(s)? ")

a = gameWin(comp, you)
print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is tie!")
    # playsound('Rushi2.mpeg')
elif a :
    print("You Win ! ! !")
    playsound('Rushi2.mpeg')
else:
    print("You lose.....")
    # playsound('Rushi2.mpeg')