"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

# A helldiver is a super citizen
# all supercitizens are free

class SuperCitizen:
    def __init__(self, name: str, citizenClass: str, requisition_slips: int, free_status: boolean, age: int, rifle_training: bool):

        #assigns name
        if name: self.name = name
        else: self.name = ""

        #assigns class
        if  citizenClass: self.citizenClass = citizenClass
        else: self.citizenClass = ""

        #All supercitizens are free
        if requisition_slips: self.requisition_slips = requisition_slips

        #if in debt over 50k, citizen is no longer free
        if requisition_slips > -50000: self.free_status = free_status
        else: self.free_status = false

        if age > 0: self.age = age
        else: age = ""

        if rifle_training: self.rifle_training = "RIFLE TRAINED"
        else: rifle_training = "UNTRAINED"

        if free_status: self.free_status = "FREE TO VOTE"
        else: self.free_status = "=== ! CAUTION ! ===\n  CITIZEN IS NOT FREE TO VOTE"

    def display_citizen(self):
        print(
            f"Citizen Log:{self.name}\n==========\nCitizen Class:{self.citizenClass}\n"
            f"age: {self.age}\nRequisition Balance: {self.requisition_slips}"
            f"Rifle Training status: {self.rifle_training}"
            f"Freedom Status: {self.free_status}"
        )
    def create_citizen_entry(self):
        self.name = input("Welcome to the citizen log.\nEnter citizen name below to begin.")





# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class Helldiver(SuperCitizen):
    def __init__(self, name: str, citizenClass: str, requisition_slips: int, free_status: boolean, age: int, rifle_training: bool, SpecialWeaponsTrained: bool):
        super().__init__(name, age, citizenClass, requisition_slips, free_status, rifle_training)
        self.SpecialWeaponsTrained = SpecialWeaponsTrained


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    print("TODO: Implement namespace demonstration")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("TODO: Implement shallow copy and deep copy demonstration")


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")
    Supercitizen_John = SuperCitizen

    print("\nTODO: Create and test your child object")

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()