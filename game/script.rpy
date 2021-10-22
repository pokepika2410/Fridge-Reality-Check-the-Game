label start:
    show screen focus_dialogue
    $fridge = Fridge([
        f_bananas,
        f_broccoli,
        f_grapes,
        f_tomatoes,
        f_takeout,
        f_eggs,
        f_butter,
        f_milk,
        f_cheese,
        f_ketchup,
        f_cake,
        f_chicken
    ])

    scene kitchen with dissolve
    "Oh?{p}I think it's time to buy some more groceries."
    "But before that, I should check what's in my fridge!"

    show kitchenhalf with dissolve
    show kitchenopen with dissolve

    t "Looking into your fridge?{p}Guess it's time for a Tutorial!"

    t "Let's see what we have here..."
    show screen kitchen(fridge) with dissolve

    t """
    Click on items in the fridge to look at what you have{p}and what items might have gone bad.

    If an item went bad, feel free to {b}Toss{/b} them.

    Though who knows?{p}{i}Maybe there is some other household uses for them.{/i}

    How can you tell if something went bad?{p}By clicking on {b}Check{/b}!

    After clicking on an item, you can {b}Check{/b} on the item- looking at the dates, having a sniff check, and looking at/in it.

    Afterwards, you can {b}Keep{/b} it in your fridge,{p}or {b}Toss{/b} the item out.

    If you decide to {b}Keep{/b} in the fridge, you can always {b}Check{/b} it again...{p}{i}and {b}Toss{/b} if you changed your mind{/i}.

    However, once you {b}Toss{/b} an item out, it's gone for good!{p}So be careful when you {b}Toss{/b} items away.

    I think that's all as far as this Tutorial goes.

    Thanks for reading and have fun with {b}Fridge Reality Check,{/b}{p}{i} the Game{/i}!
    """

    "Okay... What should I {b}Check{/b}?"

    show screen kitchen(fridge)
    jump game_start

# thermo
label check_thermo():
    show screen focus_dialogue
    "I made sure to set my fridge temperature lower than 40℉ (or 5℃) to ensure that I’m storing food safely."
    jump game_start

# bananas
label view_bananas():
    "A bunch of bananas."
    "I put them in the fridge a few days back as some were getting overripe."
    t "Bananas should typically be stored on counters, see further information in the {a=https://www.stopwaste.org/sites/default/files/StopWaste-FoodStorageGuide-2020.pdf}Food Storage Guide{/a}."
    return
label check_bananas():
    "Oh boy, looks like these bananas have seen better days.{p}Prolonged storage in the fridge made the banana skin all brown."
    "But upon closer inspection, some bananas are still firm,{p}but others are a little on the mushier side.{p}{i}Maybe I can use the mushy bananas to make some banana bread.{/i}"
    return
label keep_bananas():
    "I remember fondly about my college roommate's banana bread, which was simple yet delicious."
    "Guess I should make some banana bread soon."
    "Nevertheless, seeing that I eat only one banana every few days, I should limit how many bananas I buy."
    "Note to self: buy less bananas at a time going forward."
    return
label toss_bananas():
    "I throw the bananas out (or into my compost or green waste bin)."
    "Seeing that I eat only one banana every few days, I should limit how many bananas I buy."
    "Note to self: buy less bananas at a time going forward."
    return

# broccoli
label view_broccoli():
    "A bunch of broccoli."
    "I think about how raw broccoli is basically a tiny tree, for better or worse..."
    return
label check_broccoli():
    "Hmmm… the broccoli is… {p}Shriveled?"
    "Can broccoli even shrivel?"
    "It should be fine if it gets some water."
    "I'll put the broccoli back in the fridge."
    "Maybe use it for soup."
    "But just in case… I'll also sprinkle some water on this guy to rehydrate."
    "No need to buy any other vegetables for now."
    return

# grapes
label view_grapes():
    "A bunch of grapes I bought from my local farmer's market."
    "I think about Dionysus when I look at purple grapes."
    "Come to think of it, I guess the Greeks favored grapes over olives if Aristaeus was less prominent.{p}{i}Unless you rather compare Dionysus to Athena who created olive trees.{/i}"
    "But also, don't grapes look like inverted olives?"
    return
label check_grapes():
    "Gah!{p}Some of the grapes have mold.{p}And I don't like mold."
    "(Sorry Dionysus and grape farmer.)"
    return
label keep_grapes():
    "I separate the moldy grapes from the ones that can still be saved and put the loose grapes into a tupperware."
    return
