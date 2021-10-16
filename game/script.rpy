# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Self")
define t = Character("Tutorial")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    #scene: kitchen?

    "Oh? I think it's time to buy some more groceries."

    "But before that, I should check what's in my fridge!"

    t "Looking into your fridge? Guess it's time for a Tutorial!"

    #instructions about clicking around items

    t "Let's see what we have here..."

    scene fridge
    #show fridge

    t "Click on items in the fridge to look at what you have and what items might have gone bad."

    t "If an item went bad, feel free to toss them.

    {i}Though who knows? Maybe there is some other household uses for them.{/i}"

    t "How can you tell if something went bad? By clicking on {b}Check{/b}!"

    t "After clicking on an item, you can {b}Check{/b} on the item- looking at the dates, a sniff check (smelling the contents), and looking in it."

    t "Afterwards, you can {b}Leave it{/b} in your fridge, or {b}Toss{/b} the item out."

    t "If you decide to {b}Leave it{/b} in the fridge, you can always {b}Check{/b} it again..."

    t "{i}and {b}Toss{/b} if you changed your mind{/i}."

    t "However, once you {b}Toss{/b} an item out, it's gone for good! So be careful when you {b}Toss{/b} items away."

    t "I think thats all as far as this Tutorial goes. Thanks for reading and have fun with {b}Fridge Reality Check, the Game{/b}!"

    "Okay... What should I {b}Check{/b}?"

    #bananas#broccoli/cauliflower#grapes#tomatoes

    #leftovers

    #eggs#butter#milk#sour cream#yogurt #cheese

    #ketchup#mayo#mustard

    #dessert

    #costco rotisserie chicken
    menu:
        "Check":
            ""
            menu:
                "Leave it"
                "Toss" #delete item from fridge
        "Leave it":
            "I'll check on this later."
    # This ends the game.

    return
