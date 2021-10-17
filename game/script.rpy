# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Self")
define t = Character("Tutorial/Narrator")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    #scene: entrance to kitchen

    "Oh? I think it's time to buy some more groceries."

    "But before that, I should check what's in my fridge!"

    scene fridge
    #show fridge(closed)

    t "Looking into your fridge? Guess it's time for a Tutorial!"

    #instructions about clicking around items

    t "Let's see what we have here..."

    #show fridge(opened, full of items)

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

    #bananas

    #broccoli/cauliflower

    #grapes

    #tomatoes

    #leftovers (take out leftovers)

    #eggs

    #butter

    #milk

    #sour cream

    #yogurt

    #cheese

    #ketchup

    #mayo

    #mustard

    #dessert (depends on what you make)

    #costco rotisserie chicken

    "Some tasty cold rotisserie chicken in a container. I ate this with family a few days back, so most of it has been eaten."

    menu:
        "Check":
            jump chicken_check #variable that chicken is true
            "Just as I suspected, this {i}chicken{/i} is more bones than white meat, but this has only been in the fridge a few days."

            "Maybe I'll make some bone broth with the remains."

            menu:
                "Leave it":
                    "Still looks good. I'll need to buy more protein for dinner."
                "Toss":
                    "I throw the chicken out (or put it in my compost if that's available in my area)." #delete item from fridge

                    "I'll need to buy more protein for dinner. Maybe a smaller chicken this time around to limit what I throw away." #add to shopping list?
        "Leave it":
            "I'll check on this later."
    #Variable if all items have been Checked/true- maybe all items start as false?
    "Seems like I {i}Checked{/i} everything I could in this fridge and am ready to go grocery shopping."
    #fridge(closed)

    "Some things I couldn't consume or use anymore that I had to {b}Toss{/b} them away, but hopefully with what I have left I can whip up a few more things."

    "If I check my fridge right before I shop, I can make sure that I don't overbuy and have to {b}Toss{/b} it out in the future- and save some money while I'm at it!"

    #entrance to kitchen
    t "Thanks for playing {b}Fridge Reality Check, the Game{/b}."

    t "Hopefully this was fun and informational and happy shopping!"

    # This ends the game.

    return
