
humanYears = int(input("Entrez le nombre d'années humaines : "))

if humanYears == 1:
    catYears = 15
    dogYears = 15

elif humanYears == 2:
    catYears = 15 + 9
    dogYears = 15 + 9

else:
    catYears = 15 + 9 + 4 
    dogYears = 15 + 9 + 5 

print([humanYears, catYears, dogYears])

