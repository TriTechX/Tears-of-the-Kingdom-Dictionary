def returnBows():
    global syntax, bows

    syntax = ["Bow name", "Attack power", "Durability", "Range", "Material", "Special ability (if applicable)", ["Locations"], "Tier"]

    bows = [
        ["Wooden Bow", 4, 20, 20, "Wood", "No special ability.", ["Hyrule Field", "South Lanayru Sky Archipelago"], "F"],
        ["Construct Bow", 5, 18, 20, "Zonaite", "No special ability.", ["South Lanayru Sky Archipelago", "North Gerudo Sky Archipelago"], "F"],
        ["Boko Bow", 4, 16, 20, "Wood", "No special ability.", ["Hyrule Field", "Central Hyrule Depths"], "F"],
        ["Old Wooden Bow", 4, 20, 20, "Wood", "No special ability.", ["Great Sky Island"], "F"],


        ["Traveler's Bow", 5, 22, 20, "Wood", "No special ability.", ["Hyrule Field", "Central Hyrule Depths"], "E"],
        ["Strong Construct Bow", 11, 26, 20, "Zonaite", "No special ability.", ["Rising Island Chain", "Death Mountain Depths"], "E"],
        ["Spiked Boko Bow", 12, 20, 20, "Wood", "No special ability.", ["Hyrule Field", "Gerudo Highlands Depths"], "E"],
        ["Lizal Bow", 14, 25, 20, "Wood", "No special ability.", ["Lanayru Wetlands", "Gerudo Desert Depths"], "E"],


        ["Soldier's Bow", 14, 36, 20, "Wood", "No special ability.", ["Hyrule Field", "Hebra Mountains"], "D"],
        ["Phrenic Bow", 10, 45, 40, "Wood", "Zooms into for long-distance shots.", ["East Necluda", "West Necluda"], "D"],
        ["Swallow Bow", 8, 30, 40, "Wood", "No special ability.", ["Hebra Mountains", "Tabantha Frontier"], "D"],

        ["Mighty Construct Bow", 24, 34, 20, "Zonaite", "No special ability.", ["Lomei Labyrinth Island", "Typhlo Ruins"], "C"],
        ["Falcon Bow", 14, 35, 40, "Wood", "No special ability.", ["Tabantha Frontier", "Hebra Mountains"], "C"],
        ["Duplex Bow", "14*2", 18, 40, "Wood", "This bow shoots 2 arrows at once, for the cost of one.", ["Hyrule Field", "Gerudo Desert Depths"], "C"],


        ["Lynel Bow", "10*3", 30, 20, "Metal", "This bow shoots 3 arrows at once, for the cost of one.", ["East Necluda", "Deep Akkala"], "B"],
        ["Knight's Bow", 26, 48, 20, "Metal", "No special ability.", ["Gerudo Desert", "Akkala Highlands"], "B"],
        ["Dragonbone Boko Bow", 24, 30, 20, "Wood", "No special ability.", ["Gerudo Highlands", "Gerudo Highlands Depths"], "B"],
        ["Zora Bow", 20, 40, 20, "Metal", "No special ability.", ["Lanayru Great Spring"], "B"],
        ["Strengthened Lizal Bow", 25, 35, 20, "Wood", "No special ability.", ["Gerudo Desert", "Akkala Highlands Depths"], "B"],
        ["Gerudo Bow", 25, 40, 40, "Metal", "Zooms into for long-distance shots.", ["Gerudo Desert", "Gerudo Highlands"], "B"],


        ["Steel Lizal Bow", 36, 50, 20, "Metal", "No special ability.", ["Hyrule Castle Island", "Gerudo Highlands Depths", "Central Hyrule Depths"], "A"],
        ["Dusk Bow", 30, 40, 40, "Metal", "Doesn't shoot light arrows like in Breath of the Wild :( (used to be called 'Twilight Bow').", ["Hyrule Castle Turret"], "A"],
        ["Royal Bow", 38, 60, 20, "Metal", "No special ability.", ["Hyrule Castle Island"], "A"],
        ["Mighty Lynel Bow", "20*3", 35, 20,"Metal", "This bow shoots 3 arrows at once, for the cost of one.", ["Lanayru Great Spring", "Akkala Highlands Depths"], "A"],
        ["Forest Dweller's Bow", "15*3", 50, 20, "Wood", "This bow shoots 3 arrows at once, for the cost of one.", ["Great Hyrule Forest"], "A"],
        ["Zonaite Bow", 30, 50, 20, "Zonaite", "This bow's fire range starts at 20, but can shoot further when charged for longer. This consumes battery.", ["Lomei Labyrinth Island", "Lomei Sky Labyrinth", "Lomei Depths Labyrinth"], "A"],


        ["Royal Guard's Bow", 50, 20, 30, "Metal", "No special ability.", ["Hyrule Castle Island"], "S"],
        ["Demon King's Bow", 60, 42, 30, "Wood", "The attack damage of this bow starts at 12, and increases by +2 with every unbroken heart container Link has. 60 is the maximum attack power. Cannot be repaired by a Rock Octorok.", ["Can be obtained by defeating Gloom Spawn and Phantom Ganon."], "S"],
        

        ["Savage Lynel Bow", "32*3", 45, 20, "Metal","This bow shoots 3 arrows at once, for the cost of one.", ["Gerudo Highlands", "Lanayru Wetlands Depths", "Floating Coliseum"], "S+"],
        ["Great Eagle Bow", "28*3", 60, 40, "Wood", "This bow shoots 3 arrows at once, for the cost of one.", ["Rito Village - Complete the side quest - 'The Legacy of the Rito', activated by speaking to Teba after completing the Wind Temple."], "S+"]
        
    ]

    return bows

