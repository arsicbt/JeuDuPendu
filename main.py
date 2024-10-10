"""Main - jeu du pendu"""

from string import ascii_lowercase
from word import get_random_word


def get_num_attempts():
    """obtenir les tentatives incorrectes"""
    while True:
        num_attempts = input("De combien d'essaies as-tu besoin ? [1-25] ")
        try:
            num_attempts = int(num_attempts)
            if 1 <= num_attempts <= 25:
                return num_attempts
            else:
                print("{0} n'est pas compris entre 1 et 25 essais :".format(num_attempts))
        except ValueError:
            print("{0} n'est pas un nombre valide.".format(num_attempts))


def get_min_word_length():
    """Obtenir la longueur de mot minimale pour le jeu"""
    while True:
        min_word_length = input("Choisis la taille de ton mot : [4-16] ")
        try:
            min_word_length = int(min_word_length)  # Conversion en entier
            if 4 <= min_word_length <= 16:
                return min_word_length
            else:
                print("{0} n'est pas compris entre 4 et 16".format(min_word_length))
        except ValueError:
            print("{0} n'est pas un nombre valide.".format(min_word_length))


def get_display_word(word, idxs):
    """Obtenir le mot à afficher"""
    if len(word) != len(idxs):
        raise ValueError("La longueur du mot et son index ne sont pas identiques")
    displayed_word = ''.join([letter if idxs[i] else '*' for i, letter in enumerate(word)])
    return displayed_word.strip()


def get_next_letter(remaining_letters):
    """Obtenir la saisie de la lettre par le joueur"""
    if len(remaining_letters) == 0:
        raise ValueError("Il ne reste plus de lettres à jouer...")
    while True:
        next_letter = input("Choisissez votre nouvelle lettre : ").lower()
        if len(next_letter) != 1:
            print("{0} n'est pas une lettre seule !".format(next_letter))
        elif next_letter not in ascii_lowercase:
            print("{0} n'est pas une lettre !".format(next_letter))
        elif next_letter not in remaining_letters:
            print("{0} tu as déjà joué cette lettre !".format(next_letter))
        else:
            remaining_letters.remove(next_letter)
            return next_letter


def play_jeudupendu():
    """Jouez au Jeu du Pendu.
    A la fin du jeu, retour si le joueur souhaite y rejouer."""
    
    # laisser le joueur choisir la difficulté
    print("Démarrage du Jeu du Pendu...")
    attempts_remaining = get_num_attempts()
    min_word_length = get_min_word_length()
    
    # choix du mot au hasard
    print("Choix d'un mot...")
    word = get_random_word(min_word_length)
    print()
    
    # initialisation des variables du jeu            
    idxs = [False] * len(word)
    remaining_letters = set(ascii_lowercase)
    wrong_letters = []
    word_solved = False
    
    # boucle principale du jeu
    while attempts_remaining > 0 and not word_solved: 
        # affichage de l'état actuel du jeu
        print("Mot : {0}".format(get_display_word(word, idxs)))
        print("Tentatives ratées : {0}".format(' '.join(wrong_letters)))
        
        # obtenir la tentative suivante du joueur
        next_letter = get_next_letter(remaining_letters)
        
        # vérifier si la lettre choisie figure dans le mot secret 
        if next_letter in word: 
            # tentative fructueuse 
            print("{0} est dans le mot !".format(next_letter))
            # affichage des lettres correctes 
            for i in range(len(word)):
                if word[i] == next_letter:
                    idxs[i] = True
        else:
            # tentative infructueuse
            print("Raté ! {0} n'est pas dans le mot".format(next_letter))
            attempts_remaining -= 1
            wrong_letters.append(next_letter)
        
        # vérifier si le mot entier a été correctement trouvé
        if False not in idxs:
            word_solved = True
    
    # fin du jeu et affichage du mot secret
    print("Le mot secret est {0}".format(word))
    
    # info victoire ou défaite 
    if word_solved:
        print("Bravo, tu as gagné !!!")   
    else: 
        print("Perdu...")      
        
    # demande au joueur s'il veut rejouer 
    try_again = input("Une autre partie ? ;) [oui/non] ")       
    return try_again.lower() == 'oui'
    
    
if __name__ == '__main__':
    while play_jeudupendu():
        print()
