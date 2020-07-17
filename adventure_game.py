import time
import random

def print_pause(string, second):
    print(string)
    time.sleep(second)

def travel_to_methods(response, part, items):
    if response == 1 and part == 1:
        flashlight(items)
    elif response == 2 and part == 1:
        wardrobe(items)
    elif response == 1 and part == 2:
        window(items)
    elif response == 2 and part == 2:
        wardrobe(items)
    elif response == 1 and part == 3:
        flashlight(items)
    elif response == 1 and part == 3:
        window(items)

def start(animal, items):
    print_pause("You find yourself in dark room far away from the city, with scary sounds outside.", 2)
    print_pause(f"You realized that sounds it’s sound of {animal} and it’s so dangerous animal.", 2)
    print_pause("So, you need to run away!", 2)
    print_pause("In front of you an open window.", 2)
    print_pause("And in your right there is a small wardrobe.", 2)
    print_pause("Also your right hand a flashlight.", 2)
    part_choosing(1, items)
    
def part_choosing(part, items):
    if part == 1:
        print_pause("Enter 1 to turn on the flashlight!", 2)
        print_pause("Enter 2 to check out the wardrobe!", 2)
    elif part == 2:
        print_pause("Enter 1 to jump through the window!", 2)
        print_pause("Enter 2 to check out the wardrobe!", 2)
    elif part == 3:
        print_pause("Enter 1 to turn on the flashlight!", 2)
        print_pause("Enter 2 to jump through the window!", 2)
    response = int(input("Please Enter 1 or 2:\n"))
    
    travel_to_methods(response, part, items)
    


def flashlight(items):
    print_pause("You tried to turn on the flashlight.", 2)
    print_pause("You shake it and also did not work.", 2)
    print_pause("You find it has an old battery.", 2)
    if "battery" in items:
        print_pause("You have battery now.", 2)
        print_pause("You change the old battery in your flashlight to the new ones.", 2)
        items.append("flashlight")
        part_choosing(2, items)
    elif "battery" in items and "flashlight" in items:
        print_pause("It's already on")
    else:
        part_choosing(2, items)

def wardrobe(items):
    print_pause("You go to the wardrobe and open it.", 2)
    if "battery" not in items:
        print_pause("You find a battery!", 2)
        print_pause("You take it with you.", 2)
        items.append("battery")
        part_choosing(3, items)
    else:
        print_pause("There is nothing to take.", 2)
        print_pause("It’s an empty.", 2)
        part_choosing(3, items)
        
        
def window(items):
    print_pause("You go to the window then jumped through it.", 2)
    print_pause(f"You find {random.randint(1,10)} {animal}s coming to you.", 2)
    if "flashlight" in items:
        print_pause("You use the flashlight to block them a few seconds.", 2)
        print_pause("Then you have pointed a way to run!!", 2)
        print_pause("You run away never see back.", 2)
        print_pause("And you did it you ran !", 2)
        print_pause("YOU WIN :) !!")
    else:
        print_pause("You can’t see a way to run!!.", 2)
        print_pause("They are realy close!!", 2)
        print_pause("YOU have been defeated", 2)
        print_pause("YOU LOSE :( !!", 2)

def full_game():
    animals = [ "bear", "snack", "lion", "tiger" ]
    items = []
    animal = random.choice(animals)
    start(animal, items)

full_game()
