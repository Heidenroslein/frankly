#Maps to navigate

screen frankhouse():
    tag menu
    viewport:
        xysize (config.screen_width, config.screen_height)
        child_size (1694, 1610)
        xinitial 0
        yinitial 2013
        draggable True
        add "frankhousebase" zoom 0.8
        
        imagebutton auto "images/maps/frankarrow_%s.png" xpos 70 ypos 1050 action Return('street')
        
        imagebutton auto "images/maps/lab_%s.png" xpos 860 ypos 170 focus_mask True action Return('lab')
        imagebutton auto "images/maps/study_%s.png" xpos 500 ypos 1200 focus_mask True action Return('study')
        imagebutton auto "images/maps/bedroom_%s.png" xpos 800 ypos 1400 focus_mask True action Return('bedroom')
        imagebutton auto "images/maps/conservatory_%s.png" xpos 200 ypos 1250 focus_mask True action Return ('conservatory')
        imagebutton auto "images/maps/foyer_%s.png" xpos 150 ypos 170 focus_mask True action Return ('entryway')
        imagebutton auto "images/maps/diningroom_%s.png" xpos 900 ypos 500 focus_mask True action Return ('dining')
        imagebutton auto "images/maps/kitchen_%s.png" xpos 400 ypos 100 focus_mask True action Return ('kitchen')
screen labstatic():
    add "images/maps/Secretlab/labbase.png"
    add "images/maps/Secretlab/poster_idle.png"
    add "images/maps/Secretlab/machinebed_idle.png"
    add "images/maps/Secretlab/bookshelf_idle.png"
    add "images/maps/Secretlab/iggs_idle.png"
    add "images/maps/Secretlab/magazines_idle.png"
    add "images/maps/Secretlab/webs.png"
    add "images/maps/secretlab/arrow_idle.png"
    
    
screen lab():
    tag menu
    use labstatic
    
    imagebutton auto "images/maps/secretlab/poster_%s.png" focus_mask True at clickables action Return ('labposter')
    imagebutton auto "images/maps/secretlab/iggs_%s.png" focus_mask True at clickables action Return ('talkiggsmonster') 
    imagebutton auto "images/maps/secretlab/machinebed_%s.png" focus_mask True at clickables action Return ('labbed')
    imagebutton auto "images/maps/secretlab/bookshelf_%s.png" focus_mask True at clickables action Return ('labbookshelf')
    imagebutton auto "images/maps/secretlab/magazines_%s.png" focus_mask True at clickables action Return ('labmagazines')
    imagebutton auto "images/maps/secretlab/arrow_%s.png" focus_mask True at clickables action Return ('frankhouse')
    add "images/maps/secretlab/webs.png"
    use inventory_button

screen bedroomstatic():
    add "images/maps/bedroom/bedroombase.png"
    add "images/maps/bedroom/bedroomposter_idle.png"
    add "images/maps/bedroom/drapesclose_idle.png"
    add "images/maps/bedroom/closet_idle.png"
    add "images/maps/bedroom/clothes_idle.png"
    add "images/maps/bedroom/icecream_idle.png"
    add "images/maps/bedroom/arrow_idle.png"
    add "images/maps/bedroom/bed_idle.png"
    add "images/maps/bedroom/mags_idle.png"
    add "images/maps/bedroom/droink_idle.png"
    
screen bedroom():
    tag menu
    use bedroomstatic
    imagebutton auto "images/maps/bedroom/arrow_%s.png" focus_mask True at clickables action Return('frankhouse')
    imagebutton auto "images/maps/bedroom/bedroomposter_%s.png" focus_mask True at clickables action Return('bedroomposter')
    imagebutton auto "images/maps/bedroom/drapesclose_%s.png" focus_mask True at clickables action Return('bedroomdrapes')
    imagebutton auto "images/maps/bedroom/closet_%s.png" focus_mask True at clickables action Return('closetbedroom')
    imagebutton auto "images/maps/bedroom/icecream_%s.png" focus_mask True at clickables action Return('icecream')
    add "images/maps/bedroom/clothes_idle.png"
    imagebutton auto "images/maps/bedroom/clothes_%s.png" focus_mask True at clickables action Return('bedroomclothes')
    add "images/maps/bedroom/bed_idle.png"
    imagebutton auto "images/maps/bedroom/bed_%s.png" focus_mask True at clickables action Return('bedroombed')
    add "images/maps/bedroom/droink_idle.png"
    add "images/maps/bedroom/mags_idle.png"
    imagebutton auto "images/maps/bedroom/mags_%s.png" focus_mask True at clickables action Return('bedroommags')
    imagebutton auto "images/maps/bedroom/droink_%s.png" focus_mask True at clickables action Return('droink')
    use inventory_button2