def returnBowDescs():
    global bowDescs

    bowDescs = [
        "This wooden bow may not be the most reliable for battling monsters, but it is excellent for hunting small animals.",
        "A bow used by a Captain Construct. Though simply built, it is made of fireproof materials and won't catch fire as wooden bows do.",
        "A basic Bokoblin bow made of wood. It's made by taking any tree branch and just tying a string to either end, so don't expect much in the way of combat effectiveness.",
        "A wooden bow from the olden days. It's built for hunting, but it's not very powerful.",

        
        "A small bow used by travelers for protection. It doesn't do a lot of damage, but it can be used to attack foes from a distance.",
        "A sturdy bow for a Captain Construct. Besides being fireproof, it's been strengthened to allow for more powerful shots.",
        "An upgraded Boko bow bound with animal bone to boost its durability and firepower. Its craftsmanship is sloppy, but it's light and easy to use.",
        "A wooden bow created by Lizalfos. It's reinforced by the bones of a large fish— a marked improvement over any standard wooden bow.",


        "A bow designed for armed conflict. Inflicts more damage than a civilian bow, but it will still burn if it touches fire.",
        "A bow passed down through the Sheikah tribe. Concentrating before drawing the string will allow you to target distant enemies as easily as those nearby.",
        "This bow is a favorite among Rito warriors. The bowstring has been specially engineered for aerial combat, which allows it to be drawn faster than a normal bow.",
        "A powerful bow for a Captain Construct. Though still fireproof, it's more complex than earlier models. The bowstring is extremely tense and requires great strength to draw.",
        "A highly refined Rito-made bow created by a master Rito craftsman. Rito warriors favor it for its superior rate of fire, which helps them excel even further at aerial combat.",
        "A bow favored by the skilled archers of the Yiga Clan. It's been engineered to fire two arrows at once to ensure your target comes to a swift and none-too-pleasant halt.",

        
        "A Lynel-made bow crafted from rough metal. True to the vicious nature of Lynel weaponry, it fires a spread of multiple arrows at once. Ideal for taking down quick-moving targets.",
        "The sturdy metal construction of this bow offers superior durability, while its lack of firing quirks makes it quite reliable. Once favored by the knights at Hyrule Castle.",
        "A Boko bow reinforced by fossils. Bokoblins handpicked the materials it's made from, so it boasts a respectable firepower.",
        "A bow favored by the Zora for fishing. It doesn't boast the highest firepower, but the special metal it's crafted from prioritizes durability.",
        "A Lizal bow with a grip reinforced by metal. The body is made from the branches of a flexible tree that grows near water, which offers some serious destructive power.",
        "This Gerudo-made bow is popular for the fine ornamentations along its limbs. Designed for hunting and warfare alike, this bow was engineered to strike distant targets.",


        "This bow is wielded by Lizalfos who are expert marksmen. The metal that reinforces much of the weapon adds some additional weight but offers heightened durability.",
        "A bow that's been in the royal family for ages. Said to have been used by a princess who fought beasts of twilight. It forcefully fires long-range arrows.",
        "In the past, the king of Hyrule presented this bow to only the most talented archers in the land. Its combat capabilities are as impressive as its extravagant design.",
        "This massive Lynel bow sports a bowstring made from a metal so tough, mere Hylians have trouble drawing it back.",
        "The Koroks made this bow for Hylians. It's crafted from flexible wood and uses sturdy vines for the bowstring. Its construction may be simple, but it fires multiple arrows at once.",
        "A Zonai bow that draws power from your Energy Cell. Power drains, and arrows can fly much farther according to how long a shot is charged.",


        "This prototype Sheikah-made bow was designed to fight the Great Calamity. Made with ancient technology, it boasts a high rate of fire and firepower but has low durability.",
        "A magical bow prized by the Demon King. Its performance reflects the power of its wielder. The higher your maximum number of hearts, the more its attack power increases.",

        "This Lynel bow is made from a special steel found at the peak of Death Mountain. It has tremendous stopping power and can pierce thick armor as easily as thin paper.",
        "A bow without equal wielded by the Rito Champion, Revali. It's said Revali could loose arrows with the speed of a gale, making him supreme in aerial combat."
    ]

    return bowDescs