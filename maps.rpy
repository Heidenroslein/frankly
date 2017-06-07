#Maps to navigate 

screen frankhouse():
    tag menu
    add "images/maps/house/base.png"
        
    add "cloud1"
    add "cloud2"
    add "cloud3"
    add "images/maps/house/foreground.png"
    add "images/maps/house/wheel.png" xpos 945 ypos 30 at rotation
      
    imagebutton idle "franksignidle" hover "franksignhover" focus_mask True action Return('street')  
    imagebutton auto "images/maps/house/lab_%s.png" focus_mask True action Return('lab')
    imagebutton auto "images/maps/house/study_%s.png" focus_mask True action Return('study')
    imagebutton auto "images/maps/house/bedroom_%s.png" focus_mask True action Return('bedroom')
    imagebutton auto "images/maps/house/conservatory_%s.png" focus_mask True action Return ('conservatory')
    imagebutton auto "images/maps/house/hallway_%s.png" focus_mask True action Return ('entryway')
    imagebutton auto "images/maps/house/dining_%s.png" focus_mask True action Return ('dining')
    imagebutton auto "images/maps/house/kitchen_%s.png" focus_mask True action Return ('kitchen')
    add "images/maps/house/overlay.png"
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
    if inventory_look == "show":
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
    add "images/maps/bedroom/bedroombase.png"
    add "images/maps/bedroom/arrow_idle.png"
    imagebutton auto "images/maps/bedroom/arrow_%s.png" focus_mask True at clickables action Return('frankhouse')
    add "images/maps/bedroom/bedroomposter_idle.png"
    imagebutton auto "images/maps/bedroom/bedroomposter_%s.png" focus_mask True at clickables action Return('bedroomposter')
    add "images/maps/bedroom/drapesclose_idle.png"
    imagebutton auto "images/maps/bedroom/drapesclose_%s.png" focus_mask True at clickables action Return('bedroomdrapes')
    add "images/maps/bedroom/closet_idle.png"
    imagebutton auto "images/maps/bedroom/closet_%s.png" focus_mask True at clickables action Return('closetbedroom')
    add "images/maps/bedroom/icecream_idle.png"
    imagebutton auto "images/maps/bedroom/icecream_%s.png" focus_mask True at clickables action Return('icecream')
    add "images/maps/bedroom/clothes_idle.png"
    imagebutton auto "images/maps/bedroom/clothes_%s.png" focus_mask True at clickables action Return('bedroomclothes')
    add "images/maps/bedroom/bed_idle.png"
    imagebutton auto "images/maps/bedroom/bed_%s.png" focus_mask True at clickables action Return('bedroombed')
    if Iggs_magazine:
        add "images/maps/bedroom/mags_idle.png"
        imagebutton auto "images/maps/bedroom/mags_%s.png" focus_mask True at clickables action Return('bedroommags')
    if inventory.has_item(dirtymag):
        add "images/gone.png"
    else:
        if use_mag:
            add "images/gone.png"
        else:
            add "images/maps/bedroom/mags_idle.png"
            imagebutton auto "images/maps/bedroom/mags_%s.png" focus_mask True at clickables action Return('bedroommags')
    if inventory.has_item(droink):
        add "images/gone.png"
    else:
        add "images/maps/bedroom/droink_idle.png"
        imagebutton auto "images/maps/bedroom/droink_%s.png" focus_mask True at clickables action Return('droink')
    if inventory_look == "show":
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
    if have_dictionary or seen_necromancy:
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
    if inventory_look == "show":
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
    if inventory.has_item(shovel): 
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
    if inventory_look == "show":
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
    if inventory.has_item(knife):
        add "images/gone.png"
    else:
        add "images/maps/kitchen/knifeshadow.png"
        add "images/maps/kitchen/knife_idle.png"
        imagebutton auto "images/maps/kitchen/knife_%s.png" focus_mask True at clickables action Return ('knifekitchen')
    add "images/maps/kitchen/arrow_idle.png"
    imagebutton auto "images/maps/kitchen/arrow_%s.png" focus_mask True at clickables action Return ('frankhouse')
    if inventory_look == "show":
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
    if picked_up_napkin:
        add "images/gone.png"
    else:
        add "images/maps/dining/napkin_idle.png"
        imagebutton auto "images/maps/dining/napkin_%s.png" focus_mask True at clickables action Return ('napkindining')
    add "images/maps/dining/arrow_idle.png"
    imagebutton auto "images/maps/dining/arrow_%s.png" focus_mask True at clickables action Return ('frankhouse')
    if inventory_look == "show":
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
        if inventory.has_item(exshoes):
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
    if inventory_look == "show":
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
    if inventory_look == "show":
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
    if inventory_look == "show":
        use inventory_button
    
screen street():
    tag menu
    add "images/maps/overworld2/base.png"
    
    imagebutton auto "images/maps/overworld2/house_%s.png" focus_mask True action Return('frankhouse')
    
    imagebutton auto "images/maps/overworld2/graveyard_%s.png" focus_mask True action Return('graveyard')
    imagebutton auto "images/maps/overworld2/church_%s.png" focus_mask True action Return ('church')
    imagebutton auto "images/maps/overworld2/town_%s.png" focus_mask True action Return ('gototown')

###### LABELS FOR THE MAPS #################

label frankhouse:
    window hide None
    hide screen inventory_button2
    hide screen inventory_button
    scene frankhousestatic
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
    scene streetstatic
    call screen street
    if _return == "frankhouse":
        jump frankhouse
    if _return == "gototown":
        scene streetstatic
        "If you keep following this road, you'll end up in town."
        "But I can't go just yet."
        jump street
    if _return == "graveyard":
        jump graveyard
    if _return == "church":
        jump church
        
####### LAB #### RETURNS AND DESCRIPTIONS ###########

label lab:
    window hide None
    scene labstatic
    hide screen inventory_button2
    hide screen inventory_button
    if have_grower:
        scene labstaticsansiggs
        $ renpy.pause(0.1)
        $ Fr_exp = "closedsado"
        dr " A-CHOO!" with hpunch
        $ Fr_exp = "sidesado"
        dr "Ugh..."
        $ Fr_exp = "sado"
        dr "The ventilation in this room isn’t very good."
        $ Fr_exp = "gone"
        "Suddenly, I become aware of the foul odor the weed-grower in my pocket is putting off."
        $ Fr_exp = "screamcryo"
        dr "Achoo! Achoo!"
        $ Fr_exp = "crazedsurprisedcryo"
        dr "GAH-! I- I can't breathe!"
        $ Fr_exp = "gone"
        play sound "music/thud.wav"
        "I collapse to the ground, gasping for air." with vpunch
        play doublesound "music/whoosh.ogg"
        scene black with hpunch
        nvlbox "{size=+40}YOU DIED.{/size}"
        nvl clear
        "Try again?"
        menu:
            "Yes, please...":
                "Alrighty!"
                $ inventory.drop(weedgrower)
                $ have_grower = False
                jump conservatory
            "{size=-13}No, I'll stay dead, thank you.{/size}":
                "Well, alright."
                return
    if have_dictionary:
        scene labstaticsansiggs
        $ renpy.pause(0.1)
        "As soon as I step into the room, the floor beneath my feet shakes." with hpunch
        $ Fr_exp = "crazedsurprisedo"
        dr "H-huh?!"
        scene black with vpunch
        $ Fr_exp = "gone"
        "Suddenly, my feet break through and I fall."
        dr "AA-{size=-10}AA{/size}{size=-10}AA-{/size}{size=-15}AH-{/size}{size=-15}HH-{/size}{size=-15}HH-{/size}{size=-15}HH-{/size}{size=-15}HH!{/size}{size=-15}!!{/size}"
        "The dictionary is too heavy, I knew I should have put more effort into the upkeep of the mansion!"
        play doublesound "music/whoosh.ogg"
        scene black with hpunch
        nvlbox "{size=+40}YOU DIED.{/size}"
        nvl clear
        "Try again?"
        menu:
            "...Yes.":
                "Good luck."
                $ have_dictionary = False
                $ inventory.drop(dictionary)
                jump study
            "{size=-15}No, I think I'll stay here.{/size}":
                "Let me know if you find anything down there!"
                return
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
    if item_use == "True":
        if player.has_selected(knife):
            "These are rare research materials, I don't want to hurt them!"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump lab
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump lab
    else:
        "It's filled with old magic books I was able to smuggle in from neighboring countries."
        "Gienel’s unique stance on magic has certainly made it hard to do any sort of research on magic fields, it was the best I could do to get my hands on intact reanimation research."
        $ Fr_exp = "sado"
        dr "What I would have given for some necromancy texts..."
        $ Fr_exp = "thinkingo"
        dr "Hah! Like there's any that haven't been destroyed by now."
        $ Fr_exp = "gone"
        if seen_necromancy:
            $ Fr_exp = "gendou1"
            dr "..."
            $ Fr_exp = "sado"
            dr "So strange that he has some..."
            $ Fr_exp = "gone"
        jump lab
    return
        
label talkiggsmonster:
    scene labstatic
    jump labdialoguebranching
    #scene black with moveinoutdissolveright
    $ Susie_hint = True
    #scene labstatic with moveinoutdissolveleft
    jump lab
    return
    
