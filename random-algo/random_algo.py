def generer_nombre_aleatoire(seed):
    """G�n�re un nombre pseudo-al�atoire bas� sur la graine (seed)."""
    hash_entier = hash(seed)
    nombre_aleatoire = (hash_entier % 1000) / 1000.0  # Normalisez entre 0 et 1
    return nombre_aleatoire

def algorithme_aleatoire(taille_sequence, graine):
    sequence = []

    for _ in range(taille_sequence):
        nombre_aleatoire = generer_nombre_aleatoire(graine)
        sequence.append(nombre_aleatoire)
        graine += 1  # Changez la graine � chaque it�ration pour obtenir une s�quence diff�rente

    return sequence

# Exemple d'utilisation avec une s�quence de 10 nombres al�atoires
taille_sequence = 10
graine = 42  # Vous pouvez changer la graine pour obtenir une s�quence diff�rente
sequence_aleatoire = algorithme_aleatoire(taille_sequence, graine)
print("S�quence al�atoire:", sequence_aleatoire)

