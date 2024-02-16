try:
    import os
    from DATA import bows
    from DATA import weapons
    from DATA import shields
    from DATA import armour
    import subprocess
    subprocess.check_output("pip install colorama", shell=True)
    import colorama
    colorama.init()

    commands = ["ALL", "W", "B", "S", "W-", "A"]


    bowData = bows.returnBows()
    bowDescs = bows.returnBowDescs()
    index = -1
    bowNames = []
    bowNamesUpper = []
    for item in bowData:
        index = index + 1
        bowNames.append(item[0])
        bowNamesUpper.append(item[0].upper())


    shieldData = shields.returnShields()
    shieldDescs = shields.returnShieldDesc()
    index = -1
    shieldNames = []
    shieldNamesUpper = []
    for item in shieldData:
        index = index + 1
        shieldNames.append(item[0])
        shieldNamesUpper.append(item[0].upper())


    weaponData = weapons.returnWeapons()
    weaponDescs = weapons.returnWeaponDescs()
    index = -1
    weaponNames = []
    weaponNamesUpper = []
    for item in weaponData:
        index = index + 1
        weaponNames.append(item[0])
        weaponNamesUpper.append(item[0].upper())


    pristineWeaponData = weapons.returnPristineWeapons()
    pristineWeaponDescs = weapons.returnPristineWeaponDescs()
    index = -1
    pristineWeaponNames = []
    pristineWeaponNamesUpper = []
    for item in pristineWeaponData:
        index = index + 1
        pristineWeaponNames.append(item[0])
        pristineWeaponNamesUpper.append(item[0].upper())


    armourData = armour.returnFamilies()
    index = -1
    armourNames = []
    armourNamesUpper = []
    armourSpecial = []
    armourSetBonus = []
    for item in armourData:
        index = index + 1
        armourNames.append(item[0])
        armourNamesUpper.append(item[0].upper())
        armourSpecial.append(item[2])
        armourSetBonus.append(item[3])

    while True:
        print(f"Welcome to the {colorama.Fore.LIGHTMAGENTA_EX}Tears of the Kingdom Equipment Dictionary!{colorama.Style.RESET_ALL}")
        print(f"{colorama.Fore.LIGHTBLACK_EX}(Type a Shield, Weapon, or Bow name...){colorama.Style.RESET_ALL}")
        valid = False
        
        while valid == False:
            request = input(">>> ")
            
            if request.upper() in shieldNamesUpper or request.upper() in weaponNamesUpper or request.upper() in bowNamesUpper or request.upper() in armourNamesUpper:
                valid = True
            else:
                if request.upper() in commands:
                    valid = True
                else:
                    valid = False
        
        
        
        #Shields
        if request.upper() in shieldNamesUpper:
            idx = shieldNamesUpper.index(request.upper())
            index = -1
            
            for item in shieldData:
                index = index + 1
                if item[0].upper() == request.upper():
                    info = item
                    break
            
            defense = info[1]
            durability = info[2]
            material = info[3]
            locations = info[4]
            tier = info[5]
            
            efficiency = round((defense * durability)/18, 1)
            efficiency = float(efficiency)
            if efficiency < 1:
                eColour = colorama.Fore.RED
            if efficiency >=4 and efficiency < 12:
                eColour = colorama.Fore.LIGHTRED_EX
            if efficiency >= 12 and efficiency < 20:
                eColour = colorama.Fore.LIGHTYELLOW_EX
            if efficiency >=20 and efficiency < 32:
                eColour = colorama.Fore.LIGHTGREEN_EX
            if efficiency >= 32 and efficiency < 40:
                eColour = colorama.Fore.GREEN
            if efficiency >= 40 and efficiency < 160.4:
                eColour = colorama.Fore.BLUE
            if efficiency >= 160.4 and efficiency < 360:
                eColour = colorama.Fore.LIGHTBLUE_EX
            if efficiency > 360:
                eColour = colorama.Fore.LIGHTMAGENTA_EX
            
            if defense <= 10:
                defenseLevel = "Low"
                defenseColour = colorama.Fore.RED
            if defense > 10 and defense <= 30:
                defenseLevel = "Low-mid"
                defenseColour = colorama.Fore.YELLOW
            if defense > 30 and defense <= 60:
                defenseLevel = "High-mid"
                defenseColour = colorama.Fore.LIGHTGREEN_EX
            if defense > 60 and defense < 90:
                defenseLevel = "High"
                defenseColour = colorama.Fore.LIGHTGREEN_EX
            if defense == 90:
                defenseLevel = "Very high"
                defenseColour = colorama.Fore.LIGHTMAGENTA_EX
            
            if durability <= 5:
                durabilityLevel = "Low"
                durabilityColour = colorama.Fore.RED
            if durability > 5 and durability <= 10:
                durabilityLevel = "Low-mid"
                durabilityColour = colorama.Fore.YELLOW
            if durability > 10 and durability <= 20:
                durabilityLevel = "High-mid"
                durabilityColour = colorama.Fore.LIGHTGREEN_EX
            if durability > 20 and durability <= 50:
                durabilityLevel = "High"
                durabilityColour = colorama.Fore.LIGHTGREEN_EX
            if durability >50 and durability <= 100:
                durabilityLevel = "Very high"
                durabilityColour = colorama.Fore.LIGHTCYAN_EX
            if durability == 800:
                durabilityLevel = "Extremely High"
                durabilityColour = colorama.Fore.LIGHTMAGENTA_EX
            
            if material == "Wood":
                materialColour = colorama.Fore.YELLOW
                materialDesc = "(This shield will " + colorama.Fore.RED + "burn " + colorama.Style.RESET_ALL + "if in contact with " + colorama.Fore.RED + "fire" + colorama.Style.RESET_ALL + ".)"
            elif material == "Metal":
                materialColour = colorama.Fore.LIGHTBLACK_EX
                materialDesc = "(This shield will attract " + colorama.Fore.LIGHTYELLOW_EX + "lightning " + colorama.Style.RESET_ALL + "during a " + colorama.Fore.LIGHTYELLOW_EX + "thunderstorm" + colorama.Style.RESET_ALL + ".)"
            elif material == "Zonaite":
                materialColour = colorama.Fore.GREEN
                materialDesc = "(This shield is impervious to both" + colorama.Fore.RED + " fire " + colorama.Style.RESET_ALL + "and " + colorama.Fore.LIGHTYELLOW_EX + "electricity" + colorama.Style.RESET_ALL + ".)"
            
            locationStr = ""
            finalIdx = len(locations) -1
            index = -1
            for item in locations:
                index = index + 1
                if "Akkala" in item:
                    locationColour = colorama.Fore.YELLOW
                elif "Hyrule" in item:
                    locationColour = colorama.Fore.LIGHTGREEN_EX
                elif "Eldin" in item:
                    locationColour = colorama.Fore.RED
                elif "Faron" in item:
                    locationColour = colorama.Fore.GREEN
                elif "Gerudo" in item:
                    locationColour = colorama.Fore.YELLOW
                elif "Hebra" in item:
                    locationColour = colorama.Fore.LIGHTBLUE_EX
                elif "Lanayru" in item:
                    locationColour = colorama.Fore.BLUE
                elif "Necluda" in item:
                    locationColour = colorama.Fore.BLUE
                else:
                    locationColour = ""
                if "Hyrule Castle" in item:
                    locationColour = colorama.Fore.LIGHTBLACK_EX
                    
                if index != finalIdx:
                    locationStr = locationStr + locationColour + item + colorama.Style.RESET_ALL +  ", "
                else:
                    locationStr = locationStr + locationColour + item + colorama.Style.RESET_ALL
            
            if tier == "F":
                tierColour = colorama.Fore.RED
            if tier == "E":
                tierColour = colorama.Fore.RED
            if tier == "D":
                tierColour = colorama.Fore.LIGHTRED_EX
            if tier == "C":
                tierColour = colorama.Fore.YELLOW
            if tier == "B":
                tierColour = colorama.Fore.GREEN
            if tier == "A":
                tierColour = colorama.Fore.LIGHTGREEN_EX
            if tier == "S":
                tierColour = colorama.Fore.BLUE
            if tier == "S+":
                tierColour = colorama.Fore.LIGHTBLUE_EX
            if tier == "X":
                tierColour = colorama.Fore.LIGHTMAGENTA_EX
            
            shieldName = shieldNames[idx]
            if "Hylian" in shieldName:
                nameColour = colorama.Fore.BLUE
            elif "Zora" in shieldName:
                nameColour = colorama.Fore.BLUE
            elif "Gerudo" in shieldName:
                nameColour = colorama.Fore.YELLOW
            elif "Kite" in shieldName:
                nameColour = colorama.Fore.LIGHTBLUE_EX
            elif "Royal" in shieldName and "Royal Guard's" not in shieldName:
                nameColour = colorama.Fore.LIGHTYELLOW_EX
            elif "Royal Guard's" in shieldName:
                nameColour = colorama.Fore.MAGENTA
            else:
                nameColour = ""
            
            print("------\n- " + nameColour + shieldNames[idx] + colorama.Style.RESET_ALL + "\n------\n'" + shieldDescs[idx] + "'\n------")
            print(f"Defense: {defenseColour}{defense}{colorama.Style.RESET_ALL} ({defenseColour}{defenseLevel}{colorama.Style.RESET_ALL})")
            print(f"Durability: {durabilityColour}{durability}{colorama.Style.RESET_ALL} ({durabilityColour}{durabilityLevel}{colorama.Style.RESET_ALL})")
            print(f"Material: {materialColour}{material}{colorama.Style.RESET_ALL} {materialDesc}")
            print(f"Locations Found: {locationStr}")
            print(f"Tier: {tierColour}{tier}{colorama.Style.RESET_ALL}")
            print("------")
            print(f"Efficiency: {eColour}{efficiency}{colorama.Style.RESET_ALL}")
            print("------")
        ######################################################################
        
        
        
        #Non-pristine weapons
        if request.upper() in weaponNamesUpper:
            idx = weaponNamesUpper.index(request.upper())
            desc = weaponDescs[idx]
            index = -1
            
            for item in weaponData:
                index = index + 1
                if item[0].upper() == request.upper():
                    info = item
                    break
        
            name = info[0]
            attack = info[1]
            trueAttack = info[2]
            durability = info[3]
            material = info[4]
            state = info[5]
            type = info[6]
            special = info[7]
            locations = info[8]
            tier = info[9]

            if name != "Master Sword":
                efficiency = (int(trueAttack)*int(durability))/12
            else:
                efficiency = 100.0

            if efficiency < 15:
                effiColour = colorama.Fore.RED
            if efficiency >=15 and efficiency <30:
                effiColour = colorama.Fore.LIGHTYELLOW_EX
            if efficiency >= 30 and efficiency < 60:
                effiColour = colorama.Fore.GREEN
            if efficiency >= 60 and efficiency < 90:
                effiColour = colorama.Fore.LIGHTGREEN_EX
            if efficiency >=90 and efficiency < 120:
                effiColour = colorama.Fore.BLUE
            if efficiency >= 120:
                effiColour = colorama.Fore.LIGHTMAGENTA_EX
            
            specialUp = special.upper()
            if "BREAKING POINT" in specialUp:
                specialColour = colorama.Fore.LIGHTMAGENTA_EX
            elif "CHARGE ATTACK" in specialUp:
                specialColour = colorama.Fore.LIGHTGREEN_EX
            elif "DEMOLISHER" in specialUp:
                specialColour = colorama.Fore.RED
            elif "DESPERATE" in specialUp:
                specialColour = colorama.Fore.RED
            elif "EXTRA" in specialUp:
                specialColour = colorama.Fore.LIGHTCYAN_EX
            elif "RECYCLING" in specialUp:
                specialColour = colorama.Fore.GREEN
            elif "STRONG FUSION" in specialUp:
                specialColour = colorama.Fore.LIGHTYELLOW_EX
            elif "WATER WARRIOR" in specialUp:
                specialColour = colorama.Fore.BLUE
            elif "WIND BURST" in specialUp:
                specialColour = colorama.Fore.LIGHTBLUE_EX
            elif "IMPROVED FLURRY RUSH" in specialUp:
                specialColour = colorama.Fore.LIGHTCYAN_EX
            elif "WIND RAZOR" in specialUp:
                specialColour = colorama.Fore.LIGHTBLUE_EX
            elif "NO SPECIAL ABILITY" in specialUp:
                specialColour = colorama.Fore.RED
            elif "REVITALIZED" in specialUp:
                specialColour = colorama.Fore.BLUE
            elif "GLOOM" in specialUp:
                specialColour = colorama.Fore.CYAN
            else:
                specialColour = ""
            
            
            if state == "Normal":
                stateColour = colorama.Fore.LIGHTGREEN_EX
            elif state == "Decayed":
                stateColour = colorama.Fore.LIGHTBLACK_EX
        
            if type == "One-handed":
                typeColour = colorama.Fore.LIGHTGREEN_EX
            if type == "Two-handed":
                typeColour = colorama.Fore.LIGHTYELLOW_EX
            if type == "Spear":
                typeColour = colorama.Fore.LIGHTMAGENTA_EX
            
            if attack <= 5:
                attackLevel = "Low"
                attackColour = colorama.Fore.RED
            if attack > 5 and attack <= 15:
                attackLevel = "Low-mid"
                attackColour = colorama.Fore.YELLOW
            if attack > 15 and attack <= 35:
                attackLevel = "High-mid"
                attackColour = colorama.Fore.LIGHTGREEN_EX
            if attack > 35 and attack < 50:
                attackLevel = "High"
                attackColour = colorama.Fore.LIGHTGREEN_EX
            if attack == 50:
                attackLevel = "Very high"
                attackColour = colorama.Fore.LIGHTMAGENTA_EX
        
            if name != "Master Sword":
                if trueAttack <= 5:
                    trueAttackLevel = "Low"
                    trueAttackColour = colorama.Fore.RED
                if trueAttack > 5 and trueAttack <= 15:
                    trueAttackLevel = "Low-mid"
                    trueAttackColour = colorama.Fore.YELLOW
                if trueAttack > 15 and trueAttack <= 35:
                    trueAttackLevel = "High-mid"
                    trueAttackColour = colorama.Fore.LIGHTGREEN_EX
                if trueAttack > 35 and trueAttack < 50:
                    trueAttackLevel = "High"
                    trueAttackColour = colorama.Fore.LIGHTGREEN_EX
                if trueAttack == 50:
                    trueAttackLevel = "Very high"
                    trueAttackColour = colorama.Fore.LIGHTMAGENTA_EX
            else:
                trueAttackLevel = "High"
                trueAttackColour = colorama.Fore.LIGHTGREEN_EX
        
            if name != "Master Sword":
                if durability <= 10:
                    durabilityLevel = "Low"
                    durabilityColour = colorama.Fore.RED
                if durability > 10 and durability <= 20:
                    durabilityLevel = "Low-mid"
                    durabilityColour = colorama.Fore.YELLOW
                if durability > 20 and durability <= 30:
                    durabilityLevel = "High-mid"
                    durabilityColour = colorama.Fore.LIGHTGREEN_EX
                if durability > 30 and durability <= 50:
                    durabilityLevel = "High"
                    durabilityColour = colorama.Fore.LIGHTGREEN_EX
                if durability >50 and durability <= 70:
                    durabilityLevel = "Very high"
                    durabilityColour = colorama.Fore.LIGHTCYAN_EX
                if durability == 70:
                    durabilityLevel = "Extremely High"
                    durabilityColour = colorama.Fore.LIGHTMAGENTA_EX
            else:
                durabilityLevel = "High"
                durabilityColour = colorama.Fore.LIGHTGREEN_EX
        
            
            locationStr = ""
            finalIdx = len(locations) -1
            index = -1
            for item in locations:
                index = index + 1
                if "Akkala" in item:
                    locationColour = colorama.Fore.YELLOW
                elif "Hyrule" in item:
                    locationColour = colorama.Fore.LIGHTGREEN_EX
                elif "Eldin" in item:
                    locationColour = colorama.Fore.RED
                elif "Faron" in item:
                    locationColour = colorama.Fore.GREEN
                elif "Gerudo" in item:
                    locationColour = colorama.Fore.YELLOW
                elif "Hebra" in item:
                    locationColour = colorama.Fore.LIGHTBLUE_EX
                elif "Lanayru" in item:
                    locationColour = colorama.Fore.BLUE
                elif "Necluda" in item:
                    locationColour = colorama.Fore.BLUE
                elif "Light Dragon" in item:
                    locationColour = colorama.Fore.LIGHTBLUE_EX
                elif "Sky Island" in item:
                    locationColour = colorama.Fore.LIGHTYELLOW_EX
                else:
                    locationColour = ""
                if "Hyrule Castle" in item:
                    locationColour = colorama.Fore.LIGHTBLACK_EX
                if "Depths" in item:
                    locationColour = colorama.Fore.MAGENTA
                    
                if index != finalIdx:
                    locationStr = locationStr + locationColour + item + colorama.Style.RESET_ALL +  ", "
                else:
                    locationStr = locationStr + locationColour + item + colorama.Style.RESET_ALL
            
            
            if tier == "F":
                tierColour = colorama.Fore.RED
            if tier == "E":
                tierColour = colorama.Fore.RED
            if tier == "D":
                tierColour = colorama.Fore.LIGHTRED_EX
            if tier == "C":
                tierColour = colorama.Fore.YELLOW
            if tier == "B":
                tierColour = colorama.Fore.GREEN
            if tier == "A":
                tierColour = colorama.Fore.LIGHTGREEN_EX
            if tier == "S":
                tierColour = colorama.Fore.BLUE
            if tier == "S+":
                tierColour = colorama.Fore.LIGHTMAGENTA_EX
            if tier == "Legendary":
                tierColour = colorama.Fore.LIGHTYELLOW_EX
            
            if material == "Wood":
                materialColour = colorama.Fore.YELLOW
                materialDesc = "(This weapon will " + colorama.Fore.RED + "burn " + colorama.Style.RESET_ALL + "if in contact with " + colorama.Fore.RED + "fire" + colorama.Style.RESET_ALL + ".)"
            elif material == "Metal":
                materialColour = colorama.Fore.LIGHTBLACK_EX
                materialDesc = "(This weapon will attract " + colorama.Fore.LIGHTYELLOW_EX + "lightning " + colorama.Style.RESET_ALL + "during a " + colorama.Fore.LIGHTYELLOW_EX + "thunderstorm" + colorama.Style.RESET_ALL + ".)"
            elif material == "Zonaite":
                materialColour = colorama.Fore.GREEN
                materialDesc = "(This weapon is impervious to both" + colorama.Fore.RED + " fire " + colorama.Style.RESET_ALL + "and " + colorama.Fore.LIGHTYELLOW_EX + "electricity" + colorama.Style.RESET_ALL + ".)"
            elif material == "Unknown":
                materialColour = colorama.Fore.RED
                materialDesc = "(I have no clue what material this weapon is made of.)"
        
            if tier != "Legendary" and name != "Master Sword":
                print("------\n- " + name + "\n------\n'" + desc + "'\n------")
            elif tier == "Legendary" and name != "Master Sword":
                print("------\n- " + tierColour + name + colorama.Style.RESET_ALL + "\n------\n'" + desc + "'\n------")
            else:
                print("------\n- " + colorama.Fore.BLUE + name + colorama.Style.RESET_ALL + "\n------\n'" + desc + "'\n------")
        
        
            
            print(f"Attack Power: {attackColour}{attack}{colorama.Style.RESET_ALL} ({attackColour}{attackLevel}{colorama.Style.RESET_ALL})")
            
            if name != "Master Sword":
                print(f"True Attack Power: {trueAttackColour}{trueAttack}{colorama.Style.RESET_ALL} ({trueAttackColour}{trueAttackLevel}{colorama.Style.RESET_ALL})")
            else:
                print(f"True Attack Power: {trueAttackColour}{trueAttack[0:3]}{colorama.Style.RESET_ALL}{trueAttack[3:len(trueAttack)]} ({trueAttackColour}{trueAttackLevel}{colorama.Style.RESET_ALL})")
        
            if name != "Master Sword":
                print(f"Durability: {durabilityColour}{durability}{colorama.Style.RESET_ALL} ({durabilityColour}{durabilityLevel}{colorama.Style.RESET_ALL})")
            else:
                print(f"Durability: {durabilityColour}{durability[0:2]}{colorama.Style.RESET_ALL}{durability[2:len(durability)]} ({durabilityColour}{durabilityLevel}{colorama.Style.RESET_ALL})")
                
            print(f"Material: {materialColour}{material}{colorama.Style.RESET_ALL} {materialDesc}")
            
            print(f"State: {stateColour}{state}{colorama.Style.RESET_ALL}")
            print(f"Type: {typeColour}{type}{colorama.Style.RESET_ALL}")
            if " - " in special:
                specialList = special.split(" - ")
                print(f"Special Ability: {specialColour}{specialList[0]}{colorama.Style.RESET_ALL} - {specialList[1]}")
            else:
                print(f"Special Ability: {specialColour}{special}{colorama.Style.RESET_ALL}")
                
            print(f"Locations Found: {locationStr}")
            print(f"Tier: {tierColour}{tier}{colorama.Style.RESET_ALL} ({stateColour}{state}{colorama.Style.RESET_ALL})")
            print("------")
            print(f"Efficiency: {effiColour}{round(efficiency, 1)}{colorama.Style.RESET_ALL}")
            print("------")
        
        
            if name in pristineWeaponNames: 
                idx = pristineWeaponNamesUpper.index(request.upper())
                desc = pristineWeaponDescs[idx]
                index = -1
                
                for item in pristineWeaponData:
                    index = index + 1
                    if item[0].upper() == request.upper():
                        info = item
                        break
        
        
                name = info[0]
                attack = info[1]
                trueAttack = info[2]
                durability = info[3]
                material = info[4]
                state = info[5]
                type = info[6]
                special = info[7]
                locations = info[8]
                tier = info[9]
            
                specialUp = special.upper()
                
                if "BREAKING POINT" in specialUp:
                    specialColour = colorama.Fore.LIGHTMAGENTA_EX
                elif "CHARGE ATTACK" in specialUp:
                    specialColour = colorama.Fore.LIGHTGREEN_EX
                elif "DEMOLISHER" in specialUp:
                    specialColour = colorama.Fore.RED
                elif "DESPERATE" in specialUp:
                    specialColour = colorama.Fore.RED
                elif "EXTRA" in specialUp:
                    specialColour = colorama.Fore.LIGHTCYAN_EX
                elif "RECYCLING" in specialUp:
                    specialColour = colorama.Fore.GREEN
                elif "STRONG FUSION" in specialUp:
                    specialColour = colorama.Fore.LIGHTYELLOW_EX
                elif "WATER WARRIOR" in specialUp:
                    specialColour = colorama.Fore.BLUE
                elif "WIND BURST" in specialUp:
                    specialColour = colorama.Fore.LIGHTBLUE_EX
                elif "IMPROVED FLURRY RUSH" in specialUp:
                    specialColour = colorama.Fore.LIGHTCYAN_EX
                elif "WIND RAZOR" in specialUp:
                    specialColour = colorama.Fore.LIGHTBLUE_EX
                elif "NO SPECIAL ABILITY" in specialUp:
                    specialColour = colorama.Fore.RED
                elif "REVITALIZED" in specialUp:
                    specialColour = colorama.Fore.BLUE
                else:
                    specialColour = ""

                
                if type == "One-handed":
                    typeColour = colorama.Fore.LIGHTGREEN_EX
                if type == "Two-handed":
                    typeColour = colorama.Fore.LIGHTYELLOW_EX
                if type == "Spear":
                    typeColour = colorama.Fore.LIGHTMAGENTA_EX
                
                if attack <= 5:
                    attackLevel = "Low"
                    attackColour = colorama.Fore.RED
                if attack > 5 and attack <= 15:
                    attackLevel = "Low-mid"
                    attackColour = colorama.Fore.YELLOW
                if attack > 15 and attack <= 35:
                    attackLevel = "High-mid"
                    attackColour = colorama.Fore.LIGHTGREEN_EX
                if attack > 35 and attack < 50:
                    attackLevel = "High"
                    attackColour = colorama.Fore.LIGHTGREEN_EX
                if attack == 50:
                    attackLevel = "Very high"
                    attackColour = colorama.Fore.LIGHTMAGENTA_EX
            
                if name != "Master Sword":
                    if trueAttack <= 5:
                        trueAttackLevel = "Low"
                        trueAttackColour = colorama.Fore.RED
                    if trueAttack > 5 and trueAttack <= 15:
                        trueAttackLevel = "Low-mid"
                        trueAttackColour = colorama.Fore.YELLOW
                    if trueAttack > 15 and trueAttack <= 35:
                        trueAttackLevel = "High-mid"
                        trueAttackColour = colorama.Fore.LIGHTGREEN_EX
                    if trueAttack > 35 and trueAttack < 50:
                        trueAttackLevel = "High"
                        trueAttackColour = colorama.Fore.LIGHTGREEN_EX
                    if trueAttack == 50:
                        trueAttackLevel = "Very high"
                        trueAttackColour = colorama.Fore.LIGHTMAGENTA_EX
                else:
                    trueAttackLevel = "High"
                    trueAttackColour = colorama.Fore.LIGHTGREEN_EX
            
                if name != "Master Sword":
                    if durability <= 10:
                        durabilityLevel = "Low"
                        durabilityColour = colorama.Fore.RED
                    if durability > 10 and durability <= 20:
                        durabilityLevel = "Low-mid"
                        durabilityColour = colorama.Fore.YELLOW
                    if durability > 20 and durability <= 30:
                        durabilityLevel = "High-mid"
                        durabilityColour = colorama.Fore.LIGHTGREEN_EX
                    if durability > 30 and durability <= 50:
                        durabilityLevel = "High"
                        durabilityColour = colorama.Fore.LIGHTGREEN_EX
                    if durability >50 and durability <= 70:
                        durabilityLevel = "Very high"
                        durabilityColour = colorama.Fore.LIGHTCYAN_EX
                    if durability == 70:
                        durabilityLevel = "Extremely High"
                        durabilityColour = colorama.Fore.LIGHTMAGENTA_EX
                else:
                    durabilityLevel = "High"
                    durabilityColour = colorama.Fore.LIGHTGREEN_EX
            
                
                locationStr = ""
                finalIdx = len(locations) -1
                index = -1
                for item in locations:
                    index = index + 1
                    if "Akkala" in item:
                        locationColour = colorama.Fore.YELLOW
                    elif "Hyrule" in item:
                        locationColour = colorama.Fore.LIGHTGREEN_EX
                    elif "Eldin" in item:
                        locationColour = colorama.Fore.RED
                    elif "Faron" in item:
                        locationColour = colorama.Fore.GREEN
                    elif "Gerudo" in item:
                        locationColour = colorama.Fore.YELLOW
                    elif "Hebra" in item:
                        locationColour = colorama.Fore.LIGHTBLUE_EX
                    elif "Lanayru" in item:
                        locationColour = colorama.Fore.BLUE
                    elif "Necluda" in item:
                        locationColour = colorama.Fore.BLUE
                    elif "Light Dragon" in item:
                        locationColour = colorama.Fore.LIGHTBLUE_EX
                    elif "Sky Island" in item:
                        locationColour = colorama.Fore.LIGHTYELLOW_EX
                    else:
                        locationColour = ""
                    if "Hyrule Castle" in item:
                        locationColour = colorama.Fore.LIGHTBLACK_EX
                    if "Depths" in item:
                        locationColour = colorama.Fore.MAGENTA
                        
                    if index != finalIdx:
                        locationStr = locationStr + locationColour + item + colorama.Style.RESET_ALL +  ", "
                    else:
                        locationStr = locationStr + locationColour + item + colorama.Style.RESET_ALL
                
                
                if tier == "F":
                    tierColour = colorama.Fore.RED
                if tier == "E":
                    tierColour = colorama.Fore.RED
                if tier == "D":
                    tierColour = colorama.Fore.LIGHTRED_EX
                if tier == "C":
                    tierColour = colorama.Fore.YELLOW
                if tier == "B":
                    tierColour = colorama.Fore.GREEN
                if tier == "A":
                    tierColour = colorama.Fore.LIGHTGREEN_EX
                if tier == "S":
                    tierColour = colorama.Fore.BLUE
                if tier == "S+":
                    tierColour = colorama.Fore.LIGHTMAGENTA_EX
                if tier == "Legendary":
                    tierColour = colorama.Fore.LIGHTYELLOW_EX
                
                if material == "Wood":
                    materialColour = colorama.Fore.YELLOW
                    materialDesc = "(This weapon will " + colorama.Fore.RED + "burn " + colorama.Style.RESET_ALL + "if in contact with " + colorama.Fore.RED + "fire" + colorama.Style.RESET_ALL + ".)"
                elif material == "Metal":
                    materialColour = colorama.Fore.LIGHTBLACK_EX
                    materialDesc = "(This weapon will attract " + colorama.Fore.LIGHTYELLOW_EX + "lightning " + colorama.Style.RESET_ALL + "during a " + colorama.Fore.LIGHTYELLOW_EX + "thunderstorm" + colorama.Style.RESET_ALL + ".)"
                elif material == "Zonaite":
                    materialColour = colorama.Fore.GREEN
                    materialDesc = "(This weapon is impervious to both" + colorama.Fore.RED + " fire " + colorama.Style.RESET_ALL + "and " + colorama.Fore.LIGHTYELLOW_EX + "electricity" + colorama.Style.RESET_ALL + ".)"
                elif material == "Unknown":
                    materialColour = colorama.Fore.RED
                    materialDesc = "(I have no clue what material this weapon is made of.)"
        
                stateColour = colorama.Fore.LIGHTMAGENTA_EX
                print("This weapon has a " + colorama.Fore.LIGHTMAGENTA_EX + "pristine" + colorama.Style.RESET_ALL + " counterpart.")
                print("------\n- " + name + "✨\n------\n'" + desc + "'\n------")
                print(f"Attack Power: {attackColour}{attack}{colorama.Style.RESET_ALL} ({attackColour}{attackLevel}{colorama.Style.RESET_ALL})")
                print(f"True Attack Power: {trueAttackColour}{trueAttack}{colorama.Style.RESET_ALL} ({trueAttackColour}{trueAttackLevel}{colorama.Style.RESET_ALL})")
                print(f"Durability: {durabilityColour}{durability}{colorama.Style.RESET_ALL} ({durabilityColour}{durabilityLevel}{colorama.Style.RESET_ALL})")
                print(f"Material: {materialColour}{material}{colorama.Style.RESET_ALL} {materialDesc}")
                print(f"State: {stateColour}{state}{colorama.Style.RESET_ALL}")
                print(f"Type: {typeColour}{type}{colorama.Style.RESET_ALL}")
                if " - " in special:
                    specialList = special.split(" - ")
                    print(f"Special Ability: {specialColour}{specialList[0]}{colorama.Style.RESET_ALL} - {specialList[1]}")
                else:
                    print(f"Special Ability: {specialColour}{special}{colorama.Style.RESET_ALL}")
                    
                print(f"Locations Found: {locationStr}")
                print(f"Tier: {tierColour}{tier}{colorama.Style.RESET_ALL} ({stateColour}{state}{colorama.Style.RESET_ALL})")
                print("------")
                if name != "Master Sword":
                    efficiency = (int(trueAttack)*int(durability))/12
                else:
                    efficiency = 100.0
                if efficiency < 15:
                    effiColour = colorama.Fore.RED
                if efficiency >=15 and efficiency <30:
                    effiColour = colorama.Fore.LIGHTYELLOW_EX
                if efficiency >= 30 and efficiency < 60:
                    effiColour = colorama.Fore.GREEN
                if efficiency >= 60 and efficiency < 90:
                    effiColour = colorama.Fore.LIGHTGREEN_EX
                if efficiency >=90 and efficiency < 120:
                    effiColour = colorama.Fore.BLUE
                if efficiency >= 120:
                    effiColour = colorama.Fore.LIGHTMAGENTA_EX
                print(f"Efficiency: {effiColour}{round(efficiency, 1)}{colorama.Style.RESET_ALL}")
                print("------")

        

        if request.upper() in bowNamesUpper:
            idx = bowNamesUpper.index(request.upper())
            desc = bowDescs[idx]
            index = -1
            
            for item in bowData:
                index = index + 1
                if item[0].upper() == request.upper():
                    info = item
                    break
                    
            name = info[0]
            attack = str(info[1])
            totalAttack = eval(attack)
            durability = info[2]
            range = info[3]
            material = info[4]
            special = info[5]
            locations = info[6]
            tier = info[7]

            locationStr = ""
            finalIdx = len(locations) -1
            index = -1
            for item in locations:
                index = index + 1
                if "Akkala" in item:
                    locationColour = colorama.Fore.YELLOW
                elif "Hyrule" in item:
                    locationColour = colorama.Fore.LIGHTGREEN_EX
                elif "Eldin" in item:
                    locationColour = colorama.Fore.RED
                elif "Faron" in item:
                    locationColour = colorama.Fore.GREEN
                elif "Gerudo" in item:
                    locationColour = colorama.Fore.YELLOW
                elif "Hebra" in item:
                    locationColour = colorama.Fore.LIGHTBLUE_EX
                elif "Lanayru" in item:
                    locationColour = colorama.Fore.BLUE
                elif "Necluda" in item:
                    locationColour = colorama.Fore.BLUE
                elif "Light Dragon" in item:
                    locationColour = colorama.Fore.LIGHTBLUE_EX
                elif "Sky Island" in item:
                    locationColour = colorama.Fore.LIGHTYELLOW_EX
                else:
                    locationColour = ""
                if "Hyrule Castle" in item:
                    locationColour = colorama.Fore.LIGHTBLACK_EX
                if "Depths" in item:
                    locationColour = colorama.Fore.MAGENTA
                    
                if index != finalIdx:
                    locationStr = locationStr + locationColour + item + colorama.Style.RESET_ALL +  ", "
                else:
                    locationStr = locationStr + locationColour + item + colorama.Style.RESET_ALL

            
            if material == "Wood":
                    materialColour = colorama.Fore.YELLOW
                    materialDesc = "(This weapon will " + colorama.Fore.RED + "burn " + colorama.Style.RESET_ALL + "if in contact with " + colorama.Fore.RED + "fire" + colorama.Style.RESET_ALL + ".)"
            elif material == "Metal":
                materialColour = colorama.Fore.LIGHTBLACK_EX
                materialDesc = "(This weapon will attract " + colorama.Fore.LIGHTYELLOW_EX + "lightning " + colorama.Style.RESET_ALL + "during a " + colorama.Fore.LIGHTYELLOW_EX + "thunderstorm" + colorama.Style.RESET_ALL + ".)"
            elif material == "Zonaite":
                materialColour = colorama.Fore.GREEN
                materialDesc = "(This weapon is impervious to both" + colorama.Fore.RED + " fire " + colorama.Style.RESET_ALL + "and " + colorama.Fore.LIGHTYELLOW_EX + "electricity" + colorama.Style.RESET_ALL + ".)"
            elif material == "Unknown":
                materialColour = colorama.Fore.RED
                materialDesc = "(I have no clue what material this weapon is made of.)"

            specialUp = special.upper()
                
            if "ZOOM" in specialUp:
                specialColour = colorama.Fore.LIGHTMAGENTA_EX
            elif "COST OF ONE" in specialUp:
                specialColour = colorama.Fore.LIGHTGREEN_EX
            elif "TWILIGHT" in specialUp:
                specialColour = colorama.Fore.RED
            elif "CHARGED" in specialUp:
                specialColour = colorama.Fore.RED
            elif "ROCK OCTOROK" in specialUp:
                specialColour = colorama.Fore.LIGHTCYAN_EX
            else:
                specialColour = ""

            if tier == "F":
                tierColour = colorama.Fore.RED
            if tier == "E":
                tierColour = colorama.Fore.RED
            if tier == "D":
                tierColour = colorama.Fore.LIGHTRED_EX
            if tier == "C":
                tierColour = colorama.Fore.LIGHTYELLOW_EX
            if tier == "B":
                tierColour = colorama.Fore.GREEN
            if tier == "A":
                tierColour = colorama.Fore.LIGHTGREEN_EX
            if tier == "S":
                tierColour = colorama.Fore.BLUE
            if tier == "S+":
                tierColour = colorama.Fore.LIGHTMAGENTA_EX

            if durability <= 10:
                durabilityLevel = "Low"
                durabilityColour = colorama.Fore.RED
            if durability > 10 and durability <= 20:
                durabilityLevel = "Low-mid"
                durabilityColour = colorama.Fore.YELLOW
            if durability > 20 and durability <= 30:
                durabilityLevel = "High-mid"
                durabilityColour = colorama.Fore.LIGHTGREEN_EX
            if durability > 30 and durability <= 50:
                durabilityLevel = "High"
                durabilityColour = colorama.Fore.LIGHTGREEN_EX
            if durability >50 and durability <= 60:
                durabilityLevel = "Very high"
                durabilityColour = colorama.Fore.LIGHTCYAN_EX
            if durability == 60:
                durabilityLevel = "Extremely High"
                durabilityColour = colorama.Fore.LIGHTMAGENTA_EX

            if totalAttack <= 5:
                attackLevel = "Low"
                attackColour = colorama.Fore.RED
            if totalAttack > 5 and totalAttack <= 15:
                attackLevel = "Low-mid"
                attackColour = colorama.Fore.YELLOW
            if totalAttack > 15 and totalAttack <= 35:
                attackLevel = "High-mid"
                attackColour = colorama.Fore.LIGHTGREEN_EX
            if totalAttack > 35 and totalAttack < 50:
                attackLevel = "High"
                attackColour = colorama.Fore.LIGHTGREEN_EX
            if totalAttack >= 50 and totalAttack < 60:
                attackLevel = "Very high"
                attackColour = colorama.Fore.LIGHTMAGENTA_EX
            if totalAttack >= 60:
                attackLevel = "Extremely high"
                attackColour = colorama.Fore.MAGENTA

            if "*" in attack:
                atkCheck = attack[0:2]
                atkCheck = int(atkCheck)

                if atkCheck <= 5:
                    checkLevel = "Low"
                    checkColour = colorama.Fore.RED
                if atkCheck > 5 and atkCheck <= 15:
                    checkLevel = "Low-mid"
                    checkColour = colorama.Fore.YELLOW
                if atkCheck > 15 and atkCheck <= 35:
                    checkLevel = "High-mid"
                    checkColour = colorama.Fore.LIGHTGREEN_EX
                if atkCheck > 35 and atkCheck < 50:
                    checkLevel = "High"
                    checkColour = colorama.Fore.LIGHTGREEN_EX
                if atkCheck >= 50 and atkCheck < 60:
                    checkLevel = "Very high"
                    checkColour = colorama.Fore.LIGHTMAGENTA_EX
                if atkCheck >= 60:
                    checkLevel = "Extremely high"
                    checkColour = colorama.Fore.MAGENTA

            if range == 20:
                rangeLevel = "Low"
                rangeColour = colorama.Fore.RED
            elif range == 30:
                rangeLevel = "Mid"
                rangeColour = colorama.Fore.LIGHTYELLOW_EX
            elif range == 40:
                rangeLevel = "High"
                rangeColour = colorama.Fore.LIGHTGREEN_EX
            else:
                rangeLevel = ""
                rangeColour = ""
                

            
            print("------\n- " + name + "\n------\n'" + desc + "'\n------")
            if "*" in attack:
                print(f"Attack Power: {checkColour}{atkCheck}{colorama.Style.RESET_ALL}{attack[2:len(attack)]} ({checkColour}{checkLevel}{colorama.Style.RESET_ALL})")
            else:
                print(f"Attack Power: {attackColour}{attack}{colorama.Style.RESET_ALL} ({attackColour}{attackLevel}{colorama.Style.RESET_ALL})")
            print(f"Total Attack Power: {attackColour}{totalAttack}{colorama.Style.RESET_ALL} ({attackColour}{attackLevel}{colorama.Style.RESET_ALL})")
            print(f"Durability: {durabilityColour}{durability}{colorama.Style.RESET_ALL} ({durabilityColour}{durabilityLevel}{colorama.Style.RESET_ALL})")
            print(f"Range: {rangeColour}{range}{colorama.Style.RESET_ALL} ({rangeColour}{rangeLevel}{colorama.Style.RESET_ALL})")
            print(f"Material: {materialColour}{material}{colorama.Style.RESET_ALL} {materialDesc}")
            print(f"Special Ability: {specialColour}{special}{colorama.Style.RESET_ALL}")
            print(f"Locations Found: {locationStr}")
            print(f"Tier: {tierColour}{tier}{colorama.Style.RESET_ALL}")
            print("------")


        if request.upper() in armourNamesUpper:
            for item in armourData:
                index = index + 1
                if item[0].upper() == request.upper():
                    info = item
                    break

            name = info[0]
            defenseLevels = info[1]
            specialEffect = info[2]
            setBonus = info[3]
            setItems = info[4]
            dyeable = info[5]

            specialUp = specialEffect.upper()
            if "ATTACK UP" in specialUp:
                specialColour = colorama.Fore.RED
            elif "GLOW" in specialUp:
                specialColour = colorama.Fore.LIGHTGREEN_EX
            elif "NO SPECIAL EFFECTS" in specialUp:
                specialColour = colorama.Fore.RED
            elif "STEALTH UP" in specialUp:
                specialColour = colorama.Fore.LIGHTMAGENTA_EX
            elif "NIGHT SPEED" in specialUp:
                specialColour = colorama.Fore.BLUE
            elif "MOBILITY" in specialUp:
                specialColour = colorama.Fore.LIGHTMAGENTA_EX
            elif "SLIP" in specialUp:
                specialColour = colorama.Fore.LIGHTBLUE_EX
            elif "SWIM" in specialUp:
                specialColour = colorama.Fore.LIGHTBLUE_EX
            elif "GLOW" in specialUp:
                specialColour = colorama.Fore.LIGHTYELLOW_EX
            elif "FLAME" in specialUp:
                specialColour = colorama.Fore.RED
            elif "CLIMB" in specialUp:
                specialColour = colorama.Fore.LIGHTGREEN_EX
            elif "COLD" in specialUp:
                specialColour = colorama.Fore.LIGHTBLUE_EX
            elif "SHOCK" in specialUp:
                specialColour = colorama.Fore.LIGHTYELLOW_EX
            elif "HEAT" in specialUp or "HOT" in specialUp:
                specialColour = colorama.Fore.RED
            elif "GLOOM" in specialUp or "ENERGY" in specialUp:
                specialColour = colorama.Fore.LIGHTCYAN_EX
            elif "RUPEE" in specialUp:
                specialColour = colorama.Fore.LIGHTGREEN_EX
            elif "STORMY" in specialUp:
                specialColour = colorama.Fore.LIGHTYELLOW_EX
            else:
                specialColour = ""


            setUp = setBonus.upper()
            if "NO SET BONUS" in setUp:
                setColour = colorama.Fore.RED
            elif "DISGUISE" in setUp:
                setColour = colorama.Fore.LIGHTMAGENTA_EX
            elif "ATTACK UP" in setUp:
                setColour = colorama.Fore.RED
            elif "NIGHT SPEED" in setUp:
                setColour = colorama.Fore.BLUE
            elif "IMPACT" in setUp:
                setColour = colorama.Fore.LIGHTMAGENTA_EX
            elif "SLIP" in setUp:
                setColour = colorama.Fore.LIGHTBLUE_EX
            elif "SWIM" in setUp:
                setColour = colorama.Fore.LIGHTBLUE_EX
            elif "CHARGE ATK." in setUp:
                setColour = colorama.Fore.LIGHTGREEN_EX
            elif "CLIMBING" in setUp:
                setColour = colorama.Fore.LIGHTGREEN_EX
            elif "LIGHTNING PROOF" in setUp or "SHOCK DAMAGE" in setUp or "STORMY" in setUp:
                setColour = colorama.Fore.LIGHTYELLOW_EX
            elif "FIREPROOF" in setUp:
                setColour = colorama.Fore.RED
            elif "UNFREEZABLE" in setUp:
                setColour = colorama.Fore.LIGHTBLUE_EX
            elif "GLOOM" in setUp or "ENERGY" in setUp:
                setColour = colorama.Fore.LIGHTCYAN_EX
            elif "COLD" in setUp:
                setColour = colorama.Fore.LIGHTBLUE_EX
            elif "HOT" in setUp:
                setColour = colorama.Fore.RED
            else:
                setColour = ""




            
            print(f"------\nThe '{name}' Set\n------")
            if len(defenseLevels) != 1:
                print(f"Upgradable: {colorama.Fore.LIGHTGREEN_EX}Yes.{colorama.Style.RESET_ALL}")
                print(f"Defense Levels:\n  Base - {defenseLevels[0]}\n  {colorama.Fore.RED}Lvl 1 - {defenseLevels[1]}{colorama.Style.RESET_ALL}\n  {colorama.Fore.LIGHTYELLOW_EX}Lvl 2 - {defenseLevels[2]}{colorama.Style.RESET_ALL}\n  {colorama.Fore.LIGHTGREEN_EX}Lvl 3 - {defenseLevels[3]}{colorama.Style.RESET_ALL}\n  {colorama.Fore.BLUE}Lvl 4 - {defenseLevels[4]}{colorama.Style.RESET_ALL}")
            else:
                print(f"Upgradable: {colorama.Fore.RED}No.{colorama.Style.RESET_ALL}")
                print(f"Base Defense: {defenseLevels[0]}")

            if " - " not in specialEffect:
                print(f"Special Effect: {specialColour}{specialEffect}{colorama.Style.RESET_ALL}")
            else:
                specialList = specialEffect.split(" - ")
                print(f"Special Effect: {specialColour}{specialList[0]}{colorama.Style.RESET_ALL} - {specialList[1]}")

            if " - " not in setBonus:
                print(f"Set Bonus: {setColour}{setBonus}{colorama.Style.RESET_ALL}")
            else:
                setBonusList = setBonus.split(" - ")
                print(f"Set Bonus: {setColour}{setBonusList[0]}{colorama.Style.RESET_ALL} - {setBonusList[1]}")
            print(f"Items In Set:\n  {colorama.Fore.RED}Headgear - {setItems[0]}{colorama.Style.RESET_ALL}\n  {colorama.Fore.LIGHTYELLOW_EX}Armour - {setItems[1]}{colorama.Style.RESET_ALL}\n  {colorama.Fore.LIGHTGREEN_EX}Legwear - {setItems[2]}{colorama.Style.RESET_ALL}")
            if "YES" in dyeable.upper():
                dyeableColour = colorama.Fore.LIGHTGREEN_EX
            else:
                dyeableColour = colorama.Fore.RED
            print(f"Dyeable: {dyeableColour}{dyeable}{colorama.Style.RESET_ALL}")
            print("-------")



        if request.upper() in commands:
            command = request.upper()
            if command == "W-":
                index = -1
                print("-------")
                for item in weaponData:
                    index = index + 1
                    info = item
                    tier = info[9]
                    weapon = info[0]

                    trueAttack = info[2]
                    name = info[0]
                    durability = info[3]

                    if name != "Master Sword":
                        efficiency = (int(trueAttack)*int(durability))/12
                    else:
                        efficiency = 100.0
                    if efficiency < 15:
                        effiColour = colorama.Fore.RED
                    if efficiency >=15 and efficiency <30:
                        effiColour = colorama.Fore.LIGHTYELLOW_EX
                    if efficiency >= 30 and efficiency < 60:
                        effiColour = colorama.Fore.GREEN
                    if efficiency >= 60 and efficiency < 90:
                        effiColour = colorama.Fore.LIGHTGREEN_EX
                    if efficiency >=90 and efficiency < 120:
                        effiColour = colorama.Fore.BLUE
                    if efficiency >= 120:
                        effiColour = colorama.Fore.LIGHTMAGENTA_EX
                    if tier == "F":
                        tierColour = colorama.Fore.RED
                    if tier == "E":
                        tierColour = colorama.Fore.RED
                    if tier == "D":
                        tierColour = colorama.Fore.LIGHTRED_EX
                    if tier == "C":
                        tierColour = colorama.Fore.YELLOW
                    if tier == "B":
                        tierColour = colorama.Fore.GREEN
                    if tier == "A":
                        tierColour = colorama.Fore.LIGHTGREEN_EX
                    if tier == "S":
                        tierColour = colorama.Fore.BLUE
                    if tier == "S+":
                        tierColour = colorama.Fore.LIGHTMAGENTA_EX
                    if tier == "Legendary":
                        tierColour = colorama.Fore.LIGHTYELLOW_EX
                    print("- "+ tierColour + tier + ": " + weaponNames[index] + colorama.Style.RESET_ALL + f" - {effiColour}{round(efficiency, 1)}{colorama.Style.RESET_ALL}")
                print("-------")
            if command == "S":
                index = -1
                print("-------")
                for item in shieldData:
                    index = index + 1
                    info = item
                    tier = info[5]
                    shield = info[0]
                    defense = info[1]
                    durability = info[2]

                    efficiency = round((defense * durability)/18, 1)
                    efficiency = float(efficiency)
                    if efficiency < 1:
                        eColour = colorama.Fore.RED
                    if efficiency >=4 and efficiency < 12:
                        eColour = colorama.Fore.LIGHTRED_EX
                    if efficiency >= 12 and efficiency < 20:
                        eColour = colorama.Fore.LIGHTYELLOW_EX
                    if efficiency >=20 and efficiency < 32:
                        eColour = colorama.Fore.LIGHTGREEN_EX
                    if efficiency >= 32 and efficiency < 40:
                        eColour = colorama.Fore.GREEN
                    if efficiency >= 40 and efficiency < 160.4:
                        eColour = colorama.Fore.BLUE
                    if efficiency >= 160.4 and efficiency < 360:
                        eColour = colorama.Fore.LIGHTBLUE_EX
                    if efficiency > 360:
                        eColour = colorama.Fore.LIGHTMAGENTA_EX
                    
                    if tier == "F":
                        tierColour = colorama.Fore.RED
                    if tier == "E":
                        tierColour = colorama.Fore.RED
                    if tier == "D":
                        tierColour = colorama.Fore.LIGHTRED_EX
                    if tier == "C":
                        tierColour = colorama.Fore.YELLOW
                    if tier == "B":
                        tierColour = colorama.Fore.GREEN
                    if tier == "A":
                        tierColour = colorama.Fore.LIGHTGREEN_EX
                    if tier == "S":
                        tierColour = colorama.Fore.BLUE
                    if tier == "S+":
                        tierColour = colorama.Fore.LIGHTBLUE_EX
                    if tier == "X":
                        tierColour = colorama.Fore.LIGHTMAGENTA_EX
                    print("- "+ tierColour + tier + ": " + shieldNames[index] + colorama.Style.RESET_ALL + f" - {eColour}{efficiency}{colorama.Style.RESET_ALL}")
                print("-------")
            if command == "B":
                index = -1
                print("-------")
                for item in bowData:
                    index = index + 1
                    info = item
                    tier = info[7]
                    bow = info[0]
                        
                    if tier == "F":
                        tierColour = colorama.Fore.RED
                    if tier == "E":
                        tierColour = colorama.Fore.RED
                    if tier == "D":
                        tierColour = colorama.Fore.LIGHTRED_EX
                    if tier == "C":
                        tierColour = colorama.Fore.YELLOW
                    if tier == "B":
                        tierColour = colorama.Fore.GREEN
                    if tier == "A":
                        tierColour = colorama.Fore.LIGHTGREEN_EX
                    if tier == "S":
                        tierColour = colorama.Fore.BLUE
                    if tier == "S+":
                        tierColour = colorama.Fore.LIGHTBLUE_EX
                    if tier == "X":
                        tierColour = colorama.Fore.LIGHTMAGENTA_EX
                    print("- "+ tierColour + tier + ": " + bowNames[index] + colorama.Style.RESET_ALL)
                print("-------")
                    

            if command == "W":
                index = -1
                print("-------")
                for item in pristineWeaponData:
                    index = index + 1
                    info = item
                    tier = info[9]
                    name = info[0]
                    
                    trueAttack = info[2]
                    durability = info[3]
                    
                    if name != "Master Sword":
                        efficiency = (int(trueAttack)*int(durability))/12
                    else:
                        efficiency = 100.0

                    if efficiency < 15:
                        effiColour = colorama.Fore.RED
                    if efficiency >=15 and efficiency <30:
                        effiColour = colorama.Fore.LIGHTYELLOW_EX
                    if efficiency >= 30 and efficiency < 60:
                        effiColour = colorama.Fore.GREEN
                    if efficiency >= 60 and efficiency < 90:
                        effiColour = colorama.Fore.LIGHTGREEN_EX
                    if efficiency >=90 and efficiency < 120:
                        effiColour = colorama.Fore.BLUE
                    if efficiency >= 120:
                        effiColour = colorama.Fore.LIGHTMAGENTA_EX
                    
                    weapon = info[0]
                        
                    if tier == "F":
                        tierColour = colorama.Fore.RED
                    if tier == "E":
                        tierColour = colorama.Fore.RED
                    if tier == "D":
                        tierColour = colorama.Fore.LIGHTRED_EX
                    if tier == "C":
                        tierColour = colorama.Fore.YELLOW
                    if tier == "B":
                        tierColour = colorama.Fore.GREEN
                    if tier == "A":
                        tierColour = colorama.Fore.LIGHTGREEN_EX
                    if tier == "S":
                        tierColour = colorama.Fore.BLUE
                    if tier == "S+":
                        tierColour = colorama.Fore.LIGHTMAGENTA_EX
                    if tier == "Legendary":
                        tierColour = colorama.Fore.LIGHTYELLOW_EX
                    print("- "+ tierColour + tier + ": " + pristineWeaponNames[index] + " ✨" + colorama.Style.RESET_ALL + f" - {effiColour}{round(efficiency, 1)}{colorama.Style.RESET_ALL}")
                print("-------")

            if command == "A":
                index = -1
                print("-------")
                for item in armourData:
                    index = index + 1
                    info = item
                    specialEffect = info[2]
                    setBonus = info[3]
                    armourName = info[0]

                    specialUp = specialEffect.upper()
                    if "ATTACK UP" in specialUp:
                        specialColour = colorama.Fore.RED
                    elif "GLOW" in specialUp:
                        specialColour = colorama.Fore.LIGHTGREEN_EX
                    elif "NO SPECIAL EFFECTS" in specialUp:
                        specialColour = colorama.Fore.RED
                    elif "STEALTH UP" in specialUp:
                        specialColour = colorama.Fore.LIGHTMAGENTA_EX
                    elif "NIGHT SPEED" in specialUp:
                        specialColour = colorama.Fore.BLUE
                    elif "MOBILITY" in specialUp:
                        specialColour = colorama.Fore.LIGHTMAGENTA_EX
                    elif "SLIP" in specialUp:
                        specialColour = colorama.Fore.LIGHTBLUE_EX
                    elif "SWIM" in specialUp:
                        specialColour = colorama.Fore.LIGHTBLUE_EX
                    elif "GLOW" in specialUp:
                        specialColour = colorama.Fore.LIGHTYELLOW_EX
                    elif "FLAME" in specialUp:
                        specialColour = colorama.Fore.RED
                    elif "CLIMB" in specialUp:
                        specialColour = colorama.Fore.LIGHTGREEN_EX
                    elif "COLD" in specialUp:
                        specialColour = colorama.Fore.LIGHTBLUE_EX
                    elif "SHOCK" in specialUp:
                        specialColour = colorama.Fore.LIGHTYELLOW_EX
                    elif "HEAT" in specialUp or "HOT" in specialUp:
                        specialColour = colorama.Fore.RED
                    elif "GLOOM" in specialUp or "ENERGY" in specialUp:
                        specialColour = colorama.Fore.LIGHTCYAN_EX
                    elif "RUPEE" in specialUp:
                        specialColour = colorama.Fore.LIGHTGREEN_EX
                    elif "STORMY" in specialUp:
                        specialColour = colorama.Fore.LIGHTYELLOW_EX
                    else:
                        specialColour = ""

                    print("- The " + specialColour + armourNames[index] + colorama.Style.RESET_ALL + " set")
                print("-------")
                    
        input(colorama.Fore.LIGHTBLACK_EX + "Press [ENTER] to search again." + colorama.Style.RESET_ALL)
        os.system("clear")
except Exception as error:
    import time
    print("Error:\n", error)
    time.sleep(60)
            