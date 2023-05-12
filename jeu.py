 while vie!=0 and grandeur!=0 :
            lettre_choisi = input("Choisi une lettre  ")
            print("\n")
            if lettre_choisi in mot :
                print("Bravo!")
                if lettre_choisi in barre:
                    print ("Tu l'as déja dit !")
                    resultat = ' '.join(barre)
                    print(resultat)
                else:
                    position=int(mot.index(lettre_choisi))
                    barre.pop(position)
                    barre.insert(position,lettre_choisi)
                    resultat = ' '.join(barre)
                    print(resultat)
                    grandeur=grandeur-1
                    
                                else:
                print("Raté")
                if grandeur==longueur :
                    print(longueur*"_ ")
                else:
                    print (resultat)
                vie=vie-1
                print("Il te reste",vie,"vies")
                print("\n")
