# def first_fuction():
#     print("Hello World")

# first_fuction()

# def add_two_numbers():
#     return 5+5  ### lorsque return est utilisé il faut le stock dans une variable au moment d'appeler la fonction 

# variable = add_two_numbers()  ## Création de la "variable" pour stocker le resulat de return 
# print(variable) # affiche le resultat de la variable 



# def check_weather():
#     weather = "sunny"
#     if weather == "sunny":
#         print(" It's sunny day! Enjoy! ")
#     else:
#         print("it might Rain...")
        
# check_weather()


#########################################################################

# # Exercice 1 
# def add_two_numbers(num1, num2):
    
#     print (f"Les nombres sont : {num1} et {num2}")
#     return num1 + num2  


# resultat = add_two_numbers(5, 5) 

# print(f"La somme est : {resultat}")
    
    
# # Exercice 2 

# nom = input("Quel est votre nom : ? ")

# def greet(name):
    
#     print(f"Hello {name}")
    
# greet(nom)
 
 
 # exercie 3
 
# nombre = int(input(" Donne un nombre : "))

# def check_even_or_odd(number):
    
#     return "Even" if number % 2 == 0 else "Odd"

# resultat = check_even_or_odd(nombre)
# print(resultat)

# exercice 4 

# list = [1,2,3]

# def sum_list(numbers):
    
#     # total = 0
#     # for i in numbers:
#     #     total += i
#     return sum(numbers)

# resultat = sum_list(list)
# print(resultat)

# exercie 5

# day_of_week = ['Sunday', 'Monday','Tuesday','Wednesday', 'Friday','Saturday']

# def print_days(days):
#     for days in day_of_week :
#         print(days)

# print_days(day_of_week)

# Exercice 6 

# test = 0

# def check_sign(number):
#     if number > 0:
#         print("Positive")
#     elif number < 0:
#         print("Negative")
#     else:
#         print("zero")


# check_sign(5)

# Exercice 7 

def repeat_word(word, number):
    
    for i in range(number):
        print(word)
        
repeat_word("Hello", 7)
    
    
    
    

 