label labmagazines:
    scene labstatic
    if item_use == "True":
        if player.has_selected(knife):
            "To previous researh materials?!"
            "Never!"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump lab
        if player.has_selected(napkin):
            "I wipe some of the books down, but nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump lab
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump lab
    else:
        "Reference pictures for my boyfriend! <3"
        if Susie_hint:
            if inventory.has_item(dirtymag):
                "I already have a periodical of this nature."
                if Iggs_magazine:
                    "Iggs would kill me if I picked up another one."
                else:
                    "I don't need it."
            else:
                $ Fr_exp = "surprisedo"
                dr "Oh."
                $ Fr_exp = "neutralhappyo"
                dr "I wonder if this would be a periodical that Susie would find interesting."
                $ Fr_exp = "gone"
                window show
                "I reach forward to pocket a dubious magazine when Iggs sees me."
                scene labstaticsansiggs with Dissolve(0.1)
                show iggsangrypeevedo at slidedissolvein
                ig "Um, Dr. Frank? What are you doing?"
                window auto
                show iggsangrypeeved
                hide iggsangrypeevedo
                $ Fr_exp = "thinkingo"
                dr "I'm picking up some reading material, that's all."
                $ Fr_exp = "thinking"
                show iggsplzo
                hide iggsangrypeeved
                ig "We're on a mission here. Can't you do your... alone {i}reading{/i} time later?"
                show iggsplzfrown
                hide iggsplzo
                $ Fr_exp = "angryyello"
                dr "Hey, wait a minute! This isn't for me! It's for Susie!"
                $ Fr_exp = "angryneutral"
                show iggsangrypeevedo at centerbob
                hide iggsplzfrown
                ig "So Susie was the one who bought all of those magazines then. Even the ones in your bedroom."
                show iggsangrypeeved
                hide iggsangrypeevedo
                $ Fr_exp = "closedangryo"
                dr "NGGGHH."
                $ Fr_exp = "angryneutralo"
                dr "You're right Iggs. We don't have time for this. We're on a mission, right?"
                $ Fr_exp = "neutralhappyo"
                dr "And I need this to advance said mission."
                $ Fr_exp = "cocky"
                play sound "music/additem.mp3"
                $inventory.add(dirtymag)
                show iggsangrypeeved at slidedissolveout
                "I purposefully pocket the magazine, making sure Iggs can see me do it."
                show iggsclosedsad at centerbobwithdissolvein
                $ Fr_exp = "gone"
                "He only sighs."
                show iggsclosedsad at slidedissolveout
                $ renpy.pause(0.2)
                $ Iggs_magazine = True
        jump lab
    return
    
label labbed:
    scene labstatic
    if item_use == "True":
        if player.has_selected(knife):
            "I stab the table!"
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump lab
        if player.has_selected(napkin):
            "I wipe a bit of the table down, but there's still some dubious red splotches."
            $ Fr_exp = "gendou1"
            dr "..."
            $ Fr_exp = "neutral1sideo"
            dr "...I'll get that later."
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump lab
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump lab
    else:
        "The dissecting table, in a way it's also my boyfriend's crib."
        "...That doesn't sound weird, does it?"
        jump lab
    return
    
label labposter:
    scene labstatic
    if item_use == "True":
        if player.has_selected(knife):
            "I stab the diagram, but it only makes the specimen sparkle harder."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump lab
        if player.has_selected(dirtymag):
            $ Fr_exp = "gendou2"
            dr "..."
            $ Fr_exp = "happyangryo"
            dr "Yes, I think I've cracked the code to beautiful men"
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump lab
    else:
        "Truly the epitome of my life's work."
        jump lab
    return
    
##### BEDROOM ####  RETURNS AND DESCRIPTIONS ####

label bedroom:
    window hide None
    scene bedroomstatic
    hide screen inventory_button2
    hide screen inventory_button
    if have_grower:
        scene bedroomstatic
        $ renpy.pause(0.1)
        $ Fr_exp = "closedsado"
        dr " A-CHOO!" with hpunch
        $ Fr_exp = "sidesado"
        dr "Ugh..."
        $ Fr_exp = "sado"
        dr "The ventilation in this room isn’t very good."
        $ Fr_exp = "gone"
        "Suddenly, I become aware of the foul odor the weed-grower in my pocket is putting off."
        $ Fr_exp = "screamcryo"
        dr "Achoo! Achoo!"
        $ Fr_exp = "crazedsurprisedcryo"
        dr "GAH-! I- I can't breathe!"
        $ Fr_exp = "gone"
        play sound "music/thud.wav"
        "I collapse to the ground, gasping for air." with vpunch
        play doublesound "music/whoosh.ogg"
        scene black with hpunch
        nvlbox "{size=+40}YOU DIED.{/size}"
        nvl clear
        "Try again?"
        menu:
            "Yes, please...":
                "Alrighty!"
                $ inventory.drop(weedgrower)
                $ have_grower = False
                jump conservatory
            "{size=-13}No, I'll stay dead, thank you.{/size}":
                "Well, alright."
                return
    if have_dictionary:
        scene bedroomstatic
        $ renpy.pause(0.1)
        "As soon as I step into the room, the floor beneath my feet shakes." with hpunch
        $ Fr_exp = "crazedsurprisedo"
        dr "H-huh?!"
        scene black with vpunch
        $ Fr_exp = "gone"
        "Suddenly, my feet break through and I fall."
        dr "AA-{size=-10}AA{/size}{size=-10}AA-{/size}{size=-15}AH-{/size}{size=-15}HH-{/size}{size=-15}HH-{/size}{size=-15}HH-{/size}{size=-15}HH!{/size}{size=-15}!!{/size}"
        "The dictionary is too heavy, I knew I should have put more effort into the upkeep of the mansion!"
        play doublesound "music/whoosh.ogg"
        scene black with hpunch
        nvlbox "{size=+40}YOU DIED.{/size}"
        nvl clear
        "Try again?"
        menu:
            "...Yes.":
                "Good luck."
                $ have_dictionary = False
                $ inventory.drop(dictionary)
                jump study
            "{size=-15}No, I think I'll stay here.{/size}":
                "Let me know if you find anything down there!"
                return
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
    if item_use == "True":
        if player.has_selected(knife):
            "I don't want to cut up my magazines of dubious nature!"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
        if player.has_selected(droink):
            "Perish the thought!"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
    else:
        "\"Meaty Man Monthly.\"{w} {i}Strictly{/i} for research purposes."
        if Iggs_magazine:
            "But I already have something like this in my inventory, I don't need another one."
            if use_mag:
                "Or at least, I did before I gave it to Susie. And I don't think I'll need another magazine for now."
            $ Fr_exp = "surprisedsideo"
            dr "I wouldn't want anyone getting the wrong idea about me, after all!"
            $ Fr_exp = "gone"
            jump bedroom
        else:
            $ Fr_exp = "gendou1"
            dr "..."
            $ Fr_exp = "gone"
            "I pick it up and add it to my inventory."
            play sound "music/additem.mp3"
            $inventory.add(dirtymag)
            "...just in case."
            jump bedroom
    return
    
label bedroomposter:
    scene bedroomstatic
    if item_use == "True":
        if player.has_selected(knife):
            "And cut up my beautiful face?"
            "Never!"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
        if player.has_selected(napkin):
            "I wipe the poster down a little bit."
            "Just so I can more easily admire my own beauty."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
            
    else:
        "A wonderful face to wake up to everyday."
        jump bedroom
    return

label icecream:
    scene bedroomstatic
    if item_use == "True":
        if player.has_selected(knife):
            "I use the knife to pick up a little dab of ice cream."
            $ Fr_exp = "neutralhappyo"
            dr "Hmm, tasty."
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
        if player.has_selected(droink):
            "Dr. Oink eats a bit of the ice cream."
            $ Fr_exp = "happyyello"
            dr "So, what do you think?"
            $ Fr_exp = "gone"
            "She gives it a solid 6/10. Too much artificial sweetener."
            $ Fr_exp = "neutral1sideo"
            dr "Everyone's a critic."
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
    else:
        "Half-finished bubblegum ice cream tubs are scattered across the floor."
        "Look, I was sad, okay?!"
        jump bedroom
    return

label droink:
    scene bedroomstatic
    if item_use == "True":
        if player.has_selected(knife):
            $ Fr_exp = "happyangryo"
            dr "En garde!"
            $ Fr_exp = "gone"
            "I challenge Dr. Oink to a knife fight."
            "She pulls out a beaker of acid from behind her back."
            "{size=-10}...I put the knife away.{/size}"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
        if player.has_selected(dirtymag):
            "Dr. Oink says she prefers science.{w} But she thanks me anyway."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
    else:
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
            $ Dr_Oink_Count = 3
            jump bedroom
        elif Dr_Oink_Count == 3:
            "Okay okay, I pick up Dr. Oink to take with me."
            play sound "music/additem.mp3"
            $inventory.add(droink)
            jump bedroom
        
    return
label bedroombed:
    scene bedroomstatic
    if item_use == "True":
        if player.has_selected(knife):
            "I stab my bed."
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
        if player.has_selected(dirtymag):
            $ Fr_exp = "closedsweato"
            dr "Maybe later."
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
    else:
        "A big comfy bed fit for only the best of the best."
        "And by the best of the best, I mean me."
        jump bedroom
    return
label closetbedroom:
    scene bedroomstatic
    if item_use == "True":
        if player.has_selected(knife):
            $ Fr_exp = "thinkingo"
            dr "Hmm, I don't think destroying this will help me with anything."
            $ Fr_exp = "sidesado"
            dr "In all honesty, it just seems like more work."
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
        if player.has_selected(napkin):
            "I clean up a bit."
            "Nothing happens, though I do feel a bit more energized."
            $ Fr_exp = "confusedo"
            dr "Maybe I should clean more often."
            $ Fr_exp = "gendou2"
            dr "..."
            $ Fr_exp = "neutral1sideo"
            dr "Or not."
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
    else:
        "I don’t wanna open these.{w} The skeletons I have stored in here are going to fall out."
        "Packing was never my strong suit."
        jump bedroom
    return
label bedroomclothes:
    scene bedroomstatic
    if item_use == "True":
        if player.has_selected(knife):
            "I don't think this is how laundry works."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
        if player.has_selected(napkin):
            "I'd add this to my dirty laundry pile, except I have a gut feeling that I might need this for something later."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
        if player.has_selected(bedshirt):
            "Yup, this is where I got my shirt."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
        if player.has_selected(droink):
            "Dr. Oink judges me for my lifestyle choices."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
        if player.has_selected(fancyshirt):
            "And after all that effort I put in to make this?!"
            "I'll keep it for a bit longer."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
    else:
        if bedroomclothesvisit == 0:
            "A messy assortment of worn clothes. I still have a while until laundry day."
            if have_shirt == False:
                $ Fr_exp = "thinkingo"
                dr "The only thing that would fit my monster would be..."
                $ Fr_exp = "gone"
                show bedshirtbig at itemslidein
                "I pick up my old night shirt."
                $ Fr_exp = "closedhappyo"
                dr "Perfect, this'll fit!"
                show bedshirtbig at itemslideout
                $ Fr_exp = "gone"
                $inventory.add(bedshirt)
                $ have_shirt = True
                if have_shoes or have_pants == False:
                    $ Fr_exp = "gendou2o"
                    dr "But I'm still missing some clothing articles..."
                    $ Fr_exp = "gone"
                    if have_pants == False:
                        $ Fr_exp = "neutral1o"
                        dr "None of these pants will fit him."
                        $ Fr_exp = "gone"
                        if dick == "4" or dick == "5":
                            $ Fr_exp = "cockyo"
                            dr "Not with those additional enhancements I gave him."
                            $ Fr_exp = "gone"
                $ bedroomclothesvisit += 1
                jump bedroom
        elif bedroomclothesvisit == 1:
            "Laundry day is when you shift the pile of clothes a few inches in one direction, right?"
            jump bedroom
    return
