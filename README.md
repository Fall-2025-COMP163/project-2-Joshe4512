Character Abilities Showcase
Course: COMP 163 - Project 2 Author: Joshua Evans Date: November 4, 2025

Project Description
This project implements a class-based battle system in Python to demonstrate Object-Oriented Programming (OOP) concepts. It features a hierarchy of character classes (Warrior, Mage, Rogue) that inherit from a base Player class. The program simulates combat interactions, special abilities, and weapon composition using a text-based interface.

How to Run
Prerequisites: Ensure you have Python 3.x installed.

File Setup: Make sure the script file (e.g., main.py) is in your current directory.

Execution: Open your terminal or command prompt and run:

Bash

python main.py
Expected Output: The console will display:

Character statistics.

A demonstration of Polymorphism (different attack behaviors).

A showcase of Special Abilities (Power Strike, Fireball, Sneak Attack).

Weapon details (Composition).

A full simulated battle between the Warrior and Mage.

Bonus Creative Features
Rogue Critical Hit Logic: Implemented a randomized critical hit system for the Rogue class using random.randint(1, 10). There is a 30% chance for the Rogue to deal double damage on a standard attack, adding an element of unpredictability to the combat.

Weapon Composition: Integrated a standalone Weapon class to demonstrate "Has-A" relationships (Composition) alongside the standard inheritance models.

Console Polish: Added clear separators (===, ---) and descriptive print statements to the battle logs to make the combat flow easier to read and understand for the user.

AI Usage
Tools Used: ChatGPT and Google Gemini.

Usage Description:

Concept Explanation: AI was used to clarify complex OOP concepts, specifically how inheritance hierarchies work and the proper syntax for using super() to initialize parent attributes.

Code Refinement: AI assisted in refining the code syntax for efficiency and ensuring that the SimpleBattle class interacted correctly with the custom character classes.

Debugging: AI helped identify and fix errors related to missing attributes (e.g., damage_bonus spelling errors) and missing print statements in the attack methods.

AI Also helped with ReadMe file.
