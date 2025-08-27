Superhero Class Program
Overview
This Python program implements a class hierarchy for superheroes, demonstrating key Object-Oriented Programming (OOP) concepts as part of the "Design Your Own Class" and "Polymorphism Challenge" assignments. The program defines a base Superhero class and three derived classes (FlyingHero, Speedster, Gadgeteer) to showcase inheritance, encapsulation, and polymorphism.
Purpose
The program fulfills two assignments:

Assignment 1: Design Your Own Class - Creates a Superhero class with attributes, methods, constructors, and encapsulation, along with inherited subclasses.
Assignment 2: Polymorphism Challenge - Implements polymorphic behavior through a use_power() method that varies across different superhero types.

Features

Base Class (Superhero):
Attributes: name, alias, strength, city, is_active (encapsulated with _ prefix).
Methods: describe() for summary, toggle_active() for status, use_power() for polymorphic behavior.
Encapsulation: Uses @property for controlled access to name (read-only) and strength (with validation).


Derived Classes:
FlyingHero: Adds flight_speed and defines use_power() as flying.
Speedster: Adds run_speed and defines use_power() as running.
Gadgeteer: Adds gadget and defines use_power() as deploying a gadget.


Polymorphism: Each subclass overrides use_power() to provide unique behavior (e.g., "soars," "dashes," "deploys").
Example Usage: Creates instances of each subclass and demonstrates their functionality in a loop.

File Structure

superheroes.py: The main Python file containing the class definitions and example usage.

Requirements

Python 3.x
No external libraries required.

How to Run

Ensure Python 3 is installed on your system.
Save the superheroes.py file in your working directory.
Open a terminal and navigate to the directory.
Run the program:python superheroes.py


The program will output descriptions and power usage for three superheroes, followed by a demonstration of encapsulation and status toggling for one hero.

Example Output
Superheroes in Action:
Iron Man (Tony Stark), Strength: 80, Protects: New York
Iron Man deploys their Armor Suit! 🛠️

The Flash (Barry Allen), Strength: 70, Protects: Central City
The Flash dashes at 760 mph! 🏃‍♂️

Superman (Clark Kent), Strength: 100, Protects: Metropolis
Superman soars through the skies at 2000 mph! ✈️

Testing Iron Man's status:
Iron Man is now retired
Strength before: 80
Strength after: 85
Iron Man (Tony Stark), Strength: 85, Protects: New York

Assignment Fulfillment

Assignment 1:
Class Design: Superhero class with attributes (name, alias, strength, city, is_active) and methods (describe, toggle_active, use_power).
Constructors: Each class uses __init__ to initialize unique values, with subclasses extending via super().
Encapsulation: Protected attributes with _ prefix and @property for controlled access.
Inheritance: Three subclasses inherit from Superhero.


Assignment 2:
Polymorphism: use_power() method is implemented differently in each subclass (FlyingHero, Speedster, Gadgeteer).
Demonstration: Main block iterates over a list of superheroes to show varied use_power() outputs.



Notes

The code is written in pure Python, requiring no external dependencies.
Comments in superheroes.py explain the purpose of each class and method.
The program is designed to be simple yet comprehensive, showcasing OOP principles in an engaging superhero theme.

Author
Ogayo Andrew
Created as part of the OOP Python assignment.