screen graveyardstatic():
    add "images/maps/graveyard/gravebase.png"
    add "images/maps/graveyard/church_idle.png"
    if sylios_garden == True:
        add "images/maps/graveyard/sylios_idle.png"
    add "images/maps/graveyard/bushes_idle.png"
    add "images/maps/graveyard/graves_idle.png"
    add "images/maps/graveyard/arrow_idle.png"

screen town():
    tag menu
    add black

screen studystatic:
    add "images/maps/study/base.png"
    add "images/maps/study/globe_idle.png"
    add "images/maps/study/shelfbase.png"
    add "images/maps/study/deskbase.png"
    add "images/maps/study/arrow_idle.png"
    
screen study():
    tag menu
    add "images/maps/study/base.png"
    add "images/maps/study/carpet.png"
    add "images/maps/study/globe_idle.png"
    imagebutton auto "images/maps/study/globe_%s.png" focus_mask True at clickables action Return ('studyglobe')
    add "images/maps/study/deskbase.png"
    add "images/maps/study/donut_idle.png"
    imagebutton auto "images/maps/study/donut_%s.png" focus_mask True at clickables action Return ('donutstudy')
    add "images/maps/study/newspaper_idle.png"
    imagebutton auto "images/maps/study/newspaper_%s.png" focus_mask True at clickables action Return ('newspaperstudy')
    add "images/maps/study/deskitems.png"
    add "images/maps/study/jars_idle.png"
    imagebutton auto "images/maps/study/jars_%s.png" focus_mask True at clickables action Return ('jarsstudy')
    add "images/maps/study/shelfbase.png"
    if have_dictionary:
        add "images/maps/study/nodictionary_idle.png"
        imagebutton auto "images/maps/study/nodictionary_%s.png" focus_mask True at clickables action Return ('putdictionarydown')
    else:
        add "images/maps/study/dictionary_idle.png"
        imagebutton auto "images/maps/study/dictionary_%s.png" focus_mask True at clickables action Return ('dictionarystudy')
    add "images/maps/study/plushes_idle.png"
    imagebutton auto "images/maps/study/plushes_%s.png" focus_mask True at clickables action Return ('plushesstudy')
    add "images/maps/study/button_idle.png"
    imagebutton auto "images/maps/study/button_%s.png" focus_mask True at clickables action Return ('buttonstudy')
    add "images/maps/study/sign_idle.png"
    imagebutton auto "images/maps/study/sign_%s.png" focus_mask True at clickables action Return ('signstudy')
    add "images/maps/study/wallcubbord_idle.png"
    imagebutton auto "images/maps/study/wallcubbord_%s.png" focus_mask True at clickables action Return ('wallcubbordstudy')
    add "images/maps/study/arrow_idle.png"
    use inventory_button
    
    imagebutton auto "images/maps/study/arrow_%s.png" focus_mask True at clickables action Return ('frankhouse')


