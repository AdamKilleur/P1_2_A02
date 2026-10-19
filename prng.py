import qcm
import random

if __name__ == '__main__':
    filename = "QCM.txt"

# --------------------------------------------- Variable
    questions = qcm.build_questionnaire(filename) # chargement du questionnaire
    random.shuffle(questions) # mélange aléatoirement les questions
# --------------------------------------------- Variable

    for q in range(len(questions)):
        print(questions[q][0])
        for r in range(len(questions[q][1])):
            print("\t\t" + str(r+1) + " - Réponse possibles" + " : " + questions[q][1][r][0])

        reponse = input("Entrez la bonne réponse : ")
