
# Demander un mot à l'utilisateur
mot = input("Tape un mot : ")

# Créer un dictionnaire vide
dictionnaire = {}

# Parcourir chaque lettre du mot avec son index
for index in range(len(mot)):
    lettre = mot[index]

    # Si la lettre est déjà dans le dictionnaire, ajouter l'index à la liste
    if lettre in dictionnaire:
        dictionnaire[lettre].append(index)
    else:
        # Sinon, créer une nouvelle entrée avec l'index dans une liste
        dictionnaire[lettre] = [index]

# Afficher le dictionnaire final
print(dictionnaire)