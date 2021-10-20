label game_start():
    if fridge.all_checked():
        jump game_end
    window hide
    hide screen focus_dialogue
    $ renpy.pause(hard=True)

label food_navi(food):
    show screen focus_dialogue
    if not food.checked:
        call expression "view_[food.key]"
        menu: 
            Check:
                $ fridge.update(food.check())
                call expression "check_[food.key]"
            Leave it:
                "I'll check on this later."
    else:
        call expression "check_[food.key]"
        if food.key not in ["broccoli", "butter", "ketchup"]:
            if food.key == "tomatoes":
                menu: 
                    Fruit:
                        call expression "fruit_[food.key]"
                    Vegetable:
                        call expression "veg_[food.key]"
            else if food.key == "cake":
                menu: 
                    Keep:
                        call expression "keep_[food.key]"
                    Put in Freezer:
                        call expression "freezer_[food.key]"
            else:
                menu:
                    Keep:
                        call expression "keep_[food.key]"
                    Toss:
                        $ fridge.toss(food)
                        call expression "toss_[food.key]"
    jump game_start

#--------------------------------------------------------------------------
# KITCHEN SCREEN
#--------------------------------------------------------------------------
screen cooking(fridge):
    zorder -10
    add "/images/bg/kitchen.png"

    # populate fridge
    for i in fridge.items:
        imagebutton:
            idle "/images/food/{}.png".format(i.key)
            xpos i.xstart
            ypos i.ystart
            tooltip i.name
            alpha 0.5
            focus_mask True
            mouse "hover"
            action Call("food_navi", i)

    $ tooltip = GetTooltip()
    if tooltip:
        fixed xmaximum 500 xoffset 50:
            text "[tooltip.name]":
                xpos 600 ypos 745
                xalign 0.5
                color "#7c345e"
            text "{size=24}[tooltip.tooltip]{/size}":
                xpos 600 ypos 790
                xalign 0.5
                color "#483e54"

screen focus_dialogue:
    zorder 0
    modal True
    imagebutton:
        idle Solid("#0000")
        action renpy.curry(renpy.end_interaction)(True)
    key "K_SPACE" action renpy.curry(renpy.end_interaction)(True)
    # key "mouseup_4" action ShowMenu('history') # access log on scrollup