screen conservatory():
    tag menu
    add "images/maps/conservatory/base.png"
    add "images/maps/conservatory/porch_idle.png"
    add "images/maps/conservatory/windows_idle.png"
    imagebutton auto "images/maps/conservatory/windows_%s.png" focus_mask True at clickables action Return ('windowconserve')
    imagebutton auto "images/maps/conservatory/porch_%s.png" focus_mask True at clickables action Return ('porchconserve')
    add "images/maps/conservatory/potrose_idle.png"
    imagebutton auto "images/maps/conservatory/potrose_%s.png" focus_mask True at clickables action Return ('potroseconserve')
    add "images/maps/conservatory/pots_idle.png"
    imagebutton auto "images/maps/conservatory/pots_%s.png" focus_mask True at clickables action Return ('potconserve')
    if have_grower:
        add "images/maps/conservatory/havegrowall_idle.png"
        imagebutton auto "images/maps/conservatory/havegrowall_%s.png" focus_mask True at clickables action Return ('havegrowallconserve')
        add "growersparkles1"
        add "growersparkles2"
    else:
        add "images/maps/conservatory/growall_idle.png"
        imagebutton auto "images/maps/conservatory/growall_%s.png" focus_mask True at clickables action Return ('growallconserve')
    if have_shovel: 
        add "images/gone.png"
    else:
        add "images/maps/conservatory/shovel_idle.png"
        imagebutton auto "images/maps/conservatory/shovel_%s.png" focus_mask True at clickables action Return ('shovelconserve')
    if use_mag:
        add "images/maps/conservatory/susiemag_idle.png"
        imagebutton auto "images/maps/conservatory/susiemag_%s.png" focus_mask True at clickables action Return ('susiemagconserve')
    else:
        add "images/maps/conservatory/susie_idle.png"
        imagebutton auto "images/maps/conservatory/susie_%s.png" focus_mask True at clickables action Return ('susieconserve')
    add "images/maps/conservatory/plants_idle.png"
    imagebutton auto "images/maps/conservatory/plants_%s.png" focus_mask True at clickables action Return ('plantsconserve')
    add "images/maps/conservatory/arrow_idle.png"
    imagebutton auto "images/maps/conservatory/arrow_%s.png" focus_mask True at clickables action Return ('frankhouse')
    use inventory_button2
    
screen kitchen():
    tag menu
    add "images/maps/kitchen/base.png"
    add "images/maps/kitchen/backcounter.png"
    add "images/maps/kitchen/window_idle.png"
    imagebutton auto "images/maps/kitchen/window_%s.png" focus_mask True at clickables action Return ('windowkitchen') 
    add "images/maps/kitchen/flower_idle.png"
    imagebutton auto "images/maps/kitchen/flower_%s.png" focus_mask True at clickables action Return ('flowerkitchen')
    add "images/maps/kitchen/fridge_idle.png"
    imagebutton auto "images/maps/kitchen/fridge_%s.png" focus_mask True at clickables action Return ('fridgekitchen')
    add "images/maps/kitchen/sink.png"
    add "images/maps/kitchen/dishes_idle.png"
    imagebutton auto "images/maps/kitchen/dishes_%s.png" focus_mask True at clickables action Return ('disheskitchen')
    add "images/maps/kitchen/forwardcounter.png"
    add "images/maps/kitchen/takeout_idle.png"
    imagebutton auto "images/maps/kitchen/takeout_%s.png" focus_mask True at clickables action Return ('takeoutkitchen')
    add "images/maps/kitchen/coffee_idle.png"
    imagebutton auto "images/maps/kitchen/coffee_%s.png" focus_mask True at clickables action Return ('coffeekitchen')
    add "images/maps/kitchen/roach_idle.png"
    imagebutton auto "images/maps/kitchen/roach_%s.png" focus_mask True at clickables action Return ('roachkitchen')
    add "images/maps/kitchen/frontcounter.png"
    add "images/maps/kitchen/frontjar_idle.png"
    if have_knife:
        add "images/gone.png"
    else:
        add "images/maps/kitchen/knifeshadow.png"
        add "images/maps/kitchen/knife_idle.png"
        imagebutton auto "images/maps/kitchen/knife_%s.png" focus_mask True at clickables action Return ('knifekitchen')
    add "images/maps/kitchen/arrow_idle.png"
    imagebutton auto "images/maps/kitchen/arrow_%s.png" focus_mask True at clickables action Return ('frankhouse')
    use inventory_button2

screen dining():
    tag menu
    add "images/maps/dining/base.png"
    add "images/maps/dining/table_idle.png"
    add "images/maps/dining/cabnet_idle.png"
    imagebutton auto "images/maps/dining/cabnet_%s.png" focus_mask True at clickables action Return ('cabnetdining')
    add "images/maps/dining/table_idle.png"
    imagebutton auto "images/maps/dining/table_%s.png" focus_mask True at clickables action Return ('tabledining')
    add "images/maps/dining/chairs_idle.png"
    imagebutton auto "images/maps/dining/chairs_%s.png" focus_mask True at clickables action Return ('chairsdining')
    add "images/maps/dining/lamp_idle.png"
    imagebutton auto "images/maps/dining/lamp_%s.png" focus_mask True at clickables action Return ('lampdining')
    add "images/maps/dining/napkin_idle.png"
    imagebutton auto "images/maps/dining/napkin_%s.png" focus_mask True at clickables action Return ('napkindining')
    add "images/maps/dining/arrow_idle.png"
    imagebutton auto "images/maps/dining/arrow_%s.png" focus_mask True at clickables action Return ('frankhouse')
    use inventory_button2

