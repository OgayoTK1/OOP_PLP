# Assignment 1: Design Your Own Class (Superhero)
# Base class for all superheroes
class Superhero:
    def __init__(self, name, alias, strength, city):
        self._name = name  # Encapsulated attribute
        self._alias = alias
        self._strength = strength
        self._city = city
        self._is_active = True

    # Getter for name (encapsulation)
    @property
    def name(self):
        return self._name

    # Setter for strength with validation
    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        if value < 0:
            raise ValueError("Strength cannot be negative")
        self._strength = value

    # Method to describe the superhero
    def describe(self):
        return f"{self._alias} ({self._name}), Strength: {self._strength}, Protects: {self._city}"

    # Method to toggle active status
    def toggle_active(self):
        self._is_active = not self._is_active
        return f"{self._alias} is now {'active' if self._is_active else 'retired'}"

    # Abstract-like method for polymorphism (to be overridden)
    def use_power(self):
        raise NotImplementedError("Subclasses must implement use_power()")


# Assignment 2: Polymorphism Challenge
# Subclass for flying superheroes
class FlyingHero(Superhero):
    def __init__(self, name, alias, strength, city, flight_speed):
        super().__init__(name, alias, strength, city)
        self.flight_speed = flight_speed

    def use_power(self):
        return f"{self._alias} soars through the skies at {self.flight_speed} mph! ✈️"


# Subclass for speedster superheroes
class Speedster(Superhero):
    def __init__(self, name, alias, strength, city, run_speed):
        super().__init__(name, alias, strength, city)
        self.run_speed = run_speed

    def use_power(self):
        return f"{self._alias} dashes at {self.run_speed} mph! 🏃‍♂️"


# Subclass for gadget-using superheroes
class Gadgeteer(Superhero):
    def __init__(self, name, alias, strength, city, gadget):
        super().__init__(name, alias, strength, city)
        self.gadget = gadget

    def use_power(self):
        return f"{self._alias} deploys their {self.gadget}! 🛠️"


# Example usage
if __name__ == "__main__":
    # Create instances of different superhero types
    iron_man = Gadgeteer("Tony Stark", "Iron Man", 80, "New York", "Armor Suit")
    flash = Speedster("Barry Allen", "The Flash", 70, "Central City", 760)
    superman = FlyingHero("Clark Kent", "Superman", 100, "Metropolis", 2000)

    # Demonstrate polymorphism with use_power()
    heroes = [iron_man, flash, superman]
    print("Superheroes in Action:")
    for hero in heroes:
        print(hero.describe())
        print(hero.use_power())
        print()

    # Demonstrate encapsulation and methods
    print("Testing Iron Man's status:")
    print(iron_man.toggle_active())
    print(f"Strength before: {iron_man.strength}")
    iron_man.strength = 85  # Using setter
    print(f"Strength after: {iron_man.strength}")
    print(iron_man.describe())
