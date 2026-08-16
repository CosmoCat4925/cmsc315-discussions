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


# TODO 1: Create a parent class.
class SuperCitizen:
    # Class variables
    GOVERNMENT = "Super Earth"
    MIN_VOTING_REQUISITION = -50000

    def __init__(self, name: str, citizen_class: str, requisition_slips: int, free_status: bool, age: int, rifle_training: bool):
        # Instance variables
        self.name = name if name else "Unknown Citizen"
        self.citizen_class = citizen_class if citizen_class else "Class C"
        self.requisition_slips = requisition_slips
        self.age = age if age > 0 else 18

        # Determine training display status
        self.rifle_training = "RIFLE TRAINED" if rifle_training else "UNTRAINED"

        # Determine freedom status based on financial threshold
        if self.requisition_slips > self.MIN_VOTING_REQUISITION and free_status:
            self.free_status = "FREE TO VOTE"
        else:
            self.free_status = "=== ! CAUTION ! ===\n  CITIZEN IS NOT FREE TO VOTE"

    def display_citizen(self):
        """Displays formatted information about the citizen."""
        print(
            f"Citizen Log: {self.name}\n"
            f"========================\n"
            f"Allegiance: {self.GOVERNMENT}\n"
            f"Citizen Class: {self.citizen_class}\n"
            f"Age: {self.age}\n"
            f"Requisition Balance: {self.requisition_slips}\n"
            f"Rifle Training Status: {self.rifle_training}\n"
            f"Freedom Status: {self.free_status}"
        )

    def create_citizen_entry(self):
        """Allows interactive update of citizen name."""
        self.name = input("Welcome to the citizen log.\nEnter citizen name below to begin: ")


# TODO 2: Create a child class that inherits from the parent class.
class Helldiver(SuperCitizen):
    # Class variable specific to child class
    BRANCH = "Helldiver Corps"

    def __init__(self, name: str, citizen_class: str, requisition_slips: int, free_status: bool,
                 age: int, rifle_training: bool, special_weapons_trained: bool, cape_design: str, loadout: list):
        # Call parent constructor using super()
        # Every helldiver is a supercitizen
        super().__init__(name, citizen_class, requisition_slips, free_status, age, rifle_training)

        # New instance variables unique to helldivers
        self.special_weapons_trained = special_weapons_trained
        self.cape_design = cape_design
        self.loadout = loadout  # Nested mutable structure used for copy demonstration

    def deploy_to_super_destroyer(self, ship_name: str):
        """New method unique to the Helldiver child class."""
        print(f"\n[DEPLOYMENT] Helldiver {self.name} assigned to the SES '{ship_name}'. Ready for drop!")

    def display_citizen(self):
        """Overrides the parent method to include Helldiver-specific data."""
        super().display_citizen()
        print("---- Citizen Enlistment Information ---- ")
        training_str = "QUALIFIED" if self.special_weapons_trained else "UNQUALIFIED"
        print(
            f"Military Branch: {self.BRANCH}\n"
            f"Cape Design: {self.cape_design}\n"
            f"Special Weapons Training: {training_str}\n"
            f"Active Loadout: {self.loadout}\n"
            f"----------------------------------------"
        )


# TODO 3: Demonstrate class namespaces and instance namespaces.
def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # Create two objects of the child class
    diver1 = Helldiver("John-117", "Class A", 25000, True, 25, True, True, "Cape of Glory", ["AR-23", ["Orbital Strike", "Resupply"]])
    diver2 = Helldiver("Sarah-042", "Class A", 40000, True, 22, True, False, "Foesmasher", ["R-63", ["Eagle Airstrike"]])

    # Access class variable through the class itself
    print(f"Class variable accessed via Class (Helldiver.BRANCH): {Helldiver.BRANCH}")

    # Access the same class variable through an object instance
    print(f"Class variable accessed via Instance (diver1.BRANCH): {diver1.BRANCH}")

    # Add a new attribute to ONLY diver1
    diver1.medal_count = 150
    print(f"\nDynamically added 'medal_count' attribute to diver1: {diver1.medal_count}")

    # Display instance namespaces
    print("\n[diver1 Instance Namespace (__dict__)]:")
    print(diver1.__dict__)

    print("\n[diver2 Instance Namespace (__dict__)]:")
    print(diver2.__dict__)

    # Display class namespace
    print("\n[Helldiver Class Namespace (__dict__)]:")
    for key, value in Helldiver.__dict__.items():
        if not key.startswith("__"):  # Filter internal dunder attributes for clear scanning
            print(f"  {key}: {value}")


# TODO 4: Demonstrate shallow copying and deep copying.
def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # Create an object containing nested mutable data (list within a list)
    original_diver = Helldiver(
        "Eagle-One", "Class S", 100000, True, 28, True, True,
        "Fallen Hero's Vengeance", ["AR-23 Liberator", ["Stratagem 1: Bomb", "Stratagem 2: Turret"]]
    )

    # Perform shallow and deep copies
    shallow_diver = copy(original_diver)
    deep_diver = deepcopy(original_diver)

    print(f"Original Loadout before modification: {original_diver.loadout}")

    # Modify the original object's nested mutable structure
    print("\nModifying nested array in original_diver.loadout[1]...\n(Appending stratagem 3: 500kg Bomb)")
    original_diver.loadout[1].append("Stratagem 3: 500kg Bomb")

    # Display results to show difference
    print("\n--- Results After Modification ---")
    print(f"Original Diver Loadout: {original_diver.loadout}")
    print(f"Shallow Copy Loadout:  {shallow_diver.loadout}  <-- Changed! (Shares reference to inner list)")
    print(f"Deep Copy Loadout:     {deep_diver.loadout}  <-- Unchanged! (Completely isolated duplicate)")

    """
    SHALLOW VS. DEEP COPYING EXPLANATION:
    - Shallow Copy (copy()): Constructs a new object instance, but populates it with references 
      to the nested child elements of the original object. Because nested structures (e.g., lists 
      or dictionaries) point to the exact same memory address, mutating nested data in the original 
      reflects inside the shallow copy as well.
        
        Think of it as a pointer from C++. A shallow copy doesn't house the information buut rather,
        points to where it's stored. shallow copy -> data whereas a deepcopy is a proper copy of data:
        deepcopy[] = [data, data, data] or so.
      
    - Deep Copy (deepcopy()): Recursively creates new copies of the target object AND all nested 
      objects inside it. It completely duplicates the entire object tree, isolating the original 
      and copied objects into distinct memory spaces.
    """


# TODO 5: Complete the main function.
def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n--- Testing Parent Class Object ---")
    citizen = SuperCitizen("Jane Doe", "Class B", -60000, True, 30, False)
    citizen.display_citizen()

    print("\n--- Testing Child Class Object ---")
    diver = Helldiver("Viper", "Class A", 12000, True, 24, True, True, "Mantel of Loyalty", ["SG-225", ["Gatling Sentry"]])
    diver.display_citizen()
    diver.deploy_to_super_destroyer("Harbinger of Freedom")

    # Execute namespace and copy demonstrations
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()