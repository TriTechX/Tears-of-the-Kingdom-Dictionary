#this is gonna be such a chunky file lol

def returnFamilies():
    global familySyntax, itemSyntax, families, items, setUpgradeCost, setPrices
    #So I hope that I can be a little bit more efficient here with my lists. I'm going to basically just shove the descriptions in the lists here, something that I was afraid of doing because of clutter in the shields, weapons, and bows.

    familySyntax = ["Name", ["Defense Levels"], "Special Effects", "Set Bonus", ["Items in Set"], "Dyeable"]
    itemSyntax = ["Name", ["Location"], "Family", "Description"]
    setUpgradeCost = ["Name", [["Rupees", ["Materials"]], ["Rupees", ["Materials"]], ["Rupees", ["Materials"]], ["Rupees", ["Materials"]]]]
    #if not upgradable, ["Name", [None]]

    
    families = [["Archaic", [1], "No special effects.", "No set bonus.", ["None", "Archaic Tunic", "Archaic Legwear"], "No."],
                ["Hylian", [3, 5, 8, 12, 20], "No special effects.", "No set bonus.", ["Hylian Hood", "Hylian Tunic", "Hylian Trousers"], "Yes."],
                #No tiers
                ["Radiant", [3, 5, 8, 12, 20], "This armour set glows in the dark.", "Disguise; Bone Weap. Prof. - Neutralizes stal enemies, and adds 80% to the whole weapon's attack power of any bone, or bone-fused, weapons.", ["Radiant Mask", "Randiant Shirt", "Radiant Tights"], "Yes."],
                ["Royal Guard", [4, 6, 10, 15, 24], "No special effects.", "Charge Atk. Stamina Up - Reduces the amount of stamina used in charge attacks.", ["Royal Guard Cap", "Royal Guard Uniform", "Royal Guard Boots"], "No."],
                ["Evil Spirit", [4], "Stealth Up", "Disguise; Bone Weap. Prof. - Neutralizes stal enemies, and adds 80% to the whole weapon's attack power of any bone, or bone-fused, weapons.", ["Evil Spirit Mask", "Evil Spirit Armor", "Evil Spirit Greaves"], "No."],
                ["Awakening", [3, 5, 8, 12, 20], "No special effects.", "Attack Up", ["Mask Awakening", "Tunic of Awakening", "Trousers of Awakening"], "No."],
                ["Yiga", [1, 3, 5, 7, 12], "Stealth Up", "Night Speed Up", ["Yiga Mask", "Yiga Armor", "Yiga Tights"], "Yes."],
                ["Wind", [3, 5, 8, 12, 20], "No special effects.", "Attack Up", ["Cap of the Wind", "Tunic of the Wind", "Trousers of the Wind"], "No."],
                ["Wild", [4, 7, 12, 18, 28], "No special effects.", "Attack Up", ["Cap of the Wild", "Tunic of the Wild", "Trousers of the Wild"], "Yes."],
                ["Twilight", [3, 5, 8, 12, 20], "No special effects.", "Attack Up", ["Cap of Twilight", "Tunic of Twilight", "Trousers of Twilight"], "No."],
                ["Tingle's", [2], "No special effects.", "Night Speed Up", ["Tingle's Hood", "Tingle's Shirt", "Tingle's Tights"], "No."],
                ["Time", [3, 5, 8, 12, 20], "No special effects.", "Attack Up", ["Cap of Time", "Tunic of Time", "Trousers of Time"], "No."],
                ["Stealth", [2, 4, 6, 9, 16], "Stealth Up", "Night Speed Up", ["Stealth Mask", "Stealth Chest Guard", "Stealth Tights"], "Yes."],
                ["Sky", [3, 5, 8, 12, 20], "No special effects.", "Attack Up", ["Cap of the Sky", "Tunic of the Sky", "Trousers of the Sky"], "No."],
                ["Hero", [3, 5, 8, 12, 20], "No special effects.", "Attack Up", ["Cap of the Hero", "Tunic of the Hero", "Trousers of the Hero"], "No."],
                ["Soldier", [4, 7, 12, 18, 28], "No special effects.", "No set bonus.", ["Soldier's Helm", "Soldier's Armor", "Soldier's Greaves"], "Yes."],
                ["Glide", [2, 4, 6, 9, 16], "Skydive Mobility Up", "Impact Proof - Negates ALL fall damage.", ["Glide Mask", "Glide Shirt", "Glide Tights"], "Yes."],
                ["Froggy", [3, 5, 8, 12, 20], "Slip Resistance", "Slip Proof - Will no longer slip when climbing in the rain.", ["Froggy Hood", "Froggy Sleeve", "Froggy Leggings"], "Yes."],
                ["Zora", [3, 5, 8, 12, 20], "Swim Speed Up", "Swim Dash Stamina Up - Reduces the amount of stamina used when dashing in water.", ["Zora Helm", "Zora Armor", "Zora Greaves"], "Yes."],
                ["Miner's", [3, 5, 8, 12, 20], "Glow", "Shining Steps - Every few steps you take leave behind glowy remnants.", ["Miner's Mask", "Miner's Top", "Miner's Trousers"], "TBC"],
                ["Flamebreaker", [3, 5, 8, 12, 20], "Flame Guard", "Fireproof - Negates ALL fire damage.", ["Flamebreaker Helm", "Flamebreaker Armor", "Flamebreaker Boots"], "Yes."],
                ["Fierce Deity", [3, 5, 8, 12, 20], "Attack Up", "Charge Atk. Stamina Up - Reduces the amount of stamina used in charge attacks.", ["Fierce Deity Mask", "Fierce Deity Armor", "Fierce Deity Boots"], "No."],
                ["Climbing", [3, 5, 8, 12, 20], "Climb Speed Up", "Climbing Jump Stamina Up - Reduces the amount of stamina used when jumping whilst climbing.", ["Climber's Bandanna", "Climbing Gear", "Climbing Boots"], "Yes."],
                ["Snowquill", [3, 5, 8, 12, 20], "Cold Resistance", "Unfreezable - Cannot be frozen by ice elemental attacks.", ["Snowquill Headdress", "Snowquill Tunic", "Snowquill Trousers"], "Yes."],
                ["Rubber", [3, 5, 8, 12, 20], "Shock Resistance", "Lightning Proof - Completely immune to lightning strikes.", ["Rubber Helm", "Rubber Armor", "Rubber Tights"], "Yes."],
                ["Phantom", [8], "Attack Up", "No set bonus.", ["Phantom Helmet", "Phantom Armor", "Phantom Greaves"], "No."],
                ["Desert Voe", [3, 5, 8, 12, 20], "Heat Resistance", "Shock Damage Resist - Reduces damage taken from electric elemental attacks.", ["Desert Voe Headband", "Desert Voe Spaulder", "Desert Voe Trousers"], "Yes."],
                ["Depths", [3, 5, 8, 12, 20], "Gloom Resistance", "Gloom Attack Resist - Adds 1 extra gloom-resistant heart, and reduces all damage taken by gloom attacks to 1 heart.", ["Hood of the Depths", "Tunic of the Depths", "Gaiters of the Depths"], "Yes."],
                ["Dark", [3], "No special effects.", "Night Speed Up - Gives you a 23% speed up bonus during the night.", ["Dark Hood", "Dark Tunic", "Dark Trousers"], "No."],
                ["Barbarian", [3, 5, 8, 12, 20], "Attack Up", "Charge Atk. Stamina Up - Reduces the amount of stamina used in charge attacks.", ["Barbarian Helm", "Barbarian Armor", "Barbarion Leg Wraps"], "Yes."],
                ["Zonaite", [4, 7, 12, 18, 28], "Energy Up - Doubles how long your battery lasts for.", "Energy Recharge Up - Your batteries recharge approximately 30% faster.", ["Zonaite Helm", "Zonaite Waistguard", "Zonaite SHin Guards"], "Yes."],
                ["Mystic", [3], "Rupee Padding - Whenever attacked, rupees are lost instead of health.", "No set bonus.", ["Mystic Headpiece", "Mystic Robe", "Mystic Trousers"], "TBC"],
                ["Frostbite", [2, 4, 6, 9, 16], "Cold Weather Attack - Causes an ice burst at the end of every combo or charge attack in cold weather.", "Cold Weather Charge - Charge attacks charge faster in cold climates, and an ice burst is caused at the end of every charge attack or combo.", ["Frostbite Headdress", "Frostbite Shirt", "Frostbite Trousers"], "Yes."],
                ["Ember", [2, 4, 6, 9, 16], "Hot Weather Attack - Causes a flame burst at the end of every combo or charge attack in hot weather.", "Hot Weather Charge - Charge attacks charge faster in hot climates, and a fire burst is caused at the end of every charge attack or combo.", ["Ember Headdress", "Ember Shirt", "Ember Trousers"], "Yes."],
                ["Charged", [2, 4, 6, 9, 16], "Stormy Weather Attack - Causes an electric burst at the end of every combo or charge attack in stormy weather.", "Stormy Weather Charge - Charge attacks charge faster in stormy weather, and an electric burst is caused at the end of every charge attack or combo.", ["Charged Headdress", "Charged Shirt", "Charged Trousers"], "Yes."]
               ]

    return families