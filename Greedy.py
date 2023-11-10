def greedy(matrice):
    if not matrice:
        return 0, (0, 0, 0, 0)  

    ligne = len(matrice)
    colonne = len(matrice[0])
    resultat = 0, (0, 0, 0, 0)  
    maximum = float('-inf')

    for x in range(colonne):
        temp = [0] * ligne  
        for y in range(x, colonne):  
            for z in range(ligne):
                temp[z] += matrice[z][y]

            somme = 0
            debut = 0
            for z in range(ligne):
                somme += temp[z]
                if somme > maximum:
                    maximum = somme
                    resultat = maximum, (debut, x, z, y)  
                if somme < 0:
                    somme = 0
                    debut = z + 1

    return resultat  

matrice_A = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

maximum, (debut, x, z, y) = greedy(matrice_A)
print("Max sum : ", maximum)


sousMatrice = []
for i in range(debut, z + 1):
    ligne = []
    for j in range(x, y + 1):
        ligne.append(matrice_A[i][j])
    sousMatrice.append(ligne)

for row in sousMatrice:
    print(row)
