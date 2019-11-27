#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Names: Brianna Beshkin, Timothy Park, Shyam Patel, Andrew Pettit, Anant Venugopal
# Assignment: Final Project (Zombie Apocalypse Survival Game)

# main game function
def game():

    import time
    import sys
    import random
    import re

    # create class allowing to color and underline text - Tim
    class color: 
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'   

    # restart function allowing the player to restart the game or to quit the game - Tim
    def restart():
        print("\nWould you like to play again? Enter [Y] to restart. Enter [N] to quit")
        
        # choose by options y or n
        restart = "" 
        while restart !="y" and restart !="n": 
            restart = input().lower()
            if restart == "y":
                game()
            elif restart == "n":
                sys.exit("\nThanks for playing!")
            else: 
                print("ERROR: Enter Y or N")

   # function for letter by letter printing - Tim
    def write_letter():    
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.00) # CHANGE TO 0.00 FOR ERROR TESTING

    # print title screen - Shyam
    print("[---ZOMBIE APOCALYPSE SURVIVAL GAME---]")
    time.sleep(2)
    print("[---LOADING-ZOMBIES---]")
    time.sleep(2)
    print("[---LOADING-PLACES---]")
    time.sleep(2)
    print("[---LOADING-TEXT---]")
    time.sleep(2)
    print("[---LOADING-GAME---]")
        
    # print welcome prompt and enter name
    name = str(input("\nWelcome to the zombie apocalypse game! Please enter your name to begin: "))
    for letter in name:
        write_letter()
        
    # print introduction
    intro = "\nSo " + name + ", it seems like you're the only survivor left.\nAfter this zombie outbreak in your city, most of your friends and family are missing.\nIt's up to you " + name + ", to survive and find the others.\n"
    for letter in intro:
        write_letter()
   
    # character select function: sets skill attributes based on character selection - Brianna
    def character_select():

        # create skills dictionary to hold values
        global skills
        skills = {"health": 0, "strength": 0, "intelligence": 0, "stamina": 0}
        
        # choose character by options 1, 2, or 3
        print("\nChoose your character:\n")
        print("[1] Police officer:\nStrongest officer in his town, but had low scores on police academy exams. Very experienced with guns.\n"
              "\n[2] Computer Programmer:\nHas many honor awards from college, but was never good at sports. Has background knowledge in robotics.\n"
              "\n[3] Athlete:\nGot first place in several marathons, but never finished high school. Able to outperform most in physical tasks.")
        
        # set skills based on choice 1, 2, or 3 and add values to skills dictionary
        global character
        character = ""  
        while character != "1" and character != "2" and character != "3":
            character = input()
            if character == "1":
                print("You chose " + color.UNDERLINE + "POLICE OFFICER" + color.END)
                skills["health"] += 40
                skills["strength"] = 3
                skills["intelligence"] = 1
                skills["stamina"] = 2
            elif character == "2":
                print("You chose " + color.UNDERLINE + "COMPUTER PROGRAMMER" + color.END)
                skills["health"] += 20
                skills["strength"] = 1
                skills["intelligence"] = 3
                skills["stamina"] = 2
            elif character == "3":
                print("You chose " + color.UNDERLINE + "ATHLETE" + color.END)
                skills["health"] += 30
                skills["strength"] = 2
                skills["intelligence"] = 1
                skills["stamina"] = 3
            else:
                print("ERROR: Enter 1, 2, or 3")
    
    character_select()

    # print inventory select prompt
    inv_prompt = "\nIt's going to be a long and arduous journey to make it out alive. Gather some supplies that will help you along your way.\n"
    for letter in inv_prompt:
        write_letter()
    
    
    # inventory select function: choose items and add to inventory - Tim
    def inventory_select():
        
        # create inventory dictionary to hold items
        global inventory       
        inventory = {}
        
        # choose items by options 1, 2, or 3 and update dictionary
        print("\nSelect an item:")
        print("[1] Band Aids\n[2] Gluten Free Bread\n[3] Vodka")
        item = "" 
        while item != "1" and item != "2" and item != "3":
            item = input()
            if item == "1":
                inventory.update({"Band Aids": "+5 Health"})
            elif item == "2":
                inventory.update({"Gluten Free Bread": "+10 Health"})
            elif item == "3":
                inventory.update({"Vodka": "+20 Health"})
            else:
                print("ERROR: Enter 1, 2, or 3")
        
        print("\nSelect another item:")
        print("[1] Zombie Apocalypse Survival Guide\n[2] 20 lb Dumbbell\n[3] Running shoes")
        item2 = ""
        while item2 != "1" and item2 != "2" and item2 != "3":
            item2 = input()
            if item2 == "1":
                inventory.update({"Zombie Apocalypse Survival Guide": "+1 Intelligence"})
            elif item2 == "2":
                inventory.update({"20 lb Dumbbell": "+1 Strength"})
            elif item2 == "3":
                inventory.update({"Running shoes": "+1 Stamina"})
            else:
                print("ERROR: Enter 1, 2, or 3")
    
        print("\nInventory:", inventory)
    
    inventory_select()

    # print weapon select prompt
    weap_prompt = "\nYou'll need a weapon to protect yourself. You'll have the best chance if you choose a weapon that matches your skillset.\n"
    for letter in weap_prompt:
        write_letter()

    # weapon select function: choose weapon and set attack damage values - Brianna
    def weapon_select():

        # create weapons dictionary to hold weapons
        global weapons
        weapons = {}
        
        # choose weapon by options 1, 2, or 3 and update dictionary
        print("\nSelect a weapon:")
        print("[1] Uzi 9mm\n[2] Sword\n[3] Robotic Attack Dogs")
        weapon = "" 
        while weapon != "1" and weapon != "2" and weapon != "3":
            weapon = input()
            if weapon == "1":
                weapons.update({"Uzi 9mm": [20,30]})
                if character == "1":
                    weapons["Uzi 9mm"] = [30,40]  
            elif weapon == "2":
                weapons.update({"Sword": [10,25]})
                if character == "3":
                    weapons["Sword"] = [20,35]
            elif weapon == "3":
                weapons.update({"Robotic Attack Dogs": [20, 30]})
                if character == "2":
                    weapons["Robotic Attack Dogs"] = [40, 50]
            else:
                print("ERROR: Enter 1, 2, or 3")
        print("\nWeapons:", weapons)
    
    weapon_select()

    # check menu function: check skills and inventory menu - Tim
    def check_menu():
        
        # choose by options H, I, W, or C to continue
        print("\nCheck skills and health [H] \nCheck inventory [I], \nCheck weapons [W]\nTo continue [C]\n")
        check = ""
        while check != "H" and check != "I" and check != "W" and check != "C":
            check = input().upper()
            if check == "H":
                print("\nSkills:", skills)
                check_menu()                        
            elif check == "I":
                print("\nInventory:", inventory)
                check_menu()
            elif check == "W":
                print("\nWeapons:", weapons)
                check_menu()
            elif check == "C":
                break
            else:
                print("ERROR: Enter H, I, W, or C")
    
    # walmart function: choose a powerful item and add its effect - Tim
    def walmart():
        print("\nThere is a horde of zombies heading this way, just like on Black Friday!")
        print("Grab a quick snack and get out before they surround the building!")
        print("\nChoose wisely:")
        
        # choose items 1, 2, or 3 and add effect to skills
        print("[1] Smart Water\n[2] Canned Spinach\n[3] Gatorade")
        snack = ""
        while snack != "1" and snack != "2" and snack != "3":
            snack = input()
            if snack == "1":
                skills["intelligence"] += 2
                print("Adding +2 to intelligence")
                time.sleep(2)
            elif snack == "2":
                skills["strength"] += 2
                print("Adding +2 to strength")
                time.sleep(2)
            elif snack == "3":
                skills["stamina"] += 2
                print("Adding +2 to stamina")
                time.sleep(2)
            else:
                print("ERROR: Enter 1, 2, or 3")
 
    # military armory function: guess 4-digit code to pick up overpowered weapon - Tim
    def military_armory():
        print("\nThis is a good chance to find a weapon that can easily decimate these zombies.")
        print("But the door is locked with a 4-digit authentication code.")
        print("Guess the correct authentication code to gain access.\n")
        
        # create a random code between 1000 and 9999
        auth_code = random.randint(1000,9999)
        
        # set the number of chances based on character choice
        if character == "1":
            chances = 6
        if character == "2":
            chances = 8
        if character == "3":
            chances = 4

        # display if correct number is guessed, or add 1 to wrong guesses counter
        guesses = ""
        while chances > 0:         
            wrong_guesses = 0             
            for number in str(auth_code):      
                if number in guesses:    
                    print(number)    
                else:
                    print("-")     
                    wrong_guesses += 1    
            
            # add phased plasma rifle to weapons dictionary if code is guessed       
            if wrong_guesses == 0:        
                print("You guessed the correct authentication code! [[[ACCESS GRANTED]]]")
                print("You have gained access to the armory. You find a phased plasma rifle in the 40-watt range that can incinerate these zombies easily.")
                weapons.update({"Phased Plasma Rifle": [60, 80]})
                print("\nWeapons:", weapons)
                break              

            # error testing for guesses, subtract 1 from chances if guess is wrong
            guess = input("\nGuess a number:")
            if len(guess) > 1:
                print("\nERROR: Enter 1 number at a time!")
            else:
                guesses += guess                    
                if guess not in str(auth_code):  
                    chances -= 1        
                    print("\nIncorrect, you have " + str(chances) + " chances left") 
                    if chances == 0:           
                        print("\nYou've been locked out! Should have gone to Walmart...") 
      
    # choose path function: pick walmart or military armory - Tim
    def choose_path():
        print("\nYou have a limited time before these zombie scum overrun the area.")
        print("\nWhere will you go?")
        
        # choose by options 1 or 2 and call that function
        print("[1] Walmart\n[2] Military Armory")
        direction = ""
        while direction !="1" and direction !="2":
            direction = input()
            if direction == "1":
                walmart()
            elif direction == "2":
                military_armory()
            else: 
                print("ERROR: Enter 1 or 2")
    
    choose_path()
                
    # print prepare to fight prompts
    prep_prompt = "\nYou took too long to get out of the city. You've been surrounded by a zombie horde!"
    for letter in prep_prompt:
        write_letter()

    prep_prompt2 = "\nHere's your chance to use those items from earlier to help you fight your way through.\n"
    for letter in prep_prompt2:
        write_letter()

    # item select function: choose an item from inventory - Tim
    def item_select():

        print("\nInventory:", inventory)
        
        # type name of item, add effect to skills and remove from inventory
        use_item = ""
        while use_item != "c" and use_item != "band aids" and use_item != "gluten free bread" and use_item != "vodka" and use_item != "zombie apocalypse survival guide" and use_item != "20 lb dumbbell" and use_item != "running shoes":
            use_item = input("\nType the name of the item you want to use...\nTo continue [C]\n").lower()
            
            if use_item == "band aids":
                skills["health"] += 5
                del inventory["Band Aids"]
                item_select()  
            elif use_item == "gluten free bread":
                skills["health"] += 10
                del inventory["Gluten Free Bread"]
                item_select()
            elif use_item == "vodka":
                skills["health"] += 20
                del inventory["Vodka"]
                item_select()
            elif use_item == "zombie apocalypse survival guide":
                skills["intelligence"] += 1
                del inventory["Zombie Apocalypse Survival Guide"]
                item_select()    
            elif use_item == "20 lb dumbbell":
                skills["strength"] += 1
                del inventory["20 lb Dumbbell"]
                item_select()       
            elif use_item == "running shoes":
                skills["stamina"] += 1
                del inventory["Running shoes"]
                item_select()
            elif use_item == "c":
                break
            else:
                print("Error: Type the full item name correctly, or C to continue")       
    
    item_select()

    check_menu()

    #class to make zombies - Anant
    class Zombies():
        ATTRIBUTES = {'Health': 0, 'Attack' : 0}
        def __init__(self):
            self.ATTRIBUTES['Health'] += random.randint(55, 75)
            self.ATTRIBUTES['Attack'] += random.randint(30, 55)
        def __str__(self):
            return('Zombie with '+ str(self.getHealth()) + ' health and ' + str(self.getAttack()) + ' attack')
        def getHealth(self):
            return(self.ATTRIBUTES['Health'])
        def getAttack(self):
            return(self.ATTRIBUTES['Attack'])
        def takeDamage(self, damage):
            self.ATTRIBUTES['Health'] -= damage
    
    #special type of zombie reserved for bosses - Anant
    class BossZombies(Zombies):
        ATTRIBUTES = {'Health': 0, 'Attack' : 0}
        def __init__(self, name):
            super(BossZombies, self).__init__()
            self.name = name
            self.ATTRIBUTES['Health'] = Zombies.ATTRIBUTES['Health'] + random.randint(40, 60)
            self.ATTRIBUTES['Attack'] = Zombies.ATTRIBUTES['Attack'] +  random.randint(30, 40)
        def getName(self):
          return (self.name)
        def __str__(self):
            return(super().__str__() + ' named ' + self.getName())
          
    #player death function - Andy 
    def player_death():
        for i in range(5):
            time.sleep(1)
            print(i + 1)
        print("\nYou have died in the struggle. Soon you will join the zombie hordes, and hunt down your missing friends. Sucks to be you.")
        restart()
    
    # combat mechanics function - Andy
    def combat(skills, enemy, weapons):

        while True:

            # intelligence increases critical chance
            crit = skills["intelligence"]
            # strength increases base damage
            base_dmg = skills["strength"]
            # stamina increases chance for a double attack
            extra_attack = skills["stamina"]
            # set player health variable
            player_health = skills["health"]
            # get enemy health and attack from Zombie class
            enemy_health = enemy.getHealth()
            enemy_dmg = enemy.getAttack()

            # choose weapon and attack. Damage calculator
            attack = input("Do you wish to attack? ")
            if attack == "yes" or attack == "Yes":
                print(weapons)
                weapon = input("What do you want to use? ")
                weapon = weapon.lower()
                if re.search("uzi.+9mm", weapon) or re.search("uzi", weapon):
                    player_dmg1 = weapons["Uzi 9mm"]
                    player_dmg1 = int(player_dmg1[0])
                    player_dmg2 = weapons["Uzi 9mm"]
                    player_dmg2 = int(player_dmg2[1])
                    strength_check = base_dmg
                    while strength_check > 0:
                        player_dmg1 += 2
                        player_dmg2 += 2
                        strength_check -= 1
                    player_attack = random.randint(player_dmg1, player_dmg2)
                    crit_check = crit
                    crit_chance = 1
                    while crit_check > 0:
                        crit_chance += 1
                        crit_check -= 1
                    crit_roll = random.randint(crit_chance, 10)
                    if crit_roll >= 5:
                        player_attack = player_attack * 2
                    extra_chance = random.randint(1, extra_attack)
                    if extra_chance >= 3:
                        player_attack = player_attack * 1.5
                    enemy.takeDamage(player_attack)
                    enemy_health = enemy.getHealth()
                    if enemy_health <= 0:
                        print("You did %d damage!" % player_attack)
                        print("Congratulations, you have slayed the zombie!")
                        break
                    print("You did %d damage!" % player_attack)
                    # ranged weapon users have a chance to receive no damage
                    miss = random.randint(1, 5)
                    if miss >= 4:
                        print("Because you were standing so far back the enemy missed.")
                        print("Your health:", player_health)
                        print("Enemy's health:", enemy_health)
                    else:
                        player_health -= enemy_dmg
                        print("The enemy hit you back! It did %d damage." % enemy_dmg)
                        print("Your health:", player_health)
                        print("Enemy's health:", enemy_health)
                        if player_health <= 0:
                        	player_death()
                elif re.search("sword", weapon):
                    player_dmg1 = weapons["Sword"]
                    player_dmg1 = int(player_dmg1[0])
                    player_dmg2 = weapons["Sword"]
                    player_dmg2 = int(player_dmg2[1])
                    strength_check = base_dmg
                    while strength_check > 0:
                        player_dmg1 += 2
                        player_dmg2 += 2
                        strength_check -= 1
                    player_attack = random.randint(player_dmg1, player_dmg2)
                    crit_check = crit
                    crit_chance = 1
                    while crit_check > 0:
                        crit_chance += 1
                        crit_check -= 1
                    crit_roll = random.randint(crit_chance, 10)
                    if crit_roll >= 5:
                        player_attack = player_attack * 2
                    extra_chance = random.randint(1, extra_attack)
                    if extra_chance >= 3:
                        player_attack = player_attack * 1.5
                    enemy.takeDamage(player_attack)
                    enemy_health = enemy.getHealth()
                    if enemy_health <= 0:
                        print("You did %d damage!" % player_attack)
                        print("Congratulations, you have slayed the zombie!")
                        break
                    print("You did %d damage!" % player_attack)
                    player_health -= enemy_dmg
                    print("The Enemy hit you back! It did %d damage." % enemy_dmg)
                    print("Your health:", player_health)
                    print("Enemy's health:", enemy_health)
                    if player_health <= 0:
                    	player_death()
                elif re.search("robotic.+attack.+dogs", weapon):
                    player_dmg1 = weapons["Robotic Attack Dogs"]
                    player_dmg1 = int(player_dmg1[0])
                    player_dmg2 = weapons["Robotic Attack Dogs"]
                    player_dmg2 = int(player_dmg2[1])
                    strength_check = base_dmg
                    while strength_check > 0:
                        player_dmg1 += 2
                        player_dmg2 += 2
                        strength_check -= 1
                    player_attack = random.randint(player_dmg1, player_dmg2)
                    crit_check = crit
                    crit_chance = 1
                    while crit_check > 0:
                        crit_chance += 1
                        crit_check -= 1
                    crit_roll = random.randint(crit_chance, 10)
                    if crit_roll >= 5:
                        player_attack = player_attack * 2
                    extra_chance = random.randint(1, extra_attack)
                    if extra_chance >= 3:
                        player_attack = player_attack * 1.5
                    enemy.takeDamage(player_attack)
                    enemy_health = enemy.getHealth()
                    if enemy_health <= 0:
                        print("You did %d damage!" % player_attack)
                        print("Congratulations, you have slayed the zombie!")
                        break
                    print("You did %d damage!" % player_attack)
                    miss = random.randint(1, 2)
                    if miss == 2:
                        print("Because you were standing so far back the enemy missed.")
                        print("Your health:", player_health)
                        print("Enemy's health:", enemy_health)
                    else:
                        player_health -= enemy_dmg
                        print("The Enemy hit you back! It did %d damage." % enemy_dmg)
                        print("Your health:", player_health)
                        print("Enemy's health:", enemy_health)
                        if player_health <= 0:
                        	player_death()
                elif re.search("phased.+plasma.+rifle", weapon):
                    player_dmg1 = weapons["Phased Plasma Rifle"]
                    player_dmg1 = int(player_dmg1[0])
                    player_dmg2 = weapons["Phased Plasma Rifle"]
                    player_dmg2 = int(player_dmg2[1])
                    strength_check = base_dmg
                    while strength_check > 0:
                        player_dmg1 += 2
                        player_dmg2 += 2
                        strength_check -= 1
                    player_attack = random.randint(player_dmg1, player_dmg2)
                    crit_check = crit
                    crit_chance = 1
                    while crit_check > 0:
                        crit_chance += 1
                        crit_check -= 1
                    crit_roll = random.randint(crit_chance, 10)
                    if crit_roll >= 5:
                        player_attack = player_attack * 2
                    extra_chance = random.randint(1, extra_attack)
                    if extra_chance >= 3:
                        player_attack = player_attack * 1.5
                    enemy.takeDamage(player_attack)
                    enemy_health = enemy.getHealth()
                    if enemy_health <= 0:
                        print("You did %d damage!" % player_attack)
                        print("Congratulations, you have slayed the zombie!")
                        break
                    print("You did %d damage!" % player_attack)
                    miss = random.randint(1, 3)
                    if miss >= 2:
                        print("Because you were standing so far back the enemy missed.")
                        print("Your health:", player_health)
                        print("Enemy's health:", enemy_health)
                    else:
                        player_health -= enemy_dmg
                        print("The enemy hit you back! It did %d damage." % enemy_dmg)
                        print("Your health:", player_health)
                        print("Enemy's health:", enemy_health)
                        if player_health <= 0:
                        	player_death()

            else:
                run = input("Do you wish to run away? ")
                run = run.lower()
                if re.search("yes", run) or re.search(".+yes"):
                    run_chance = random.randint(0, 10)
                    if run_chance > 5:
                        print("Congratulations! You've successfully run away. Coward.")
                        break
                    else:
                        print("Oh bother, looks like you're too tubby to run away. Probably all that honey you've been eating.")
	
    print("A zombie approaches you, get ready to fight")
    zombie1 = Zombies()
    zombie2 = Zombies()
    combat(skills, zombie1, weapons)
    print("While you were fending off the first zombie another one leaps to attack you")
    combat(skills, zombie2, weapons)
    arnold = BossZombies("Arnold Schwarzenegger")
    print("You've almost escaped the horde but a gargantuan zombie touting the name " + arnold.getName() + " is blocking your path. Get ready for a difficult fight")
    combat(skills, arnold, weapons)
    
    restart()
    
if __name__ == '__main__':
    game()