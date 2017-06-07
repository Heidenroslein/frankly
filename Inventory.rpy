init -1 python:
    import renpy.store as store
    import renpy.exports as renpy # we need this so Ren'Py properly handles rollback with classes
    from operator import attrgetter
    
    ###This sets initial inventory page to 0!###
    inv_page = 0
    ###Item none here lets us use the item stuff in the screen inventory_screen###
    item = None
    class Player(store.object):
        def __init__(self, name, selection, kind=None, max_hp=0, max_mp=0):
            self.name=name
            self.selection=[]
            self.kind=kind
            self.max_hp=max_hp
            self.hp=max_hp
            self.max_mp=max_mp
            self.mp=max_mp
        def toggleselect(self, item):
            if item in self.selection:
                self.deselect(item)
            else:
                self.select(item)
        def select(self, item):
            self.selection.append(item)
        def deselect(self, item):
            if item in self.selection: 
                self.selection.remove(item)
        def dump(self):
            self.selection=[]
        def combine(self, item):
            if self.selection in combinationlist:
                for line in item.recipe:
                    inventory.drop(line[0], line[1])
                inventory.add(item)
            else:
                message = "It didn't work!"
                renpy.show_screen ("inventory_popup", message=message)
        def has_selected(self, item):
                if item in self.selection:
                    return True
                else:
                    return False
            
        
                
    player = Player("Dr. Frank", 100, 50)
    ###Im not sure what this does...?###
    
    
    ###I tried leaving off (store.object) here, but it gave me an error when i started playing around with code, saying that StoreModule has no attribute of item###
    class Item(store.object):
        def __init__(self, name, kind="None", image_idle="", image_hover="", recipe=False):
            ###These were my pockets in my box###
            global cookbook
            self.name = name
            self.kind = kind
            self.image_idle=image_idle
            self.image_hover=image_hover
            self.recipe=recipe
    ###This is my Item box###
        class Kind:
            ###Im setting my Kinds to numbers###
            SHIRT = 1
            NAPKIN = 2
            PANTS = 3
            SHOES = 4
            WEAPON = 5
            MAGAZINE = 6
            TOOL = 7
            PLANT = 8
            BODYPART = 9
            BOOK = 10
            FANCYSHIRT = 11
            PIG = 12
        #def combine_with(self, other):
            ####Combines this item with another.###
            #combo = frozenset([self.kind, other.kind])
            #if combo in combinations:
                #return combinations[combo](self, other)
                
                
    class Inventory(store.object):
        ###This is my Inventory box ### 
        def __init__(self, money=10):
            self.money = money
            ### I think this self.items[] is creating a pocket in which I can store my inventory items, like a string..? ###
            self.items = []
        ###Here I am defining what it means to add something to the inventory, like inventory.add(chocolate) for example ###
        def add(self, item): # a simple method that adds an item; we could also add conditions here (like check if there is space in the inventory)
            self.items.append(item)
        ### Defining what it means to drop ###
        def drop(self, item):
            self.items = [i for i in self.items if i.name != item.name]
        ### Defining what it means to buy, which i dont need to worry about for my game###
        def buy(self, item):
            if self.money >= item.cost:
                self.items.append(item)
                self.money -= item.cost
        ### HEAVEN HELP ME
        def has_item (self, item):
                if item.name in [i.name for i in self.items]:
                    return True
                else:
                    return False
        def __eq__(self, other):
            return self.name == other.name
        
    def item_use():
        item.use()
        
    def find_outcome (item1 , item2):
        name_list = [ item1.name , item2.name ]
        name_list.sort() # this sorts the name in alphabetical order
        combined_name = ''.join([name_list[0],'-',name_list[1]])
        if combined_name in [x[0] for x in combo_list]:
            result_name = combo_list[ [x[0] for x in combo_list].index(combined_name) ][1]
            for item in complete_item_list:
                if item.name == result_name:
                    inventory.items.append(item)
                    break
            inventory.drop(item1)
            inventory.drop(item2)
            player.selection=[]
            return True
        else:
            message = "It didn't work!"
            renpy.show_screen ("inventory_popup", message=message)
        
    combo_list = [ ("Bed Shirt-Napkin", "Fancy Shirt")]
    #(X, Y) -> X = Ingredients, Y = Outcome
    
    
    #FOR LATER, if you learn a recipe later try:
    #combo_list.append( (INGREDIENTS , OUTCOME) )

