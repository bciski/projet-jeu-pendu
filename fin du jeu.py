 if vie==0 :
            print("dommage c’est PERDU")
        elif grandeur==0 :
            print("GG! tu as gagné!")
            score=score+5
            print("Tu a gagné 5 points !")
        replay=int(input("Tape 1 pour une nouvelle partie, et sur 2 si tu veux quitter "))
        if replay != 1 :
            break
    print(prénom,"vous avez un score de ",score)
