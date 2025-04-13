# Import Animal to allow Hyena to inherit functions from Animal
from Animal import Animal
from Animal import random

class Hyena(Animal):
    # Hyena count
    numOfHyenas = 0

    # List of possible hyenas sounds
    list_of_hyena_sounds = ["Hah", "Heh", "Gah", "Geh"]

    # List of hyena names
    list_of_hyena_names = []

    file_path = "animalNames.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()

        # Iterate through the lines in the file
        line_num = 1
        for line in lines:
            if line_num==3:
                list_of_hyena_names.extend(line.strip().split(","))
                break
            else:
                line_num += 1

    def __init__(self, name="a_name", animal_id="an_id", birth_date="2099-01-01", color="a_color", sex="a_sex", weight="a_weight", originating_zoo="a_zoo", arrival_date="2099-01-01"):

        # Increment the created hyena count
        Hyena.numOfHyenas += 1

        # Call the constructor of the parent class (Animal) with 'Hyena' as the species
        super().__init__("hyena",name,animal_id,birth_date, color, sex, weight, originating_zoo, arrival_date)

    def make_sound(self):
        return self.list_of_hyena_sounds[random.randint(0,3)]

    # Get an unused hyena name
    def get_hyena_name(self):
        return self.list_of_hyena_names.pop(0)