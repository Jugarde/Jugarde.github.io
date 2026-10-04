def afficher_plateau(plateau):
    """Affiche le plateau de jeu de manière visuelle."""
    print("\n")
    print(f" {plateau[0]} | {plateau[1]} | {plateau[2]} ")
    print("---+---+---")
    print(f" {plateau[3]} | {plateau[4]} | {plateau[5]} ")
    print("---+---+---")
    print(f" {plateau[6]} | {plateau[7]} | {plateau[8]} ")
    print("\n")

def verifier_victoire(plateau, joueur):
    """Vérifie si le joueur actuel a gagné."""
    # Toutes les combinaisons gagnantes possibles (lignes, colonnes, diagonales)
    combinaisons_gagnantes = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Lignes
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Colonnes
        (0, 4, 8), (2, 4, 6)             # Diagonales
    ]
    
    for a, b, c in combinaisons_gagnantes:
        if plateau[a] == plateau[b] == plateau[c] == joueur:
            return True
    return False

def verifier_match_nul(plateau):
    """Vérifie s'il n'y a plus de cases vides."""
    return " " not in plateau

def jouer():
    """Fonction principale du jeu."""
    # On crée une liste de 9 espaces vides pour représenter le plateau
    plateau = [" " for _ in range(9)]
    joueur_actuel = "X"
    jeu_en_cours = True

    print("Bienvenue dans le jeu du Morpion !")
    print("Pour jouer, entrez un chiffre de 1 à 9 correspondant à la case.")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")

    while jeu_en_cours:
        afficher_plateau(plateau)
        
        # Gestion de l'entrée du joueur
        try:
            choix = int(input(f"C'est au tour de {joueur_actuel}. Choisissez une case (1-9) : ")) - 1
            
            if choix < 0 or choix > 8:
                print("⚠️ Ce numéro n'est pas valide. Choisissez entre 1 et 9.")
                continue
            
            if plateau[choix] != " ":
                print("⚠️ Cette case est déjà prise !")
                continue
                
            # On place le symbole
            plateau[choix] = joueur_actuel
            
            # Vérification de la victoire
            if verifier_victoire(plateau, joueur_actuel):
                afficher_plateau(plateau)
                print(f"🎉 Félicitations ! Le joueur {joueur_actuel} a gagné !")
                jeu_en_cours = False
            
            # Vérification du match nul
            elif verifier_match_nul(plateau):
                afficher_plateau(plateau)
                print("🤝 Match nul ! Personne n'a gagné.")
                jeu_en_cours = False
            
            # Changement de joueur
            else:
                joueur_actuel = "O" if joueur_actuel == "X" else "X"

        except ValueError:
            print("⚠️ Erreur : Veuillez entrer un NOMBRE entier.")

if __name__ == "__main__":
    jouer()