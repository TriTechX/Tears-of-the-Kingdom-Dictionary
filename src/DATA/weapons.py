def returnWeapons():
    global weapons
    syntax = ["Weapon name", "Attack power", "True attack power", "Durability", "Material", "State", "Type", "Special abilities (if applicable)", ["Locations"], "Tier"]
    syntax
    
    weapons = [
        ["Tree Branch", 2, 2, 4, "Wood", "Normal", "One-handed", "No special ability.", ["Great Sky Island", "Hyrule Field"], "F"],
        ["Torch", 2, 2, 8, "Wood", "Normal", "One-handed", "This weapon will not lose durability if on fire.", ["Hyrule Field", "Gerudo Desert"], "F"],
        ["Long stick", 2, 2, 18, "Wood", "Normal", "Spear", "No special ability.", ["Tabantha Frontier", "Hebra Mountains", "Great Sky Island"], "F"],
        ["Wooden Mop", 3, 2, 8, "Wood", "Normal", "Spear", "No special ability.", ["Hyrule Field", "Eldin Canyon"], "F"],
        ["Traveler's Spear", 3, 2, 24, "Metal", "Decayed", "Spear", "No special ability.", ["Death Mountain", "Gerudo Highlands"], "F"],
        ["Traveler's Sword", 5, 5, 16, "Metal", "Decayed", "One-handed", "No special ability.", ["Hyrule Field", "Central Hyrule Depths"], "F"],
        ["Rusty Halberd", 3, 2, 12, "Metal", "Normal", "Spear", "This weapon can be fed to a Rock Octorok to return a non-rusty weapon.", ["Hyrule Field", "Eldin Canyon Depths"], "F"],
        ["Soup Ladle", 4, 4, 5, "Wood", "Normal", "One-handed", "No special ability.", ["Hyrule Field", "West Necluda", "various towns"], "F"],
        ["Wooden Stick", 4, 4, 12, "Wood", "Normal", "One-handed", "No special ability.", ["Hyrule Field", "Central Hyrule Depths", "Great Sky Island"], "F"],
        ["Thick Stick", 5, 6, 14, "Wood", "Normal", "Two-handed", "No special ability.", ["Hyrule Field", "Hebra Mountains", "Great Sky Island"], "F"],
        ["Rusty Broadsword", 5, 5, 6, "Metal", "Normal", "One-handed", "This weapon can be fed to a Rock Octorok to return a non-rusty weapon.", ["Hyrule Field", "Eldin Canyon Depths"], "F"],
        ["Rusty Claymore", 6, 7, 8, "Metal", "Normal", "Two-handed", "This weapon can be fed to a Rock Octorok to return a non-rusty weapon.", ["Hyrule Field", "East Necluda Depths"], "F"],
        ["Bokoblin Arm", 20, 20, 5, "Bone", "Normal", "One-handed", "No special ability.", [""], "F"],
        ["Lizalfos Arm", 22, 22, 5, "Bone", "Normal", "One-handed", "No special ability.", [""], "F"],
        ["Moblin Arm", 28, 30, 5, "Bone", "Normal", "Two-handed", "No special ability.", [""], "F"],
        
        
        ["Traveler's Claymore", 6, 7, 16, "Metal", "Decayed", "Two-handed", "No special ability.", ["Hyrule Field", "Gerudo Desert"], "E"],
        ["Farming Hoe", 6, 7, 7, "Metal", "Normal", "Two-handed", "No special ability.", ["Hyrule Field", "West Necluda"], "E"],
        ["Boat Oar", 4, 5, 8, "Wood", "Normal", "Two-handed", "No special ability.", ["East Necluda", "Necluda Sea", "Lurelin Village"], "E"],
        ["Farmer's Pitchfork", 4, 3, 12, "Metal", "Normal", "Spear", "No special ability.", ["Hyrule Field", "West Necluda"], "E"],
        ["Fishing Harpoon", 4, 3, 12, "Metal", "Normal", "Spear", "No special ability.", ["Lurelin Village"], "E"],
        ["Throwing Spear", 3, 2, 20, "Metal", "Decayed", "Spear", "Can be thrown further than a normal weapon without 'Long Throw'.", ["Central Hyrule Depths", "Hyrule Field"], "E"],
        ["Soldier's Spear", 4, 3, 25, "Metal", "Decayed", "Spear", "Quick Charge - Charge attacks will charge 2x faster.", ["Hyrule Field", "Eldin Canyon"], "E"],
        ["Feathered Spear", 4, 3, 25, "Metal", "Decayed", "Spear", "Wind Burst - Attacks will produce bursts of wind, much like Korok Fronds.", ["Hebra Mountains", "Tabantha Frontier"], "E"],
        ["Sturdy Long Stick", 4, 3, 34, "Wood", "Normal", "Spear", "Extra Durable - The weapon is significantly more durable than others of its type.", ["Gerudo Desert", "East Necluda Depths"], "E"],

        
        ["Zonaite Spear", 4, 3, 22, "Zonaite", "Normal", "Spear", "Zonaite Powered - Resonates with attached Zonai devices to slightly increase the attack power.", ["Rising Island Chain", "Lanayru Sky Archipelago"], "D"],
        ["Magic Staff", 4, 3, 14, "Unknown", "Normal", "Spear", "This weapon will awake the latent power of any gems of which it is fused to.", ["Eldin Mountains", "North Gerudo Sky Archipelago"], "D"],
        ["Sturdy Wooden Stick", 5, 5, 24, "Wood", "Normal", "One-handed", "Extra Durable - The weapon is significantly more durable than others of its type.", ["Hyrule Field", "East Necluda"], "D"],
        ["Sturdy Thick Stick", 5, 8, 26, "Wood", "Normal", "Two-handed", "Extra Durable - The weapon is significantly more durable than others of its type.", ["Hyrule Field", "Gerudo Desert"], "D"],
        ["Boomerang", 6, 6, 16, "Wood", "Decayed", "One-handed", "This weapon will return to you if thrown.", ["Lanayru Great Spring", "Lanayru Wetlands"], "D"],
        ["Soldier's Broadsword", 6, 6, 17, "Metal", "Decayed", "One-handed", "Quick Charge - Charge attacks will charge 2x faster.", ["Hyrule Field", "Eldin Canyon"], "D"],
        ["Feathered Edge", 6, 6, 18, "Metal", "Decayed", "One-handed", "Wind Burst - Attacks will produce bursts of wind, much like Korok Fronds.", ["Hebra Mountains", "Tabantha Frontier"], "D"],
        ["Eightfold Blade", 6, 6, 16, "Metal", "Decayed", "One-handed", "This weapon deals 16x damage in a sneakstrike rather than x8.", ["Hyrule Field", "Gerudo Highlands"], "D"],
        ["Zonaite Sword", 6, 6, 15, "Zonaite", "Normal", "One-handed", "Zonaite Powered - Resonates with attached Zonai devices to slightly increase the attack power.", ["Necluda Sky Archipelago", "South Eldin Sky Archipelago"], "D"],
        ["Knight's Halberd", 6, 4, 26, "Metal", "Decayed", "Spear", "Desperate Strength - The entire weapon's damage is multiplied by 2x when Link is down to his last heart.", ["Gerudo Desert", "Faron Grasslands"], "D"],
        ["Forest Dweller's Spear", 6, 4, 24, "Wood", "Decayed", "Spear", "Fuse Recycling - This weapon allows the reuse of specific one-time use fuse materials.", ["Great Hyrule Forest"], "D"],
        ["Zonaite Longsword", 8, 9, 15, "Zonaite", "Normal", "Two-handed", "Zonaite Powered - Resonates with attached Zonai devices to increase the attack power.", ["Lanayru Sky Archipelago", "Necluda Sky Archipelago"], "D"],


        ["Magic Rod", 6, 6, 14, "Unknown", "Normal", "One-handed", "This weapon will awake the latent power of any gems of which it is fused to.", ["Gerudo Highlands", "West Necluda"], "C"],
        ["Zora Sword", 6, 6, 20, "Metal", "Decayed", "One-handed", "Water Warrior - The entire weapon's damage is multiplied by 2x when it gets wet.", ["Lanayru Great Spring"], "C"],
        ["Gerudo Spear", 6, 4, 15, "Metal", "Decayed", "Spear", "Strong Fusion - The fused material's attack damage is multiplied by 2x.", ["Gerudo Desert"], "C"],
        ["Zora Spear", 6, 4, 20, "Metal", "Decayed", "Spear", "Water Warrior - The entire weapon's damage is multiplied by 2x when it gets wet.", ["Lanayru Wetlands", "Upland Zorana"], "C"],
        ["Strong Zonaite Spear", 6, 4, 24, "Zonaite", "Normal", "Spear", "Zonaite Powered - Resonates with attached Zonai devices to increase the attack power.", ["Lanayru Sky Archipelago", "Lomei Labyrinth Island"], "C"],
        ["Knight's Broadsword", 7, 7, 18, "Metal", "Decayed", "One-handed", "Desperate Strength - The entire weapon's damage is multiplied by 2x when Link is down to his last heart.", ["Gerudo Desert", "Hyrule Castle"], "C"],
        ["Forest Dweller's Sword", 7, 7, 17, "Wood", "Decayed", "One-handed", "Fuse Recycling - This weapon allows the reuse of specific one-time use fuse materials.", ["Eldin Mountains", "Great Hyrule Forest"], "C"],
        ["Strong Zonaite Sword", 7, 7, 16, "Zonaite", "Normal", "One-handed", "Zonaite Powered - Resonates with attached Zonai devices to increase the attack power.", ["Lanayru Sky Archipelago", "Thunderhead Isles"], "C"],
        ["Magic Scepter", 7, 8, 14, "Unknown", "Normal", "Two-handed", "This weapon will awake the latent power of any gems of which it is fused to.", ["Central Hyrule Depths", "Mount Lanayru Depths"], "C"],

        
        ["Royal Halberd", 7, 5, 30, "Metal", "Decayed", "Spear", "Improved Flurry Rush - This weapon deals twice the amount of damage during a flurry rush.", ["Hyrule Castle", "East Necluda"], "B"],
        ["Gerudo Scimitar", 8, 8, 10, "Metal", "Decayed", "One-handed", "Strong Fusion - The fused material's attack damage is multiplied by 2x.", ["Gerudo Desert"], "B"],
        ["Lizal Boomerang", 8, 8, 17, "Metal", "Normal", "One-handed", "This weapon will return to you if thrown.", ["Hebra Mountains", "Mount Lanayru"], "B"],
        ["Soldier's Claymore", 8, 9, 17, "Metal", "Decayed", "Two-handed", "Charge Atk. Stamina Up - This decreases the amount of stamina used in a charge attack.", ["Hyrule Field", "Eldin Canyon"], "B"],
        ["Zora Longsword", 8, 9, 20, "Metal", "Decayed", "Two-handed", "Water Warrior - The entire weapon's damage is multiplied by 2x when it gets wet.", ["Lanayru Great Spring"], "B"],
        ["Eightfold Longblade", 8, 9, 9, "Metal", "Decayed", "Two-handed", "Wind Razor - This weapon cleaves the wind and creates a vacuum that can deal damage.", ["Hyrule Ridge", "Gerudo Highlands"], "B"],
        ["Mighty Zonaite Spear", 8, 6, 27, "Zonaite", "Normal", "Spear", "Zonaite Powered - Resonates with attached Zonai devices to increase the attack power.", ["South Lomei Castle", "Greater Sky Islands"], "B"],
        ["Cobble Crusher", 9, 10, 18, "Metal", "Decayed", "Two-handed", "Demolisher - Deals 1.5x damage to rock-type enemies or breakable rocks.", ["Eldin Canyon", "Eldin Canyon Depths"], "B"],

        
        ["Royal Broadsword", 10, 10, 20, "Metal", "Decayed", "One-handed", "Improved Flurry Rush - This weapon deals twice the amount of damage during a flurry rush.", ["Hyrule Castle", "Gerudo Highlands Depths"], "A"],
        ["Mighty Zonaite Sword", 10, 10, 18, "Zonaite", "Normal", "One-handed", "Zonaite Powered - Resonates with attached Zonai devices to increase the attack power.", ["South Lomei Labyrinth", "Faron Grasslands"], "A"],
        ["Gerudo Claymore", 10, 11, 10, "Metal", "Decayed", "Two-handed", "Strong Fusion - The fused material's attack damage is multiplied by 2x.", ["Gerudo Desert", "Gerudo Highlands"], "A"],
        ["Strong Zonaite Longsword", 10, 11, 16, "Zonaite", "Normal", "Two-handed", "Zonaite Powered - Resonates with attached Zonai devices to increase the attack power.", ["Lanayru Sky Archipelago", "Thunderhead Isles"], "A"],
        ["Gnarled Long Stick", 10, 7, 22, "Wood", "Normal", "Spear", "No special ability.", ["Gerudo Desert"], "A"],
        ["Giant Boomerang", 11, 12, 18, "Metal", "Decayed", "Two-handed", "This weapon will return to you if thrown.", ["Hyrule Field", "Eldin Canyon"], "A"],
        ["Knight's Claymore", 11, 12, 18, "Metal", "Decayed", "Two-handed", "Desperate Strength - The entire weapon's damage is multiplied by 2x when Link is down to his last heart.", ["Hyrule Field", "Gerudo Desert"], "A"],
        ["Gnarled Wooden Stick", 14, 14, 14, "Wood", "Normal", "One-handed", "No special ability.", ["Gerudo Desert", "Mount Lanayru"], "A"],
        ["Mighty Zonaite Longsword", 15, 16, 18, "Zonaite", "Normal", "Two-handed", "Zonaite Powered - Resonates with attached Zonai devices to increase the attack power.", ["South Lomei Labyrinth", "North Lomei Labyrinth"], "A"],


        ["Royal Claymore", 14, 15, 20, "Metal", "Decayed", "Two-handed", "Improved Flurry Rush - This weapon deals twice the amount of damage during a flurry rush.", ["Great Plateau", "Hyrule Castle"], "S"],
        ["Royal Guard's Spear", 15, 11, 14, "Metal", "Decayed", "Spear", "Breaking Point - The weapon yields twice as much attack power during the 3 hits before it breaks.", ["Hyrule Castle Island", "Akkala Citadel Ruins Summit"], "S"],
        ["Gnarled Thick Stick", 19, 20, 16, "Wood", "Normal", "Two-handed", "No special ability.", ["East Necluda", "Gerudo Highlands"], "S"],
        ["Royal Guard's Sword", 22, 22, 10, "Metal", "Decayed", "One-handed", "Breaking Point - The weapon yields twice as much attack power during the 3 hits before it breaks.", ["Hyrule Castle Island"], "S"],
        ["Royal Guard's Claymore", 32, 34, 11, "Metal", "Decayed", "Two-handed", "Breaking Point - The weapon yields twice as much attack power during the 3 hits before it breaks.", ["Hyrule Castle Island"], "S"],

        
        ["Gloom Spear", 40, 30, 16, "Metal", "Normal", "Spear", "Gloom Toll - The weapon will degrade Link's heart containers whenever used. This weapon cannot be repaired by a Rock Octorok.", ["Can be obtained by defeating Gloom Spawn and Phantom Ganon."], "S+"],
        ["Gloom Sword", 41, 41, 15, "Metal", "Normal", "One-handed", "Gloom Toll - The weapon will degrade Link's heart containers whenever used. This weapon cannot be repaired by a Rock Octorok.", ["Can be obtained by defeating Gloom Spawn and Phantom Ganon."], "S+"],
        ["Gloom Club", 50, 53, 14, "Metal", "Normal", "Two-handed", "Gloom Toll - The weapon will degrade Link's heart containers whenever used. This weapon cannot be repaired by a Rock Octorok.", ["Can be obtained by defeating Gloom Spawn and Phantom Ganon."], "S+"],

        
        ["Sea-Breeze Boomerang", 16, 16, 20, "Wood", "Normal", "One-handed", "This weapon will return to you if thrown.", ["Hebra Canyon Mine"], "Legendary"],
        ["Sword of the Hero", 17, 17, 27, "Metal", "Normal", "One-handed", "No special ability.", ["Dalite Grove - Depths"], "Legendary"],
        ["Lightscale Trident", 22, 16, 70, "Metal", "Normal", "Spear", "Water Warrior - The entire weapon's damage is multiplied by 2x when it gets wet.", ["Talk to Dento at Zora's Domain."], "Legendary"],
        ["White Sword of the Sky", 24, 24, 45, "Metal", "Normal", "One-handed", "No special ability.", ["Complete 'The Mother Goddess Statue' side quest", "offer x1 Dinraal's Claw, x1 Naydra's Claw, and x1 Farosh's Claw after completing the quest for a replacement."], "Legendary"],
        ["Scimitar of the Seven", 28, 28, 60, "Metal", "Normal", "One-handed", "Strong Fusion - The fused material's attack damage is multiplied by 2x.", ["Complete the side quest 'The Missing Owner'."], "Legendary"],
        ["Dusk Claymore", 32, 34, 50, "Metal", "Normal", "Two-handed", "No special ability.", ["Gleeok Den - Depths, underneath Typhlo Ruins."], "Legendary"],
        ["Biggoron's Sword", 36, 38, 60, "Metal", "Normal", "Two-handed", "No special ability.", ["Akkala House of Bones - Depths"], "Legendary"],
        ["Boulder Breaker", 38, 40, 40, "Metal", "Normal", "Two-handed", "Demolisher - Deals 1.5x damage to rock-type enemies or breakable rocks.", ["Complete the side quest 'The Soul of the Gorons'."], "Legendary"],
        ["Fierce Deity Sword", 38, 40, 35, "Metal", "Normal", "Two-handed", "No special ability.", ["Cephla Lake Cave - after completing the side quest: 'Misko's Treasure: The Fierce Deity', unlocked for completing 'Misko's Cave of Chests'."], "Legendary"],

        
        ["Master Sword", 30, "45 (against Gloom enemies)", "40, ∞ (when fighting Ganondorf)", "Metal", "Normal", "One-handed", "Revitalized Sword of Legend - Allows the weapon to regain durability over time, after running out of energy. Fires a beam when thrown and Link is at full health. Gleams with a sacred lustre around Gloom-infested enemies.", ["The Light Dragon: can be pulled if Link has at least 2 wheels of stamina."], "Legendary"]
    ]

    return weapons