label bedroomdrapes:
    scene bedroomstatic
    if item_use == "True":
        if player.has_selected(knife):
            "If I rip my blinds, that would just make more light come through."
            "So, no thanks."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
        if player.has_selected(droink):
            "Dr. Oink says that if I open my blinds and clean my room, it would help improve my mood."
            "I ignore her."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump bedroom
    else:
        "*HISS* DAYLIGHT."
        jump bedroom
    return
    
##### STUDY  ##### LABELS AND DESCRIPTIONS ###
label study:
    window hide None
    scene studystatic
    hide screen inventory_button2
    hide screen inventory_button
    if have_grower:
        scene studystatic
        $ renpy.pause(0.1)
        $ Fr_exp = "closedsado"
        dr " A-CHOO!" with hpunch
        $ Fr_exp = "sidesado"
        dr "Ugh..."
        $ Fr_exp = "sado"
        dr "The ventilation in this room isn’t very good."
        $ Fr_exp = "gone"
        "Suddenly, I become aware of the foul odor the weed-grower in my pocket is putting off."
        $ Fr_exp = "screamcryo"
        dr "Achoo! Achoo!"
        $ Fr_exp = "crazedsurprisedcryo"
        dr "GAH-! I- I can't breathe!"
        $ Fr_exp = "gone"
        play sound "music/thud.wav"
        "I collapse to the ground, gasping for air." with vpunch
        play doublesound "music/whoosh.ogg"
        scene black with hpunch
        nvlbox "{size=+40}YOU DIED.{/size}"
        nvl clear
        "Try again?"
        menu:
            "Yes, please...":
                "Alrighty!"
                $ inventory.drop(weedgrower)
                $ have_grower = False
                jump conservatory
            "{size=-13}No, I'll stay dead, thank you.{/size}":
                "Well, alright."
                return
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
    if item_use == "True":
        if player.has_selected(knife):
            "I stab the globe, but nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
        if player.has_selected(napkin):
            "I wipe the globe. Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
    else:
        "A nice sturdy globe of the world."
        "It’s a nice reminder that there exists things outside my door."
        "If I ever stoop low enough to want to leave, anyway."
        jump study
    return
    
label donutstudy:
    scene studystatic
    if item_use == "True":
        if player.has_selected(knife):
            "I cut a bit of the donut off and eat it."
            $ Fr_exp = "gendou1o"
            dr "Stale, but tasty."
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
    else:
        "Bubblegum flavored donuts from my favorite pastry shop."
        "I'll finish them later. ...I swear."
        jump study
    return
    
label buttonstudy:
    scene studystatic
    if item_use == "True":
        if player.has_selected(knife):
            "I stab the button!"
            "But the entryway is already open, so nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
    else:
        "This button was set to move the bookshelf, revealing the passage to my secret lab."
        "But I got lazy and just keep it open all the time now."
        jump study
    return
label dictionarystudy:
    scene studystatic
    if item_use == "True":
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
    else:
        "A comically large dictionary."
        "It retorts that it can translate any script known and unknown to man."
        "Pretty useful!{w} But also painfully heavy."
        "I refuse to carry this around if I don’t have to."
        "Pick up?"
        menu:
            "Yes":
                $ have_dictionary = True
                play sound "music/additem.mp3"
                $inventory.add(dictionary)
                "It’s weight makes me instantly regret this decision." with hpunch
                $ Fr_exp = "closedsado"
                dr "Gah, this is impossible!"
                $ Fr_exp = "gone"
                jump study
            "No.":
                "If I can afford to not carry a two ton book around, that would be great."
                jump study
        jump study
    return
label putdictionarydown:
    scene studystatic
    if item_use == "True":
        if player.has_selected(dictionary):
            $ have_dictionary = False
            play sound "music/creak.wav"
            "I throw the dictionary back on the shelf, which makes a worrying sound." with vpunch
            $inventory.drop(dictionary)
            $ Fr_exp = "neutralhappyo"
            dr "Perfect."
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
            
    else:
        if seen_necromancy:
            "This is where the dictionary used to sit."
            "But I left it down in the church and there's no way I'm dragging it back up here."
            "Consider it a donation to the church.{w} ...I wonder if I can write it off my taxes."
            $ Fr_exp = "gendou1o"
            dr "Like I even pay taxes."
            $ Fr_exp = "gone"
            jump study
        else:
            "Should I put the dictionary down?"
            menu:
                "Yes":
                    $ have_dictionary = False
                    play sound "music/creak.wav"
                    "I throw the dictionary back on the shelf, which makes a worrying sound." with vpunch
                    $inventory.drop(dictionary)
                    $ Fr_exp = "neutralhappyo"
                    dr "Perfect."
                    $ Fr_exp = "gone"
                    jump study
                "No.":
                    $ Fr_exp = "gendou2o"
                    dr "I'm going to die."
                    $ Fr_exp = "gone"
                    jump study
        jump study
    return
label newspaperstudy:
    scene studystatic
    if item_use == "True":
        if player.has_selected(knife):
            "I stab the paper. {w}Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
        if player.has_selected(dictionary):
            "I can already read this just fine, thank you."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
    else:
        "I pick up yesterday's newspaper."
        show newspaperview at newspaperslideup
        $ renpy.pause()
        show newspaperview at newspaperslidedown
        $ renpy.pause(0.6)
        "I put the newspaper back down."
        jump study
    return

label jarsstudy:
    scene studystatic
    if item_use == "True":
        if player.has_selected(knife):
            "I stab the jars!" with hpunch
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
        if player.has_selected(decomparm):
            "If I didn't already have a use for this arm, I'd probably add it to my pickled collection."
            "But there's plenty of severed arms in the ocean, so I can pass for today."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
        elif player.has_selected(napkin):
            $ Fr_exp = "neutral1sideo"
            dr "That sounds a lot like {i}cleaning{/i}, no thanks."
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
    else:
        "I gotta spruce up my study somehow, right?"
        "Some of these are even... {size=+10}HANDY.{/size}"
        "{size=-10}Geddit? Like.. a hand?{/size}"
        "{w=0.2}.{w=0.2}.{w=0.2}."
        $ Fr_exp = "sado"
        dr "I'm going to die alone."
        $ Fr_exp = "gone"
        jump study
    return
label plushesstudy:
    scene studystatic
    if item_use == "True":
        if player.has_selected(knife):
            $ Fr_exp = "comicshocko"
            play sound "music/whoosh.ogg"
            dr "I would {size=+10}NEVER{/size}!" with hpunch
            $ Fr_exp = "crazedsad2o"
            dr "What kind of heartless man do you take me for?!"
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
        if player.has_selected(napkin):
            "I lovingly wipe down some of the plushes."
            $ Fr_exp = "closedhappyblusho"
            dr "There! All clean! Look at how beautiful all of you are."
            $ Fr_exp = "gone"
            bbydr "Why thank you, Dr. Frank. You're so beautiful too!"
            $ Fr_exp = "closedshyblusho"
            dr "Stop it, you're embarrassing me!"
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
    else:
        "They're limited edition, {size=+10}OKAY?!{/size}"
        jump study
    return
    
label wallcubbordstudy:
    if item_use == "True":
        if player.has_selected(napkin):
            "I wipe the nifty knick knacks down."
            "Nothing happens."
            $ Fr_exp = "gendou1o"
            dr "I should get a life."
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
    else:
        scene studystatic
        "Lots of nifty knick knacks."
        jump study
    return
    
    
label signstudy:
    scene studystatic
    if item_use == "True":
        if player.has_selected(knife):
            $ Fr_exp = "angryyello"
            dr "You can't tell me what to do!"
            $ Fr_exp = "gone"
            "As a symbolic act of rebellion against corporate industrialism, I stab the sign."
            "Like any good dystopian novel, nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
        if player.has_selected(napkin):
            "I wipe the sign down, to make sure people can read to GO AWAY."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
        if player.has_selected(dictionary):
            "I don't need to use the dictionary to read the sign!"
            "I DO have a basic grasp of English, thank you."
            "{size=-10}And I'm assuming you do too, if you've gotten this far into the game.{/size}"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump study
    else:
        "Don't enter, go away!"
        "{size=-10}But if you want to get to the secret lair, you should do it from the overworld map.{/size}"
        jump study
    return
    
##### CONSERVATORY ##### LABELS AND DESCRIPTIONS ###
label conservatory:
    window hide None
    scene conservatorystatic
    hide screen inventory_button2
    hide screen inventory_button
    if have_dictionary:
        scene conservatorystatic
        $ renpy.pause(0.1)
        "As soon as I step into the room, the floor beneath my feet shakes." with hpunch
        $ Fr_exp = "crazedsurprisedo"
        dr "H-huh?!"
        scene black with vpunch
        $ Fr_exp = "gone"
        "Suddenly, my feet break through and I fall."
        dr "AA-{size=-10}AA{/size}{size=-10}AA-{/size}{size=-15}AH-{/size}{size=-15}HH-{/size}{size=-15}HH-{/size}{size=-15}HH-{/size}{size=-15}HH!{/size}{size=-15}!!{/size}"
        "The dictionary is too heavy, I knew I should have put more effort into the upkeep of the mansion!"
        play doublesound "music/whoosh.ogg"
        scene black with hpunch
        nvlbox "{size=+40}YOU DIED.{/size}"
        nvl clear
        "Try again?"
        menu:
            "...Yes.":
                "Good luck."
                $ have_dictionary = False
                $ inventory.drop(dictionary)
                jump study
            "{size=-15}No, I think I'll stay here.{/size}":
                "Let me know if you find anything down there!"
                return
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
    if _return == "potroseconserve":
        jump potroseconserve
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
    scene conservatorystatic
    if item_use == "True":
        if player.has_selected(knife):
            "I try to lock pick the porch door open."
            "Turns out it's been open the whole time."
            "Not like I need to leave, though."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
        elif player.has_selected(napkin):
            "I clean the window a bit."
            "There, now it's spotless."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
    else:
        "I can see out to the deck outside."
        "Nothing of importance out there."
        jump conservatory
    return

