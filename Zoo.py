# Zoo.py
# Main Zookeeper code is kept here

from Animal import Animal
from Hyena import Hyena
from Lion import Lion
from Bear import Bear

from _datetime import date

# Create lists of the species

list_of_hyenas = []
list_of_lions = []
list_of_tigers = []
list_of_bears = []

# Date variables
current_date = date.today()
current_year = current_date.year

def calc_birth_date(the_season, the_years):
    year_of_birthday = int(current_year) - int(the_years)

    the_birth_day = ""

    if "spring" in the_season:
        the_birth_day = str(year_of_birthday) + "-03-21"
    elif "summer" in the_season:
        the_birth_day = str(year_of_birthday) + "-06-21"
    elif "fall" in the_season:
        the_birth_day = str(year_of_birthday) + "-09-23"
    elif "winter" in the_season:
        the_birth_day = str(year_of_birthday) + "-12-21"
    else:
        the_birth_day = str(year_of_birthday) + "-01-01"

    return the_birth_day

def process_one_line(one_line):
    # Create variables to help parse arrivingAnimals.txt
    a_species = ""
    a_sex = ""
    age_in_years = 99
    season = ""
    color = ""
    weight = ""
    origin_01 = ""
    origin_02 = ""

    print(one_line)
    group_of_words = one_line.strip().split(",")
    print(group_of_words)
    single_words= group_of_words[0].strip().split(" ")
    age_in_years = single_words[0]
    a_sex = single_words[3]
    a_species = single_words[4]
    single_words = group_of_words[1].strip().split(" ")
    season = single_words[2]
    color = group_of_words[2].strip()
    weight = group_of_words[3].strip()
    origin_01 = group_of_words[4].strip()
    origin_02 = group_of_words[5].strip()

    from_zoo = origin_01 + ", " + origin_02

    birth_day = calc_birth_date(season, age_in_years)

    if "hyena" in a_species:
        # Create a hyena object
        my_hyena = Hyena("aName","anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        # Fill in Name and Unique ID
        my_hyena.name = Hyena.get_hyena_name(my_hyena)
        my_hyena.animal_id = "Hya" + str(Hyena.numOfHyenas).zfill(2)
        # add to the Hyena list
        list_of_hyenas.append(my_hyena)

    if "lion" in a_species:
        # Create a lion object
        my_lion = Lion("aName","anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        # Fill in Name and Unique ID
        my_lion.name = Lion.get_lion_name(my_lion)
        my_lion.animal_id = "Lio" + str(Lion.numOfLions).zfill(2)
        # add to the Lion list
        list_of_lions.append(my_lion)

    if "bear" in a_species:
        # Create a bear object
        my_bear = Bear("aName","anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        # Fill in Name and Unique ID
        my_bear.name = Bear.get_bear_name(my_bear)
        my_bear.animal_id = "Lio" + str(Bear.numOfBears).zfill(2)
        # add to the Bear list
        list_of_bears.append(my_bear)

# ArrivingAnimals.txt read one line at a time
# Open the file in read mode
file_path = "arrivingAnimals.txt"
with open(file_path, "r") as file:
    # Iterate through the file line by line
    for line in file:
        process_one_line(line)

# Print a spacer liner
print("\n----------------------")

# Access the count variable numOfAnimals
print(f"\nNumber of animals created: {Animal.numOfAnimals}")

# Access the count variable numofHyenas
print(f"\nNumber of hyenas created: {Hyena.numOfHyenas}")

# Access the count variable numofHyenas
print(f"\nNumber of lions created: {Lion.numOfLions}")

# Output the animals
# Zoo population
print()
print("Zookeeper's Challenge Zoo Population")
print()
print("Hyena Habitat")
print()
for hyena in list_of_hyenas:
    print (hyena.animal_id + "," + hyena.name + "; " + hyena.make_sound() + "; birthdate " + str(hyena.birth_date) + "; " + hyena.color + "; " + hyena.sex + "; " + hyena.weight + "; " + hyena.originating_zoo + "; arrived " + str(hyena.arrival_date))
print()
print("Lion Habitat")
print()
for lion in list_of_lions:
    print (lion.animal_id + "," + lion.name + "; " + lion.make_sound() + "; birthdate " + str(lion.birth_date) + "; " + lion.color + "; " + lion.sex + "; " + lion.weight + "; " + lion.originating_zoo + "; arrived " + str(lion.arrival_date))
print()
print("Bear Habitat")
print()
for bear in list_of_bears:
    print (bear.animal_id + "," + bear.name + "; " + bear.make_sound() + "; birthdate " + str(bear.birth_date) + "; " + bear.color + "; " + bear.sex + "; " + bear.weight + "; " + bear.originating_zoo + "; arrived " + str(bear.arrival_date))