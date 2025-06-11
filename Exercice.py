
# Exerice 1

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age




chat1 = Cat("Grisou", 5)
chat2 = Cat("Bobby", 10)
chat3 = Cat("Dylan", 15)


def chat_plus_age(chat1, chat2, chat3):
    return max(chat1, chat2, chat3, key=lambda chat: chat.age)

plus_vieux_chat = chat_plus_age(chat1, chat2, chat3)

print(f"Le chat le plus vieux est {plus_vieux_chat.name} et il a {plus_vieux_chat.age} ans.")


# Exercice 2
    
    
class Dog:
    def __init__(self,name, height):
        self.name = name
        self.height = height
    def bark(self):
        print("Woof!")
    def jump(self):
        jump_height = self.height*2
        print(self.name,"jumped",jump_height)
        
        
davids_dog = Dog("Rex",25)
print(davids_dog)
davids_dog.bark()
davids_dog.jump()


sarahs_dog = Dog("Tom",50)
print(sarahs_dog)
sarahs_dog.bark()
sarahs_dog.jump()


# Exercice 3

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Création d'une chanson
stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

# Appel de la méthode pour chanter la chanson
stairway.sing_me_a_song()


# Exercice 4

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("Animaux dans le zoo :", self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped_animals = {}

        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = [animal]
            else:
                grouped_animals[first_letter].append(animal)

        self.grouped_animals = grouped_animals

    def get_groups(self):
        for letter, group in self.grouped_animals.items():
            print(f"{letter}: {group}")



ramat_gan_safari = Zoo("Ramat Gan Safari")

ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Baboon")

ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Bear")

ramat_gan_safari.get_animals()

ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