screen entryway():
    tag menu
    add "images/maps/entryway/base.png"
    add "images/maps/entryway/carpet_idle.png"
    imagebutton auto "images/maps/entryway/carpet_%s.png" focus_mask True at clickables action Return ('carpetentryway')
    add "images/maps/entryway/door_idle.png"
    imagebutton auto "images/maps/entryway/door_%s.png" focus_mask True at clickables action Return ('doorentryway')
    add "images/maps/entryway/cabnetsmall.png"
    if opened_shoeentryway:
        add "images/maps/entryway/opencabnet_idle.png"
        imagebutton auto "images/maps/entryway/opencabnet_%s.png" focus_mask True at clickables action Return ('openedcabnetentryway')
        if have_shoes:
            add "images/gone.png"
        else:
            add "images/maps/entryway/dominikshoes.png"
    else:
        add "images/maps/entryway/lockedcabnet_idle.png"
        imagebutton auto "images/maps/entryway/lockedcabnet_%s.png" focus_mask True at clickables action Return ('lockedcabnetentryway')
    add "images/maps/entryway/shoes_idle.png"
    imagebutton auto "images/maps/entryway/shoes_%s.png" focus_mask True at clickables action Return ('shoesentryway')
    add "images/maps/entryway/chair_idle.png"
    imagebutton auto "images/maps/entryway/chair_%s.png" focus_mask True at clickables action Return ('chairentryway')
    add "images/maps/entryway/arrow_idle.png"
    imagebutton auto "images/maps/entryway/arrow_%s.png" focus_mask True at clickables action Return ('frankhouse')
    use inventory_button

screen church():
    tag menu
    add "images/maps/church/base.png"
    if have_pants:
        add "images/maps/church/donation_idle.png"
        imagebutton auto "images/maps/church/donation_%s.png" focus_mask True at clickables action Return ('donationpants')
    else:
        add "images/maps/church/donationpants_idle.png"
        imagebutton auto "images/maps/church/donationpants_%s.png" focus_mask True at clickables action Return ('donationpantschurch')
    add "images/maps/church/books_idle.png"
    add "images/maps/church/stainglass_idle.png"
    imagebutton auto "images/maps/church/stainglass_%s.png" focus_mask True at clickables action Return ('stainglasschurch')
    add "images/maps/church/altar_idle.png"
    imagebutton auto "images/maps/church/altar_%s.png" focus_mask True at clickables action Return ('altarchurch')
    imagebutton auto "images/maps/church/books_%s.png" focus_mask True at clickables action Return ('bookschurch')
    add "images/maps/church/chairs_idle.png"
    imagebutton auto "images/maps/church/chairs_%s.png" focus_mask True at clickables action Return ('chairschurch')
    if use_grower:
        add "images/maps/church/flowersaltarweeds_idle.png"
        imagebutton auto "images/maps/church/flowersaltarweeds_%s.png" focus_mask True at clickables action Return ('flowersaltarweeds')
    else:
        add "images/maps/church/flowersaltar_idle.png"
        imagebutton auto "images/maps/church/flowersaltar_%s.png" focus_mask True at clickables action Return ('flowersaltartchurch')
    add "images/maps/church/arrow_idle.png"
    imagebutton auto "images/maps/church/arrow_%s.png" focus_mask True at clickables action Return ('street')
    use inventory_button2

screen graveyard():
    tag menu
    use graveyardstatic
    imagebutton auto "images/maps/graveyard/church_%s.png" focus_mask True at clickables action Return ('outsidechurch')
    add "images/maps/graveyard/woodfence.png"
    add "images/maps/graveyard/bushes_idle.png"
    imagebutton auto "images/maps/graveyard/bushes_%s.png" focus_mask True at clickables action Return ('bushes')
    if sylios_garden == True:
        add "images/maps/graveyard/sylios_idle.png"
    if sylios_garden == True:
        imagebutton auto "images/maps/graveyard/sylios_%s.png" focus_mask True at clickables action Return ('talksylios')
    add "images/maps/graveyard/graves_idle.png"
    imagebutton auto "images/maps/graveyard/graves_%s.png" focus_mask True at clickables action Return ('graves')
    imagebutton auto "images/maps/graveyard/arrow_%s.png" focus_mask True at clickables action Return ('street')
    add "images/maps/graveyard/overgrass.png"
    use inventory_button2
    
