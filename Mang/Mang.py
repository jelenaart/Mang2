import random
player_score=0
computer_score=0
choices=["kamen", "bumaga", "noznici"]
print("Kamen davit noznici. Noznici rezut bumagu. Bumaga nakrivaet kamen")
while True:
    try:
        player=input("Viberi: kamen, bumaga, noznici, leave? ==> ")
        if player in choices:
            break
        else:
            print("Poprobui eshe raz!")
    except ValueError:
        print("Neverno vvedeno!")
#while player !="leave":
#    player=player.lower()
#    computer=random.choice(choices)
#    print("Ti vibral "+player+",komputer vibral "+computer+".")
#    if player==computer:
#        print("Ni4ya!")
#    elif player=="kamen":
#        if computer=="noznici":
#            print("Ti viigral!")
#            player_score=player_score+1
#        else:
#            print("pobedil komputer!")
#            computer_score=computer_score+1
#        print("Tvoi s4et: ",player_score, "s4et komputera: ", computer_score)
#    elif player=="bumaga":
#        if computer=="kamen":
#            print("ti pobedil!")
#            player_score=player_score+1
#        else:
#            print("pobedil komputer!")
#            computer_score=computer_score+1
#        print("Tvoi s4et: ",player_score, "s4et komputera: ", computer_score)
#    elif player=="noznici":
#        if computer=="bumaga":
#            print("ti pobedil!")
#            player_score=player_score+1
#        else:
#            print("pobedil komputer!")
#            computer_score=computer_score+1
#        print("Tvoi s4et: ",player_score, "s4et komputera: ", computer_score)
#    else:
#        print("Error! Poprobui eshe raz!")
#    print()                             
