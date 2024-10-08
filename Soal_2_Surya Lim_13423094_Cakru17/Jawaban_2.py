import random

class Robot:
    def __init__(self, name, hitpoint, damage_hi, damage_lo):
        self.name = name
        self.hitpoint =  hitpoint
        self.damage_hi = damage_hi
        self.damage_lo = damage_lo
    
    def attack(self, enemy):
        enemy.hitpoint -= random.randint(self.damage_lo, self.damage_hi)

class Battle:

    def start_fight(robot1, robot2):

        max_hp_1 = robot1.hitpoint
        max_hp_2 = robot2.hitpoint


        while robot1.hitpoint > 0 and robot2.hitpoint > 0:
            
            hp_before_1 = robot1.hitpoint
            hp_before_2 = robot2.hitpoint

            robot1.attack(robot2)
            if robot2.hitpoint > 0:
                print(robot1.name + " has done " + str(hp_before_2 - robot2.hitpoint) + " damage to "+str(robot2.name)+" (" + str(robot2.hitpoint) + "/" + str(max_hp_2) + ")" )
            else:
                print(robot1.name + " has done a " + str(hp_before_2 - robot2.hitpoint) + "-damage final blow to " + str(robot2.name))
                break

            robot2.attack(robot1)
            if robot1.hitpoint > 0:
                print(robot2.name+ " has done " + str(hp_before_1 - robot1.hitpoint) + " damage to "+str(robot1.name)+" (" + str(robot1.hitpoint) + "/" + str(max_hp_1) + ")" )
            else:
                print(robot2.name + " has done a " + str(hp_before_1 - robot1.hitpoint) + "-damage final blow to " + str(robot1.name))
                break

        if robot1.hitpoint < 0:
            print(robot2.name + " wins")
        else:
            print(robot1.name + " wins")

class Game:
    def add_robot(list):
        name = input("Insert robot name: ")
        hitpoint = int(input("Insert robot hitpoint: "))
        damage_lo = int(input("Insert lowest damage: "))
        damage_hi = int(input("Insert highest damage: "))
        robot = Robot(name, hitpoint, damage_hi, damage_lo)
        list.append(robot)

    def start_game():
        first_robot = int(input("Select first robot (example input: 1): "))
        second_robot = int(input("Select second robot (example input: 1): "))

        while first_robot == second_robot:
            first_robot = int(input("Select first robot (example input: 1): "))
            second_robot = int(input("Select second robot (example input: 1): "))
        
        return first_robot, second_robot


robot1 = Robot("German Sheperd", 10, 5, 3)
robot2 = Robot("Mastiff", 20, 3, 2)
robot3 = Robot("Bulldog", 7, 8, 6)
list = [robot1, robot2, robot3]
print("________________________")
print("_______ROBOBATTLE_______")
print("________________________")
print("Choose your robot: ")
for i in range (len(list)):
    print(str(i+1) + ". " + str(list[i].name) + "; hitpoint: " + str(list[i].hitpoint) + "; attack: " + str(list[i].damage_lo) + "-" + str(list[i].damage_hi))
bool_add_robot = input("Do you want to add a robot (Y/N)? ")

while bool_add_robot == "Y" and len(list) <= 10:
    Game.add_robot(list)
    for i in range (len(list)):
        print(str(i+1) + ". " + str(list[i].name) + "; hitpoint: " + str(list[i].hitpoint) + "; attack: " + str(list[i].damage_lo) + "-" + str(list[i].damage_hi))
    bool_add_robot = input ("Do you still want to add a robot (Y/N)? ")

first_robot, second_robot = Game.start_game()

Battle.start_fight(list[first_robot-1], list[second_robot-1])