label plantsconserve:
    scene conservatorystatic
    if item_use == "True":
        if player.has_selected(knife):
            "I stab some of the plants."
            "They glare at me, but the knife is so dull that I don't do any lasting damage."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
        elif player.has_selected(weedgrower):
            "Woah, I better be careful with that!"
            "I don't want the plants to overgrow, it would be a hassle to weed all of them."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
        elif player.has_selected(shovel):
            "Dig up my own plants? That sounds like a lot of work, and for what?"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
    else:
        "It might not look like it, but I have a bit of a green thumb, you just can't see it because of my gloves."
        "Gangrene? Nah."
        jump conservatory
    return
label windowconserve:
    scene conservatorystatic
    if item_use == "True":
        if player.has_selected(knife):
            "I carve out an SOS signal into the windowpane."
            "But nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
        elif player.has_selected(napkin):
            "I wipe a bit of the window down for good measure."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
    else:
        "It's a beautiful day today."
        "A perfect day to kick a certain someone's ass."
        jump conservatory
    return
label potconserve:
    scene conservatorystatic
    if item_use == "True":
        if player.has_selected(knife):
            "These pots are already so broken I don't want to risk breaking them any further with the knife."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
        elif player.has_selected(napkin):
            "I clean the pots up a bit."
            "They're still pretty broken."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
    else:
        "A collection of broken pots that can I use to carry some of the Weed Grower around."
        jump conservatory
        return

label potroseconserve:
    scene conservatorystatic
    if item_use == "True":
        if player.has_selected(knife):
            "I stab the plants."
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
        elif player.has_selected(weedgrower):
            "Woah now, I don't want to make more work for myself!"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
    else:
        "Even more plants."
        "I have a lot of these."
        jump conservatory
    return

label shovelconserve:
    scene conservatorystatic
    if item_use == "True":
        if player.has_selected(dirtymag):
            "Hmm, isn't there somewhere else I should use this?"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
    else:
        if shovel_click == 0:
            if use_mag:
                "I can see a shovel sitting behind Susie. I think with him being distracted, I can reach it just fine."
            else:
                "I can see a shovel sitting behind Susie. I won’t be able to grab it without getting close enough for him to attack me."
                $ seen_shovel_susie = True
            $ shovel_click = 1
            jump conservatory
        elif shovel_click == 1:
            "I can see a shovel sitting here, do I want to grab it?"
            menu:
                "Yes":
                    if use_mag == False:
                        $ Fr_exp = "comicshocko"
                        dr "W-wait a minute! Susie is sitting right there, I can’t reach it without being attacked!"
                        $ Fr_exp = "gone"
                        menu:
                            "Reach Anyway.":
                                "I reach out and-."
                                $ renpy.music.set_volume(1.0, delay=0.1, channel='sound')
                                play doublesound "music/whoosh.ogg"
                                scene black with hpunch
                                nvlbox "{size=+40}YOU DIED.{/size}"
                                nvl clear
                                "Try again?"
                                menu:
                                    "Yes please...":
                                        "Have fun!"
                                        jump conservatory
                                    "{size=-12}No, I think I'll stay dead.{/size}":
                                        "Enjoy purgatory!"
                                        return
                            "Treasure Life.":
                                $ Fr_exp = "closedsweato"
                                dr "I should value my own life more."
                                $ Fr_exp = "neutral1o"
                                dr "I need to find a way to distract him first."
                                $ Fr_exp = "gone"
                                jump conservatory
                        jump conservatory
                    else:
                        "I manage to sneak around the distracted Susie and grab the shovel."
                        play sound "music/additem.mp3"
                        $inventory.add(shovel)
                        jump conservatory
                "No.":
                    "Maybe later..."
                    jump conservatory
    return
label susiemagconserve:
    scene conservatorystatic
    if item_use == "True":
        if player.has_selected(knife):
            "Dueling a man-eating plant with a knife can only end in one way."
            "{size=+30}{cps=*3}DEATH{/cps} {/size}{w}{size=-10}...mine specifically.{/size}" with hpunch
            "I put the knife away."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
        elif player.has_selected(shovel):
            "I don't have a death wish."
            "I don't uproot Susie."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory 
        elif player.has_selected(weedgrower):
            "My hypothesis as to what would happen if I were to pour some of the weedgrower on Susie..."
            "-Is that Susie would grow two heads."
            "Now in theory, that sounds cool, but in practice I can only see that ending with someone's death and a headache."
            "So I'll pass."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
        elif player.has_selected(napkin):
            "Getting as close as I can, I wipe a bit of the drool from Susie's mouth."
            $ Fr_exp = "closedsweato"
            dr "Maybe I should give you a little alone time..."
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
    else:
        "Don't want to disturb him..."
        if use_mag == True:
            if inventory.has_item(shovel):
                jump conservatory
            else:
                "I should use this opportunity to grab the shovel."
        jump conservatory
    return
label susieconserve:
    scene conservatorystatic
    if item_use == "True":
        if player.has_selected(knife):
            "Dueling a man-eating plant with a knife can only end in one way."
            "{size=+30}{cps=*3}DEATH{/size}{/cps} {w}{size=-10}...mine specifically.{/size}" with hpunch
            "I put the knife away."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
        elif player.has_selected(shovel):
            "I don't have a death wish."
            "I don't uproot Susie."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
        elif player.has_selected(weedgrower):
            "My hypothesis as to what would happen if I were to pour some of the weedgrower on Susie..."
            "-Is that Susie would grow two heads."
            "Now in theory, that sounds cool, but in practice I can only see that ending with someone's death and a headache."
            "So I'll pass."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
        elif player.has_selected(dirtymag):
            "I slide up towards Susie, keeping my head low."
            $ Fr_exp = "gendou1o"
            dr "Hey kid, wanna see something cool?"
            $ Fr_exp = "gone"
            "The plant hisses at me as I bring out a certain magazine."
            show dirtymag at itemslidein
            "He goes silent as he sees the sparkling muscles on the cover."
            $ Fr_exp = "cockyo"
            dr "I can accidentally leave this behind if I’m able to get closer to certain gardening equipment."
            $ Fr_exp = "gone"
            show dirtymag at itemslideout
            "He grabs the magazine in his jaws, opening it up to a full spread image. He no longer pays me any mind."
            hide dirtymag
            $ use_mag = True
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
    else:
        if visit_susie == 0:
            "It's Susie, my thesis project from my PhD program."
            "He's named after the Black Eyed Susan."
            "Look, I built him to specifically lust after the flesh of man. Yes, he’s going to bite, that’s kind of in his nature. "
            "There was no need for them to kick me out of the program for it. And he even only bit someone once, that's pretty good for a man-eating plant."
            $ visit_susie = 1
            jump conservatory
        elif visit_susie == 1:
            "My man-eating plant thesis project.{w} It lusts after the flesh of men."
            jump conservatory
    return
label havegrowallconserve:
    scene conservatorystatic
    if item_use == "True":
        if player.has_selected(weedgrower):
            "I put the weed-grower down."
            $ have_grower = False
            $ inventory.drop(weedgrower)
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
    else:
        "Should I put the weed-grower down?"
        menu:
            "Yes, please.":
                $ have_grower = False
                "I can’t stand sneezing this much. I put the weed-grower back down."
                $ inventory.drop(weedgrower)
                jump conservatory
            "{size=-5}No, I love dying.{/size}":
                "I embrace death."
                jump conservatory
    return
label growallconserve:
    scene conservatorystatic
    if item_use == "True":
        if player.has_selected(knife):
            "I stab the bag of weed-grower."
            "Some of it puffs out in a cloud of smoke that makes me sneeze."
            $ Fr_exp = "angryneutralo"
            dr "{i}Ugh...{/i} Why do I do this to myself?"
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump conservatory
            
        else:
            "Nothing happens."
            
    else:
        "I made this for my midterm project. We were supposed to make a weed-killer."
        "...I ended up creating something that makes weeds grow at an almost comical rate."
        "On top of that, I’m either deathly allergic to this or it’s poisonous. Either way I don’t want to pick this up unless I need to."     
        "Pick it up?"
        menu:
            "Yes, please.":
                play sound "music/additem.mp3"
                "Holding my nose, I put it in my inventory."
                $ Fr_exp = "closedsado"
                dr "A-CHOO!" with hpunch
                $ Fr_exp = "sidesado"
                dr "Ugh... This sucks."
                $ Fr_exp = "gone"
                $ have_grower = True
                $ inventory.add(weedgrower)
                jump conservatory
            "No, thank you.":
                "I love myself. I don’t pick up the Weed-Grower."
                jump conservatory
        jump conservatory
    return
    
