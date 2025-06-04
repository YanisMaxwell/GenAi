
liste = [("name", "Elie"), ("job", "Instructor")]

dictionnaire = dict(liste)

print(dictionnaire)

########################################
lettre_debut = ["CA", "NJ", "RI"]
ville = ["California", "New Jersey", "Rhode Island"]

etat_dict = {}

for i in range(len(lettre_debut)):
    etat_dict[lettre_debut[i]] = ville[i]

print(etat_dict)
##########################################
voyelles = ['a', 'e', 'i', 'o', 'u']
dictionnaire = {}

for lettre in voyelles:
    dictionnaire[lettre] = 0

print(dictionnaire)

##################################

alphabet_dict = {}

for i in range(26):  
    lettre = chr(65 + i)  
    alphabet_dict[i + 1] = lettre 

print(alphabet_dict)
