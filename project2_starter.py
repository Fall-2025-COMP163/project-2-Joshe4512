"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Joshua Evans ]
Date: [11/4/25]

AI Usage: [ChatGPT and Google Gemini helped explain code to further knowledge of inheritance and classes, and the super function. AI also helped improve code for better syntax and efficiency]
Example: AI helped with inheritance structure and method overriding concepts
"""

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
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================
import random 
class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """
    
    def __init__(self, name, health, strength, magic):
        """Initialize basic character attributes"""
        # TODO: Set the character's name, health, strength, and magic
        # These should be stored as instance variables
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        pass
        # The class "character" is first made for us to be able to make characters. 
        # We initialize the character attributes while also using self, so it can be called every time we make a new character 
        # Self is also used with the parameters "name, health, strength, and magic," which we use to pass in when creating the object. 
        # Self shows how an object refers to its own data and the instance to the object itself.
        # Attributes are then made, and we use the argument and assign it to the variable "self.name" so it can be called later 
        
        
    def attack(self, target):
        """
        Basic attack method that all characters can use.
        This method should:
        1. Calculate damage based on strength
        2. Apply damage to the target
        3. Print what happened
       
        """
        damage = self.strength 
        target.take_damage(damage)
        print(f"{self.name} attacked {target.name} for {damage} damage!")
       
        #EXPLANATIONS
        # This is an instance method that defines a behavior for the character class
        # It uses self as the parameter, so it can be the character attacking 
        # Logically, this calculates damage based on strength by using "self.strength" and calls on "take_damage" to use on the target
        # Finally, it prints out what happened 
        # TODO: Implement basic attack
        # Damage should be based on self.strength
        # Use target.take_damage(damage) to apply damage
        pass
        
    def take_damage(self, damage):
        """
        Reduces this character's health by the damage amount.
        Health should never go below 0.
        """
        self.health -= damage

        if self.health < 0:
            self.health = 0
        # TODO: Implement taking damage
        # Reduce self.health by damage amount
        # Make sure health doesn't go below 0
        pass
        # Another Instance method that uses the self parameter for the character to be attacked 
        # the line self.health -= damage updates the character's health by taking the value of "self.health" and subtracting it from damage and giving a new health value.
        # This also uses an if statement that tells us that the player's health should never be below zero 
        
    def display_stats(self):
        """
        Prints the character's current stats in a nice format.
        """
        print(f"--- {self.name}'s Stats ---")
        print(f"  Health: {self.health}")
        print(f"  Strength: {self.strength}")
        print(f"  Magic: {self.magic}")

        # TODO: Print character's name, health, strength, and magic
        # Make it look nice with formatting
        pass

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
        super().__init__(name, health,strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0

        
        # TODO: Call super().__init__() with the basic character info
        # TODO: Store the character_class (like "Warrior", "Mage", etc.)
        # TODO: Add any other player-specific attributes (level, experience, etc.)
        pass
        
    def display_stats(self):
        """
        Override the parent's display_stats to show additional player info.
        Should show everything the parent shows PLUS player-specific info.
       
        # Prints additional info
        """
        # TODO: Call the parent's display_stats method using super()
        # TODO: Then print additional player info like class and level
        super().display_stats() #calls the parent "display stats method" and overwrites it 
        print(f"Class: {self.character_class}")
        print(f"Level: {self.level}")
        print(f"Experience: {self.experience}")
        pass

class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a warrior with appropriate stats.
        Warriors should have: high health, high strength, low magic
       
        
        
        """
        # TODO: Call super().__init__() with warrior-appropriate stats
        # Suggested stats: health=120, strength=15, magic=5
        super().__init__(name, "Warrior", health=120, strength= 15, magic=5)
        
        pass
        
    def attack(self, target):
        """
        Override the basic attack to make it warrior-specific.
        Warriors should do extra physical damage.
        
        """
        damage = self.strength + 5
        target.take_damage(damage)
        # TODO: Implement warrior attack
        # Should do more damage than basic attack
        # Maybe strength + 5 bonus damage?
        pass
        
    def power_strike(self, target):
        """
        Special warrior ability - a powerful attack that does extra damage.
        """
        damage = self.strength + 10
        target.take_damage(damage)
        # TODO: Implement power strike
        # Should do significantly more damage than regular attack
        pass

class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a mage with appropriate stats.
        Mages should have: low health, low strength, high magic
        """
        
        super().__init__(name, "Mage", health=80, strength=8, magic=20)    
        # TODO: Call super().__init__() with mage-appropriate stats
        # Suggested stats: health=80, strength=8, magic=20
        pass
        
    def attack(self, target):
        """
        Override the basic attack to make it magic-based.
        Mages should use magic for damage instead of strength.
        """
        damage = self.magic 
        target.take_damage(damage)
        # TODO: Implement mage attack
        # Should use self.magic for damage calculation instead of strength
        pass
        
    def fireball(self, target):
        """
        Special mage ability - a powerful magical attack.
        """
        damage = self.magic + 10 
        target.take_damage(damage)
        # TODO: Implement fireball spell
        # Should do magic-based damage with bonus
        pass

class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a rogue with appropriate stats.
        Rogues should have: medium health, medium strength, medium magic
        """
        super().__init__(name, "Rogue", health=90, strength=12, magic=10) 
        # TODO: Call super().__init__() with rogue-appropriate stats
        # Suggested stats: health=90, strength=12, magic=10
        pass
        
    def attack(self, target):
        """
        Override the basic attack to make it rogue-specific.
        Rogues should have a chance for extra damage (critical hits).
        """
        damage = self.strength 
        
        if random.randint(1,10) <=3:
            damage= self.strength*2

        target.take_damage(damage)
            
        # TODO: Implement rogue attack
        # Could add a chance for critical hit (double damage)
        # Hint: use random.randint(1, 10) and if result <= 3, it's a crit
        pass
        
    def sneak_attack(self, target):
        """
        Special rogue ability - guaranteed critical hit.
        """
        damage = self.strength*2
        target.health -= damage
        # TODO: Implement sneak attack
        # Should always do critical damage
        pass

class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
        """
        Create a weapon with a name and damage bonus.
        """
        self.weapon= weapon
        self.weapon_name= Sword
        self.weapon_damge= damage*1.15
        
        # TODO: Store weapon name and damage bonus
        pass
        
    def display_info(self):
        """
        Display information about this weapon.
        """
        Print(f"Weapon Name: {self.weapon}")
        print(f"Damage Bonus:{self.weapon_damage}")
        # TODO: Print weapon name and damage bonus
        pass

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # TODO: Create one of each character type
    # warrior = Warrior("Sir Galahad")
    # mage = Mage("Merlin")
    # rogue = Rogue("Robin Hood")
    
    # TODO: Display their stats
    # print("\n📊 Character Stats:")
    # warrior.display_stats()
    # mage.display_stats()
    # rogue.display_stats()
    
    # TODO: Test polymorphism - same method call, different behavior
    # print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    # dummy_target = Character("Target Dummy", 100, 0, 0)
    # 
    # for character in [warrior, mage, rogue]:
    #     print(f"\n{character.name} attacks the dummy:")
    #     character.attack(dummy_target)
    #     dummy_target.health = 100  # Reset dummy health
    
    # TODO: Test special abilities
    # print("\n✨ Testing Special Abilities:")
    # target1 = Character("Enemy1", 50, 0, 0)
    # target2 = Character("Enemy2", 50, 0, 0)
    # target3 = Character("Enemy3", 50, 0, 0)
    # 
    # warrior.power_strike(target1)
    # mage.fireball(target2)
    # rogue.sneak_attack(target3)
    
    # TODO: Test composition with weapons
    # print("\n🗡️ Testing Weapon Composition:")
    # sword = Weapon("Iron Sword", 10)
    # staff = Weapon("Magic Staff", 15)
    # dagger = Weapon("Steel Dagger", 8)
    # 
    # sword.display_info()
    # staff.display_info()
    # dagger.display_info()
    
    # TODO: Test the battle system
    # print("\n⚔️ Testing Battle System:")
    # battle = SimpleBattle(warrior, mage)
    # battle.fight()
    
    print("\n✅ Testing complete!")