##### ENTRYWAY ##### LABELS AND DESCRIPTIONS ###
label entryway:
    window hide None
    scene entrywaystatic
    hide screen inventory_button2
    hide screen inventory_button
    if have_dictionary:
        scene entrywaystatic
        $ renpy.pause(0.1)
        "As soon as I step into the room, the floor beneath my feet shakes." with hpunch
        $ Fr_exp = "crazedsurprisedo"
        dr "H-huh?!"
        scene black with vpunch
        $ Fr_exp = "gone"
        "Suddenly, my feet break through and I fall."
        dr "AA-{size=-10}AA{/size}{size=-10}AA-{/size}{size=-15}AH-{/size}{size=-15}HH-{/size}{size=-15}HH-{/size}{size=-15}HH-{/size}{size=-15}HH!{/size}{size=-15}!!{/size}"
        "The dictionary is too heavy, I knew I should have put more effort into the upkeep of the mansion!"
        play doublesound "music/whoosh.ogg"
        scene black with hpunch
        nvlbox "{size=+40}YOU DIED.{/size}"
        nvl clear
        "Try again?"
        menu:
            "...Yes.":
                "Good luck."
                $ have_dictionary = False
                $ inventory.drop(dictionary)
                jump study
            "{size=-15}No, I think I'll stay here.{/size}":
                "Let me know if you find anything down there!"
                return
    if have_grower:
        scene entrywaystatic
        $ renpy.pause(0.1)
        $ Fr_exp = "closedsado"
        dr " A-CHOO!" with hpunch
        $ Fr_exp = "sidesado"
        dr "Ugh..."
        $ Fr_exp = "sado"
        dr "The ventilation in this room isn’t very good."
        $ Fr_exp = "gone"
        "Suddenly, I become aware of the foul odor the weed-grower in my pocket is putting off."
        $ Fr_exp = "screamcryo"
        dr "Achoo! Achoo!"
        $ Fr_exp = "crazedsurprisedcryo"
        dr "GAH-! I- I can't breathe!"
        $ Fr_exp = "gone"
        play sound "music/thud.wav"
        "I collapse to the ground, gasping for air." with vpunch
        play doublesound "music/whoosh.ogg"
        scene black with hpunch
        nvlbox "{size=+40}YOU DIED.{/size}"
        nvl clear
        "Try again?"
        menu:
            "Yes, please...":
                "Alrighty!"
                $ inventory.drop(weedgrower)
                $ have_grower = False
                jump conservatory
            "{size=-13}No, I'll stay dead, thank you.{/size}":
                "Well, alright."
                return
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
    scene entrywaystatic
    if item_use == "True":
        if player.has_selected(knife):
            "I stab the shoe with the dull butter knife."
            "It lets out a depressing noise, but otherwise nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump entryway
        if player.has_selected(dirtymag):
            "Look, I didn't want to say anything..."
            "But why are you showing a dirty magazine to an inanimate object?"
            "...{size=-10}Whatever floats your boat, I guess.{/size}"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump entryway
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump entryway
    if look_smallshoes == 0:
        $ Fr_exp = "gone"
        "This random assortment of shoes are all the footwear I own."
        $ Fr_exp = "thinkingo"
        dr  "Hmm, none of these would fit the Monster, though."
        $ Fr_exp = "cockyo"
        dr "{size=+10}Naturally{/size}, his feet are really big."
        $ Fr_exp = "neutral1side"
        dr "..."
        $ Fr_exp = "crazedsidesado"
        dr "Shoot, but what am I supposed to do...?"
        $ Fr_exp = "angryneutralsmallo"
        dr "The only person who would have shoes that would fit him is..."
        $ Fr_exp = "gone"
        ".{w=0.2}.{w=0.2}.{w=0.2}{i}Dominik{/i}."
        "He had left behind a pair of his shoes after the breakup."
        "But in a fit of rage I had thrown them, along with all his other shit, inside the entryway cupboard and threw away the key."
        $ Fr_exp = "crazedsad2o"
        dr "Shit."
        $ Fr_exp = "gone"
        $ looked_shoes = "True"
        $ look_smallshoes =+1
        jump entryway
    else:
        "A group of well-worn shoes."
        "They're all the ones I own, and they're too small for my boyfriend."
        jump entryway

label carpetentryway:
    scene entrywaystatic
    if item_use == "True":
        if player.has_selected(knife):
            "Have you ever tried to stab a carpet?"
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump entryway
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump entryway
    "One of the few decorations on the ground floor that isn't from my Grandmother."
    "I added it to increase the amount of RADICAL SCIENCE."
    jump entryway
    
label chairentryway:
    scene entrywaystatic
    if item_use == "True":
        if player.has_selected(knife):
            "I poke a hole in the fancy chair."
            "Good thing my grandmother is no longer around to see it, she'd box my ears."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump entryway
        elif player.has_selected(dirtymag):
            "Hypothetically, I {i}could{/i} sit down and peruse the magazine..."
            "But I also have more important stuff to do."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump entryway
        elif player.has_selected(exshoes):
            "I sit down and put his shoes on my feet."
            "They're so big I can barely walk."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump entryway
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump entryway
    "It’s a fancy chair!"
    "I don’t really care!"
    jump entryway

label doorentryway:
    scene entrywaystatic
    if item_use == "True":
        if player.has_selected(knife):
            "I stab my front door with a rusty butterknife."
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump entryway
        elif player.has_selected(droink):
            "Dr. Oink has the same desire to leave the house that I do."
            "Meaning she doesn't want to go outside."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump entryway
        elif player.has_selected(dirtymag):
            "My front door starts to blush, but otherwise nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump entryway
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump entryway
    "The front door."
    "If I want to leave the house, I should do it from the overworld map."
    jump entryway
    
label openedcabnetentryway:
    scene entrywaystatic
    if item_use == "True":
        if player.has_selected(exshoes):
            "Wait, why would I put this back? I need this!"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump entryway
        elif player.has_selected(knife):
            "I've already opened this."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump entryway
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump entryway
    "A cupboard that used to be locked."
    "Now it's missing it's door. Eh, I can fix it later."
    jump entryway
    
label lockedcabnetentryway:
    scene entrywaystatic
    if item_use == "True":
        if player.has_selected(knife):
            $ Fr_exp = "gone"
            "Using all the strength I can muster, I pry the cupboard door off of its hinges."
            $ Fr_exp = "closedangryo"
            dr "GAH!"
            $ opened_shoeentryway = True
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            $ Fr_exp = "neutral1o"
            dr "There, it’s open."
            $ Fr_exp = "neutral2o"
            dr "That was almost as hard as opening that jar of premium bubblegum jam last week."
            $ Fr_exp = "gone"
            "Rummaging inside, I find his shoes."
            show exshoesbig at slowitemslidein
            play sound "music/additem.mp3"
            $inventory.add(exshoes)
            $ have_shoes = True
            $ Fr_exp = "gendou1"
            dr "..."
            $ Fr_exp = "wearysadcryo"
            dr "What an asshole."
            show exshoesbig at slowitemslideout
            $ Fr_exp = "sad"
            dr "..."
            hide exshoesbig
            $ Fr_exp = "sado"
            dr "I can’t believe he’s really gone."
            $ Fr_exp = "gone"
            scene darkenedentryway with Dissolve(1.0)
            window show Dissolve(0.8)
            "It wasn’t supposed to happen like this."
            "I had been okay by myself.{w} I was a genius, surrounded by those who couldn’t appreciate the beauty and grace of my work."
            "Alone.{w} Misunderstood."
            "I had convinced myself I was okay like this."
            "I had my future all planned out, I was going to die as an unknown genius, someone ahead of his time."
            "But then..."
            show dominikneutral at slowslidein
            "{i}Dominik{/i}..."
            "The way he had looked at me, at my research!"
            "I didn’t even know it was possible! That someone could potentially understand me!"
            "He knew what my work meant, what I meant."
            show dominikneutral at slowslideout
            "But he left.{w} And I was alone again."
            hide dominikneutral
            "And now this life I had chosen for myself has unbearable."
            window hide
            scene entrywaystatic with Dissolve(0.8)
            window show Dissolve(0.5)
            $ Fr_exp = "wearysadcry"
            "...The shoe’s leather is rough on my hands."
            $ Fr_exp = "sidesado"
            dr "I should get this back to Iggs and the Monster."
            $ Fr_exp = "gone"
            jump entryway
        else:
            "As try at I might, the door remains locked!"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump entryway
    "A locked cupboard."
    "I had thrown all of Dominik’s things in here after he left me."
    if looked_shoes == "True":
        $ Fr_exp = "nervousangryo"
        dr "His shoes are in here."
        $ Fr_exp = "gone"
        play sound "music/lock.ogg"
        "Naturally, it's locked."
        $ Fr_exp = "crazedsado"
        dr "...Shit."
        $ Fr_exp = "gone"
        "The key was long gone, I had fed it to Susie weeks ago."
        "I’ll need to find something to open it with. Either smash it in, or {b}pry{/b} the door off."
        $ Fr_exp = "gone"
        jump entryway
    else: 
        "I didn’t want to throw them out, just in case he came running back into my arms realizing what a mistake he had made."
        $ Fr_exp = "sadcry"
        dr "..."
        $ Fr_exp = "gone"
        "It’s been a week and still no signs of him running back into my good graces, unfortunately."
        $ Fr_exp = "gone"
        jump entryway
    jump entryway
##### DINING ROOM ##### LABELS AND DESCRIPTIONS ###
label dining:
    window hide None
    scene diningroomstatic
    hide screen inventory_button2
    hide screen inventory_button
    if have_dictionary:
        scene diningroomstatic
        $ renpy.pause(0.1)
        "As soon as I step into the room, the floor beneath my feet shakes." with hpunch
        $ Fr_exp = "crazedsurprisedo"
        dr "H-huh?!"
        scene black with vpunch
        $ Fr_exp = "gone"
        "Suddenly, my feet break through and I fall."
        dr "AA-{size=-10}AA{/size}{size=-10}AA-{/size}{size=-15}AH-{/size}{size=-15}HH-{/size}{size=-15}HH-{/size}{size=-15}HH-{/size}{size=-15}HH!{/size}{size=-15}!!{/size}"
        "The dictionary is too heavy, I knew I should have put more effort into the upkeep of the mansion!"
        play doublesound "music/whoosh.ogg"
        scene black with hpunch
        nvlbox "{size=+40}YOU DIED.{/size}"
        nvl clear
        "Try again?"
        menu:
            "...Yes.":
                "Good luck."
                $ have_dictionary = False
                $ inventory.drop(dictionary)
                jump study
            "{size=-15}No, I think I'll stay here.{/size}":
                "Let me know if you find anything down there!"
                return
    if have_grower:
        scene diningroomstatic
        $ renpy.pause(0.1)
        $ Fr_exp = "closedsado"
        dr " A-CHOO!" with hpunch
        $ Fr_exp = "sidesado"
        dr "Ugh..."
        $ Fr_exp = "sado"
        dr "The ventilation in this room isn’t very good."
        $ Fr_exp = "gone"
        "Suddenly, I become aware of the foul odor the weed-grower in my pocket is putting off."
        $ Fr_exp = "screamcryo"
        dr "Achoo! Achoo!"
        $ Fr_exp = "crazedsurprisedcryo"
        dr "GAH-! I- I can't breathe!"
        $ Fr_exp = "gone"
        play sound "music/thud.wav"
        "I collapse to the ground, gasping for air." with vpunch
        play doublesound "music/whoosh.ogg"
        scene black with hpunch
        nvlbox "{size=+40}YOU DIED.{/size}"
        nvl clear
        "Try again?"
        menu:
            "Yes, please...":
                "Alrighty!"
                $ inventory.drop(weedgrower)
                $ have_grower = False
                jump conservatory
            "{size=-13}No, I'll stay dead, thank you.{/size}":
                "Well, alright."
                return
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
    scene diningroomstatic
    if item_use == "True":
        if player.has_selected(knife):
            "I dramatically stab the dull butter knife into the middle of the table."
            "Nothing happens, except for the new unsightly scar in the middle of the table."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump dining
        elif player.has_selected(exshoes):
            "Don't put dirty shoes on the table!"
            "Is probably what my grandmother would say."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump dining
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump dining
    "A nice ornate dining table. It's covered with dust."
    "I can't even remember the last time I used this."
    jump dining
    return
        
