import qcm
import random
import os

if __name__ == '__main__':

    # ========================================= L'utilisateur entre le nom de son fichier .txt.
    # ========================================= Le programme vérifie qu'il existe avant de continuer.

    inputphrasefilename = "Veuillez insérer le nom complet de votre fichier avec le format (Exemple : .txt) \n "
    filename = input(inputphrasefilename) or "qcm.txt"
    while not os.path.exists(filename):
        filename = input(inputphrasefilename + " Le nom du fichier que vous avez inscrit n'éxiste pas.\n")

    # ========================================= Les questions du fichier sont chargées puis mélangées aléatoirement.
    # ========================================= Les deux scores (avec et sans malus) commencent à zéro.

    questions = qcm.build_questionnaire(filename)  # chargement du questionnaire

    random.shuffle(questions)  # mélange aléatoirement les questions

    score_comparatif = 0

    score_evaluatif = 0

    # ========================================= Début du QCM : l'utilisateur entre son pseudo et lit les consignes.
    # ========================================= Il choisit ensuite son mode de cotation (1 ou 2).

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

    utilisateur = input("Choisissez votre mode : ")
    while utilisateur not in ("1", "2"):
        utilisateur = input("Choix invalide. Entrez 1 ou 2 : ")
    utilisateur = int(utilisateur)

    # ========================================= Les questions s'affichent une par une, avec leurs propositions.
    # ========================================= Les propositions sont mélangées et numérotées.

    for q in range(len(questions)):
        liste_rep = []
        print(questions[q][0])
        choices = questions[q][1]
        random.shuffle(choices)
        for r in range(len(choices)):
            print("\t\t" + str(r + 1) + " - Réponse possibles" + " : " + choices[r][0])

            # ========================================= Si la proposition est bonne, son numéro est gardé dans liste_rep.

            if choices[r][1] == True:
                liste_rep.append(r)

        # ========================================= L'utilisateur tape le numéro de sa réponse.
        # ========================================= Tant que ce n'est pas un nombre, le programme redemande.

        reponse = input("Entrez le numéro de la bonne réponse : ")
        while reponse.isdigit() == False:
            if reponse.isdigit() == True:
                reponse = int(reponse)
            else:
                reponse = input("Entrez le numéro de la bonne réponse : ")
        reponse = int(reponse)

        # ========================================= Cette partie permet de mettre à jour le score en fonction du mode de cotation préalablement choisi par l'utilisateur.

        if reponse - 1 in liste_rep:
            print('Bonne réponse !')
            score_comparatif += 1
            score_evaluatif += 1

        else:
            print("Dommage, mauvaise réponse...")
            if utilisateur == 2:
                score_comparatif -= 1

            # ========================================= Cette partie permet d'afficher un commentaire sur la réponse donnée par l'utilisateur, si un commentaire est disponible.

            for i in range(len(choices)):
                if reponse - 1 == i:
                    feedback = choices[i][2]
                    if feedback != '':
                        print('Feedback : ' + feedback + "\n")

    # ========================================= Cette partie permet d'afficher le score de l'utilisateur selon le mode de cotation sélectionné.

    if utilisateur == 2:
        print("Votre score avec les malus est de : " + str(
            score_comparatif) + "\nVotre score sans les malus est de : " + str(score_evaluatif))

    elif utilisateur == 1:
        print("Votre score est de : " + str(score_evaluatif))
