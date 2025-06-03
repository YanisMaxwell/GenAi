# Declare a variable called first and assign it to the value "Hello World".
first = "Hello World"

# Write a comment that says "This is a comment."
        # This a comment 
        
# Log a message to the terminal that says "I AM A COMPUTER!"

print("I am a computer ! ")

# Write an if statement that checks if 1 is less than 2 and if 4 is greater than 2. If it is, show the message "Math is fun."
if 1 < 2 and 4 > 2:
    print("Math is fun")

# Assign a variable called nope to an absence of value.
nope = None 
# Use the language’s “and” boolean operator to combine the language’s “true” value with its “false” value.

resultat =  True and False
print(resultat)
    
# Calculate the length of the string "What's my length?

taille = "What's my length?"
print(len(taille))

# Convert the string "i am shouting" to uppercase.

texte = "i am shouting"
texte_majuscule = texte.upper()
print(texte_majuscule)

# Convert the string "1000"to the number 1000.

string = "1000"
print(int(string))

# Combine the number 4 with the string "real" to produce "4real".
string_1 = ( "4" + "real")     
print(str(string_1))   

# Record the output of the expression 3 * "cool".
    #coolcoolcool
    
# Record the output of the expression 1 / 0.
   #rint(1/0)
   #eroDivisionError: division by zero
   
# Determine the type of [].
     #class 'list'>

 
# Ask the user for their name, and store it in a variable called name.

name = input("what is your name ? " )

# Ask the user for a number. If the number is negative, show a message that says "That number is less than 0!" If the number is positive, show a message that says "That number is greater than 0!" Otherwise, show a message that says "You picked 0!.

user_number = int(input("What is your number ? "))

    
if user_number < 0:
    print("That number is less than 0!")
elif user_number > 0:
    print("That number is greater than 0!")

else:
    print("You picked 0!")


# Find the index of "l" in "apple".
my_string = "apple"
print(my_string[3])

# Check whether "y" is in "xylophone".

mot = "xylophone"
lettre = 0 

for lettre in mot:
    if lettre == "y":
        print(lettre)

# Check whether a string called my_string is all in lowercase.

my_string = "Allez Paris !" 
print(my_string.islower())


# When you’re ready, move on to List Basics