label chairsdining:
    scene diningroomstatic
    if item_use == "True":
        if player.has_selected(knife):
            "I stab some of the chairs."
            "Eh, this is kinda boring."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump dining
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump dining
    "Some nice sturdy chairs."
    "Why do I only have three? Well because I used the others in a failed experiment."
    "Naturally."
    jump dining
    return
    
label cabnetdining:
    scene diningroomstatic
    if item_use == "True":
        if player.has_selected(knife):
            "NOPE. Not doing that."
            "My grandmother loved these plates so much, I think she'd come back from the grave just to haunt me if I messed with any of this."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump dining
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump dining
    "A nice cabinet filled with expensive old dishes. They were my grandmother’s."
    "She used to threaten to cut off my ears if I dropped any of these."
    jump dining
    return
label lampdining:
    scene diningroomstatic
    if item_use == "True":
        if player.has_selected(knife):
            "I stand on my tippy toes, trying to hit the chandelier with the butter knife."
            "Nope, can't reach."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump dining
        elif player.has_selected(decomparm):
            "I stand on my tippy toes, trying to hit the chandelier with the decomposing arm."
            "I'm able to nudge the bottom of it a bit, but nothing happens."
            "...What am I trying to do, anyway?!"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump dining
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump dining
    "A nice fancy hanging chandelier."
    "I tried to use the crystals on these in an experiment once. It didn’t work."
    jump dining
    return
label napkindining:
    scene diningroomstatic
    if item_use == "True":
        if player.has_selected(knife):
            "I stab the napkin, but the knife is so dull that it doesn't even cut."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump dining
        elif player.has_selected(napkin):
            "....This should be physically impossible to do, lmao."
            "GOOD JOB?!?!?!"
            "But also I think you're a cheater."
            "SO BYEEEE!"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            $ renpy.quit()
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump dining
    "A nice fancy napkin. It’s completely pristine."
    "Because, you know, I've never used it."
    play sound "music/additem.mp3"
    $ inventory.add(napkin)
    $ picked_up_napkin = True
    "I decide to pick it up, just in case."
    jump dining
    return

##### KITCHEN ##### LABELS AND DESCRIPTIONS ###
label kitchen:
    window hide None
    scene kitchenstatic
    hide screen inventory_button2
    hide screen inventory_button
    if have_dictionary:
        scene kitchenstatic
        $ renpy.pause(0.1)
        "As soon as I step into the room, the floor beneath my feet shakes." with hpunch
        $ Fr_exp = "crazedsurprisedo"
        dr "H-huh?!"
        scene black with vpunch
        $ Fr_exp = "gone"
        "Suddenly, my feet break through and I fall."
        dr "AA-{size=-10}AA{/size}{size=-10}AA-{/size}{size=-15}AH-{/size}{size=-15}HH-{/size}{size=-15}HH-{/size}{size=-15}HH-{/size}{size=-15}HH!{/size}{size=-15}!!{/size}"
        "The dictionary is too heavy, I knew I should have put more effort into the upkeep of the mansion!"
        play doublesound "music/whoosh.ogg"
        scene black with hpunch
        nvlbox "{size=+40}YOU DIED.{/size}"
        nvl clear
        "Try again?"
        menu:
            "...Yes.":
                "Good luck."
                $ have_dictionary = False
                $ inventory.drop(dictionary)
                jump study
            "{size=-15}No, I think I'll stay here.{/size}":
                "Let me know if you find anything down there!"
                return
    if have_grower:
        scene kitchenstatic
        $ renpy.pause(0.1)
        $ Fr_exp = "closedsado"
        dr " A-CHOO!" with hpunch
        $ Fr_exp = "sidesado"
        dr "Ugh..."
        $ Fr_exp = "sado"
        dr "The ventilation in this room isn’t very good."
        $ Fr_exp = "gone"
        "Suddenly, I become aware of the foul odor the weed-grower in my pocket is putting off."
        $ Fr_exp = "screamcryo"
        dr "Achoo! Achoo!"
        $ Fr_exp = "crazedsurprisedcryo"
        dr "GAH-! I- I can't breathe!"
        $ Fr_exp = "gone"
        play sound "music/thud.wav"
        "I collapse to the ground, gasping for air." with vpunch
        play doublesound "music/whoosh.ogg"
        scene black with hpunch
        nvlbox "{size=+40}YOU DIED.{/size}"
        nvl clear
        "Try again?"
        menu:
            "Yes, please...":
                "Alrighty!"
                $ inventory.drop(weedgrower)
                $ have_grower = False
                jump conservatory
            "{size=-13}No, I'll stay dead, thank you.{/size}":
                "Well, alright."
                return
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
    scene kitchenstatic
    if item_use == "True":
        if player.has_selected(knife):
            "I stab the fridge, but nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
        elif player.has_selected(napkin):
            $ Fr_exp = "gone"
            "I wipe a bit of the fridge down with the napkin."
            $ Fr_exp = "closedhappyo"
            dr "There! I did my allotted cleaning for the year."
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
    if fridge_click == 0:
        "Nothing in here except pickled bugs, plants, and unidentified failed projects."
        $ fridge_click += 1
    elif fridge_click == 1:
        "I should probably throw some of these out."
        $ fridge_click = 0
    jump kitchen
label takeoutkitchen:
    scene kitchenstatic
    if item_use == "True":
        if player.has_selected(knife):
            "I stab the takeout boxes, which only crumple under the attack in a sad way."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
        elif player.has_selected(napkin):
            $ Fr_exp = "gone"
            $ Fr_exp = "confusedo"
            dr "Hmm, I'd like to clean this up... but that seems like too much work."
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
    if takeout_click == 0:
        "I don’t have time to cook, I have science to do, the horizon of human knowledge to expand!"
        $ takeout_click += 1
    elif takeout_click == 1:
        dr "Maybe I can convince Iggs to clean up this kitchen."
        dr "He’ll probably ask for a raise, though."
        $ takeout_click = 0
    jump kitchen
label coffeekitchen:
    scene kitchenstatic
    if item_use == "True":
        if player.has_selected(knife):
            "I poke the coffee machine, which makes a pleasant sound."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
        elif player.has_selected(napkin):
            "I clean the coffee pot a bit."
            "It still looks pretty dirty."
            "Eh, whatever."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
    if coffee_click == 0:
        "In case you were wondering, it’s possible to stay awake for 4 days straight while drinking my very own almost-patented Dr. Frank coffee."
        $ coffee_click += 1
    elif coffee_click == 1:
        "It’s not patented yet because Iggs keeps telling me not to. Something about lawsuits and people getting hurt from drinking it."
        "I have no idea what he means.{w} Staying awake for 4 days straight is the future of humankind!"
        $ coffee_click = 0
    jump kitchen
label disheskitchen:
    scene kitchenstatic
    if item_use == "True":
        if player.has_selected(knife):
            "I stab some of the dirty dishes, hoping they'll go away and I won't have to clean them."
            "Unfortunately... nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
        elif player.has_selected(napkin):
            $ Fr_exp = "gone"
            $ Fr_exp = "comicangryshocko"
            play sound "music/whoosh.ogg"
            dr "EXCUSE ME?!" with hpunch
            $ Fr_exp = "crazedangrylinesyello"
            dr "Are you, the player, trying to get me to do my dishes?!"
            $ Fr_exp = "crazedsado"
            dr "I've never been more insulted in my life!"
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
        if player.has_selected(droink):
            "Dr. Oink judges me for my lifestyle choices."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
    "A pile of dirty dishes."
    "Surely a work of art."
    jump kitchen
label windowkitchen:
    scene kitchenstatic
    if item_use == "True":
        if player.has_selected(knife):
            "I dramatically try to make my prison escape by prying off the window hinges."
            "Nah, j/k! Why would I want to go outside, anyway?"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
        elif player.has_selected(napkin):
            "I spit on the napkin and wipe a spot off the window."
            "It still looks pretty dirty."
            "Perfect."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
    "A window that looks out to my backyard."
    "The grass is so overgrown it looks a bit like a jungle."
    $ Fr_exp = "gendou1"
    dr "..."
    $ Fr_exp = "neutral1sideo"
    dr "Eh, I'll get around to it later."
    $ Fr_exp = "gone"
    jump kitchen
label roachkitchen:
    scene kitchenstatic
    if item_use == "True":
        if player.has_selected(knife):
            "I brandish my knife."
            $ Fr_exp = "cockyo"
            dr "Pay rent... or suffer the consequences!"
            $ Fr_exp = "gone"
            "To my surprise, Mrs. Pretty Princess pulls out a machete."
            ".{w=0.2}.{w=0.2}.{w=0.2}{size=-12}I quietly put my knife away.{/size}"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
        elif player.has_selected(dirtymag):
            $ Fr_exp = "gendou1o"
            dr "Hey kid, wanna see something cool?"
            $ Fr_exp = "gone"
            "I carefully open to a full spread page of some hot bois."
            "Mrs. Pretty Princess gives me a thumbs up."
            "...Or she would have if she had opposible thumbs."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
        elif player.has_selected(droink):
            $ Fr_exp = "gone"
            "I pull out Dr. Oink and set her down to Mrs. Pretty Princess."
            "They immediately begin to talk science."
            $ Fr_exp = "closedhappyo"
            dr "Great! Even more people who can appreciate Dr. Oink's intellect!"
            $ Fr_exp = "gone"
            "I pick Dr. Oink back up when they start talking about development of chemical weapons."
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
    "Aahh, don't squish those!"
    "They’re the tenants. Mrs. Pretty Princess, Mr. Handsome Prince, Mr. Slightly Too Devoted Knight, Mr. Inappropriately Dressed Butler and Mr. Her-Majesty’s Pet."
    "No, no they don’t pay any rent.{w} Unfortunately."
    jump kitchen
label flowerkitchen:
    scene kitchenstatic
    if item_use == "True":
        if player.has_selected(knife):
            "I stab the flower."
            "If it wasn't dead already, it is now."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump kitchen
    "It's a miracle this flower is still alive. I don't even remember the last time I watered it."
    jump kitchen
label knifekitchen:
    scene kitchenstatic
    if item_use == "True":
        "Nothing happens."
        $ player.dump()
        $ item_use = "False"
        $ change_cursor("1")
        jump kitchen
    "A trusty dusty knife. It’s so worn it can’t cut anymore."
    "It’s main uses recently have been to pry open jars of jam."
    play sound "music/additem.mp3"
    "I pick it up and add it to my inventory, just in case I'll need it."
    $inventory.add(knife)
    jump kitchen
    
