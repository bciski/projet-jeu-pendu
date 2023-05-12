 score = 0
    print("Tu as 6 vies")
    print("\n")
    vie = 6
    
    while play == 1 :
        vie = 6
        mot=(liste_mots[random.randint(0,21)])
        longueur=len(mot)
        barre=["_ "]
        barre=barre*longueur
        grandeur=longueur
