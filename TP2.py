import random

jeu = True

nbr_aleatoire = random.randint(0, 10)


print("J’ai choisi un nombre au hasard entre 0 et 1000, A vous de le deviner...")
print("Entrez votre essai :")

nbr_essais = 0
while jeu:
    rep = int(input())

    nbr_essais += 1
    if rep == nbr_aleatoire:
        print("Bravo! Bonne reponse!")
        print(f"Vous avez reussi en {nbr_essais} essais")
        ans = str(input("Voulez-vous rejouer? (y/n)"))
        if ans == "y":
            print("ok, entrez votre essai:")

        elif ans == "n":
            print("merci et aurevoir")
            jeu = False

    elif rep > nbr_aleatoire:
        print(f"Mauvais reponse, le nombre est plus petit que {rep}")
        print("Entrez une autre essai")

    elif rep < nbr_aleatoire:
        print(f"Mauvais reponse, le nombre est plus grand que {rep}")
        print("Entrez une autre essai")
