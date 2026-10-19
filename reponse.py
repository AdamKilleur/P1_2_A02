import qcm
def projet():
    # Initialisation
    score=0
    mode1="tapez 1 pour le mode sans malus +1 pour la bonne réponse et 0 pour la mauvaise réponse ou pour une absence"
    mode2="tapez 2 pour le mode avec malus +1 pour la bonne réponse , -1 pour la mauvaise réponse et 0 pour une absence"
    print(mode1)
    print(mode2)
    utilisateur=int(input("choisissez votre mode : "))

    # Fichier question à modifier:
    fichier="QCM2.txt"
    questions=qcm.build_questionnaire(fichier)




    print("Le questionnaire est une liste de questions.")
    """on lit et on pose les questions une par une """
    for q in range(len(questions)):
        print("\tQuestion " + str(q+1) + ": \"" + questions[q][0] + "\"")
        choices=questions[q][1]
        for r in range(len(choices)):
            texte_choices=choices[r][0]
            print("   " +str(r+1) +". " + texte_choices)
        saisie=int(input("votre reponse : "))
        choices_utilisateur=choices[saisie-1]
        correct=choices_utilisateur[1]
        """on verifie si c'est correcte ou pas"""
        if correct==True:
            print('bonne reponse')
            score +=1
        else: 
            print('mauvaise réponse')
            reponses=[]
            for r in range(len(choices)):
                if choices[r][1]==True:
                    reponses.append (choices[r][0])
            """on donne une explication suite à la mauvaise réponse"""
            print('la bonne réponse était:')
            for texte in reponses:
                print(texte)
            """on calcule le score par rapport au mode choisi par l'utilisateur"""
            if utilisateur==1:
                score +=0
            else:
                score -=1

    """on affiche le score final"""
    print("fin du quiz votre score est de :",score)
projet()
             


        
        

          
