import qcm
import random

if __name__ == '__main__':
    filename = "QCM4.txt"

# --------------------------------------------- Variable

    questions = qcm.build_questionnaire(filename) # chargement du questionnaire
    random.shuffle(questions) # mélange aléatoirement les questions

# --------------------------------------------- Variable

    print("Choississez votre mode de réponse:\n \t 1 pour le mode évaluatif \n \t 2 pour le mode comparatif")
    utilisateur=int(input("choisissez votre mode : "))
    
    liste_rep = []
    score_comparatif = 0
    score_evaluatif = 0
    
    for q in range(len(questions)):
        print(questions[q][0])
        
        for r in range(len(questions[q][1])):
            print("\t\t" + str(r+1) + " - Réponse possibles" + " : " + questions[q][1][r][0])
            
            if questions[q][1][r][1] == True:
                liste_rep.append(questions[q][1][r][0])
        
        reponse = input("Entrez la bonne réponse : ")
        
        if reponse in liste_rep:
            print('Bonne réponse !')
            score_comparatif += 1
            score_evaluatif += 1
        
        else:
            print("Dommage, mauvaise réponse...")
            if utilisateur == 2:
                score_comparatif -= 1



    if utilisateur == 2:
        print("Votre score avec les malus est de : " + str(score_comparatif) +  "\nVotre score sans les malus est de : " + str(score_evaluatif))
    elif utilisateur == 1:
        print("Votre score est de : " + str(score_evaluatif))