def returnWeaponDescs():
    global weaponDescs
    weaponDescs = ["Wooden branches such as this are pretty common, but it's surprisingly well-balanced. It doesn't do much damage but can serve as a weapon in a pinch.",
                   "This torch will stay lit once ignited, but if you put it away, the flame will be extinguished until you light it again.",
                   "A long stick fashioned from a tree branch. Its straight shape makes it work well as a lunging weapon.",
                   "Just a mop to the untrained eye, it excels at tidying up the place. But it owes its turdy construction to a true craftsman, so it actually has some combat merit.",
                   "An average spear carried by travelers for protection. It's decayed and doesn't cut well, but the shape makes it easy for anyone to handle.",
                   "An average sword used largely by travelers. The blade has decayed, but it can still serve its purpose.",
                   "A rusty polearm likely used by knights from an age past. The spearhead is in a bad shape due to prolonged exposure to the elements, so its durability is low.",
                   "A kitchen implement often used for serving delicious soups. It was carved from the wood of a sturdy tree, so it actually packs quite the wallop.",
                   "A tree branch with an added grip and excellent balance. Equip it, and use it as a weapon.",
                   "A thick bat cut from a large tree. It's not the sturdiest weapon, but its heavy end does have a bit of power behind it.",
                   "This once-fearsone sword has seen better days. It can do some damage in the right hands but also breaks quickly.",
                   "A two-handed sword not properly cared for. Although it can be used as a weapon, its durability is very low. Don't expect it to last for more than a few strikes.",
                   "A skeletal arm that keeps moving even after it's severed from its body. It's kind of gross to strap it to your back, but it'll do in a pinch. It's old and fragile, so it's quick to break.",
                   "The arm of a Stalizalfos that continues to struggle even in death. It can be used as a weapon, but it's very brittle. You can feel it wiggling when you strap it to your back...",
                   "A Moblin bone that continous to move even after being detached from its body. The bone is thick enough to be used as a weapon but is extremely brittle and easily broken.",


                   "A basic two-handed sword once wilded by aspiring adventurers. It's decayed and no longer cuts well, but it can still knock a shield right out of enemies hands.",
                   "A farming tool primarily used for tilling fields. Its fine craftmanshp is sturdy enough to whitstand backbreaking fieldwork, but its battle applications are untested.",
                   "Made for paddling boats, but it was made sturdy enough to fight strong currents. Maybe it's useful for self-defense in a pinch.",
                   "A farming tool used to collect hay efficiently. It's light enough to be used by anyone. The four prongs are hery sharp.",
                   "A fisherman's tool that excels at chatching large fish. Its particularly sharp spearhead makes it valuable as a weapon as well.",
                   "A spear for throwing with a decayed tip. Lost its sharpness, but kept the balance perfect for throwing, enabling you to throw it very far.",
                   "Although now decayed, this lightweight metal spear was made for royal soldiers. Beacause it's light and easy to handle, it enables quicker charged attacks.",
                   "A spear used by Rito soldiers, its point is now decayed. It still boasts quick attacks in midair, and it produces a strong wind.",
                   "A long, durable stick made from a branch with good piercing power. It has high durability because it comes from the hardest part of the tree.",


                   "A Zonai spear made of zonaite. It resonates with attached Zonai devices to slightly increase its attack power.",
                   "A long rod with a bit of magic, it's said to have been wielded by an ancient magician who awoke the latent power of gems.",
                   "A stick made out of a hard tree branch. The tree soaked up loads of sunshine, so it's sturdier than a regular stick and has high durability.",
                   "A solid stick cut from the crooked branch of a tough tree. It has high durability, despite the way it looks.",
                   "A decayed wooden boomerang. A useful tool that comes back after you throw it. Its current state has not lessened its performance.",
                   "A light, thin metal sword used by the guards of Hyrule Castle. Its light weight makes it easy to handle and enables quicker charged attacks.",
                   "A double-edged Rito sword with a decayed blade. Swinging it produces a strong wind.",
                   "A single-edged sword of the Sheikah tribe. Its small blade, now decayed, is suited for covert actions and yields more powerful sneakstrikes than ordinairy blades.",
                   "A Zonai sword made of zonaite. It resonates with attached Zonai devices to slightly increase its attack power.",
                   "Now decayed, this halberd was made for knights of Hyrule. It reflects theis courage in defending the kingdom. It can yield powerful attacks when you're down to your last heart.",
                   "A Korok spear with a decayed tip. It's still full of vitality. Bursting materials attached to the spearhead can be reused again and again.",
                   "A large sword used by the Zonai and made of zonaite. It resonates with attached Zonai devices to slightly increase its attack power.",


                   "A small and intensely magic rod, It's said to have been wielded by an ancient magician who awoke maximum latent power in gems.",
                   "A long Zora sword with a decaying blade. Made of a metal favored by the Zora, it yields a high attack power when it gets wet.",
                   "A Gerudo spear with a decayed blade that is designed to draw force to its tip. Attaching a material greatly enhances the material's power but doesn't add as much durability.",
                   "A Zora spear with a decayed point. It's made of water-resistant metal and yields a high attack power when it gets wet.",
                   "A tough spear used by the Zonai. It is highly durable. It resonates with attached Zonai devices to increase some of its attack power.",
                   "Knights of Hyrule once caried this sword. Even in its decayed state, it shows its true resolve in desperation and can yield powerful attacks when you're down to your last heart.",
                   "A living, wooden Korok sword with a decayed blade. Bursting materials attached to the tip can be reused again and again.",
                   "A strong Zonai sword made of zonaite. It resonates with attached Zonai devices to increase some of its attack power.",
                   "A long mysterious magical rod, it's said to have been wielded by an ancient magician who awoke the latent power of gems.",


                   "Although now decayed, this spear was once given to knights who guarded critical areas of Hyrule Castle. It enables a powerful flurry rush during a perfect dodge.",
                   "A decaying scimitar from the Gerudo region, it is designed for maximazing force. Attaching a material greatly enhances the material's power but doesn't add as much durability.",
                   "A curved zword favored by the Lizalfos. It's made of metal so it can safely be used near fire. If you throw it, it will return to you.",
                   "A lightweight metal weapon forged for royal soldier. It's decayed now, but still easy to wield, so it consumes less stamina during charge attacks.",
                   "A decayed Zora longsword, it's suited for battles near water because it's made of an unusual metal that increases attack power when it's wet.",
                   "A longblade that no longer cuts as well as it once did, due to its decayed edge. However, ehrn wielded by a proficient fighter, it cleaves the wind and creates a vacuum.",
                   "A powerful Zonai spear made of zonaite. It resonates with attached Zonai devices to greatly increase its attack power.",
                   "In its former state, this hefty weapon knocked out many a foe. Decayed, it still packs a punch and is great for breaking rocks.",


                   "A sword gifted to accomplished knights by the royal family. Crafted for sword masters, it increases the power of flurry rush during perfect dodge.",
                   "A powerful sword used by Zonai and made of zonaite. It resonates with attached Zonai devices to greatly increase its attack power.",
                   "A two-handed Gerudo sword a decayed blade. Attaching a meterial greatly increases the material's power but doesn't add as much durability.",
                   "A strong, large sword used by the Zonai and made of zonaite. It resonates with attached Zonai devices to increase some of its attack power.",
                   "A long stick made bumpy at one end when its shoots were cut off. It has higher attack power than a normal stick.",
                   "A massive boomerang that is weakened and decayed. It was originally used for hunting, but it can be a challenge to wield it. Thrown well, it will come back to the thrower.",
                   "A claymore, now decayed, once carried by knight of Hyrule. It resonates with the desire to protect at all cost and can yield powerful attacks when you're down to your last heart.",
                   "A very swingable stick made by honing a dried branch to the proper thickness and length. Its attack power is much greater than that of a normal stick.",
                   "A powerful, large sword used by the Zonai and made of zonaite. It resonates with attached Zonai devices to greatly increase its attack power.",


                   "A large sword, now decayed, issued to the royal family's guard. It's tuned for skilled users and yields a powerful flurry rush during a perfect dodge.",
                   "A decayed prototype spear wielded by knights. It's made from a special metal with low durability, but which yields massive destructive power just before it breaks.",
                   "A stick cut from a tree trunk. It's been dried to increase its hardness. It has high attack power for something made of wood.",
                   "A decayed prototypical sword for knights. Its metal may not be as durable as other, but the sword yield massive destructive power just before it breaks.",
                   "A decayed claymore prototype for the royal guard. It's made of a metal refined using an unuasual method, and it holds massive destructive power just before it breaks.",


                   "A spear whose ominous appearance strikes fear into hearts. it is said to cost its bearer a part of their soul because its gloom wil gradually wear down the body of its wielder.",
                   "This slender sword has an ominous presence. It is said to end the life of anyone it touches. Its gloom will gradually wear down the body of its wielder.",
                   "A metal stick with madness and symbolic of doom. Its forceful strike can smash an object to pieces. Its gloom will gradually wear down the body of its wielder.",


                   "A boomerang said to have been used by a hero who traveled the Great Sea. It smells faintly of salt water.",
                   "A sword once wielded by a hero in an ancient age. When it's grasped, a strange sense of nostalgia washes over you. Take it when going alone would otherwise be dangerous.",
                   "A spear of peerless grace cherished by the Zora Champion Mipha. Although Mipha specialized in healing abilities, her spearmanship was in a class all its own.",
                   "A sword said to have once belonged to a hero from the sky. Its beautiful white blade stands out. When it's wielded, a strange yet heavenly breeze kicks up around you.",
                   "A famous sword once beloved by the Gerudo Champion Urbosa. It is said that when Urbose swung this sword in battle, her movements resembled a beautiful dance.",
                   "A slander claymore thought to have been handed down to the kingdom of Hyrule ages ago. The blade shines with a holy luster.",
                   "A legendary greatsword forged by a Goron craftsman for a hero who traveled through time. The exceptionally sharp cutting edge is a testament to the craftsman's mastery.",
                   "This two-handed weapopn was once wielded by the Goron Champion Daruk. Daruk made swinging it around look easy, but a Hylian would need an immense amount of strength.",
                   "A perculiar greatsword allegedly used by a hero from a world in which the moon threatened to fall. It slashes wildly in battle as if possessed by Fierce Deity.",


                   "The Legendary sword that seals the darkness. Its corruption was healed by its time with the Light Dragon. The blade gleams with sacred luster that can oppose the Demon King."]

    return weaponDescs


