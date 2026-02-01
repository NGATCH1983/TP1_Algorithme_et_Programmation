# Exercice 1 : Calculateur de pourboire et partage d'addition
# IFT-1004 - Travail pratique #1 - Hiver 2026
#
# Écrivez votre programme ci-dessous.
# Consultez l'énoncé pour les spécifications détaillées.

print("#############################################################")
print("      Calculateur de pourboire et partage d'addition         ")
print("#############################################################")
TPS = 0.05
TVQ = 0.09975
pourcentage_minimum = 0
pourcentage_maximum = 100
effectif_minimum = 1
montant_null = 0

continuer = "o"

while continuer == "o" or continuer == "O":

    # Montant avant taxes
    montant = float(input("Entrer le montant de la facture avant taxes ($): "))
    while montant <= montant_null:
        print("Erreur : Le montant doit être supérieur à 0.")
        montant = float(input("Entrer le montant de la facture avant taxes ($): "))

    # Pourboire
    pourcentage = float(input("Entrer le pourcentage de pourboire désiré (%): "))
    while pourcentage <= pourcentage_minimum or pourcentage > pourcentage_maximum:
        print("Erreur : La valeur du pourboire doit être entre 0.0 et 100 ")
        pourcentage = float(input("Entrer le pourcentage de pourboire désiré (%): "))

    # Nombre de personnes
    personnes = int(input("Entrer le nombre de personnes pour diviser l'addition: "))
    while personnes <= effectif_minimum:
        print("Erreur : Le nombre de personnes doit être d'au moins une personne.")
        personnes = int(input("Entrer le nombre de personnes pour diviser l'addition: "))

    # Calculs
    montant_tps = montant * TPS
    montant_tvq = (montant + montant_tps) * TVQ
    sous_total_apres_taxes = montant + montant_tps + montant_tvq
    pourboire = montant * pourcentage / 100
    total = sous_total_apres_taxes + pourboire
    montant_par_personne = total / personnes

    # Affichage
    print("==================== RÉCAPITULATIF ====================")
    print(f"Sous -total (avant taxes ): {montant:.2f} $")
    print(f"TPS (5%): {montant_tps:.2f} $")
    print(f"TVQ (9.975%): {montant_tvq:.2f} $")
    print(f"Sous -total (après taxes ): {sous_total_apres_taxes:.2f} $")
    print(f"Pourboire ({pourcentage:.1f}%): {pourboire:.2f} $")
    print("--------------------------------------------------------")
    print(f"TOTAL: {total:.2f} $")
    print("========================================================")

    if personnes > effectif_minimum:
        print(f"Divisé entre {personnes} personnes:")
        print(f"Montant par personne: {montant_par_personne:.2f} $")

    continuer = input("Voulez -vous faire un autre calcul (O/n)? ")

print("Merci d'avoir utilisé le calculateur. Bonne soirée!")
