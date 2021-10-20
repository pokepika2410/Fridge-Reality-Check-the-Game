label game_start():
    if fridge.all_checked():
        jump game_end
    window hide
    hide screen focus_dialogue
    $ renpy.pause(hard=True)

label food_navi(food):
    show screen focus_dialogue
    if not food.checked:
        call expression "view_{}".format(food.key)
        menu: 
            "Check":
                $ fridge.update(food.check())
                call expression "check_{}".format(food.key)
            "Leave it":
                "I'll check on this later."
    else:
        call expression "check_{}".format(food.key)
        if food.key not in ["broccoli", "butter", "ketchup"]:
            if food.key == "tomatoes":
                menu: 
                    "Fruit":
                        call expression "fruit_{}".format(food.key)
                    "Vegetable":
                        call expression "veg_{}".format(food.key)
            elif food.key == "cake":
                menu: 
                    "Keep":
                        call expression "keep_{}".format(food.key)
                    "Put in Freezer":
                        call expression "freezer_{}".format(food.key)
            else:
                menu:
                    "Keep":
                        call expression "keep_{}".format(food.key)
                    "Toss":
                        $ fridge.toss(food)
                        call expression "toss_{}".format(food.key)
    jump game_start

# Transforms ------------------------------------------------------------------
transform focus_effect:
    on idle:
        linear 0.15 yoffset 0
    on hover:
        ease 0.15 yoffset -15

#--------------------------------------------------------------------------
# KITCHEN SCREEN
#--------------------------------------------------------------------------
screen kitchen(fridge):
    zorder 0
    # add "/images/bg/fridge.png":
    #     zoom 0.1 xpos 0 ypos 0

    # populate fridge
    for i in fridge.items:
        imagebutton:
            idle Transform("/images/food/{}.png".format(i.key), zoom=0.25)
            xpos i.xstart / 2
            ypos i.ystart / 2
            tooltip i.name
            focus_mask True
            mouse "hover"
            action Call("food_navi", i)
            at focus_effect

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