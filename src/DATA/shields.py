def returnShields():
    global shields
    syntax = ["Shield Name", "Defense", "Durability", "Material", "Locations", "Tier"]
    
    shields = [["Pot Lid", 1, 10, "Wood", ["Hyrule Field", "East Necluda"], "F"],
               ["Old Wooden Shield", 2, 12, "Wood", ["Great Sky Island", "Gerudo Desert"], "F"],
               ["Wooden Shield", 2, 12, "Wood", ["Hyrule Field", "Hebra Mountains"], "F"], 
               ["Rusty Shield", 3, 16, "Metal", ["Hyrule Field", "East Necluda"], "F"],
               ["Hunter's Shield", 3, 10, "Wood", ["Tabantha Frontier", "Hebra Mountains"], "F"], 
               ["Fisherman's Shield", 3, 10, "Wood", ["Lurelin Village"], "F"], 
               ["Emblazoned Shield", 3, 12, "Wood", ["East Necluda, West Necluda"], "F"], 
               ["Boko Shield", 3, 5, "Wood", ["Hyrule Field", "Hebra Mountains", "Greater Hyrule"], "F"], 
               ["Traveler's Shield", 4, 12, "Wood", ["Hyrule Field", "Eldin Mountains"], "F"], 

               
               ["Spiked Boko Shield", 10, 7, "Wood", ["Hyrule Field", "East Necluda"], "E"], 
               ["Lizal Shield", 16, 8, "Metal", ["Lanayru Great Spring", "Faron Sea"], "E"],
               ["Dragonbone Boko Shield", 25, 8, "Wood", ["Gerudo Highlands", "Gerudo Desert"], "E"],


               ["Zonaite Shield", 11, 15, "Zonaite", ["Necluda Archipelago", "Eldin Sky Archipelago"], "D"], 
               ["Kite Shield", 14, 16, "Wood", ["Hebra Mountains", "Tabantha Frontier"], "D"],
               ["Shield of the Mind's Eye", 16, 16, "Wood", ["East Necluda", "West Necluda", "Greater Necluda"], "D"],
               ["Soldier's Shield", 16, 16, "Wood", ["Hyrule Field", "Eldin Canyon"], "D"],
               ["Reinforced Lizal Shield", 22, 12, "Metal", ["Tabantha Tundra", "Abandoned Kakariko Mine"], "D"],

               
               ["Zora Shield", 24, 20, "Metal", ["Lanayru Great Spring", "Lanayru Great Spring Sky"], "C"],
               ["Gerudo Shield", 28, 20, "Metal", ["Gerudo Shield", "Gerudo Highlands"], "C"],

               
               ["Lynel Shield", 30, 12, "Metal", ["Hyrule Field", "Central Hyrule Depths"], "B"],
               ["Forest Dweller's Shield", 30, 18, "Wood", ["Great Hyrule Forest"], "B"],
               ["Steel Lizal Shield", 35, 15, "Metal", ["Gerudo Desert", "Mount Lanayru"], "B"],

               
               ["Knight's Shield", 40, 23, "Metal", ["Gerudo Desert", "Tabantha Frontier Depths"], "A"],
               ["Mighty Lynel Shield", 44, 15, "Metal", ["Faron Grasslands", "Eldin Canyon Depths"], "A"],
               ["Mighty Zonaite Shield", 50, 20, "Zonaite", ["Lomei Labyrinth Island", "North Lomei Labyrinth"], "A"],
               ["Savage Lynel Shield", 62, 20, "Metal", ["Akkala Highlands", "Central Hyrule Depths"], "A"],

               
               ["Daybreaker", 48, 60, "Metal", ["Gerudo Town"], "S"],
               ["Royal Shield", 55, 29, "Metal", ["Hyrule Field", "Gerudo Highlands Depths"], "S"],
               ["Royal Guard's Shield", 70, 14, "Metal", ["Hyrule Castle Island"], "S"],

               
               ["Sea-Breeze Shield", 65, 90, "Metal", ["Western Abandoned Lanayru Mine"], "S+"],

               ["Hylian Shield", 90, 800, "Metal", ["Hyrule Castle Docks"], "X"]
              ]

    
    return shields


