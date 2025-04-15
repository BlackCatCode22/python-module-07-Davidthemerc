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

    def __init__(self, name, money, habitat_to_visit):

        self.name = name
        self.money = money
        self.habitat_to_visit = habitat_to_visit

        # Add one every time this object is created
        Visitor.numOfVisitors += 1

    def get_visitor_name(self):
        rando = random.randint(0,len(self.list_of_visitor_names)-1)
        # This piece of code is meant to prevent the first visitor name in the list from having the
        # extra space contained in the txt file rendered into the output, just like I did for the
        # animals. Those extra spaces will still annoy me!
        if (self.list_of_visitor_names[rando][0]) != " ":
            self.list_of_visitor_names[rando] = " " + self.list_of_visitor_names[rando]
        return self.list_of_visitor_names.pop(rando)