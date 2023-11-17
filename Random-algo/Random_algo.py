import random

def generer_matrice_aleatoire_entiers(taille_m, taille_n):
    random.seed()  # Utilise la graine basée sur l'heure actuelle
    matrice = []

    for _ in range(taille_m):
        ligne = [random.randint(0, 100) for _ in range(taille_n)]
        matrice.append(ligne)

    return matrice

# Exemple d'utilisation avec une matrice de dimensions 3x3
taille_m = 3
taille_n = 3
matrice_aleatoire_entiers = generer_matrice_aleatoire_entiers(taille_m, taille_n)

# Afficher la matrice aléatoire d'entiers
for ligne in matrice_aleatoire_entiers:
    print(ligne)
