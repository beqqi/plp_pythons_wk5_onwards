# Define a base class called 'superhero'
class superhero:
    # Constructor to initialize name and power attributes
    def __init__(self, name, power):
        self.name = name
        self.power = power

    # Method to display superhero's information
    def display_info(self):
        return f"Superhero Name: {self.name}, Power: {self.power}"
    
    # Define a nested class 'batman' inside 'superhero'
    class batman:
        # Constructor to initialize name, power, and gadget attributes
        def __init__(self, name, power, gadget):
            superhero.__init__(self, name, power)  # Call the base class constructor
            self.gadget = gadget

        # Method to display batman's information, including gadget
        def display_info(self):
            base_info = superhero.display_info(self)  # Get base info from superhero
            return f"{base_info}, Gadget: {self.gadget}"
        

class Animal:
    def __init__(self, species, habitat):
        self.species = species
        self.habitat = habitat

    def display_info(self):
        return f"Animal Species: {self.species}, Habitat: {self.habitat}"
    
    # Polymorphic method - each subclass will override this
    def move(self):
        pass

class Fish(Animal):
    def __init__(self, species, habitat):
        super().__init__(species, habitat)
    
    def move(self):
        return "Fish moves by swimming"

class Bird(Animal):
    def __init__(self, species, habitat):
        super().__init__(species, habitat)
    
    def move(self):
        return "Bird moves by flying"


        
# Create an instance of superhero
hero = superhero("Superman", "Flight")
print(hero.display_info())  # Output: Superhero Name: Superman, Power: Flight

# Create an instance of batman (nested class)
bat = superhero.batman("Batman", "Intelligence", "Batarang")
print(bat.display_info())  

# Create an instance of animal
fishy = Fish("Goldfish", "Freshwater")
birdy = Bird("Eagle", "Mountains")

# Demonstrate polymorphism
print(fishy.display_info())
print(fishy.move()) 

print(birdy.display_info())
print(birdy.move())  