def returnPristineWeapons():
    global pristineWeapons
    pristineWeapons = [
        
        ["Traveler's Spear", 4, 3, 25, "Metal", "Pristine", "Spear", "No special ability.", ["Central Hyrule Depths", "Abandoned Gerudo Mine", "Abandoned Eldin Mine"], "F"],
        ["Traveler's Sword", 7, 7, 20, "Metal", "Pristine", "One-handed", "No special ability.", ["Central Hyrule Depths", "Abandoned Gerudo Mine", "Abandoned Eldin Mine"], "F"],
        ["Boomerang", 8, 8, 18, "Wood", "Pristine", "One-handed", "This weapon will return to you if thrown.", ["Gerudo Highlands Depths", "Tanagar Canyon Depths"], "F"],

    
        ["Throwing Spear", 8, 6, 26, "Metal", "Pristine", "Spear", "Can be thrown further than a normal weapon without 'Long Throw'.", ["Central Hyrule Depths"], "E"],
        ["Traveler's Claymore", 9, 10, 20, "Metal", "Pristine", "Two-handed", "No special ability.", ["Abandoned Gerudo Mine", "Abandoned Eldin Mine"], "E"],


        ["Soldier's Spear", 10, 7, 35, "Metal", "Pristine", "Spear", "Quick Charge - Charge attacks will charge 2x faster.", ["Central Hyrule Depths", "Greater Hyrule Depths"], "D"],
        ["Feathered Spear", 10, 7, 35, "Metal", "Pristine", "Spear", "Wind Burst - Attacks will produce bursts of wind, much like Korok Fronds.", ["Abandoned Hebra Mine"], "D"],
        ["Soldier's Broadsword", 12, 12, 23, "Metal", "Pristine", "One-handed", "Quick Charge - Charge attacks will charge 2x faster.", ["Central Hyrule Depths", "Greater Hyrule Depths"], "D"],
        ["Feathered Edge", 13, 13, 27, "Metal", "Pristine", "One-handed", "Wind Burst - Attacks will produce bursts of wind, much like Korok Fronds.", ["Abandoned Hebra Mine", "Tanagar Canyon Depths"], "D"],


        ["Zora Spear", 11, 8, 40, "Metal", "Pristine", "Spear", "Water Warrior - The entire weapon's damage is multiplied by 2x when it gets wet.", ["Abandoned Lanayru Mine", "Abandoned Kakariko Mine"], "C"],
        ["Zora Sword", 12, 12, 27, "Metal", "Pristine", "One-handed", "Water Warrior - The entire weapon's damage is multiplied by 2x when it gets wet.", ["Abandoned Lanayru Mine"], "C"],
        ["Gerudo Spear", 12, 9, 20, "Metal", "Pristine", "One-handed", "Strong Fusion - The fused material's attack damage is multiplied by 2x.", ["Abandoned Gerudo Mine"], "C"],
        ["Cobble Crusher", 14, 15, 30, "Metal", "Pristine", "Two-handed", "Demolisher - Deals 1.5x damage to rock-type enemies or breakable rocks.", ["Abandoned Eldin Mine"], "C"],
        ["Forest Dweller's Spear", 14, 10, 35, "Wood", "Pristine", "Spear", "Fuse Recycling - This weapon allows the reuse of specific one-time use fuse materials.", ["Great Hyrule Forest Depths"], "B"],
        

        ["Knight's Halberd", 14, 10, 40, "Metal", "Pristine", "Spear", "Desperate Strength - The entire weapon's damage is multiplied by 2x when Link is down to his last heart.", ["Abandoned Hebra Mine", "Gerudo Highlands Depths", "Abandoned Kakariko Mine"], "B"],
        ["Eightfold Blade", 15, 15, 26, "Metal", "Pristine", "One-handed", "This weapon deals 16x damage in a sneakstrike rather than x8.", ["Abandoned Kakariko Mine", "Abandoned Hateno Mine", "Abandoned Lurelin Mine"], "B"],
        ["Forest Dweller's Sword", 16, 16, 27, "Wood", "Pristine", "One-handed", "Fuse Recycling - This weapon allows the reuse of specific one-time use fuse materials.", ["Great Hyrule Forest Depths"], "B"],
        ["Soldier's Claymore", 16, 17, 25, "Metal", "Pristine", "Two-handed", "Charge Atk. Stamina Up - This decreases the amount of stamina used in a charge attack.", ["Greater Hyrule Depths", "(Excludes Central Hyrule Depths)"], "B"],
        

        ["Gerudo Scimitar", 17, 17, 14, "Metal", "Pristine", "One-handed", "Strong Fusion - The fused material's attack damage is multiplied by 2x.", ["Abandoned Gerudo Mine"], "A"],
        ["Gerudo Claymore", 22, 24, 14, "Metal", "Pristine", "Two-handed", "Strong Fusion - The fused material's attack damage is multiplied by 2x.", ["Abandoned Gerudo Mine", "Abandoned Kara Kara Mine"], "A"],
        ["Zora Longsword", 18, 19, 30, "Metal", "Pristine", "Two-handed", "Water Warrior - The entire weapon's damage is multiplied by 2x when it gets wet.", ["Southern Abandoned Lanayru Mine"], "A"],
        ["Knight's Broadsword", 18, 18, 27, "Metal", "Pristine", "One-handed", "Desperate Strength - The entire weapon's damage is multiplied by 2x when Link is down to his last heart.", ["Greater Northwestern Hyrule Depths"], "A"],
        ["Royal Guard's Spear", 24, 18, 15, "Metal", "Pristine", "Spear", "Breaking Point - The weapon yields twice as much attack power during the 3 hits before it breaks.", ["Gerudo Highlands Depths", "Crenel Hills Depths"], "A"],
        ["Eightfold Longblade", 23, 25, 25, "Metal", "Pristine", "Two-handed", "Wind Razor - This weapon cleaves the wind and creates a vacuum that can deal damage.", ["Abandoned Kakariko Mine", "Abandoned Hateno Mine", "Abandoned Lurelin Mine"], "A"],
        ["Knight's Claymore", 24, 26, 30, "Metal", "Pristine", "Two-handed", "Desperate Strength - The entire weapon's damage is multiplied by 2x when Link is down to his last heart.", ["Abandoned Hebra Mine", "Necluda Depths", "Gerudo Highlands Depths"], "A"],


        ["Royal Halberd", 18, 14, 50, "Metal", "Pristine", "Spear", "Improved Flurry Rush - This weapon deals twice the amount of damage during a flurry rush.", ["Gerudo Highlands Depths", "Abandoned Hebra Mine"], "S"],
        ["Giant Boomerang", 23, 25, 40, "Metal", "Pristine", "Two-handed", "This weapon will return to you if thrown.", ["Gerudo Highlands Depths", "Tanagar Canyon Depths"], "S"],
        ["Royal Broadsword", 24, 24, 35, "Metal", "Pristine", "One-handed", "Improved Flurry Rush - This weapon deals twice the amount of damage during a flurry rush.", ["Abandoned Hebra Mine", "Gerudo Highlands Depths", "Crenel Hills Depths"], "S"],
        ["Royal Guard's Sword", 30, 30, 15, "Metal", "Pristine", "One-handed", "Breaking Point - The weapon yields twice as much attack power during the 3 hits before it breaks.", ["Gerudo Highlands Depths", "Crenel Hills Depths", "Eventide Island Depths"], "S"],
        

        ["Royal Claymore", 34, 36, 40, "Metal", "Pristine", "Two-handed", "Improved Flurry Rush - This weapon deals twice the amount of damage during a flurry rush.", ["Abandoned Hebra Mine", "Gerudo Highlands Depths"], "S+"],
        ["Royal Guard's Claymore", 39, 41, 12, "Metal", "Pristine", "Two-handed", "Breaking Point - The weapon yields twice as much attack power during the 3 hits before it breaks.", ["Gerudo Highlands Depths", "Abandoned Kakariko Mine", "Eventide Island Depths"], "S+"]
        ]

    return pristineWeapons


