import qcm
import random

if __name__ == '__main__':
    filename = "QCM.txt"

# --------------------------------------------- Variable

    questions = qcm.build_questionnaire(filename) # chargement du questionnaire

    random.shuffle(questions) # mélange aléatoirement les questions

    score = 0

    liste_rep = []

# --------------------------------------------- Code
    print("Choississez votre mode de réponse:\n \t 1 pour celui sans malus \n \t 2 pour celui avec malus")
    utilisateur = int(input("Choisissez votre mode : "))

    for q in range(len(questions)):
        print(questions[q][0])
        for r in range(len(questions[q][1])):
            print("\t\t" + str(r+1) + " - Réponse possibles" + " : " + questions[q][1][r][0])
            if questions[q][1][r][1] == True:
                liste_rep.append(questions[q][1][r][0])

        reponse = input("Entrez la bonne réponse : ")
        if reponse in liste_rep:
            print('Bonne réponse !')
            score += 1
        else:
            print("Dommage, mauvaise réponse...")
            if utilisateur == 2 :
                score -= 1
    print("Votre score est de : " + str(score))