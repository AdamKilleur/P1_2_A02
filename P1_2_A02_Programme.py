import qcm
import random

if __name__ == '__main__':
    filename = input("Veuillez insérer le nom complet de votre fichier avec le format (Exemple : .txt) \n ")

    # --------------------------------------------- Variable

    questions = qcm.build_questionnaire(filename)  # chargement du questionnaire

    random.shuffle(questions)  # mélange aléatoirement les questions

    score_comparatif = 0
    
    score_evaluatif = 0

    # --------------------------------------------- Code

    pseudo = ""
    while pseudo == "":
        pseudo = input("Veuillez entrer ci-dessous votre pseudo : ")

    print("Bonjour " + pseudo + ", bienvenue dans le questionnaire QCM !\n"
    "Vous allez devoir répondre à une série de questions à choix multiples.\n"
    "Pour chaque question, entrez la réponse complète que vous croyez correcte.\n"
    "Bonne chance ! \n ")

    print("Avant de commencer le QCM, veuillez choisir votre mode de cotation:\n \t "
            "1 pour le mode évaluatif \n \t " 
            "2 pour le mode comparatif \n ")


    utilisateur = (input("Choisissez votre mode : "))
    assert utilisateur == int, "Veuillez entrer un chiffre entier entre 1 et 2"
    utilisateur = int(utilisateur)
    assert utilisateur != 1 or 2, "Veuillez entrer un chiffre entier entre 1 et 2"


# = Imprime la question avec ses propositions
    for q in range(len(questions)):
        liste_rep = []
        print(questions[q][0])
        choices = questions[q][1]
        random.shuffle(choices)
        for r in range(len(choices)):
            print("\t\t" + str(r + 1) + " - Réponse possibles" + " : " + choices[r][0])

# ========= Création d'une liste contenant les bonnes réponses
            if choices[r][1] == True:
                liste_rep.append(questions[q][1][r][0])

        reponse = input("Entrez la bonne réponse : ")

# ===== Met à jour le score en fonction du mode de cotation
        if reponse in liste_rep:
            print('Bonne réponse !')
            score_comparatif += 1
            score_evaluatif += 1

        else:
            print("Dommage, mauvaise réponse...")
            if utilisateur == 2:
                score_comparatif -= 1

# ===== Imprime un feedback s'il est présent
        for i in range(len(choices)):
            if reponse == choices[i][0]:
                feedback = choices[i][2]
                if feedback != '':
                    print('Feedback : ' + choices[i][2])

# = Imprime le score en fonction du mode de cotation
    if utilisateur == 2:
        print("Votre score avec les malus est de : " + str(score_comparatif) + "\nVotre score sans les malus est de : " + str(score_evaluatif))
    
    elif utilisateur == 1:
        print("Votre score est de : " + str(score_evaluatif))