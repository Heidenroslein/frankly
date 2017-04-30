# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
#TODO make sure to credit: Amiralo, Z, Laiska (writing help), Goldbar Kinjo (coding), CHOCO!!! ;;;---;;; (coding), Sean (coding), anyone who ever wrote a lemmasoft tutorial, my mucisian! :D, Mention i used textures from freepik.com, 
init 1 python:
    def change_cursor(type="default"):
        persistent.mouse = type
        if type == "default":
            setattr(config, "mouse", None)
        elif type == "1":
            setattr(config, "mouse", {"default": [("images/gui/cursor1.png", 0, 0)]})
        elif type == "2":
            setattr(config, "mouse", {"default": [("images/gui/cursor2.png", 0, 0)]})
            
    if not hasattr(persistent, "mouse"):
        change_cursor()
    else:
        change_cursor(persistent.mouse)
init python:
    def nvl_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("music/nvlvoiceshort.ogg", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()


# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8", show_two_window=True, ctc="ctc_blink")
define dr = Character('Dr. Frank', color="#ccff99", show_two_window=True, ctc="ctc_blink")
define ig = Character('Iggs', color="#ccff99", show_two_window=True, ctc="ctc_blink")
define hotboi = Character('Gorgeous Specimen', color="#ccff99", show_two_window=True, ctc="ctc_blink")
define voi = Character('???', color="#ccff99", show_two_window=True, ctc="ctc_blink")
define nvlbox = Character(None, kind = nvl, callback=nvl_voice, ctc="ctc_blink", ctc_position="fixed", what_xpos=683, what_xalign=0.5)
define mon = Character('Monster', color="#ccff99", show_two_window=True, ctc="ctc_blink")
define syl = Character('Sylios', color="#ccff99", show_two_window=True, ctc="ctc_blink")
define bbydr = Character('Dr. Frank Talking In A Baby Voice', color="#ccff99", show_two_window=True, ctc="ctc_blink", size=50, ypos=-50)
define dom = Character('Dominik', color="#ccff99", show_two_window=True, ctc="ctc_blink")

init:
    
    $ opened_shoeentryway = False
    $ Fr_exp = "angry"
    $ monsterwith = False
    $ sylios_books = False
    $ Susie_hint = False
    $ Meaty_Man_Inventory = False
    $ Iggs_magazine = False
    $ dick = "None"
    $ sylios_garden = False
    
    
    $ use_grower = False
    $ use_mag = False
    
    
    $ twoleft = Position(xalign=0.25)
    $ twofarleft = Position(xalign=0.15)
    $ tworight = Position(xalign=0.75)
    $ twofarright = Position(xalign=0.95)
    $ dialoguepos = Position(xalign=0.45)
    $ dialoguetworight = Position(xalign=0.60)
    $ dialoguetwoleft = Position(xalign=0.10)
    image build-a-boyfriend = DynamicDisplayable(build_boyfriend)
    $ hairstyle = "bald"
    $ haircolorstyle = "red"
    $ penisstyle = "no penis"
    $ eyestyle = "one"
    $ skinstyle = "vanilla"
    $ armstatus = True
    $ looked_shoes = "False"
    $ meet_sylios = False
    $ distract_hint = False
    $ weedgrower_graves = False
    $ seen_flowers = False
    $ seen_necromancy = False
    $ sylios_route = False
    $ need_arm = False
    $ need_to_distract_sylios = True
    
    #Story progress##
    $ need_shovel = False
    $ need_clothes = True
    $ wearing_pants = False
    $ wearing_shoes = False 
    $ wearing_shirt = False
    
    #Items progress###
    $ have_dictionary = False
    $ have_shirt = False
    $ have_pants = False
    $ have_shoes = False
    $ have_grower = False
    $ have_shoes = False
    $ have_knife = False
    
    
    #GUI inventory stuff#
    $ inventory_pos = "right"
    $ inventory_look = "show"
    $ item_use = False
    $ dialogue_choice = False
    $ you_are_here = "gone"
    
    
    #changing variables for item descriptions#
    $ fridge_click = 0
    $ coffee_click = 0
    $ takeout_click = 0
    $ shovel_click = 0
    $ grave_visit = 0
    $ bedroomclothesvisit = 0
    $ Dr_Oink_Count = 0
    $ look_smallshoes = 0
    $ visit_susie = 0
    
    #IGgs dialogue
    $ ig_visit = 0
    $ pep_nip = False
    $ papa_dialogue = False
    $ dom_dialogue = False
    $ sylios_question = False
    $ droink_iggs = False
    $ bad_shirt = False
    $ need_clothes_question = 0
    $ fancy_shirt_question = 0
    $ normal_shirt_question = 0
    $ shoe_question = 0
    
    #Sylios dialogue
    $ sylios_visit = 0
    $ sylios_flirt = False
    $ cauldian_church = False
    $ not_priest = False
    $ sylios_avoidance = False
    $ sylios_droink = False
    $ please_leave_sylios = False
    $ srsly_plz_leave_sylios = False
    $ flirt_game = False
    $ shovel_sylios = False
    
    
init 2:
    $ change_cursor("1")

    


    
init python:
    complete_item_list = [
        Item("Bed Shirt", Item.Kind.SHIRT, image_idle="images/gui/clickitems/bedshirt_idle.png", image_hover="images/gui/clickitems/bedshirt_hover.png"),
        Item("Napkin", Item.Kind.NAPKIN, image_idle="images/gui/clickitems/napkin_idle.png", image_hover="images/gui/clickitems/napkin_hover.png"),
        Item("Abandoned Pants", Item.Kind.PANTS, image_idle="images/gui/clickitems/pants_idle.png", image_hover="images/gui/clickitems/pants_hover.png"),
        Item("Ex's Shoes", Item.Kind.SHOES, image_idle="images/gui/clickitems/shoessmall_idle.png", image_hover="images/gui/clickitems/shoessmall_hover.png"),
        Item("Kitchen Knife", Item.Kind.WEAPON, image_idle="images/gui/clickitems/knife_idle.png", image_hover="images/gui/clickitems/knife_hover.png"),
        Item("Meaty Man Monthly", Item.Kind.MAGAZINE, image_idle="images/gui/clickitems/dirtymag_idle.png", image_hover="images/gui/clickitems/dirtymag_hover.png"),
        Item("Rusty Trusty Shovel", Item.Kind.TOOL, image_idle="images/gui/clickitems/shovel_idle.png", image_hover="images/gui/clickitems/shovel_hover.png"),
        Item("Weedy Grower", Item.Kind.PLANT, image_idle="images/gui/clickitems/weedgrower_idle.png", image_hover="images/gui/clickitems/weedgrower_hover.png"),
        Item("Decomposing Arm", Item.Kind.BODYPART, image_idle="images/gui/clickitems/arm_idle.png", image_hover="images/gui/clickitems/arm_hover.png"),
        Item("Dictionary", Item.Kind.BOOK, image_idle="images/gui/clickitems/dictionary_idle.png", image_hover="images/gui/clickitems/dictionary_hover.png"),
        Item("Fancy Shirt", Item.Kind.FANCYSHIRT, image_idle="images/gui/clickitems/fancyshirt_idle.png", image_hover="images/gui/clickitems/fancyshirt_hover.png"),
        Item("Dr. Oink", Item.Kind.PIG, image_idle="images/gui/clickitems/droink_idle.png", image_hover="images/gui/clickitems/droink_hover.png"),
        ]

# The game starts here.
label start:
    $ cookbook = list()
    python:
        ###I have to define the player here since now we have equip-able stuff
        player = Player("Dr. Frank", 100, 50)
        ###I'm defining all of my possible inventory items here!###
        
        
        bedshirt = complete_item_list[0]
        napkin = complete_item_list[1]
        pants = complete_item_list[2]
        exshoes = complete_item_list[3]
        knife = complete_item_list[4]
        dirtymag = complete_item_list[5]
        shovel = complete_item_list[6]
        weedgrower = complete_item_list[7]
        decomparm = complete_item_list[8]
        dictionary = complete_item_list[9]
        fancyshirt = complete_item_list[10]
        droink = complete_item_list[11]
#        decomparm = Item("Decomposing Arm", Item.Kind.BODYPART, image_idle="images/gui/arm_idle.png", image_hover="images/gui/arm_hover.png")
#        dictionary = Item("Dictionary", Item.Kind.BOOK)
#        fancyshirt = Item("Fancy Shirt", Item.Kind.FANCYSHIRT, image_idle="images/gui/fancyshirt_idle.png", image_hover="images/gui/fancyshirt_hover.png", recipe=[[bedshirt,1],[decomparm,1]])
#        ###This says that the inventory at the beginning of my game is empty###
        inventory = Inventory()
        ###Here i am adding a bedshirt to my initial inventory###
        #inventory.add(bedshirt)
    window auto
    
#################### OLD DEMO SHIT ###############################
#    $ Fr_exp = "neutral1"
#    dr "You've created a new Ren'Py game."
#    scene black with dissolve
#    #show screen inventory_button
#    show iggstest
#    $ Fr_exp = "neutral2"
#    dr "Once you add a story, pictures, and music, you can release it to the world!"
#    $inventory.add(bedshirt)
#    dr "I gave u a shirt!"
#    $ Fr_exp = "neutral1"
#    hide iggstest
#    show iggstest2
#    ig "I can't believe you missed the deadline, Dr. Frank."
#    $ Fr_exp = "neutral2"
#    dr "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
#    $ Fr_exp = "neutral1"
#    dr "POOP POOP POOP POOP POOP POOP POOP POOP POOP POOP POOP POOP POOP POOP POOP POOP POOP POOP POOP POOP POOP POOP POOP POOP"
#    $ Fr_exp = "screamcryo"
#    dr "Poop"
#    dr "Now you have an arm!"
#    dr "Poopy"
#    dr "Combine shit."
#    dr "Pooooop"
###################### END OF OLD DEMO SHIT ###############################
    $ Fr_exp = "gone"
    $ you_are_here = "gone"
    $inventory.add(decomparm)
    call storybookscene from _call_storybookscene
    call firstscene from _call_firstscene
    call gravefirst from _call_gravefirst
    call monsterpenultimate from _call_monsterpenultimate
    call setup from _call_setup
    call dress_up_minigame from _call_dress_up_minigame
    call afterbuildingscreen from _call_afterbuildingscreen
    #call demo from _call_demo
    scene black with dissolve
    show monsterneutral
    $ renpy.pause()
    $ armstatus = False
    $ renpy.pause()
    call meetthebf
    call frankhouse
    

    return
