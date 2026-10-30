def horloge_lamport(c1, c2):
    """
    Fait une comparaison de c1 par rapport à c2 selon l'algorithme de Lamport.

    Args:
        c1 timestamp1
        c2 timestamp2

    Returns:
        int: la valeur de l'horloge après la comparaison
    """
    if c1[0] < c2[0]:
        return c1[0]+1
    else:
        return c2[0]+1
def delai_message(delai_max, graine):
    """
    Génère un délai aléatoire pour la livraison d'un message.

    Args:
        delai_max (int): le délai maximum en millisecondes
        graine (int): la graine pour le générateur de nombres aléatoires

    Returns:
        int: un délai aléatoire compris entre 0 et delai_max
    """
    import random
    random.seed(graine)
    return random.randint(0, delai_max)

def verifier_voisins(processus, destinataire):
    """
    Vérifie si le destinataire est un voisin du processus.

    Args:
        processus (Processus): le processus qui envoie le message
        destinataire (str): le nom du destinataire

    Returns:
        bool: True si le destinataire est un voisin, False sinon
    """
    return destinataire in processus.voisins