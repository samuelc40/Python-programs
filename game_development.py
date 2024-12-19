
class GameCharacter:
    def __init__(self, health, strength, agility):
        self.health = health
        self.strength = strength
        self.agility = agility

    def display_character_info(self):
        print(f"Health: {self.health}, Strength: {self.strength}, Agility: {self.agility}")


class Warrior(GameCharacter):
    def __init__(self, health, strength, agility, armor):
        super().__init__(health, strength, agility)
        self.armor = armor

    def display_warrior_info(self):
        self.display_character_info()
        print(f"Armor: {self.armor}")


class Mage(GameCharacter):
    def __init__(self, health, strength, agility, mana, magic_power):
        super().__init__(health, strength, agility)
        self.mana = mana
        self.magic_power = magic_power

    def display_mage_info(self):
        self.display_character_info()
        print(f"Mana: {self.mana}, Magic Power: {self.magic_power}")


class Ninja(Warrior):
    def __init__(self, health, strength, agility, armor, stealth, speed):
        super().__init__(health, strength, agility, armor)
        self.stealth = stealth
        self.speed = speed

    def display_ninja_info(self):
        self.display_warrior_info()
        print(f"Stealth: {self.stealth}, Speed: {self.speed}")


class NinjaMage(Ninja, Mage):
    def __init__(self, health, strength, agility, armor, stealth, speed, mana, magic_power):
        Ninja.__init__(self, health, strength, agility, armor, stealth, speed)
        Mage.__init__(self, health, strength, agility, mana, magic_power)

    def display_ninja_mage_info(self):
        self.display_ninja_info()
        print(f"Mana: {self.mana}, Magic Power: {self.magic_power}")


warrior = Warrior(health=150, strength=80, agility=60, armor=50)
warrior.display_warrior_info()

print("")

mage = Mage(health=100, strength=40, agility=70, mana=200, magic_power=90)
mage.display_mage_info()

print("")

ninja = Ninja(health=130, strength=75, agility=90, armor=40, stealth=85, speed=100)
ninja.display_ninja_info()

print("")

ninja_mage = NinjaMage(
    health=120, strength=65, agility=80, armor=30, stealth=95, speed=110,
    mana=180, magic_power=85
)
ninja_mage.display_ninja_mage_info()
