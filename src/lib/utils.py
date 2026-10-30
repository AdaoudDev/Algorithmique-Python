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