screen street():
    tag menu
    add "images/maps/streetbase.png"
    
    imagebutton auto "images/maps/streethousearrow_%s.png" xpos 200 ypos 320 focus_mask True action Return('frankhouse')
    
    imagebutton auto "images/maps/streettownarrow_%s.png" xpos 1050 ypos 450 focus_mask True action Return('graveyard')
    imagebutton auto "images/maps/streettownarrow_%s.png" xpos 800 ypos 200 focus_mask True action Return ('church')

###### LABELS FOR THE MAPS #################

label frankhouse:
    window hide None
    call screen frankhouse
    
    if _return == "street":
        jump street
        
    if _return == "lab":
        jump lab
    if _return == "bedroom":
        jump bedroom 
    if _return == "study":
        jump study
    if _return == "conservatory":
        jump conservatory
    if _return == "entryway":
        jump entryway
    if _return == "dining":
        jump dining
    if _return == "kitchen":
        jump kitchen
        
        
label street:
    window hide None
    call screen street
    if _return == "frankhouse":
        jump frankhouse
    if _return == "town" and monsterwith == True:
        jump street
    if _return == "town" and monsterwith == False:
        show streetno
        "What am I thinking?"
        "I can't go just yet!"
        jump street
    if _return == "graveyard":
        jump graveyard
    if _return == "church":
        jump church
        
####### LAB #### RETURNS AND DESCRIPTIONS ###########

label lab:
    window hide None
    call screen lab
    if _return == "frankhouse":
        jump frankhouse
    if _return == "talkiggsmonster":
        jump talkiggsmonster
    if _return == "labbookshelf":
        jump labbookshelf
    if _return == "labmagazines":
        jump labmagazines
    if _return == "labbed":
        jump labbed
    if _return == "labposter":
        jump labposter

label labbookshelf:
    scene labstatic
    "It's filled with old magic books I was able to smuggle in from neighboring countries."
    "Gienel’s unique stance on magic has certainly made it hard to do any sort of research on magic fields."
    "It was the best I could do to get my hands on intact reanimation research."
    dr "What I would have given for some necromancy texts..."
    dr "Hah! Like there's any that haven't been destroyed by now."
    if sylios_books:
        dr "..."
        dr "So strange that he has some..."
    jump lab
    return
        
label talkiggsmonster:
    scene labstatic
    scene black with moveinoutdissolveright
    "Hi! You're talking to Iggs and the Monster right now!"
    scene labstatic with moveinoutdissolveleft
    jump lab
    return
    
label labmagazines:
    scene labstatic
    "Reference pictures for my boyfriend! <3"
    if Susie_hint:
        if Meaty_Man_Inventory:
            "I already have a periodical of this nature."
            if Iggs_magazine:
                "Iggs would kill me if I picked up another one."
            else:
                "I don't need it."
        else:
            dr "Oh."
            dr "I wonder if this would be a periodical that Susie would find interesting."
            "I reach forward to pocket a dubious magazine when Iggs sees me."
            ig "Um, Dr. Frank? What are you doing?"
            dr "I'm picking up some reading material, that's all."
            ig "We're on a mission here. Can't you do your... alone {i}reading{/i} time later?"
            dr "Hey, wait a minute! This isn't for me! It's for Susie!"
            ig "So Susie was the one who bought all of those magazines then. Even the ones in your bedroom."
            dr "NGGGHH."
            dr "NGGGHH. {fast} You're right Iggs. We don't have time for this. We're on a mission, right?"
            dr "And I need this to advance said mission."
            "I purposefully pocket the magazine, making sure Iggs can see me do it."
            "He only sighs."
            $ Iggs_magazine = True
            $ Meaty_Man_Inventory = True
    jump lab
    return
    
label labbed:
    scene labstatic
    "The dissecting table, in a way it's also my boyfriend's crib."
    "...That doesn't sound weird, does it?"
    jump lab
    return
    
