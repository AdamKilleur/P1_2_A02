import qcm
import random

if __name__ == '__main__':
    filename = "QCM.txt"

    # --------------------------------------------- Variable

    questions = qcm.build_questionnaire(filename)  # chargement du questionnaire

    random.shuffle(questions)  # mélange aléatoirement les questions

    liste_rep = []

    score_comparatif = 0
    
    score_evaluatif = 0

    # --------------------------------------------- Code

    print("Choississez votre mode de réponse:\n \t 1 pour le mode évaluatif \n \t 2 pour le mode comparatif")
    utilisateur = int(input("choisissez votre mode : "))


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

# ===== Regarde s'il y a un feedback et le print si et uniquement s'il est présent
        for i in range(len(choices)):
            if reponse == choices[i][0]:
                feedback = choices[i][2]
                if feedback != '':
                    print('Feedback :' + choices[i][2])

# = Imprime le score en fonction du mode de cotation
    if utilisateur == 2:
        print("Votre score avec les malus est de : " + str(
            score_comparatif) + "\nVotre score sans les malus est de : " + str(score_evaluatif))
    
    elif utilisateur == 1:
        print("Votre score est de : " + str(score_evaluatif))