###This is my button to open the inventory!###
screen inventory_button:
    add "images/gui/inventory_screen/fencebutton.png"
    imagebutton auto "images/gui/inventory_screen/inventory_button_%s.png" xpos 0 ypos 0 focus_mask True action [ Show("inventory_screen"), Hide("inventory_button"), SetVariable("inventory_pos", "right"), SetVariable("inventory_look", "noshow")]
 
screen inventory_button2: 
    add "images/gui/inventory_screen/fencebutton2.png"
    imagebutton auto "images/gui/inventory_screen/inventory_button2_%s.png" xpos 0 ypos 0 focus_mask True action [ Show("inventory_screen"), Hide("inventory_button2"), SetVariable("inventory_pos", "left"), SetVariable("inventory_look", "noshow")]

###THis is my inventory screen!###,
screen inventory_screen:
    add "images/gui/inventory_screen/inventoryscreen.png"
    modal True
    if inventory_pos == "left":
        imagebutton auto "images/gui/inventory_screen/inventory_exit_%s.png" xpos 0 ypos 0 focus_mask True action [ Hide("inventory_screen"), Hide ("item_options"), Show("inventory_button2"), SetVariable("inventory_look", "show"), player.dump]
    elif inventory_pos == "right": 
        imagebutton auto "images/gui/inventory_screen/inventory_exit_%s.png" xpos 0 ypos 0 focus_mask True action [ Hide("inventory_screen"), Hide ("item_options"), Show("inventory_button"), SetVariable("inventory_look", "show"), player.dump]
    $ x = 235 # coordinates of the top left item position
    $ y = 180
    ###Im not entirely sure how this works, but its setting how to sort items!###
    $ sorted_items = sorted(inventory.items, key=attrgetter('kind'), reverse=True)
    ###i here means what page of the inventory###
    $ i = 0
    $ next_inv_page = inv_page + 1
    #$ prev_inv_page = inv_page - 1
    ###Adjust the number here for how many 
    if next_inv_page > int(len(inventory.items)/4):
        $ next_inv_page = 0
    for item in sorted_items:
        if i+1 <= (inv_page+1)*4 and i+1>inv_page*4:
            $ x += 170
            $ picidle = item.image_idle
            $ pichover = item.image_hover
            imagebutton idle picidle hover pichover xpos x ypos y focus_mask True action [ Show("item_options"), SetVariable("item", item), lambda:player.toggleselect(item)]
            if item in player.selection:
                add "images/gui/selected.png" xpos x ypos y #anchor (0.5,0.5)
        $ i += 1
        if len(inventory.items)>4:
            imagebutton auto "images/gui/inventory_screen/inventory_screen_arrowdown_%s.png" xpos 0 ypos 0 focus_mask True action [SetVariable('inv_page', next_inv_page), Show("inventory_screen")]
            #imagebutton auto "images/gui/inventory_screen/inventory_screen_arrowup_%s.png" xpos 0 ypos 0 focus_mask True action [SetVariable('inv_page', prev_inv_page), Show("inventory_screen")]
    
  