label labposter:
    scene labstatic
    "Truly the epitome of my life's work."
    jump lab
    return
    
##### BEDROOM ####  RETURNS AND DESCRIPTIONS ####

label bedroom:
    window hide None
    call screen bedroom
    if _return == "frankhouse":
        jump frankhouse
    if _return == "bedroommags":
        jump bedroommags
    if _return == "bedroomposter":
        jump bedroomposter
    if _return == "icecream":
        jump icecream
    if _return == "droink":
        jump droink
    if _return == "bedroombed":
        jump bedroombed
    if _return == "closetbedroom":
        jump closetbedroom
    if _return == "bedroomclothes":
        jump bedroomclothes
    if _return == "bedroomdrapes":
        jump bedroomdrapes
        
label bedroommags:
    scene bedroomstatic
    "\"Meaty Man Monthly.\" Strictly for research purposes."
    dr "..."
    "I pick it up and add it to my inventory."
    "...just in case."
    jump bedroom
    return
    
label bedroomposter:
    scene bedroomstatic
    #TODO descrip
    "Bedroomposter"
    jump bedroom
    return

label icecream:
    scene bedroomstatic
    "Half-finished bubblegum ice cream tubs are scattered across the floor."
    "Look, I was sad, okay?!"
    jump bedroom
    return

label droink:
    scene bedroomstatic
    if Dr_Oink_Count == 0:
        "It's my oldest friend, Dr. Oink. {w} Dominik didn't find her very cute."
        "In hindsight, maybe it was never meant to be."
        $ Dr_Oink_Count += 1
        jump bedroom
    elif Dr_Oink_Count == 1:
        "Hey wait, are you making fun of me?"
        "So what if I’m a grown man still sleeping with a stuffed animal!"
        $ Dr_Oink_Count += 1
        jump bedroom
    elif Dr_Oink_Count == 2:
        "Don't tell anyone, but Dr. Oink isn't even a doctor."
        $ Dr_Oink_Count = 0
        jump bedroom
        
    return
label bedroombed:
    scene bedroomstatic
    "Bed"
    jump bedroom
    return
label closetbedroom:
    scene bedroomstatic
    "I don’t wanna open these.{w} The skeletons I have stored in here are going to fall out."
    "Packing was never my strong suit."
    jump bedroom
    return
label bedroomclothes:
    scene bedroomstatic
    if bedroomclothesvisit == 0:
        "A messy assortment of worn clothes. I still have a while until laundry day."
        if have_shirt == False:
            dr "The only thing that would fit my monster would be..."
            "I pick up my old night shirt."
            dr "Perfect, this'll fit!"
            $ have_shirt = True
            if have_shoes or have_pants == False:
                dr "But I'm still missing some clothing articles..."
                if have_pants == False:
                    dr "None of these pants will fit him."
                    if dick == "Big":
                        dr "Not with those additional enhancements I gave him."
            $ bedroomclothesvisit += 1
            jump bedroom
    elif bedroomclothesvisit == 1:
        "Laundry day is when you shift the pile of clothes a few inches in one direction, right?"
        jump bedroom
    return
label bedroomdrapes:
    scene bedroomstatic
    "*HISS* DAYLIGHT."
    jump bedroom
    return
    
##### STUDY  ##### LABELS AND DESCRIPTIONS ###
label study:
    window hide None
    call screen study
    if _return == "frankhouse":
        jump frankhouse
    if _return == "studyglobe":
        jump studyglobe
    if _return == "donutstudy":
        jump donutstudy
    if _return == "buttonstudy":
        jump buttonstudy
    if _return == "dictionarystudy":
        jump dictionarystudy
    if _return == "putdictionarydown":
        jump putdictionarydown
    if _return == "newspaperstudy":
        jump newspaperstudy
    if _return == "jarsstudy":
        jump jarsstudy
    if _return == "plushesstudy":
        jump plushesstudy
    if _return == "wallcubbordstudy":
        jump wallcubbordstudy
    if _return == "signstudy":
        jump signstudy
        
label studyglobe:
    scene studystatic
    "Something."
    jump study
    return
    
label donutstudy:
    scene studystatic
    "donuts"
    jump study
    return
    
label buttonstudy:
    scene studystatic
    "buttons"
    jump study
    return
label dictionarystudy:
    scene studystatic
    "dictionarryy"
    $ have_dictionary = True
    jump study
    return
