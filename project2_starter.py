"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Joshua Evans
Date: 11/4/25

AI Usage: ChatGPT and Google Gemini helped explain code to further knowledge of inheritance,
classes, and the super function. AI also helped improve code for better syntax and efficiency.
AI helped troubleshoot the weapon creation class. AI improved code for displaying stats by improving the formatting.


import random

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT
# ============================================================================

class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """
    
    def __init__(self, name, health, strength, magic):
        # Initialize basic character attributes (Encapsulation)
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        
    def attack(self, target):
        # Basic attack method - will be overridden by child classes (Polymorphism)
        damage = self.strength 
        target.take_damage(damage)
        print(f"{self.name} attacked {target.name} for {damage} damage!")
        
    def take_damage(self, damage):
        # Reduces health but prevents it from dropping below zero
        self.health -= damage
        if self.health < 0:
            self.health = 0
        
    def display_stats(self):
        # Prints the character's current stats in a nice format
        print(f"--- {self.name}'s Stats ---")
        print(f"  Health: {self.health}")
        print(f"  Strength: {self.strength}")
        print(f"  Magic: {self.magic}")


class Player(Character):
    """
    # Base class for player characters.
    # Inherits from Character and adds player-specific features.
    """
    
    def __init__(self, name, character_class, health, strength, magic):
        # Call the parent constructor using super() to handle basic stats
        super().__init__(name, health, strength, magic)
        
        # Add player-specific attributes
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        
    def display_stats(self):
        # Override parent method to show extra player info
        super().display_stats()
        print(f"Class: {self.character_class}")
        print(f"Level: {self.level}")
        print(f"Experience: {self.experience}")


class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        # Initialize as a Warrior with high health and strength
        super().__init__(name, "Warrior", health=120, strength=15, magic=5)
        
    def attack(self, target):
        # Override basic attack: Warrior adds +5 damage
        damage = self.strength + 5
        target.take_damage(damage)
        
    def power_strike(self, target):
        # Unique Warrior ability: Deals extra heavy damage
        damage = self.strength + 10
        target.take_damage(damage)


class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """
    
    def __init__(self, name):
        # Initialize as a Mage with high magic and low health
        super().__init__(name, "Mage", health=80, strength=8, magic=20)    
        
    def attack(self, target):
        # Override basic attack: Mage uses Magic instead of Strength
        damage = self.magic 
        target.take_damage(damage)
        
    def fireball(self, target):
        # Unique Mage ability: Powerful magic attack
        damage = self.magic + 10 
        target.take_damage(damage)


class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        # Initialize as a Rogue with balanced stats
        super().__init__(name, "Rogue", health=90, strength=12, magic=10) 
        
    def attack(self, target):
        # Override basic attack: Rogue has a chance for Critical Hit
        damage = self.strength 
        
        # 30% chance for critical hit (double damage)
        if random.randint(1, 10) <= 3:
            damage = self.strength * 2

        target.take_damage(damage)
            
    def sneak_attack(self, target):
        # Unique Rogue ability: Guaranteed critical hit
        damage = self.strength * 2
        target.take_damage(damage)        


class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
        # Store weapon attributes
        self.name = name
        self.damage_bonus = damage_bonus
        
    def display_info(self):
        # Display weapon details
        print(f"Weapon Name: {self.name}")
        print(f"Damage Bonus: {self.damage_bonus}")


# ============================================================================
# MAIN PROGRAM FOR TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # Create characters (inheritance)
    # These objects inherit attributes from the Player and Character classes
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")
    
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()
    
    # Polymorphism - same method, different behavior
    # We can treat all these different classes the same way using a loop
    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)
    
    for character in [warrior, mage, rogue]:
         print(f"\n{character.name} attacks the dummy:")
         character.attack(dummy_target) # Each class runs its own version of attack()
         dummy_target.health = 100  # Reset dummy health
    
    # Special abilities
    # Calling unique methods that only exist on specific subclasses
    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)
    
    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)
    
    # Composition
    # Creating independent objects that can be associated with characters
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
    
    sword.display_info()
    staff.display_info()
    dagger.display_info()
    
    # Test battle system (provided for you)
    # Passing objects into a separate system to see how they interact
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")
