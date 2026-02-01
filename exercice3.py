# Exercice 3 : Convertisseur Entier <-> Binaire (CODE À DÉBOGUER)
# Ce programme contient plusieurs erreurs que vous devez corriger.
# NE PAS réécrire le programme de zéro, mais corriger les erreurs existantes.

print("Bienvenue dans le convertisseur Entier <-> Binaire!")

continuer = "O"

while continuer == "O" or continuer == "o":
    print("\n=== MENU ===")
    print("1. Convertir un entier en binaire")
    print("2. Convertir un nombre binaire en entier")
    
    choix = input("Votre choix (1 ou 2): ")
    
    if choix == "1":
        # Conversion entier -> binaire
        nombre = int(input("Entrez un nombre entier positif: "))
        
        if nombre < 0:
            print("Erreur: le nombre doit être positif.")
        else:
            resultat_binaire = ""
            nombre_temp = nombre
            
            if nombre_temp == 0:
                resultat_binaire = "0"
            else:
                while nombre_temp > 0:
                    reste = nombre_temp % 2
                    resultat_binaire = str(reste) + resultat_binaire
                    nombre_temp = nombre_temp // 2  # Division entière nécessaire
            
                print(f"{nombre} en binaire = {resultat_binaire}")
    
    elif choix == "2":
        # Conversion binaire -> entier
        binaire = input("Entrez un nombre binaire: ")
        
        # Vérifier que c'est bien un nombre binaire (que des 0 et des 1)
        valide = True
        for bit in binaire:
            if bit != "0" and bit != "1":
                valide = False
        
        if not valide:
            print("Erreur: ce n'est pas un nombre binaire valide.")
        else:
            resultat_entier = 0
            puissance = 0
            position = len(binaire) - 1
            
            while position >= 0:
                bit = int(binaire[position])
                resultat_entier += bit * (2 ** puissance)
                puissance += 1
                position -= 1
            
            print(f"{binaire} en entier = {resultat_entier}")
    
    else:
        print("Choix invalide. Veuillez entrer 1 ou 2.")
    
    continuer = input("\nVoulez-vous faire une autre conversion (O/n)? ")

print("Au revoir !")