screen item_options:
    add "images/gui/inventory_screen/inventory_options_base.png"
    if len(player.selection)==1:
        imagebutton auto "images/gui/inventory_screen/inventory_options_examine_%s.png" xpos 0 ypos 0 focus_mask True action [ Hide("item_options"), Hide ("inventory_screen"), Show("examine_screen"), lambda:player.deselect(item)]
    else:
        add "images/gui/inventory_screen/inventory_options_examine_idle.png"
    if len(player.selection)==1:
        if inventory_pos == "left":
            imagebutton auto "images/gui/inventory_screen/inventory_options_use_%s.png" xpos 0 ypos 0 focus_mask True action [ Hide("item_options"), Hide ("inventory_screen"), Show("inventory_button2"), SetVariable("item_use", "True"), SetVariable("inventory_look", "show"), Function(change_cursor, "2"),]
        elif inventory_pos == "right":
            imagebutton auto "images/gui/inventory_screen/inventory_options_use_%s.png" xpos 0 ypos 0 focus_mask True action [ Hide("item_options"), Hide ("inventory_screen"), Show("inventory_button"), SetVariable("item_use", "True"), SetVariable("inventory_look", "show"), Function(change_cursor, "2"),]
    else:
        add "images/gui/inventory_screen/inventory_options_use_idle.png"
    if len(player.selection)==2:
        imagebutton auto "images/gui/inventory_screen/inventory_options_combinesmall_%s.png" xpos 700 ypos 450 focus_mask True action Function( find_outcome , player.selection[0] , player.selection[1] )
    else:
        add "images/gui/inventory_screen/inventory_options_combine_idle.png"
screen examine_screen:
    add "images/gui/examine_screen/examine_screen_base.png"
    modal True
    if inventory_pos == "left":
        imagebutton auto "images/gui/examine_screen/examine_screen_return_%s.png" xpos 0 ypos 0 focus_mask True action [Hide ("examine_screen"), Show ("inventory_button2"), player.dump]
    elif inventory_pos == "right":    
        imagebutton auto "images/gui/examine_screen/examine_screen_return_%s.png" xpos 0 ypos 0 focus_mask True action [Hide ("examine_screen"), Show ("inventory_button"), player.dump]

    
screen inventory_popup(message):
    zorder 100
    frame:
        style_group "invstyle"
        hbox:
            text message
    timer 1.5 action Hide("inventory_popup")    
    
    #def combine_food_god(a, b):
    #if a.kind is Item.Kind.CLOTHING:
        #return combine_food_god(b, a)
    #return "GODLIKE " + a.name

#def combine_food_weapon(a, b):
    #if a.kind is Item.Kind.WEAPON:
        #return combine_food_weapon(b, a)
    #return "DANGEROUS " + a.name

#combinations = {
    #frozenset([Item.Kind.FOOD, Item.Kind.GOD]): combine_food_god,
    #frozenset([Item.Kind.FOOD, Item.Kind.WEAPON]): combine_food_weapon
#}
        







































#class Item:
#    class Kind:
#        WEAPON = 1
#        FOOD   = 2
#        GOD    = 3
#    def __init__(self, name, poo, hp=0, mp=0):
#        self.name = name
#        self.poo = poo
#        self.hp = hp
#        self.mp = mp
#    def __str__(self):
#        return 'I am a ' + self.name
        
#gun = Item('gun', Item.Kind.WEAPON)
#apple = Item('apple', poo=Item.Kind.WEAPON, mp=10)
#tencommandments = Item('The Ten Commandments', Item.Kind.GOD, 10)

#inventory = [gun, apple, tencommandments]

#for item in inventory:
#    if item.poo == Item.Kind.GOD:
#        print "God swoops down and says not to drop the {}".format(item)
#    else:
#        print "I don't know what {} is? O:".format(item)
        
#for meatballs in inventory:
#    if meatballs.hp <5:
#        print "YOU DUN DIED SUCKER HAHA, {} doesn't cure for shit.".format(meatballs.name)
#    elif meatballs.hp >5:
#        print "Congrats u didnt die"

#class Item:
#    """This is my Item box"""
#    class Kind:
#        WEAPON = 1
#        FOOD   = 2
#        GOD    = 3
#    def __init__(self, name, kind):
#        """These were my pockets in my box"""
#        self.name = name
#        self.kind = kind
#    def combine_with(self, other):
#        """Combines this item with another."""
#        combo = frozenset([self.kind, other.kind])
#        if combo in combinations:
#            return combinations[combo](self, other)

#a = Item('banana', Item.Kind.FOOD)
#b = Item('sword', Item.Kind.WEAPON)
#c = Item('chalice', Item.Kind.GOD)
#print "THIS IS A " + a.combine_with(b)