def returnShieldDesc():
    global shieldDescs
    shieldDescs = ["The lid of a large soup pot. It smells vaguely of poultry broth...Yum! It can take quite a beating before breaking.",
                  "An aged, worn-out wooden shield. It can withstand lighter attacks such as arrows.",
                  "This lightweight, simple shield is ideal for less experienced fighters. It can withstand light attacks, but blocking stronger blows is not recommended",
                  "It’s likely this rusty old shield once belonged to a knight. It still has some defensive capabilities, but its usefulness has been worn down by time.",
                  "Favored by hunters for its rabbit design, which is said to bring luck on hunts. It's easy to use, but its durability leaves something to be desired.",
                  "Often carried by fisherman for its fish design, which represents hope for a great catch. Its light wooden construction makes it convenient to take onto a boat.",
                  "This shield features a traditional design from Necluda. Its combat capabilities aren't much better than the standard wooden shield, but it found popularity for its design.",
                  "A bokoblin-made shield created by attaching a handhold to any flat tree bark, picked up off the ground. It’s pretty shoddy, so don’t expect it to last very long.",
                  "A sturdy shield loved by many an adventurer. It is made of animal hide and sturdy wood and is best suited to defending against weak monsters or animals.",
                  "A Boko Shield made of slightly stronger wood and reinforced with animal bones.",
                  "A Shield used by Zonai and made of zonaite. It lowers the energy consumption of an attached Zonai device.",
                  "Rito warriors cherish this shield. Its unique shape is designed with midbattle flight in mind to facilitate aerial combat.",
                  "A common shield found among the Lizalfos. It's made of metal, but its sloppy craftmanship offers poor durability.",
                  "This Boko shield is reinforced with fossilized bone. Its defensive capabilities are respectable, but its predictably slipshod craftsmanship spells low durability.",
                  "A small Sheikah-made shield. Its design is intended to decrease blind spots without sacrificing too much defense.",
                  "A shield once used by the guards of Hyrule Castle. It’s easy to handle, but its core is made of wood so it can catch fire.",
                  "This Lizal shield has been strengthened by adding a different type of metal to the mix. The edge is lined with spikes, so handle with care.",
                  "A Zora-made shield adorned with intricate ornamentation. It’s said that true masters of this shield can redirect attacks as a rock redirects rushing water.",
                  "The design of this metal shield has changed over time to match the Gerudo's sword-and-shield fighting style. It's favored by soldiers and travelers alike.",
                  "A sturdy shield favored by Lynels for its defensive and offensive capabilities. First and foremost a shield, but the bladed edges can deal slashing attacks when deflecting.",
                  "The Koroks made this shield specifically for Hylians. It's made from the finest hard wood of trees that grow only in Korok Forest, so it's sturdier than it looks.",
                  "This Lizal shield is adorned with several metal shells as a means of reinforcement. Its defensive capabilities are high, but its weight requires a skilled soldier to bear.",
                  "A shield favored by the knights who served the Hyrulean royal family. Its sturdy metal construction makes it quite durable, but its weight requires decent skill to wield.",
                  "This Lynel-made shield has been reinforced with armor and even more blades. Stronger in both defense and offense, it can tear through basic armor when deflecting.",

                   
                  "A shield used by Zonai and made of zonaite. It is very durable and draws on its stored energy to more efficiently use an attached Zonai device.",

                   "This ultimate Lynel shield is favored by the White-Maned Lynels. It excels at defending against even the most brutal of attacks and cutting down powerful foes when deflecting.",

                   
                  "This shield was cherished by the Gerudo Champion Urbosa. The gold used to make it was handpicked to ensure a design that is both lightweight and very durable.",

                   
                  "A shield issued to the Hyrulean royal family’s immediate guard detail. It boasts a high defense, but these days it’s more of a collector’s item due to it’s ornamentation.",
                   
                  "This shield was forged using ancient Sheikah technology. It boasts extremely high stopping power, but its structural weakness made its low durability impractical for combat.",
                   
                  "A shield said to have been favorite of a hero who traveled the open seas. It was apparently a family heirloom, passed down through many generations.",
                   
                  "A shield passed down through the Hyrulean royal family, along with the legend of the hero who wielded it. It's defensive capabilities and durability outshine all other shields."]

    return shieldDescs