# Import Animal to allow lion to inherit functions from Animal
from Animal import Animal
from Animal import random

class Lion(Animal):
    # Lion count
    numOfLions = 0

    # List of possible lions sounds
    list_of_lion_sounds = ["Roarrr!", "ROARRRRRRR!", "Hmmmph.", "ROAR! GRRRR!"]

    # List of lion names
    list_of_lion_names = []

    file_path = "animalNames.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()

        # Iterate through the lines in the file
        line_num = 1
        for line in lines:
            if line_num==3:
                list_of_lion_names.extend(line.strip().split(","))
                break
            else:
                line_num += 1

    def __init__(self, name="a_name", animal_id="an_id", birth_date="2099-01-01", color="a_color", sex="a_sex", weight="a_weight", originating_zoo="a_zoo", arrival_date="2099-01-01"):

        # Increment the created lion count
        Lion.numOfLions += 1

        # Call the constructor of the parent class (Animal) with 'lion' as the species
        super().__init__("lion",name,animal_id,birth_date, color, sex, weight, originating_zoo, arrival_date)

    def make_sound(self):
        return self.list_of_lion_sounds[random.randint(0,3)]

    # Get an unused lion name
    def get_lion_name(self):
        return self.list_of_lion_names.pop(0)