import random 
print(''' Welcome to the Rock,Paper and Scissor game. THe rule of the game is shown below:-
1. rock  vs scissor---> rock win
2. scissor vs paper--->  scissor win 
3. paper vs rock---> paper win''')


def game(computer, player):
    if computer == player:
        return None #tie
    elif computer == 'R':
        if player == 'P':
            return True  #winner
        elif player == 'S':
            return False #lose

    elif computer == 'P':
        if player == 'S':
            return True
        elif player == 'R':
            return False

    elif computer == 'S':
        if player == 'R':
            return True
        elif player == 'P':
            return False


computer = print("Computer turn: Rock(R), Paper(P) and Scissor(S)")
randomNum = random.randint(1, 3)
# print(randomNum)
# 1-->rock
# 2-->Paper
# 3-->scissor

if randomNum == 1:
    computer = 'R'
elif randomNum == 2:
    computer = 'P'
elif randomNum == 3:
    computer = 'S'


player = input("Player turn: Rock(R), Paper(P) and Scissor(S) ")
i=game(computer,player)

if i==None:
    print("game is tie!")
elif i==True:
    print("You win")
elif i==False:
    print("computer Win!")

print(f"computer choose { computer}")
print(f"player choose { player}")