label toss_grapes():
    "Just to be safe, I'll toss it out (or into my compost or green waste bin if that's available in my area)."
    "While I want to support farmers, maybe I should splurge less at the farmer's market."
    "Upon watching {a=https://www.youtube.com/watch?v=CLFOK4U34wI}Life of a Strawberry{/a} I think about the Life of my Grapes and want to limit wasting effort and additional resources beyond just food."
    "If I want to buy any fruits, I need to cut back to make sure it's an amount I can consume."
    return

# tomatoes
label view_tomatoes():
    "Some ripe tomatoes."
    "I previously had them outside loosely on the counter, away from sunlight, heat, and moisture."
    "When they got ripe, I had to put them into the fridge."
    t "Tomatoes should typically be stored on counters. For more information,  refer to the {a=https://www.stopwaste.org/sites/default/files/StopWaste-FoodStorageGuide-2020.pdf}Food Storage Guide{/a}."
    return
label check_tomatoes():
    if f_tomatoes.xstart == 393:
        "Tomatoes the fruit in the fruit crisper drawer."
    else:
        "The controversial red item."
        "Is this a fruit?{p}Or a vegetable?"
        "Science dictates that it is a fruit (a berry specifically),{p}but culinarily they are vegetables since they go in a bunch of cooked dishes."
        "At least that's what they argued in Nix v. Hedden against the Tariff of 1883."
        "In the end, I make the rules in this (fridge) kingdom.{p}I must take a side."
        "I looked down into the fruit and vegetable crisper drawers…{p}Which crisper drawer should the tomatoes go into?"
    return
label fruit_tomatoes():
    "I slowly picked up the tomatoes and head down to the crisper drawers…{p}BUT THEN-"
    "…{p}nothing happened."
    "The tomatoes went into the fruit crisper drawer."
    $ fridge.update(f_tomatoes.move(xpos=393, ypos=550))
    "Quite anti-climatic if I do say so myself."
    return
label veg_tomatoes():
    "I slowly picked up the tomatoes and head down to the crisper drawers…{p}BUT THEN-"
    t "STOP"
    "I freeze (in my movement, not from the fridge)."
    t "In case you haven't seen the {a=https://www.stopwaste.org/sites/default/files/StopWaste-FoodStorageGuide-2020.pdf}Food Storage Guide{/a}, fruits and vegetables need to be separate in the fridge."
    t "And tomatoes are a fruit!"
    "I nodded promptly at the voice in my head."
    "The tomatoes went into the fruit crisper drawer."
    $ fridge.update(f_tomatoes.move(xpos=393, ypos=550))
    return

# takeout
label view_takeout():
    "Food I took home from the last time I ate out."
    "I forgot to bring my tupperware that day so it's in a takeout container instead."
    return
label check_takeout():
    "Looking in the container, food still looks good."
    "However it's an awkward amount.{p}Not enough for even half a meal!"
    return
label keep_takeout():
    "I'll probably eat this for lunch or dinner tomorrow stir fried with some vegetables{p}Or have it as a late afternoon snack if I'm feeling lazy."
    return
label toss_takeout():
    "I throw the food away, thinking about how I'll be eating out with my friends this coming weekend."
    "I'll need to make sure I either portion the food out to 2 meals or order less."
    return

# eggs
label view_eggs():
    "A carton of eggs."
    "I buy them on a fairly consistent basis."
    "I really like eggs, what can I say?"
    return
label check_eggs():
    "I open up the carton."
    "There are 2 eggs inside."
    "Ah yes… {i}those two…{/i}{p}I actually forgot about {i}those two{/i} for a few weeks now, going straight to newer cartons."
    "Well, better late than never-{p}float test time!"
    "…{p}…"
    "The two eggs are {i}juuuuuuust{/i} low enough to be considered underwater."
    return
label keep_eggs():
    "Looks like the eggs are still good."
    "I'll buy another carton, but need to make sure I eat those two eggs first."
    "I scribble on the carton \"Eat this first!\" to make sure I don't forget again."
    "I'll also make sure to put the new carton below this one so this won't get buried in my fridge again."
    return
label toss_eggs():
    "The eggs are almost rotten, which if I round up like I would in math, means it's rotten."
    "Going by \"feed yourself, feed others, feed the soil\", I'll feed this to one of my pets (if I have a pet)."
    return

# butter
label view_butter():
    "A stick of refrigerated butter (unopened)."
    return