label putdictionarydown:
    scene studystatic
    "U put the dictionary down"
    $ have_dictionary = False
    jump study
    return
label newspaperstudy:
    scene studystatic
    "Your looking at da newspaper"
    jump study
    return
label jarsstudy:
    scene studystatic
    "Its a shit ton of gross shit."
    jump study
    return
label plushesstudy:
    scene studystatic
    "THEY'RE LIMITED EDITION OKAY???"
    jump study
    return
label wallcubbordstudy:
    scene studystatic
    "herpherp"
    jump study
    return
label signstudy:
    scene studystatic
    "DONT ENTER"
    jump study
    return
    
##### CONSERVATORY ##### LABELS AND DESCRIPTIONS ###
label conservatory:
    window hide None
    call screen conservatory
    if _return == "porchconserve":
        jump porchconserve
    if _return == "frankhouse":
        jump frankhouse
    if _return == "plantsconserve":
        jump plantsconserve
    if _return == "windowconserve":
        jump windowconserve
    if _return == "potconserve":
        jump potconserve
    if _return == "shovelconserve":
        jump shovelconserve
    if _return == "susiemagconserve":
        jump susiemagconserve
    if _return == "susieconserve":
        jump susieconserve
    if _return == "havegrowallconserve":
        jump havegrowallconserve
    if _return == "growallconserve":
        jump growallconserve

label porchconserve:
    "BLARGH"
    jump conservatory
    return

label plantsconserve:
    "Plants or something"
    jump conservatory
    return
label windowconserve:
    "Look out da window"
    jump conservatory
    return
label potconserve:
    "They broken"
    jump conservatory
    return
label shovelconserve:
    "ITs a shovel dovel"
    "I cant reach it behind Susie wihtout being eaten."
    "Reach anyway?"
    menu:
        "Yes":
            if use_mag == False:
                "YOU DIE."
                jump conservatory
            else:
                "Congrats, you picked it up!"
                $ have_shovel = True
                jump conservatory
        "No.":
            "Okay good, cause that shit is dangerous!"
            jump conservatory
    return
label susiemagconserve:
    "Don't want to disturb him..."
    jump conservatory
    return
label susieconserve:
    "Dangerous!"
    jump conservatory
    return
label havegrowallconserve:
    "Put the growall down?"
    menu:
        "Yes, please.":
            $ have_grower = False
            "U put it down."
            jump conservatory
        "No, I love dying.":
            "You embrace death."
            jump conservatory
    return
label growallconserve:
    "U dont have any of this rn."
    "Pick it up?"
    menu:
        "Yes plz.":
            "Congrats, ur gonna die."
            $ have_grower = True
            jump conservatory
        "No, thank you.":
            "ur a smart man."
            jump conservatory
    jump conservatory
    return
    
##### ENTRYWAY ##### LABELS AND DESCRIPTIONS ###
label entryway:
    window hide None
    call screen entryway
    if _return == "shoesentryway":
        jump shoesentryway
    if _return == "carpetentryway":
        jump carpetentryway
    if _return == "chairentryway":
        jump chairentryway
    if _return == "doorentryway":
        jump doorentryway
    if _return == "openedcabnetentryway":
        jump openedcabnetentryway
    if _return == "lockedcabnetentryway":
        jump lockedcabnetentryway
    if _return == "frankhouse":
        jump frankhouse

label shoesentryway:
    scene black
    "Something."
    jump entryway

label carpetentryway:
    scene black
    "carpetentryway"
    jump entryway
    
label chairentryway:
    scene black
    "chairentryway"
    jump entryway

label doorentryway:
    scene black
    "doorentryway"
    jump entryway
label openedcabnetentryway:
    scene black
    "openedcabnetentryway"
    $ have_shoes = True
    jump entryway
label lockedcabnetentryway:
    scene black
    "lockedcabnetentryway"
    if have_knife:
        "Hey! I can open this!"
        $ opened_shoeentryway = True
    else: 
        "Too bad I don't have anything to open this!"
    jump entryway
##### DINING ROOM ##### LABELS AND DESCRIPTIONS ###
label dining:
    window hide None
    call screen dining
    if _return == "frankhouse":
        jump frankhouse
    if _return == "tabledining":
        jump tabledining
    if _return == "chairsdining":
        jump chairsdining
    if _return == "cabnetdining":
        jump cabnetdining
    if _return == "lampdining":
        jump lampdining
    if _return == "napkindining":
        jump napkindining
        
