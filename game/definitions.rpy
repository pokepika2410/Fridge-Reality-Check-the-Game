# Voices/Characters -----------------------------------------------------------
define s = Character("Self")
define t = Character("Tutorial/Narrator")

# Images ----------------------------------------------------------------------
init -10:
    image kitchen = "/images/bg/fridge.png"

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
        xstart=666, ystart=1117,
        checked = False
    )
    f_broccoli = Food(
        key = "broccoli",
        name = "Broccoli",
        xstart=1013, ystart=1120,
        checked = False
    )
    f_grapes = Food(
        key = "grapes",
        name = "Bunch of Grapes",
        xstart=775, ystart=1130,
        checked = False
    )
    f_tomatoes = Food(
        key = "tomatoes",
        name = "Ripe Tomatoes",
        xstart=875, ystart=544,
        checked = False
    )
    f_takeout = Food(
        key = "takeout",
        name = "Takeout Box",
        xstart=1029, ystart=521,
        checked = False
    )
    f_eggs = Food(
        key = "eggs",
        name = "Carton of Eggs",
        xstart=684, ystart=956,
        checked = False
    )
    f_butter = Food(
        key = "butter",
        name = "Stick of Butter",
        xstart=1625, ystart=648,
        checked = False
    )
    f_milk = Food(
        key = "milk",
        name = "Gallon of Milk",
        xstart=930, ystart=652,
        checked = False
    )
    f_cheese = Food(
        key = "cheese",
        name = "Cheese",
        xstart=404, ystart=501,
        checked = False
    )
    f_ketchup = Food(
        key = "ketchup",
        name = "Ketchup Bottle",
        xstart=1405, ystart=714,
        checked = False
    )
    f_cake = Food(
        key = "cake",
        name = "Slice of Cake",
        xstart=404, ystart=501,
        checked = False
    )
    f_chicken = Food(
        key = "chicken",
        name = "Costco Rotisserie Chicken",
        xstart=404, ystart=501,
        checked = False
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
