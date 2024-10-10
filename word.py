import random
import os

LISTEMOTS = 'listemots.txt'

def get_random_word(min_word_length):
    """Obtenir un mot aléatoire d'une longueur minimale."""
    if not os.path.isfile(LISTEMOTS):
        raise FileNotFoundError(f"Le fichier '{LISTEMOTS}' est introuvable.")

    valid_words = []

    with open(LISTEMOTS, 'r') as f:
        for word in f:
            word = word.strip().lower()
            if len(word) >= min_word_length and '(' not in word and ')' not in word:
                valid_words.append(word)

    if not valid_words:
        raise ValueError("Aucun mot valide trouvé avec la longueur minimale donnée.")

    return random.choice(valid_words)  # Choisir un mot au hasard parmi les mots valides
