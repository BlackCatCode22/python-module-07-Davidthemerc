# Added to support random selection of animal sounds
import random

class Animal:

    # Animal counting variable
    numOfAnimals = 0

    def __init__(self,species, name, animal_id, birth_date, color, sex, weight, originating_zoo, arrival_date):

        self.species = species
        self.name = name
        self.animal_id = animal_id
        self.birth_date = birth_date
        self.color = color
        self.sex = sex
        self.weight = weight
        self.originating_zoo = originating_zoo
        self.arrival_date = arrival_date

        # Add one every time this object is created
        Animal.numOfAnimals += 1