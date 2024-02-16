# TotKED
Tears of the Kingdom Equipment Dictionary: A Python program that acts as a dictionary for all the data for armour, weapons, shields, and bows.

## Installation
You must have Python 3 installed on your computer. It must be running Windows, or unexpected errors may occur.
Download the latest ```.exe``` release for TotKED in releases. Execute the file as normal. Errors will come up saying the file is suspicious as 
it is from an unknown source. I can guarantee you that the program will not affect your computer in any malicious ways despite what Windows says.
When the blue window comes up on running the program, click "More Details", and then "Run Anyway".

## Commands
Type the name of any weapon, bow, shield, or armour set into the terminal to see specific details.\
```W``` - Prints all pristine weapon names, tiers, and efficiency numbers.\
```W-``` - Prints all weapon names (including decayed, normal, and legendary), tiers, and efficiency numbers.\
```S``` - Prints all shield names, tiers, and efficiency numbers. The value for the Hylian Shield is absurdly high (4000.0).\
```B``` - Prints all bow names, tiers, and will soon include efficiency numbers. The multipliers for multishot bows will be included in the equation.\
```A``` - Prints all armour sets. These are not tiered.\

Equations for efficiency numbers are as follows;

For shields: 
```py
round((defense*durability)/18, 1)
efficiency = float(efficiency)
```

For weapons:
```py
round(int(trueAttack)*int(durability))/12
#Note: "trueAttack is the actual attack damage of the weapon.
#Every weapon in Tears of the Kingdom has a hidden attack modifier for spear or two-handed weapons.
#For spears: true damage is shown damage is divided by 1.33
#For two-handed weapons: true damage is shown damage is divided by 0.95
#DISCLAIMER: rounding on some of the weapons for their trueAttack value may be incorrect, as the game uses
#... a mixture of floor and ceiling rounding depending on the weapon.
```

