import qcm
import random
import os

if __name__ == '__main__':

    # ========================================= La partie de code permet de lire le dossier où se trouve le .py
    # ========================================= Afin que le client puisse inscrire le nom de son fichier .txt

    inputphrasefilename = "Veuillez insérer le nom complet de votre fichier avec le format (Exemple : .txt) \n "
    filename = input(inputphrasefilename) or "qcm.txt"
    while not os.path.exists(filename):
        filename = input(inputphrasefilename + " Le nom du fichier que vous avez inscrit n'éxiste pas.\n")

    # ========================================= La partie où sont répertoriées les différentes variables, telles que :
    # ========================================= La variable contenant les questions (provenant du fichier .txt)
    # ========================================= La variable permettant de mélanger les différentes questions
    # ========================================= Les deux variables nécessaires au calcul des deux scores différents

    questions = qcm.build_questionnaire(filename)  # chargement du questionnaire

    random.shuffle(questions)  # mélange aléatoirement les questions

    score_comparatif = 0

    score_evaluatif = 0

    # ========================================= La partie du code qui correspond au début du QCM permet à l'utilisateur de saisir un pseudonyme.
    # ========================================= Elle permet également d'expliquer les règles du QCM.
    # ========================================= Elle permet aussi à l'utilisateur de choisir son mode de cotation.

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

    # ========================================= Cette partie permet d'afficher les différentes questions dans un ordre aléatoire.
    # ========================================= Elle permet également d'afficher les propositions de réponse associées à chaque question.

    for q in range(len(questions)):
        liste_rep = []
        print(questions[q][0])
        choices = questions[q][1]
        random.shuffle(choices)
        for r in range(len(choices)):
            print("\t\t" + str(r + 1) + " - Réponse possibles" + " : " + choices[r][0])

            # ========================================= Cette partie permet d'identifier les bonnes réponses et de les ajouter à une liste.
            # ========================================= Elle demande ensuite à l'utilisateur de saisir le numéro de la bonne réponse.
            # ========================================= Elle vérifie que la saisie contient uniquement des chiffres avant de la convertir en entier.

            if choices[r][1] == True:
                liste_rep.append(r)

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