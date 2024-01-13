import random
    
def winner(opponent,player):
   if (opponent == 'r' and player =='s') or (opponent == 'p' and player == 'r') or (opponent =='s' and player == 'p'):
       return True

def play():
    computer = random.choice(['r','p','s'])
    user = input("'r' for rock , 'p' for paper , 's' for sciccor  :\n ")

    if computer == user:
        return 'Tie . Computer choose:'+computer
    
    if winner(computer,user):
        return 'You lose!. Computer choose:'+computer
    
    return 'You Won!. Computer choose:'+computer

print(play())
