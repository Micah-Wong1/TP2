"""
Nom = Micah
Gr = 406
Ce code est un jeu de devinette, il choisit un nombre par hasard entre les deux nombres (choisis
par l'utilisateur ou non), que l'utilisateur doit ensuite deviner
"""
import random

jeu = True

borne_min = 0
borne_max = 100


def bornes(min_nbr, max_nbr):
    global borne_min
    global borne_max
    reply = str(input("Voulez-vous choisir la difficulte?(y/n)"))
    if reply == "y":
        borne_min = int(input("Entrez la borne minimale du jeu:"))
        borne_max = int(input("Entrez la borne maximale du jeu:"))
        print(f"J’ai choisi un nombre au hasard entre {borne_min} et {borne_max}, A vous de le deviner...")
        print("Entrez votre essai :")

    elif reply == "n":
        borne_min = min_nbr
        borne_max = max_nbr
        print(f"J’ai choisi un nombre au hasard entre {borne_min} et {borne_max}, A vous de le deviner...")
        print("Entrez votre essai :")


bornes(0, 100)
nbr_aleatoire = random.randint(borne_min, borne_max)
nbr_essais = 0


while jeu:
    reponse = int(input())

    nbr_essais += 1
    if reponse == nbr_aleatoire:
        print("Bravo! Bonne reponse!")
        print(f"Vous avez reussi en {nbr_essais} essais")
        answer = str(input("Voulez-vous rejouer? (y/n)"))

        if answer == "y":
            bornes(0, 100)
            nbr_aleatoire = random.randint(borne_min, borne_max)
            nbr_essais = 0

        elif answer == "n":
            print("merci et aurevoir")
            jeu = False

    elif reponse > nbr_aleatoire:
        print(f"Mauvais reponse, le nombre est plus petit que {reponse}")
        print("Entrez une autre essai :")

    elif reponse < nbr_aleatoire:
        print(f"Mauvais reponse, le nombre est plus grand que {reponse}")
        print("Entrez une autre essai :")
