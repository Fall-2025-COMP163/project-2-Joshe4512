"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Joshua Evans
Date: 11/4/25

AI Usage: ChatGPT and Google Gemini helped explain code to further knowledge of inheritance,
classes, and the super function. AI also helped improve code for better syntax and efficiency.
"""

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
        """Initialize basic character attributes"""
        # Encapsulation: Storing data inside the object instance
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        
    def attack(self, target):
        """
        Basic attack method that all characters can use.
        """
        # Logic: Calculate damage based on strength and apply to target
        damage = self.strength 
        target.take_damage(damage)
        print(f"{self.name} attacked {target.name} for {damage} damage!")
        
    def take_damage(self, damage):
        """
        Reduces this character's health by the damage amount.
        Health should never go below 0.
        """
        self.health -= damage
        if self.health < 0:
            self.health = 0
        
    def display_stats(self):
        """
        Prints the character's current stats in a nice format.
        """
        print(f"--- {self.name}'s Stats ---")
        print(f"  Health: {self.health}")
        print(f"  Strength: {self.strength}")
        print(f"  Magic: {self.magic}")


class Player(Character):
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features.
    """
    
    def __init__(self, name, character_class, health, strength, magic):
        """
        Initialize a player character.
        Should call the parent constructor and add player-specific attributes.
        """
        # Inheritance: Calling the parent (Character) constructor using super()
        super().__init__(name, health, strength, magic)
        
        # Player-specific attributes
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        
    def display_stats(self):
        """
        Override the parent's display_stats to show additional player info.
        """
        # Call parent method first, then add new info
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
        """
        Create a warrior with appropriate stats.
        Warriors should have: high health, high strength, low magic.
        """
        # Pass specific stats to the parent constructor
        super().__init__(name, "Warrior", health=120, strength=15, magic=5)
        
    def attack(self, target):
        """
        Override the basic attack to make it warrior-specific.
        Warriors should do extra physical damage.
        """
        # Polymorphism: Same method name 'attack', but different behavior (Warrior logic)
        damage = self.strength + 5
        target.take_damage(damage)
        print(f"{self.name} attacked {target.name} for {damage} damage!")
        
    def power_strike(self, target):
        """
        Special warrior ability - a powerful attack that does extra damage.
        """
        damage = self.strength + 10
        target.take_damage(damage)
        print(f"{self.name} used Power Strike on {target.name} for {damage} damage!")


class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a mage with appropriate stats.
        Mages should have: low health, low strength, high magic.
        """
        super().__init__(name, "Mage", health=80, strength=8, magic=20)    
        
    def attack(self, target):
        """
        Override the basic attack to make it magic-based.
        Mages should use magic for damage instead of strength.
        """
        # Polymorphism: Mage uses Magic stat for damage
        damage = self.magic 
        target.take_damage(damage)
        print(f"{self.name} attacked {target.name} for {damage} damage!")
        
    def fireball(self, target):
        """
        Special mage ability - a powerful magical attack.
        """
        damage = self.magic + 10 
        target.take_damage(damage)
        print(f"{self.name} cast Fireball on {target.name} for {damage} damage!")


class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a rogue with appropriate stats.
        Rogues should have: medium health, medium strength, medium magic.
        """
        super().__init__(name, "Rogue", health=90, strength=12, magic=10) 
        
    def attack(self, target):
        """
        Override the basic attack to make it rogue-specific.
        Rogues should have a chance for extra damage (critical hits).
        """
        # Polymorphism: Rogue has random chance logic
        damage = self.strength 
        
        # 30% chance for critical hit (double damage)
        if random.randint(1, 10) <= 3:
            damage = self.strength * 2
            print(f"CRITICAL HIT!")

        target.take_damage(damage)
        print(f"{self.name} attacked {target.name} for {damage} damage!")
            
    def sneak_attack(self, target):
        """
        Special rogue ability - guaranteed critical hit.
        """
        damage = self.strength * 2
        target.take_damage(damage)
        print(f"{self.name} used Sneak Attack on {target.name} for {damage} damage!")


class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
        """
        Create a weapon with a name and damage bonus.
        """
        # Storing weapon attributes
        self.name = name
        self.damage_bonus = damage_bonus
        
    def display_info(self):
        """
        Display information about this weapon.
        """
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
    warrior = Warrior("Marcus")
    mage = Mage("Aria")   
    rogue = Rogue("Shadow")
    
    # Display stats to see initial values
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()
    
    # Polymorphism - same method, different behavior
    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    target = Character("Target Dummy", 100, 0, 0)
    
    for character in [warrior, mage, rogue]:
         print(f"\n{character.name} attacks the dummy:")
         character.attack(target) # Each attacks differently
         target.health = 100  # Reset dummy health
    
    # Special abilities
    print("\n✨ Testing Special Abilities:")
    enemy = Character("Goblin", 200, 0, 0)
    
    warrior.power_strike(enemy)
    mage.fireball(enemy)
    rogue.sneak_attack(enemy)
    
    # Composition
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 15)
    sword.display_info()
    
    # Test battle system (provided for you)
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")