label check_butter():
    "Oooooh, looks like someone (Mr. Butter) has a fresh date~"
    "..."
    "A fresh date of 2 weeks ago..."
    "Nevertheless he looks and smells okay..."
    "Don't fret Mr. Butter!{p}I won't {a=https://www.youtube.com/watch?v=dQw4w9WgXcQ}run around and desert you{/a}!"
    "Ideally I can include Mr. Butter in my next recipe."
    return

# milk
label view_milk():
    "A half full (or half empty) gallon of milk."
    "Being lactose intolerant, I use this mostly for baking."
    "Though sometimes, right after I shower {i}and no one else is home{/i},{p}I chug a cool forbidden glass to live on the wild side."
    "{i}I may or may not have rushed to my Lactaid supply right after to make sure no trouble arises the next day.{/i}"
    return
label check_milk():
    "Ah… It's been a while since I baked… Looks like the milk got sour."
    "But I heard sour milk can be used as a buttermilk substitute..."
    return
label keep_milk():
    "Alright time to bake away."
    "I'll still need some potable milk, but this time I'll opt for half a gallon or even a quart of milk."
    return
label toss_milk():
    "I pour the sour milk down the drain, and feel the slightest bit of remorse over what-if."
    "I'll still need some potable milk, but this time I'll opt for half a gallon or even a quart of milk instead."
    return

# cheese
label view_cheese():
    "Some hardy (hearty?) cheese."
    "Tasty in, with, and on top of other foods."
    return
label check_cheese():
    "!!!"
    "I see…{p}some mold…{p}{i}(shutters){/i}"
    return
label keep_cheese():
    "In an effort to save the cheese, I did an Ecosia (or other search engine of your choice) search and find that mold doesn't spread as far in hard cheeses."
    "I cut off the moldy areas to toss, and put my cheese back to a safe place in the fridge."
    return
label toss_cheese():
    "Just to be safe, I'll toss it out (or into my compost or green waste bin if that's available in my area)."
    return

# ketchup
label view_ketchup():
    "Tomato sauce."
    "But Americans call this tomato ketchup or catsup."
    return
label check_ketchup():
    "I bought a pretty big bottle a while back."
    "Seeing as I have barely put a dent, in retrospect this was more than I could handle."
    "It still looks good... I should use this in a recipe such as naporitan spaghetti or worst of the worst, make my soup more tomato-y."
    return

# cake
label view_cake():
    "Cake."
    "My latest bake-reation."
    return
label check_cake():
    "There’s still a few good slices left."
    "But I’m not sure if I can eat it all before it starts going bad."
    "Better put some of it in the fridge to be safe."
    return
label keep_cake():
    "I keep it them all in the fridge."
    return
label freezer_cake():
    "To be safe, I put all but 2 slices into the freezer so they can stay fresh longer."
    return

# costco rotisserie chicken
label view_chicken():
    "Some tasty cold rotisserie chicken in a container."
    "I ate this with family a few days back, so most of it has been eaten."
    return
label check_chicken():
    "Just as I suspected, this \"chicken\" is more bones than white meat,{p}{i}but{/i} this has only been in the fridge a few days."
    "Maybe I'll make some bone broth with the remains."
    return
label keep_chicken():
    "Still looks good. I will need to buy more protein for dinner though."
    return
label toss_chicken():
    "I throw the chicken out (or put it in my green waste bin if that's available in my area)."
    "I'll need to buy more protein for dinner. Maybe a smaller chicken this time around to limit what I throw away."
    return

label game_end:
    hide screen kitchen with dissolve
    scene fridge with dissolve
    "Seems like I {b}Checked{/b} everything I could in this fridge and am ready to go grocery shopping."

    "Some parts I couldn't use anymore that I had to {b}Toss{/b} them away,{p}but hopefully with what I have left, I can whip up a few more things."
    "If I check my fridge right before I shop, I can make sure that I don't overbuy and have to {b}Toss{/b} it out in the future-{p}and save some money while I'm at it!"
    "After I return, I can refer to the {a=https://stopfoodwaste.org/media/resources/StopFoodWaste-FridgeDemystified2020.pdf}Fridge Demystified{/a} on where to best put my foods away."
    "Now it's time to get some groceries!"

    t "Thanks for playing {b}Fridge Reality Check, the Game{/b}."
    t "Hopefully this was fun and informational! Please fill out this {a=https://forms.gle/VkxmMCU77LYpq23Y6}Feedback Form{/a} to enter into a raffle drawing."
    t "And if you want to do a real life fridge check, refer to the {a=https://www.stopwaste.org/resource/10-minute-fridge-reality-check}10-minute Fridge Reality Checklist{/a}.{p}Happy fridge check!"

    $ MainMenu(confirm=False)()
    return