##### CHURCH ##### LABELS AND DESCRIPTIONS ###
label church:
    window hide None
    hide screen inventory_button2
    hide screen inventory_button
    scene churchstatic
    call screen church
    if _return == "donationpantschurch":
        jump donationpantschurch
    if _return == "donationpants":
        jump donationpants
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
        if meet_sylios:
            jump meetsylioschurch
        else:
            jump street
            
label meetsylioschurch:
    scene churchstatic
    $ Fr_exp = "gone"
    $ player.dump()
    $ item_use = "False"
    $ change_cursor("1")
    "I turn around to leave, with my contraband pants in tow."
    "Except-!"
    # TODO Play crash sfx here
    show syliossurprised
    $ Fr_exp = "crazedsurprisedyelllineso"
    dr "{size=+10}AAHH!{/size}" with hpunch
    $ Fr_exp = "crazedsurprisedyelllines"
    show syliossweetsmileo at centerbob
    hide syliossurprised
    voi "Oh! I see we meet again."
    show sylioshappyo
    hide syliossweetsmileo
    $ Fr_exp = "crazedsadsidesweatfrown"
    voi "Good morning, Mr. Frank."
    show sylioshappy
    hide sylioshappyo
    $ Fr_exp = "angrystraightwobo"
    dr "{i}Doctor{/i}."
    $ Fr_exp = "angrystraightwobfrown"
    show syliosneutralpeevedo at centersadbobslow
    hide sylioshappy
    voi "Excuse me?"
    show syliosneutralpeeved
    hide syliosneutralpeevedo
    $ Fr_exp = "neutral1sideo"
    dr "I'm {i}Dr.{/i} Frank."
    $ Fr_exp = "neutral1"
    show sylioshappyo at centerbob
    hide syliosneutralpeeved
    voi "Oh! Well then please do forgive me, Dr. Frank.{p} It’s nice to finally meet you."
    $ Fr_exp = "surprisedside"
    show syliosneutralo
    hide sylioshappyo
    syl "My name is Sylios, I just moved here."
    show syliosneutral
    hide syliosneutralo
    $ Fr_exp = "crazedsidesad"
    dr "..."
    show syliossideneutralo
    hide syliosneutral
    syl "I took over the care of the church from the last priest."
    show syliosneutralsmile
    hide syliossideneutralo
    $ Fr_exp = "crazedsurprisedyelllines2"
    dr "..."
    show syliossad
    hide syliosneutralsmile
    syl "{w=0.3}.{w=0.3}.{w=0.3}."
    show syliosclosedshyo at centersadbobslow
    hide syliossad
    $ Fr_exp = "crazedsidesad"
    syl "I see you found something of use in the donation box."
    show syliosclosedshy
    hide syliosclosedshyo
    $ Fr_exp = "crazedsurprisedyelllineso"
    dr "AAAH, I- UH-." with hpunch
    $ Fr_exp = "crazedsurprisedyelllines"
    show syliossweetsmileo
    hide syliosclosedshy
    syl "Haha, Dr. Frank no worries. That’s what they’re there for."
    show sylioshappyo
    hide syliossweetsmileo
    syl "If you have found use in them, then they were destined to go with you."
    show sylioshappy
    hide sylioshappyo
    $ Fr_exp = "surprisedside"
    dr "..."
    $ Fr_exp = "surprisedsideo"
    dr "Oh.{w} Uh. Thanks."
    $ Fr_exp = "gone"
    show syliossweetsmile at centerbob
    hide sylioshappy
    "He gives me a cute smile.{w} Wait, uh, I mean a sickly sweet smile."
    show syliossideneutralo
    hide syliossweetsmile
    $ Fr_exp = "surprised"
    syl "Since I just moved here..."
    show syliosneutralsmile
    hide syliossideneutralo
    $ Fr_exp = "crazedsidesad"
    dr "..."
    show syliossweat at centersadbobslow
    hide syliosneutralsmile
    syl "..."
    show syliosneutralsado
    hide syliossweat
    syl "I was hoping that someone might be able to show me around."
    show syliosneutralsmile
    hide syliosneutralsado
    $ Fr_exp = "crazedsad"
    dr "..."
    show syliossweat
    hide syliosneutralsmile
    syl "{w=0.3}.{w=0.3}.{w=0.3}."
    $ Fr_exp = "crazedhappysweato"
    dr "{size=+15}I GOTTA GO!{/size}" with hpunch
    scene streetstatic with Dissolve(0.2)
    $ Fr_exp = "gone"
    "I run out of the church as fast as possible."
    $ Fr_exp = "closedsado"
    dr "*Phew* Made it."
    $ Fr_exp = "surprisedo2"
    dr "He just about cornered me."
    $ Fr_exp = "angryneutralsmallo"
    dr "He just about cornered me.{fast} Gotta keep an eye out for that guy, he’s suspicious!"
    $ Fr_exp = "gone"
    $ sylios_garden = True
    $ meet_sylios = False
    jump street


label donationpantschurch:
    scene churchstatic
    if item_use == "True":
        if player.has_selected(pants):
            "Hey wait, I want to keep these!"
            if penis == 5:
                "Who knows when I'll find another pair that fits a double dick!"
            elif penis == 6:
                "Who knows when I'll find another pair that fits a tentacle dick!"
            else:
                "Who knows when I'll find another pair that would fit my boyfriend!"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        elif player.has_selected(knife):
            "I stab some of the clothes because they don't fit my boyfriend."
            "Nothing happens, though I do feel petty for some reason."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        
    else:
        if have_pants == True:
            "A donation box that holds a large collection of clothing."
            jump church
        else:
            "A donation box that holds a large collection of clothing."
            $ Fr_exp = "confusedo"
            dr "This is probably for the needy."
            $ Fr_exp = "gendou1"
            dr "..."
            $ Fr_exp = "gone"
            show pantsbig at slowitemslidein
            if penis == 2:
                "I see a large pair of pants that could most likely accommodate a small dick."
            elif penis == 3:
                "I see a large pair of pants that could most likely accommodate a medium-sized dick."
            elif penis == 4:
                "I see a large pair of pants that could most likely accommodate a big dick."
            elif penis == 5:
                "Luck of luck, I see a large pair of pants that could most likely accommodate a double penis."
            elif penis == 6:
                "Luck of luck, I see a large pair of pants that could most likely accommodate a strange tentacle dick."
            elif penis == 1:
                "I see a large pair of pants that could most likely accommodate a certain boyfriend monster."
            $ Fr_exp = "thinkingsmileo"
            dr "Well, I think I qualify as needy in some definitions of the word."
            $ Fr_exp = "cockyo"
            dr "I'll just-."
            $ Fr_exp = "gone"
            show pantsbig at slowitemslideout
            $ inventory.add(pants)
            $ have_pants = True
            play sound "music/additem.mp3"
            "I grab the pair of pants and try to stuff them into my pockets, or as much as possible."
            hide pantsbig
            "They don't fit, the legs hanging out."
            $ Fr_exp = "neutral1sideo"
            dr "Eh, close enough."
            $ Fr_exp = "gone"
            $ meet_sylios = True
            jump church
    ###Remember to keep this variable, b/c we dont want the pants to show up again after player gives to monster
    return
    
    
label donationpants:
    scene churchstatic
    if item_use == "True":
        if player.has_selected(pants):
            "Hey wait, I want to keep these!"
            if penis == 5:
                "Who knows when I'll find another pair that fits a double dick!"
            elif penis == 6:
                "Who knows when I'll find another pair that fits a tentacle dick!"
            else:
                "Who knows when I'll find another pair that would fit my boyfriend!"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        elif player.has_selected(knife):
            "I stab some of the other clothes because they don't fit my boyfriend."
            "Nothing happens, though I do feel petty for some reason."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
    else:
        "A donation box that holds a large collection of clothing."
        "I already took some pants from here."
        jump church
    return


label bookschurch:
    scene churchstatic
    if item_use == "True":
        if player.has_selected(dictionary):
            "I use the dictionary on the books."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            $ Fr_exp = "comicshocko"
            dr "!!!" with hpunch
            $ Fr_exp = "surprisedo"
            dr "What in the world?!"
            $ Fr_exp = "thinkingo"
            dr "They're books about..."
            $ Fr_exp = "crazedsurprisedyello"
            dr "...{size=+10} NECROMANCY!{/size}"
            $ Fr_exp = "crazedsado"
            dr "But- But these aren’t supposed to exist anymore! They burned everything!"
            $ Fr_exp = "crazedsurprisedyello"
            dr "I would have done anything to get my hands on these. What it would have done for me and my research- and it just shows up out of the blue like this?!"
            $ Fr_exp = "crazedsad2o"
            dr "This is impossible!"
            $ Fr_exp = "gone"
            "I flip one open."
            $ Fr_exp = "crazedhappyblusho"
            dr "{size=+10}AAHH!!!{/size}" with hpunch
            $ Fr_exp = "closedhappyblusho"
            dr "Oh my god, look at these old formulas and detailed descriptions of known spells! It has everything!"
            $ Fr_exp = "happyyell"
            dr "..."
            $ Fr_exp = "surprised"
            dr "..."
            $ Fr_exp = "crazedsidesado"
            dr "...But, how-?!"
            $ Fr_exp = "crazedsado"
            dr "And in an Cauldian church! They’re the ones who spearheaded the crusade against this sect of magic-! How did-?!"
            $ Fr_exp = "closedangry"
            dr "..."
            $ Fr_exp = "crazedsad2o"
            dr "...What in the world?"
            $ Fr_exp = "gone"
            play sound "music/additem.mp3"
            "I put the books back to where they were and leave the dictionary on the shelf, keeping a mental note of what I'd seen."
            $ Fr_exp = "gone"
            $ inventory.drop(dictionary)
            $ have_dictionary = False
            $ seen_necromancy = True
            jump church
        elif player.has_selected(knife):
            "These are precious books!"
            "Why would I stab them?!"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        elif player.has_selected(dirtymag):
            $ Fr_exp = "closedsweato"
            dr "Aha, I'm not sure this book would fit in with the others..."
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
    else:
        if inventory.has_item(dictionary):
            $ Fr_exp = "surprisedo"
            dr "Hey, wait a minute."
            $ Fr_exp = "thinkingsmileo"
            dr "I can use that huge dictionary in my study to decipher this!"
            $ Fr_exp = "neutralhappyo"
            dr "I lugged it all the way here after all.{w} Might as well use it."
            $ Fr_exp = "gone"
            jump church
        elif seen_necromancy:
            $ Fr_exp = "gone"
            "A large variety of books adorn the bookshelf."
            "I found some illegal necromancy texts among them."
            $ Fr_exp = "gone"
            jump church
        else:
            $ Fr_exp = "gone"
            "A large variety of books adorn the bookshelf."
            "They look really old, but well cared for."
            $ Fr_exp = "comicshocko"
            dr "!!!" with hpunch
            $ Fr_exp = "gone"
            "Even with my vast spring of knowledge, I can’t read any of the book titles."
            $ Fr_exp = "surprisedsideo"
            dr "What language is this even...?"
            $ Fr_exp = "gone"
            jump church
    return
    
