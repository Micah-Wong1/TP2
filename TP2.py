"""
Nom = Micah
Gr = 406
Ce code est un jeu de devinette, il choisit un nombre par hasard entre les deux nombres choisis
par l'utilisateur, que l'utilisateur doit ensuite deviner
"""
import random

jeu = True

borne_min = 0
borne_max = 100


def bornes():
    global borne_min
    borne_min = int(input("Entrez la borne minimale du jeu:"))
    global borne_max
    borne_max = int(input("Entrez la borne maximale du jeu:"))
    print(f"J’ai choisi un nombre au hasard entre {borne_min} et {borne_max}, A vous de le deviner...")
    print("Entrez votre essai :")


bornes()
nbr_aleatoire = random.randint(borne_min, borne_max)
nbr_essais = 0


while jeu:
    rep = int(input())

    nbr_essais += 1
    if rep == nbr_aleatoire:
        print("Bravo! Bonne reponse!")
        print(f"Vous avez reussi en {nbr_essais} essais")
        ans = str(input("Voulez-vous rejouer? (y/n)"))
        if ans == "y":
            bornes()
            nbr_aleatoire = random.randint(borne_min, borne_max)
            nbr_essais = 0

        elif ans == "n":
            print("merci et aurevoir")
            jeu = False

    elif rep > nbr_aleatoire:
        print(f"Mauvais reponse, le nombre est plus petit que {rep}")
        print("Entrez une autre essai")

    elif rep < nbr_aleatoire:
        print(f"Mauvais reponse, le nombre est plus grand que {rep}")
        print("Entrez une autre essai")
