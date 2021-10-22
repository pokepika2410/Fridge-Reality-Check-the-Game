# Voices/Characters -----------------------------------------------------------
define s = Character("Self")
define t = Character("Tutorial/Narrator")

# Images ----------------------------------------------------------------------
init -1:
    image kitchen = "/images/bg/fridge.png"
    image kitchenhalf = "/images/bg/fridge_half_open.png"
    image kitchenopen = "/images/bg/fridge_open.png"
    image kitchentitle = "/images/bg/title.png"

# Food ------------------------------------------------------------------------
init -1 python:
    class Food(store.object):
        def __init__(self, key, name, xstart=0, ystart=0, checked=False):
            self.key = key # key for image path and label jumping
            self.name = name # name of food for tooltips
            self.xstart = xstart # top left corner position of image
            self.ystart = ystart
            self.checked = False

        def __repr__(self): # for debug printing
            return str({"name": self.name, "state": self.checked})

        def check(self):
            self.checked = True
            return self
        def move(self, xpos=None, ypos=None):
            if xpos:
                self.xstart = xpos
            if ypos:
                self.ystart = ypos
            return self

    class Fridge(store.object):
        def __init__(self, items=[]):
            self.items = items
        def toss(self, food):
            self.items = [i for i in self.items if not (i.key == food.key)]
        def update(self, food):
            for i, itr in enumerate(self.items):
                if itr.key == food.key:
                    self.items[i] = food
        def all_checked(self):
            for i in self.items:
                if not i.checked:
                    return False
            return True

    f_bananas = Food(
        key = "bananas",
        name = "Bunch of Bananas",
        xstart=360, ystart=586
    )
    f_broccoli = Food(
        key = "broccoli",
        name = "Broccoli",
        xstart=508, ystart=587
    )
    f_grapes = Food(
        key = "grapes",
        name = "Bunch of Grapes",
        xstart=422, ystart=592
    )
    f_tomatoes = Food(
        key = "tomatoes",
        name = "Ripe Tomatoes",
        xstart=403, ystart=290
    )
    f_takeout = Food(
        key = "takeout",
        name = "Takeout Box",
        xstart=532, ystart=285
    )
    f_eggs = Food(
        key = "eggs",
        name = "Carton of Eggs",
        xstart=536, ystart=496
    )
    f_butter = Food(
        key = "butter",
        name = "Stick of Butter",
        xstart=825, ystart=332
    )
    f_milk = Food(
        key = "milk",
        name = "Gallon of Milk",
        xstart=474, ystart=370
    )
    f_cheese = Food(
        key = "cheese",
        name = "Cheese",
        xstart=555, ystart=390,
    )
    f_ketchup = Food(
        key = "ketchup",
        name = "Ketchup Bottle",
        xstart=717, ystart=400
    )
    f_cake = Food(
        key = "cake",
        name = "Slice of Cake",
        xstart=381, ystart=388
    )
    f_chicken = Food(
        key = "chicken",
        name = "Costco Rotisserie Chicken",
        xstart=388, ystart=483
    )


# Text tags -------------------------------------------------------------------
init python:
    def interesting(tag, argument, contents):
        color = "#d14970"
        return [
                (renpy.TEXT_TAG, "color={}".format(color)),
                (renpy.TEXT_TAG, "b"),
                (renpy.TEXT_TAG, "k={}".format(-1.2))
                ] + contents + [
                (renpy.TEXT_TAG, "/k"),
                (renpy.TEXT_TAG, "/b"),
                (renpy.TEXT_TAG, "/color")
                ]
    config.custom_text_tags["ii"] = interesting

    def title(tag, argument, contents):
        color = "#b96784"
        return [
                (renpy.TEXT_TAG, "color={}".format(color)),
                (renpy.TEXT_TAG, "b"),
                (renpy.TEXT_TAG, "k={}".format(-1.2))
                ] + contents + [
                (renpy.TEXT_TAG, "/k"),
                (renpy.TEXT_TAG, "/b"),
                (renpy.TEXT_TAG, "/color")
                ]
    config.custom_text_tags["tt"] = title

    def quote(tag, argument, contents):
        color = "#B96784"
        return [
                (renpy.TEXT_TAG, "color={}".format(color)),
                (renpy.TEXT_TAG, "i"),
                ] + contents + [
                (renpy.TEXT_TAG, "/i"),
                (renpy.TEXT_TAG, "/color")
                ]
    config.custom_text_tags["qq"] = quote

    def thoughts(tag, argument, contents):
        alpha = 0.6
        return [
                (renpy.TEXT_TAG, "i"),
                (renpy.TEXT_TAG, "alpha={}".format(alpha)),
                ] + contents + [
                (renpy.TEXT_TAG, "/i"),
                (renpy.TEXT_TAG, "/alpha"),
                ]
    config.custom_text_tags["th"] = thoughts

    def smallText(tag, argument, contents):
        size = 22
        alpha = 0.7
        return [
                (renpy.TEXT_TAG, "size={}".format(size)),
                (renpy.TEXT_TAG, "alpha={}".format(alpha)),
                ] + contents + [
                (renpy.TEXT_TAG, "/alpha"),
                (renpy.TEXT_TAG, "/size"),
                ]
    config.custom_text_tags["ss"] = smallText