label tabledining:
    scene black
    "tabledining"
    jump dining
    return
        
label chairsdining:
    scene black
    "chairsdining"
    jump dining
    return
    
label cabnetdining:
    scene black
    "cabnetdining"
    jump dining
    return
label lampdining:
    scene black
    "lampdining"
    jump dining
    return
label napkindining:
    scene black
    "napkindining"
    jump dining
    return

##### KITCHEN ##### LABELS AND DESCRIPTIONS ###
label kitchen:
    window hide None
    call screen kitchen
    if _return == "fridgekitchen":
        jump fridgekitchen
    if _return == "takeoutkitchen":
        jump takeoutkitchen
    if _return == "coffeekitchen":
        jump coffeekitchen
    if _return == "disheskitchen":
        jump disheskitchen
    if _return == "windowkitchen":
        jump windowkitchen
    if _return == "roachkitchen":
        jump roachkitchen
    if _return == "flowerkitchen":
        jump flowerkitchen
    if _return == "knifekitchen":
        jump knifekitchen
    if _return == "frankhouse":
        jump frankhouse
    
        
        
label fridgekitchen:
    scene black
    "fridgekitchen"
    jump kitchen
label takeoutkitchen:
    scene black
    "takeoutkitchen"
    jump kitchen
label coffeekitchen:
    scene black
    "coffeekitchen"
    jump kitchen
label disheskitchen:
    scene black
    "disheskitchen"
    jump kitchen
label windowkitchen:
    scene black
    "windowkitchen"
    jump kitchen
label roachkitchen:
    scene black
    "roachkitchen"
    jump kitchen
label flowerkitchen:
    scene black
    "flowerkitchen"
    jump kitchen
label knifekitchen:
    scene black
    "Pick up da knife~!"
    $ have_knife = True
    jump kitchen
    
##### CHURCH ##### LABELS AND DESCRIPTIONS ###
label church:
    window hide None
    call screen church
    if _return == "donationpantschurch":
        jump donationpantschurch
    if _return == "donationpants":
        jump donationpants
    if _return == "street":
        jump street
    if _return == "bookschurch":
        jump bookschurch
    if _return == "chairschurch":
        jump chairschurch
    if _return == "flowersaltarweeds":
        jump flowersaltarweeds
    if _return == "flowersaltartchurch":
        jump flowersaltartchurch
    if _return == "stainglasschurch":
        jump stainglasschurch
    if _return == "altarchurch":
        jump altarchurch
    if _return == "street":
        jump street
        
label donationpantschurch:
    scene black
    "PANTS"
    $ have_pants = True
    jump church
    return
label donationpants:
    scene black
    "u already have pants."
    jump church
    return
label bookschurch:
    scene black
    "bookschurch"
    jump church
    return
label chairschurch:
    scene black
    "chairschurch"
    jump church
    return
label flowersaltarweeds:
    scene black
    "flowersaltarweeds"
    jump church
    return
label flowersaltartchurch:
    scene black
    "flowersaltartchurch"
    if have_grower == True:
        $ use_grower = True
        "You used the grower!"
    jump church
    return
label altarchurch:
    scene black
    "altarchurch"
    jump church
    return
label stainglasschurch:
    scene black
    "stain glass"
    jump church
    return
##### GRAVEYARD  ##### LABELS AND DESCRIPTIONS ###

label graveyard:
    window hide None
    call screen graveyard
    if _return == "talksylios":
        jump talksylios
    if _return == "graves":
        jump graves
    if _return == "bushes":
        jump bushes
    if _return == "outsidechurch":
        jump outsidechurch
    if _return == "street":
        jump street
        
label talksylios:
    scene black
    "UR TALKING TO SYLIOS"
    jump graveyard
    return

label graves:
    scene graveyardstatic
    "GRAVES HUURRR"
    jump graveyard
    return

label bushes:
    scene graveyardstatic
    "BUSHES HURRR"
    $ sylios_garden = True
    jump graveyard
    return

label outsidechurch:
    scene graveyardstatic
    "It's the outside of the church."
    jump graveyard
    return
    
label town:
    window hide None
    call screen town

