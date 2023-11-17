def generer_nombre_aleatoire(seed):
    """Génère un nombre pseudo-aléatoire basé sur la graine (seed)."""
    hash_entier = hash(seed)
    nombre_aleatoire = (hash_entier % 1000) / 1000.0  # Normalisez entre 0 et 1
    return nombre_aleatoire

def algorithme_aleatoire(taille_sequence, graine):
    sequence = []

    for _ in range(taille_sequence):
        nombre_aleatoire = generer_nombre_aleatoire(graine)
        sequence.append(nombre_aleatoire)
        graine += 1  # Changez la graine à chaque itération pour obtenir une séquence différente

    return sequence

# Exemple d'utilisation avec une séquence de 10 nombres aléatoires
taille_sequence = 10
graine = 42  # Vous pouvez changer la graine pour obtenir une séquence différente
sequence_aleatoire = algorithme_aleatoire(taille_sequence, graine)
print("Séquence aléatoire:", sequence_aleatoire)