label chairschurch:
    scene churchstatic
    if item_use == "True":
        if player.has_selected(knife):
            "I go to stab the pew, when I notice that someone has carved the initials {space=51}\"F & D\" with a heart around it in the back of the wood."
            $ Fr_exp = "crazedangrylinesyell"
            dr "..."
            $ Fr_exp = "gone"
            "I slash through the engraving."
            $ Fr_exp = "screamcry"
            dr "..."
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        if player.has_selected(decomparm):
            "I slap the pew with the severed arm."
            "Nothing happens, naturally."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
    else:
        "A whole bunch of pews."
        "I have no idea why they have so many, it's not like that many people even attend this church. What with it being in the middle of the mountains and all."
        jump church
    return
    
    
label flowersaltarweeds:
    scene churchstatic
    if item_use == "True":
        if player.has_selected(knife):
            $ Fr_exp = "gone"
            "I cut a few of the weeds to help pretty up the roses."
            $ Fr_exp = "gendou1"
            dr "..."
            $ Fr_exp = "neutral1sideo"
            dr "Might as well tidy up a bit."
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        elif player.has_selected(shovel):
            "No way!"
            "If I dug up these roses, I'm sure Sylios would kill me."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        elif player.has_selected(bedshirt) or player.has_selected(fancyshirt) or player.has_selected(exshoes) or player.has_selected(pants):
            "You attempt to dress the roses."
            "They thank you, but politely decline."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
            
    else:
        "A nice batch of roses and thorny vines sits before the altar."
        "Well... sat."
        "They're still there, but now they're overtaken with a bunch of weeds."
        jump church
    return
    
label flowersaltartchurch:
    scene churchstatic
    if item_use == "True":
        if player.has_selected(weedgrower):
            "I quickly dump all of the powder on the roses, trying my hardest not to breathe in the dust."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            $ have_grower = False
            $ use_grower = True
            $ inventory.drop(weedgrower)
            play sound "music/additem.mp3"
            "Vines, lion’s manes, and other weeds start popping up immediately, covering up the roses that were there before."
            if need_to_distract_sylios:
                $ Fr_exp = "gendou1o"
                dr "That’ll do it. Now just to let this get Sylios away from the graves..."
            else:
                $ Fr_exp = "surprisedo"
                dr "Well, that certainly did some damage."
            $ weedgrower_graves = True
            $ Fr_exp = "gone"
            jump church
        elif player.has_selected(knife):
            "I'm not {i}that{/i} mean."
            "I only stab my own plants, not other peoples'."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        elif player.has_selected(shovel):
            if please_leave_sylios:
                if sylios_route:
                    $ Fr_exp = "crazedsurprisedo"
                    dr "I'm not that angry at him to destroy his roses..."
                    $ Fr_exp = "angryneutralo"
                    dr "There's probably something I can do."
                    $ Fr_exp = "gone"
                    $ player.dump()
                    $ item_use = "False"
                    $ change_cursor("1")
                    jump church
                else:
                    $ Fr_exp = "closedsweato"
                    dr "I feel like digging up his roses might be going a bit too far..."
                    $ Fr_exp = "gone"
                    $ player.dump()
                    $ item_use = "False"
                    $ change_cursor("1")
                    jump church
            else:
                "No way!"
                "If I dug up these roses, I'm sure Sylios would kill me."
                $ player.dump()
                $ item_use = "False"
                $ change_cursor("1")
                jump church
        elif player.has_selected(bedshirt) or player.has_selected(fancyshirt) or player.has_selected(exshoes) or player.has_selected(pants):
            "You attempt to dress the roses."
            "They thank you, but politely decline."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
    else:
        if inventory.has_item(weedgrower):
            $ Fr_exp = "closedsado"
            dr "*COUGH*"
            $ Fr_exp = "confusedo"
            dr "Well, this Weed-Grower would certainly do some damage on these roses..."
            $ Fr_exp = "confusedsideo"
            dr "Not to mention my allergies."
            $ Fr_exp = "closedsado"
            dr "ACHOO!" with hpunch
            $ Fr_exp = "gone"
            if please_leave_sylios:
                $ Fr_exp = "neutralhappyo"
                dr "I can imagine that a certain gardener would have to come running in here when he realized what had happened."
                $ Fr_exp = "gone"
            jump church
        elif please_leave_sylios:
            $ Fr_exp = "thinkingo"
            dr "Hmm, I wonder what I can do to these altar roses to get him to come over here..."
            $ Fr_exp = "gone"
            jump church
        else:
            "A nice batch of roses and thorny vines sits before the altar."
            "The Atlin religion uses roses as their center point."
            $ Fr_exp = "confusedsideo"
            dr "Wait a minute. But didn’t this used to be a Cauldian church?"
            $ Fr_exp = "confusedo"
            dr "...Strange."
            $ Fr_exp = "gone"
            $ seen_flowers = True
            jump church
    return
  
  
label altarchurch:
    scene churchstatic
    if item_use == "True":
        if player.has_selected(knife):
            "As much as I detest religion, I'm not going to tempt God by stabbing the altar."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        elif player.has_selected(napkin):
            "I wipe the altar down a bit, so it's even more shiny."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        elif player.has_selected(dirtymag):
            $ Fr_exp = "gendou1"
            dr "..."
            $ Fr_exp = "neutralhappyo"
            dr "Hey God, I got a present for you."
            $ Fr_exp = "neutral1sideo"
            dr "...Actually, now that I think about it."
            $ Fr_exp = "thinkingo"
            dr "What even {i}is{/i} your sexual orientation?"
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        elif player.has_selected(decomparm):
            $ Fr_exp = "happyangryo"
            dr "Hey God!"
            $ Fr_exp = "cockyo"
            dr "Want a severed arm?"
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
    else:
        "It's an altar. I don't really know much else about it."
        jump church
    return
   
   
label stainglasschurch:
    scene churchstatic
    if item_use == "True":
        if player.has_selected(knife):
            "I try to stab the window, but the knife is so dull nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        elif player.has_selected(shovel):
            "If I broke this, I'd probably be in huge trouble."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        elif player.has_selected(decomparm):
            "You slap the window with the severed arm."
            "{i}Surprisingly{/i}, nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        elif player.has_selected(droink):
            "Dr. Oink says she admires the use of composition and color in the window piece."
            $ Fr_exp = "neutral1sideo"
            dr "Eh, whatever. I still think it looks stupid."
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        elif player.has_selected(dictionary):
            "Not even this large dictionary can help me appreciate art."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        elif player.has_selected(dirtymag):
            show dirtymag at itemslidein
            "I look at the model on the cover of Issue 5, Volume 2 of Meaty Man Monthly."
            $ Fr_exp = "gendou1"
            dr "..."
            $ Fr_exp = "surprisedo2"
            dr "He kinda looks like the guy in this stained glass window."
            $ Fr_exp = "thinkingo"
            show dirtymag at itemslideout
            dr "If he was a lot buffer, though."
            $ Fr_exp = "gone"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump church
    else:
        $ Fr_exp = "gone"
        "It's an elaborate stained glass window."
        "It shows a sad looking boy surrounded by a black basiliskkin."
        $ Fr_exp = "nervousangryo"
        dr "What crap. I’ve never understood how anyone can believe in such illogical stories."
        $ Fr_exp = "gone"
        jump church
    return
    
    
##### GRAVEYARD  ##### LABELS AND DESCRIPTIONS ###

label graveyard:
    window hide None
    hide screen inventory_button2
    hide screen inventory_button
    scene graveyardstatic
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
    jump graveyarddialoguebranching
    jump graveyard
    return

label graves:
    scene graveyardstatic
    if item_use == "True":
        if player.has_selected(shovel):
            scene graveyardstaticsanssylios
            show syliossurprised at slidedissolvein
            $ Fr_exp = "crazedsadsidesweatfrown"
            dr "..."
            show syliossweat at centerbob
            hide syliossurprised
            syl "..."
            $ Fr_exp = "gone"
            show syliossweat at slidedissolveout
            "I can’t just start digging up body parts with him standing there!"
            hide syliossweat
            if sylios_route:
                "Even if he already knows what I’m doing."
                "It's still awkward!"
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump graveyard
        else:
            "Nothing happens."
            $ player.dump()
            $ item_use = "False"
            $ change_cursor("1")
            jump graveyard
        
    elif inventory.has_item(shovel):
        
        scene graveyardstaticsanssylios
        show syliossurprised at slidedissolvein
        $ Fr_exp = "crazedsadsidesweatfrown"
        dr "..."
        show syliossweat at centerbob
        hide syliossurprised
        syl "..."
        $ Fr_exp = "gone"
        show syliossweat at slidedissolveout
        "I can’t just start digging up body parts with him standing there!"
        hide syliossweat
        if sylios_route:
            "Even if he already knows what I’m doing."
            "It's still awkward!"
        jump graveyard
    else:
        "A handful of graves that we visited the previous night."
        "Wish I could have grabbed Mr. Lance’s penis while I had the chance, though."
        if need_arm:
            if grave_visit == 0:
                "I can’t believe his arm fell off."
                "It was such a beautiful arm, too!"
                $ grave_visit = 1
                jump graveyard
            elif grave_visit == 1:
                "I was half hoping that the GORGEOUS arm we found last night would still be laying where Iggs had dropped it."
                "But it isn’t and I need to dig up a new one."
                "...But I guess I need to find something to dig it up with first."
                $ grave_visit = 0
                jump graveyard
            
    jump graveyard
    return

label bushes:
    scene graveyardstatic
    if item_use == "True":
        "Nothing happens."
        $ player.dump()
        $ item_use = "False"
        $ change_cursor("1")
        jump graveyard
    else:
        "Immaculate rose bushes."
        "The flowers in the church never used to be this beautiful."
        $ Fr_exp = "confusedo"
        dr "Strange..."
        $ Fr_exp = "gone"
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

