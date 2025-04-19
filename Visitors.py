# Import random
import random

# Let's add some visitors to the zoo! It's a bit lonely at the moment.
class Visitor:

    # Visitor counting variable
    numOfVisitors = 0

    # List of visitor names
    list_of_visitor_names = []

    # Get the names from visitors.txt
    with open('visitors.txt',"r") as file:
        lines = file.readlines()

        # Iterate through the lines in the file
        line_num = 1
        for line in lines:
            if line_num==3:
                list_of_visitor_names.extend(line.strip().split(","))

            elif line_num==4:
                list_of_visitor_names.extend(line.strip().split(","))

            elif line_num==5:
                list_of_visitor_names.extend(line.strip().split(","))
                break
            else:
                line_num += 1

    def __init__(self, name, money, habitat_to_visit,favname):

        self.name = name
        self.money = money
        self.habitat_to_visit = habitat_to_visit
        self.favname = favname

        # Add one every time this object is created
        Visitor.numOfVisitors += 1

    def get_visitor_name(self):
        rando = random.randint(0,len(self.list_of_visitor_names)-1)

        # Error checking code, due to previously unknown issue with visitors.txt
        # Check if the selected name is valid (not empty, not just whitespace)
        if self.list_of_visitor_names[rando].strip() == "":
            raise ValueError("Empty name found in the list. Please correct the 'visitors.txt' data.")
            # Due to a correction in visitors.txt, this error doesn't exist anymore, but if it hypothetically did,
            # this line would help address the issue and point it out to the dev.

        # This piece of code is meant to add an extra leading space to the
        # first visitor name in each row of visitors.txt, because all the other
        # names have a leading space, and we don't want this name to be different.
        if (self.list_of_visitor_names[rando][0]) != " ":
            self.list_of_visitor_names[rando] = " " + self.list_of_visitor_names[rando]
        return self.list_of_visitor_names.pop(rando)