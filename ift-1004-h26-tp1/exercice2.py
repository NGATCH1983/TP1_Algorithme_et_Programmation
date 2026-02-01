# Exercice 2 : Dessin d'un sablier
# IFT-1004 - Travail pratique #1 - Hiver 2026
#
# Écrivez votre programme ci-dessous.
# Consultez l'énoncé pour les spécifications détaillées.
asterisk = '*'
vide =' '
largeur_minimum = 3
ajustement = 1
pas_normal = 2
pas_inverse = -2
diviseur = 2
reste = 0
seuil = 0
print("=== Dessin d'un sablier ===")
largeur_de_la_base = int(input("Entrer la taille du sablier (largeur de la base, minimum 3): "))

if largeur_de_la_base <= largeur_minimum:
    print("Taille incorrecte")
else:
    if largeur_de_la_base % diviseur == reste:
        largeur_de_la_base += ajustement

    # Triangle inversé
    for i in range(largeur_de_la_base, seuil, pas_inverse):
        espaces = (largeur_de_la_base - i) // diviseur
        print(vide * espaces + asterisk * i)

    # Triangle normal
    for i in range(largeur_minimum, largeur_de_la_base + ajustement, pas_normal):
        espaces = (largeur_de_la_base - i) // diviseur
        print(' ' * espaces + asterisk * i)