def returnPristineWeaponDescs():
    global pristineWeaponDescs
    pristineWeaponDescs = [
        "A spear used mainly by travelers to fend off wolves and other beasts. It's easy to hold and simple to use.",
        "A very common sword often kept by travelers to fend off small beasts. It's fairly durable but a bit unreliable against monsters.",
        "This throwing weapon was originally used by the forest-dwelling Koroks. Its unique shape allows it to return after being thrown.",

        
        "A specialized spear weighted to excel as a throwing weapon. It's perfectly balanced to be thrown farther than your average spear, able to pierce targets from a great distance.",
        "A basic two-handed sword once wielded by aspiring adventurers. Its immense weight can knock enemies' shields right out of their hands.",


        "A long spear once used by the guards of Hyrule Castle. Easy to use but difficult to master. Enables quicker charged attacks.",
        "Its lightweight design is a hallmark of Rito craftsmanship. It gives Rito warriors more maneuverability during aerial combat—and it produces a strong wind.",
        "	A sword brandished by soldiers who once protected Hyrule Castle. Its blade is well tuned for slaying monsters as it enables quicker charged attacks.",
        "Rito craftsmen forged this lightweight, double-edged sword so Rito warriors could maneuver quickly in midair. Swinging it produces a strong wind.",

        
        "This spear is a Zora's weapon of choice. It's made from a special metal and is used by the Zora for both fishing and protecting home. It yields high attack power when it gets wet.",
        "A unique sword with a thin blade of Zora design that yields high attack power when wet. This blade takes to water like a Zora.",
        "This spear was used widely by the Gerudo soldiers. Attaching a material greatly enhances the material's power but doesn't add as much durability.",
        "A Goron-made two-handed weapon. It's made from thick, hard metal and has no cutting edge, but its weight and hard surface make it a great tool for breaking rocks.",
        "The Koroks made this spear for Hylians. The shaft is made from a light, sturdy wood. Bursting materials attached to the spearhead can be reused again and again.",
        "A spear used by knights adept in mounted combat. The spearhead is modeled after an axe. It can yield powerful attacks when you're down to your last heart.",
        "A single-edged sword traditional to the Sheikah tribe. It just may be among the sharpest conventional weapons ever made. It can yield more powerful sneakstrikes.",
        "Koroks crafted this wooden sword for Hylians. It might not be the best choice for head-on attacks, but bursting materials attached to the tip can be reused again and again.",

        
        "An improved claymore, made lightweight for easier handling. It consumes less stamina for charged attacks.",
        "The most commonly used sword in the Gerudo region. Attaching a material greatly enhances the material's power but doesn't add as much durability.",
        "Only the most talented Gerudo sword fighters carry this two-handed sword. Attaching a material greatly enhances the material's power but doesn't add as much durability.",
        "A longsword made by the Zora using a special metal. It's rarely used because the Zora prefer to use spears. It yields high attack power when it gets wet.",
        "Knights of Hyrule Castle once carried this sword. It can yield powerful attacks when you're down to your last heart.",
        "This Sheikah-made spear was created using ancient technology. It has poor durability, but the magic it contains yields massive destructive power just before it breaks.",
        "A single-edged sword seldom seen in Hyrule. This weapon is passed down through the Sheikah tribe. When wielded by a proficient fighter, it cleaves wind and creates vacuum.",
        "Only the strongest of Hyrule Castle's knights carried this two-handed sword. It can yield powerful attacks when you're down to your last heart.",


        "This spear was issued to the knights who guarded Hyrule Castle's throne room. It yields a powerful flurry rush during a perfect dodge.",
        "This massive boomerang requires two hands. Originally used for hunting, it was modified for use as a weapon. The blades on the inner curves make it a bit tricky to wield.",
        "The Hyrulean royal family would award this sword to knights who achieved remarkable feats. It increases the power of flurry rush during a perfect dodge.",
       "A weapon made by the Sheikah using ancient technology. Its low durability is a downside, but it yields massive destructive power just before it breaks.",


        "A two-handed sword issued to the Hyrulean royal family's immediate guard detail. Yields a powerful strike and increases the power of flurry rush during perfect dodge.",
        "A decayed claymore prototype for the royal guard. It's made of a metal refined using an unusual method, and it holds massive destructive power just before it breaks."
    ]
    return pristineWeaponDescs