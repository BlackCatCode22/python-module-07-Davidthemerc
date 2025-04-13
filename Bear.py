# Import Animal to allow bear to inherit functions from Animal
from Animal import Animal
from Animal import random

class Bear(Animal):
    # Bear count
    numOfBears = 0

    # List of possible bears sounds
    list_of_bear_sounds = ["Growl!", "GROWWWWLLL!", "Arrrgghhh.", "GROWLLLL! GROWWWL!"]

    # List of bear names
    list_of_bear_names = []

    file_path = "animalNames.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()

        # Iterate through the lines in the file
        line_num = 1
        for line in lines:
            if line_num==11:
                list_of_bear_names.extend(line.strip().split(","))
                break
            else:
                line_num += 1

    def __init__(self, name="a_name", animal_id="an_id", birth_date="2099-01-01", color="a_color", sex="a_sex", weight="a_weight", originating_zoo="a_zoo", arrival_date="2099-01-01"):

        # Increment the created bear count
        Bear.numOfBears += 1

        # Call the constructor of the parent class (Animal) with 'bear' as the species
        super().__init__("bear",name,animal_id,birth_date, color, sex, weight, originating_zoo, arrival_date)

    def make_sound(self):
        return self.list_of_bear_sounds[random.randint(0,3)]

    # Get an unused bear name
    def get_bear_name(self):
        return self.list_of_bear_names.pop(0)