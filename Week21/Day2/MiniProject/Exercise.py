# Mini-Project: Characters Game
# Description
# Create a class called Character with the following attributes and methods:
# attribute name
# attribute life – starts with a default value of 20
# attribute attack – the base attack of a character (integer) will be a default of 10
# method basic_attack() - accepts another Character instance as a parameter. Your character will <attack> the other
# character so his <life> points should drop.


# Instructions
# Now create 3 different classes that inherit from Character:
# Every character type should say (ie. print) something when they are created, get creative :)
# Druid:
# meditate() - increases life by 10, decrease attack by 2
# animal_help()- increases attack by 5
# fight() - accepts another Character instance as a parameter and subtracts (0.75*life + 0.75*attack) from the other
# character’s life.
# Example:
# druid.fight(other_char): other_char.life - (0.75*self.life + 0.75*self.attack)

# Warrior:
# brawl() - accepts another Character instance as a parameter, subtracts (2*attack) to the other characters life and
# adds (0.5*attack) to his own life.
# train() - increases both your attack and life points by 2.
# roar() - accepts another Character instance as a parameter and subtracts their attack points by 3.

# Mage:
# curse() – accepts another Character instance as a parameter and subtracts their attack points by 2.
# summon() - increases attack attribute by 3 points.
# cast_spell() - accepts another Character instance as a parameter and subtracts attack/life to the other character’s
# life points (eg if your attack is 20 and life is 5 you will subtract 4 life points).

# Once all your classes are created start testing them, create one of each character and use each of their method.
