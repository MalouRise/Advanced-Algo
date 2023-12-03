import time

def extract_submatrix(matrix, debut, z, x, y):
    sousMatrice = []
    for i in range(debut, z + 1):
        ligne = []
        for j in range(x, y + 1):
            ligne.append(matrix[i][j])
        sousMatrice.append(ligne)
    return sousMatrice

def display_results(matrix, debut, z, x, y, start_time, stop_time, maximum):

    elapsed_time = "{:.7f}".format(stop_time - start_time)

    print("Max sum : ", maximum)
    print("Time to execute : ", elapsed_time, " seconds")

    sousMatrice = extract_submatrix(matrix, debut, z, x, y)

    for row in sousMatrice:
        print(row)

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

matrice_1 = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

matrice_2 = [
    [1, 2, -1, -4, -20, 5, 3, 2, 7, 8],
    [-8, -3, 4, 2, 1, 9, 6, -2, 1, 0],
    [3, 8, 10, 1, 3, -40, 7, 5, 1, 2],
    [-4, -1, 1, 7, -6, 0, 3, -9, 6, 4],
    [2, -7, 5, 8, 2, -1, 4, -3, 2, 1],
    [-6, 3, -2, 1, 5, 7, 0, 2, -8, -3],
    [4, 2, -50, 6, 3, 1, 9, -2, 0, 8],
    [0, 1, -3, 9, 4, 2, -7, 6, 1, -5],
    [-2, 4, 6, -1, 0, 8, -3, 7, -4, 2],
    [5, 7, -8, 2, 1, -4, 6, 3, -5, -1]
]

matrice_3 = [
    [1, -20, 3],
    [4, 5, 6],
    [7, 8, 9]
]



start = time.perf_counter()
maximum, (debut, x, z, y) = greedy(matrice_1)
stop = time.perf_counter()

display_results(matrice_1, debut, z, x, y, start, stop, maximum)


start = time.perf_counter()
maximum, (debut, x, z, y) = greedy(matrice_2)
stop = time.perf_counter()

display_results(matrice_2, debut, z, x, y, start, stop, maximum)

start = time.perf_counter()
maximum, (debut, x, z, y) = greedy(matrice_3)
stop = time.perf_counter()

display_results(matrice_3, debut, z, x, y, start, stop, maximum)


