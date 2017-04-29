### IGGS DIALOGUE ####
#screen iggsquestions:






label labdialoguebranching:
    scene labstaticsansiggs
    if inventory.has_item(bedshirt) and bad_shirt == False:
        dr "I found a shirt!"
        ig "Great!"
        "I pull out my bedshirt and move to put it on my boyfriend."
        ig "What are you doing?"
        dr "What? I’m clearly giving my boyfriend a shirt, that’s what you wanted, right?"
        dr "To abide by public decency laws and all that other crap."
        ig "Well- I mean. Don’t you have anything fancier?"
        dr "Look, this is the only thing I own that will fit him." 
        ig "You can spruce it up at least. I mean, it has- blood? Are those blood stains on the front?"
        dr "It’s coffee. And what? You want me to spruce it up? What- what does that even mean?"
        ig "I’m pretty sure that’s not coffee, Dr. Frank..."
        ig "Aahh... Do you own a tie or a bowtie or something?"
        dr "Er-. Besides the one I’m wearing..."
        dr "Er-. Besides the one I’m wearing...{fast} No. And I can’t take this off, it’ll ruin my {i}‘look’{/i}." 
        ig "..."
        ig "Well then you better find something else to go with it." 
        ig "Here, have this back. You’ll probably need to combine this with something else."
        $ bad_shirt = True
        jump lab
    if inventory.has_item(fancyshirt):
        dr "Here you go! Fancy shirt!"
        mon "Shirt shirt!"
        # TODO you dont know this joke if you didnt try to give the shirt for the first time
        ig "Wow, I can only just barely make out the coffee stains from back here."
        dr "..."
        ig "..."
        #Dr Frank sweating
        dr "..."
        ig "You know what, let’s just make sure no one touches him during the presentation. For health precautions."
        $ inventory.drop(fancyshirt)
        $ wearing_shirt = True
        if wearing_shirt == True and wearing_shoes == True and wearing_pants == True:
            jump clothedmonsterboyfriend
        else:
            jump lab
    if inventory.has_item(pants):
        "I pull out the pants I found."
        if penis == 1:
            ig "I can't believe you actually found pants big enough to fit his huge ass."
        if penis == 2 or penis == 3:
            ig "I can’t believe you actually found weird-vegetable-dick appropriate pants."
        if penis == 4:
            ig "I can’t believe you actually found huge-weird-vegetable-dick appropriate pants."
        if penis == 5:
            ig "I can’t believe you actually found double-dick appropriate pants."
        if penis == 6:
            ig "I can’t believe you actually found weird-tentacle-dick appropriate pants."
        ig "And where exactly DID you find those?"
        dr "The church." 
        ig "I... I don’t even want to know how they ended up there."
        mon "Pants! Pants!"
        $ inventory.drop(pants)
        $ wearing_pants = True
        if wearing_shirt == True and wearing_shoes == True and wearing_pants == True:
            jump clothedmonsterboyfriend
        else:
            jump lab

    show monsterneutral at dialogueslidedissolveintwoleft
    if ig_visit == 0:
        show iggsneutralfrowno at dialogueslidedissolveintworight
        ig "Hi, Dr. Frank."
        ig "Do you need anything?"
        show iggsneutral at dialoguetworight
        hide iggsneutralfrowno
        $ ig_visit = 1
        jump iggsdialogue
    if ig_visit == 1:
        show iggsslightpeevedo at dialogueslidedissolveintworight
        ig "I see you're back."
        show iggsslightpeevedfrown at dialoguetworight
        hide iggsslightpeevedo
        $ Fr_exp = "neutral1sideo"
        dr "Yeah, I have a question."
        $ Fr_exp = "neutral"
        $ ig_visit = 2
        jump iggsdialogue
    if ig_visit == 2:
        show iggsplzo at dialogueslidedissolveintworight
        ig "Again, Dr. Frank?"
        show iggsplzfrown at dialoguetworight
        hide iggsplzo
        $ Fr_exp = "angryneutralo"
        dr "Look, don't judge me!"
        $ Fr_exp = "angryyell"
        hide iggsplzfrown
        show iggsplzo at dialoguetworightbob
        ig "Well then I must apologize in advance."
        show iggsplzfrown at dialoguetworight
        hide iggsplzo
        $ ig_visit = 3
        jump iggsdialogue
    if ig_visit == 3:
        ig "Are you almost done?"
        dr "No, not yet."
        dr "And I'll be done faster if you can help me."
        ig "What can I do for you?"
        jump iggsdialogue
        

label iggsdialogue:
    $ dialogue_choice = True
    menu:
        "{size=-10}Is that pepperoni ?{/size}" if pep_nip == False:
            scene labstaticsansiggs
            show monsterneutral at dialoguetwoleft
            show iggsslightpeevedo at dialoguetworight
            ig "His nipples are pepperoni slices."
            show iggsslightpeevedfrown at dialoguetworight
            hide iggsslightpeevedo
            show monsterfrown at dialoguetwoleft
            hide monsterneutral
            $ Fr_exp = "gendou1"
            dr "..."
            show iggsplzfrown at dialoguetworight
            hide iggsslightpeevedfrown
            ig "..."
            $ Fr_exp = "confusedsideo"
            dr "Yeah?"
            $ Fr_exp = "confusedside"
            hide iggsplzfrown
            show iggsyello at dialoguetworightbob
            ig "{size=+10}OKAY, BUT WHY?!{/size}"
            show iggsyellfrown at dialoguetworight
            hide iggsyello
            show monsterneutral at dialoguetwoleft
            hide monsterfrown
            $ Fr_exp = "confusedo"
            dr "Why not?"
            show iggssadsorryfrowndowno at dialoguetworight
            hide iggsyellfrown
            $ Fr_exp = "confused"
            ig "Because? Nipples aren’t usually made of pizza toppings!"
            show iggssadsorryfrowndown at dialoguetworight
            hide iggssadsorryfrowndowno
            $ Fr_exp = "happyyello"
            dr "My dear Iggs, you’re living in the past! This is cutting edge nipple technology we’re working with here!"
            hide monsterneutral
            show monstersweetsmile at dialoguetwoleftbob
            $ Fr_exp = "cockyo"
            dr "My boyfriend has the best nipples in the world. They’re MEATY. They have enhanced flavor! They taste like- {size=+10}Pizza!{/size}"
            $ Fr_exp = "happyyell"
            hide iggssadsorryfrowndown
            show iggsplzo at dialoguetworightbob
            ig "Of course."  
            show iggsplzfrown at dialoguetworight
            hide iggsplzo
            $ pep_nip = True
            jump iggsdialogue
        "Papa!" if papa_dialogue == False:
            scene labstaticsansiggs
            show monstersweetsmileo at dialoguetwoleftbob
            show iggsneutral at dialoguetworight
            $ Fr_exp = "neutral1"
            mon "Papa is back!"
            show monstersweetsmile at dialoguetwoleft
            hide monstersweetsmileo
            show iggsworried at dialoguetworight
            hide iggsneutral
            $ Fr_exp = "thinkingo"
            dr "Okay, while I’m out your job is to uh, train him out of that." 
            $ Fr_exp = "neutral1side"
            show iggssurprisedfrownupo at dialoguetworight
            hide iggsworried
            show monsterneutral at dialoguetwoleft
            hide monstersweetsmile
            ig "Why me?"
            $ Fr_exp = "confusedo"
            show iggssurprisedfrownup at dialoguetworight
            hide iggssurprisedfrownupo
            dr "What else do I pay you for?"
            show monsterfrown at dialoguetwoleft
            hide monsterneutral
            $ Fr_exp = "confused"
            show iggsslightpeevedo at dialoguetworight
            hide iggssurprisedfrownup
            ig "For helping you run your experiments Dr. Frank, not for training your undead boyfriend out of his daddy kink."
            show iggsslightpeevedfrown at dialoguetworight
            hide iggsslightpeevedo
            $ Fr_exp = "angryyello"
            dr "Hey! This {i}IS{/i} an experiment. So it’s technically part of your job description!" 
            show monsterneutral at dialoguetwoleft
            hide monsterfrown
            $ Fr_exp = "angryneutralo"
            dr "And need I remind you that your current job is to make him stop referring to me as \"Papa\". I am to be formally addressed as \"Boyfriend.\""
            hide monsterneutral
            show monstersweetsmileo at dialoguetwoleftbob
            $ Fr_exp = "neutral1"
            show iggssurprisedfrown at dialoguetworight
            hide iggsslightpeevedfrown
            $ Fr_exp = "surprisedside"
            mon "Papa!"
            show iggsplzo at dialoguetworight
            hide iggssurprisedfrown
            show monsterneutral at dialoguetwoleft
            hide monstersweetsmileo
            ig "This is inhumane on so many levels..."
            show iggsplzfrown at dialoguetworight
            hide iggsplzo
            $ Fr_exp = "gone"
            $ papa_dialogue = True
            jump iggsdialogue
        "{size=-5}About Dominik...{/size}" if dom_dialogue == False:
            scene labstaticsansiggs
            show monsterneutral at slidedissolveintwoleftout
            show iggsworriedo at dialoguetworight
            $ Fr_exp = "neutral1side"
            ig "About Dominik..."
            show iggsworried at dialoguetworight
            hide iggsworriedo
            $ Fr_exp = "angryneutralo"
            dr "I don’t want to talk about that asshole."
            $ Fr_exp = "nervousangry"
            show iggssado at dialoguetworight
            hide iggsworried
            ig "But-."
            show iggssad at dialoguetworight
            hide iggssado
            $ Fr_exp = "crazedangryyello"
            dr "{size=+10}I SAID I DON’T WANT TO TALK ABOUT HIM!{/size}" 
            $ Fr_exp = "crazedangryyell"
            show iggssadsorrysideo at dialoguetworightbob
            hide iggssad
            ig "I know, sorry."
            $ Fr_exp = "neutral1"
            show iggsclosedsad at dialoguetworight
            hide iggssadsorrysideo
            ig "..."
            show iggssado at dialoguetworight
            hide iggsclosedsad
            ig "I was just curious, how much of your research did you end up showing him?"
            $ Fr_exp = "wearysad"
            show iggssad at dialoguetworight
            hide iggssado
            dr "..."
            $ Fr_exp = "sidesado"
            show iggssurprisedfrownup at dialoguetworightbob
            hide iggssad
            dr "Everything he wanted to see. He kept asking. And I just wanted to keep talking to him, to have him keep coming back-." 
            $ Fr_exp = "closedsad"
            show iggssad at dialoguetworight
            hide iggssurprisedfrownup
            dr "..."
            $ Fr_exp = "wearysadcryo"
            dr "...I showed him everything."
            $ Fr_exp = "wearysadcry"
            show iggsclosedsad at dialoguetworight
            hide iggssad
            ig "..."
            show iggssadsorryfrowndowno at dialoguetworight
            hide iggsclosedsad
            ig "I’m sorry, Dr. Frank."
            $ Fr_exp = "neutral1side"
            show iggssad at dialoguetworight
            hide iggssadsorryfrowndowno
            dr "..."
            show monsterfrown at dialogueslidedissolveintwoleft
            $ Fr_exp = "gone"
            $ dom_dialogue = True
            jump iggsdialogue
        "Dr. Oink!" if inventory.has_item(droink) and droink_iggs == False:
            scene labstaticsansiggs
            show monsterneutral at slidedissolveintwoleftout
            show iggsplzfrown at dialoguetworight
            $ Fr_exp = "closedhappyblusho"
            dr "Iggs!" 
            $ Fr_exp = "gendou1o"
            show iggssworried at dialoguetworight
            hide iggsplzfrown
            show droinkbig at dialoguetworightslidedissolveinitem
            dr "I don’t know if you’ve met Dr. Oink."
            $ Fr_exp = "happyyello"
            dr "Iggs, Dr. Oink. Dr. Oink, Iggs." 
            $ Fr_exp = "gone"
            show iggsplzfrown at dialoguetworightbob
            hide iggsworried
            "I hold out the esteemed doctor’s hoof for Iggs to shake."
            $ Fr_exp = "happyyell"
            ig "..."
            $ Fr_exp = "neutral1smile"
            show iggsplzo at dialoguetworight
            hide iggsplzfrown
            ig "Don’t you have more important things to do?"
            show iggsplzfrown at dialoguetworight
            hide iggsplzo
            $ Fr_exp = "comicangryshocko"
            dr "Hmph! Rude! Fine, Dr. Oink and I will grace someone else with our presence, somewhere we're appreciated."
            hide iggsplzfrown
            show iggsneutral at slidedissolveintworightout
            show droinkbig dialoguetworightslidedissolveoutitem
            $ renpy.pause (0.2)
            $ Fr_exp = "gone"
            $ droink_iggs = True
            jump lab
        "{size=-15}I hope we don't get arrested.{/size}" if sylios_question == False and need_arm == False:
            scene labstaticsansiggs
            show monsterneutral at slidedissolveintwoleftout
            if sylios_route:
                show iggsneutral at dialoguetworight
                $ Fr_exp = "angryneutralsideo"
                dr "I met the guy who saw us stealing body parts." 
                $ Fr_exp = "angryneutralside"
                show iggsscaredshito at dialoguetworightbob
                hide iggsneutral
                ig "What?! You did?! Oh god. He’s going to call the cops on us."
                show iggsscaredshit at dialoguetworight
                hide iggsscaredshito
                $ Fr_exp = "angrystraightwobo"
                dr "He won’t. Or at least that’s what he SAYS."
                $ Fr_exp = "angryneutralside"
                show iggssadsorryo at dialoguetworight
                hide iggsscaredshit
                ig "Huh? What do you mean?"
                show iggssadsorryfrown at dialoguetworight
                hide iggssadsorryo
                $ Fr_exp = "comicangryshocko"
                dr "NGGGHHH!!!!! FUCK HIM! He’s- HE’S JUST LIKE- LIKE THAT ASSHOLE! Like- like fucking Dominik." 
                $ Fr_exp = "nervousangryo"
                dr "He’s even got the same stupid pretty smile. I hate that people keep approaching me only for my research." 
                $ Fr_exp = "closedangryo"
                dr "...I hate it, I hate it so much." 
                $ Fr_exp = "closedangry"
                hide iggssadsorryfrown
                show iggssado at dialoguetworightbob
                ig "Dr. Frank...?"
                show iggssad at dialoguetworight
                hide iggssado
                $ Fr_exp = "gone"
            elif sylios_garden:
                show iggsneutral at dialoguetworight
                $ Fr_exp = "neutral1sideo"
                dr "I met the guy who saw us stealing body parts." 
                show iggssurprisedfrownupo at dialoguetworight
                hide iggsneutral
                $ Fr_exp = "neutral1"
                ig "What?! Oh god! He’s going to call the cops on us, I just know it!"
                show iggssurprisedfrownup at dialoguetworight
                hide iggssurprisedfrownupo
                $ Fr_exp = "thinkingo"
                dr "Well... he didn’t say anything about that. Or even about the pants he saw me stealing." 
                $ Fr_exp = "thinking"
                hide iggssurprisedfrownup
                show iggsscaredshito at dialoguetworightbob
                ig "He saw you stealing pants too?!"
                show iggsscaredshit at dialoguetworight
                hide iggsscaredshito
                $ Fr_exp = "surprisedo"
                dr "It was for my boyfriend!"
                $ Fr_exp = "surprisedside"
                show iggsplzo at dialoguetworight
                hide iggsscaredshit
                ig "That doesn’t make it any less wrong, Dr. Frank." 
                show iggsplzfrown at dialoguetworight
                hide iggsplzo
                $ Fr_exp = "angryneutralsideo"
                dr "Fine, whatever."
                $ Fr_exp = "neutral1"
                hide iggsplzfrown
                show iggssadsorrysideo at dialoguetworightbob
                ig "Now I’m even more worried. What kind of person doesn’t call the cops when they see someone stealing body parts...?" 
                $ Fr_exp = "gone"
                show iggssadsorrysidefrown at dialoguetworight
                hide iggssadsorrysideo
            else: 
                show iggsscaredshito at dialoguetworight
                $ Fr_exp = "neutral1"
                ig "AAAHH, what are we going to do if that guy goes to the police?"
                show iggsscaredshit at dialoguetworight
                hide iggsscaredshito
                $ Fr_exp = "confusedsideo"
                dr "Who?"
                $ Fr_exp = "confusedside"
                show iggssurprisedfrownupo at dialoguetworight
                hide iggsscaredshit
                ig "Have you already forgotten?! The guy who walked in on us stealing body parts!"
                show iggssurprisedfrownup at dialoguetworight
                hide iggssurprisedfrownupo
                $ Fr_exp = "neutral1o"
                dr "Oh yeah."
                show iggssadsorryfrown at dialoguetworight
                hide iggssurprisedfrownup
                $ Fr_exp = "gendou1"
                dr "..."
                $ Fr_exp = "confusedo"
                dr "I’ve never seen him before. I wonder what he was doing there." 
                show iggssurprisedfrowno at dialoguetworight
                hide iggssadsorryfrown
                $ Fr_exp = "confused"
                ig "Is THAT what you’re worried about, Dr. Frank?!"
                show iggssurprisedfrown at dialoguetworight
                hide iggssurprisedfrowno
                $ Fr_exp = "gone"
            show monsterneutral at dialogueslidedissolveintwoleft
            $ sylios_question = True
            jump iggsdialogue
        "{size=-10}I have a question...{/size}":
            scene labstaticsansiggs
            $ Fr_exp = "gone"
            show monsterneutral at slidedissolveintwoleftout
            show iggsworriedo at dialoguetworight
            ig "About what, Dr. Frank?"
            show iggsworried at dialoguetworight
            hide iggsworriedo
            menu:
                "{size=-10}I need help finding...{/size}":
                    menu:
                        "Shoes.":
                            dr "Shoes."
                            
                            $ dialogue_choice = False
                            jump lab
                        "A shirt." if bad_shirt == False:
                            dr "A shirt."
                            $ dialogue_choice = False
                            jump lab
                        "A fancier shirt." if bad_shirt == True:
                            if fancy_shirt_question == 0:
                                dr "A... fancier shirt? What's wrong with this one?"
                                ig "You mean, besides it being a wrinkled nightshirt from a decade old science camp?"
                                ig "I can’t believe you only own a single bowtie. I mean you wear that ‘look’ every single day."
                                ig "Wait... Dr. Frank, do you wash your clothes?"
                                dr "{fast}{size=+10}NO COMMENT.{/size}"
                                ig "{size=-10}I don’t get paid enough for this.{/size}"
                                ig "Fine, about the shirt- You’ll have to get creative, I think." 
                                ig "Do you own a cravat?"
                                dr "A what?"
                                ig "You know, those white poofy lace things that were popular in historical dress." 
                                dr "No, I absolutely don’t own any of those." 
                                ig "They shouldn’t be all that difficult to make. "
                                $ dialogue_choice = False
                                $ fancy_shirt_question = 1
                                jump lab
                            if fancy_shirt_question == 1:
                               dr "HOW DO I MAKE A FANCY SHIRT?!"
                               ig "Dr. Frank calm down." 
                               ig "You’ll need to make a cravat to make the shirt at least presentable."
                               ig "That way the conference goers won’t be able to see the blood- uh, the coffee stains from far away."  
                               ig "Do you own anything that is white, poofy, and made of lace?"
                               dr "HGGGNNN."
                               if inventory.has_item(napkin):
                                   ig "I think you have what you need in your inventory." 
                                   ig "Try to combine different things with the shirt."
                                   $ fancy_shirt_question = 2
                                   $ dialogue_choice = False
                                   jump lab
                               else:
                                   ig "I don’t think you have what you need just yet." 
                                   ig "Try searching around on the first floor a bit, I’m sure you’ll find something that can work."
                                   $ fancy_shirt_question = 2
                                   $ dialogue_choice = False
                                   jump lab
                            if fancy_shirt_question == 2:
                               dr "H-hey Iggs! H-haha!"
                               ig "..."
                               dr "I- um. I, I still don’t know how to make that fancy shirt." 
                               dr "..."
                               dr "Help. Please."
                               ig "*Sigh*"
                               ig "Go to the first floor, grab the napkin from off the table and then combine it with your crappy nightshirt."
                               ig "Viola’. A slightly more fancy but still hideous by common standards shirt." 
                               $ dialogue_choice = False
                               jump lab
                        "Some pants.":
                            dr "I gotta cover up his junk, you know?"
                            $ dialogue_choice = False
                            jump lab
                "{size=-10}What am I doing again?{/size}":
                    if need_clothes:
                        if need_clothes_question == 0:
                            scene labstaticsansiggs
                            show monsterneutral at slidedissolveintwoleftout
                            show iggsneutral at dialoguetworight
                            dr "What am I doing again?"
                            show iggsplzo at dialoguetworight
                            hide iggsneutral
                            ig "{i}That's{/i} the question of the century, Dr. Frank."
                            show iggsplzfrown at dialoguetworight
                            hide iggsplzo
                            dr "But seriously, what am I doing again?"
                            hide iggsplzfrown
                            show monstersweetsmile at dialogueslidedissolveintwoleft
                            show iggsslightpeevedfrown at dialoguetworightbob
                            "Iggs gestures rudely toward my boyfriend."
                            show iggsyello at dialoguetworight
                            hide iggsslightpeevedfrown
                            ig "{size=+10}THAT. YOU NEED TO DRESS THAT.{/size}"
                            show iggsyellfrown at dialoguetworight
                            hide iggsyello
                            dr "Oh, right."
                            if bad_shirt == True and wearing_shirt == False:
                                show iggsexasperatedo at dialoguetworight
                                hide iggsyellfrown
                                ig "And please, try to find a way to spruce up that old bedshirt."
                                hide iggsexasperatedo
                            show iggsslightpeevedfrown at dialoguetworight
                            hide iggsyellfrown
                            show monsterneutral at dialoguetwoleft
                            hide monstersweetsmile
                            $ need_clothes_question = 1
                            jump iggsdialogue
                        elif need_clothes_question == 1:
                            dr "Okay seriously, I have no idea what I’m supposed to do."
                            ig "We need to cover up your boyfriend before leaving the house, or else he’ll be arrested." 
                            ig "You don’t need a three piece suit- Try to find a shirt, some pants and shoes. That’ll do nicely." 
                            if bad_shirt == True and wearing_shirt == False:
                                ig "And not just any shirt, we a way to make that bedshirt of yours fancier. I'm sure you can figure out someway to make it more... frilly."
                            dr "Where am I going to find that??"
                            ig "Dr. Frank, this is YOUR house. I’m sure you have some stuff laying around!"
                            jump iggsdialogue
                    elif need_shovel:
                        if need_shovel_question == 0:
                            dr "What am I doing again?"
                            ig "In case you forgot, Dr. Frank, but your {i}boyfriend's{/i} arm fell off."
                            mon "..."
                            dr "..."
                            dr "Oh yeah!"
                            ig "Dr. Frank, you're a terrible boyfriend."
                            jump iggsdialogue
                        elif need_shovel_question == 1:
                            dr "Right so I need to get him a new arm..."
                            ig "Yeah."
                            dr "And..."
                            ig "And...?"
                            dr "How do I do that?"
                            ig "You'll need to dig up another arm in the graveyard."
                            #dr "Aha! See I DID need that shovel!"
                            dr "But isn't Sylios standing there?"
                            ig "Well then you'll have to find a way to distact him."
                            jump iggsdialogue
                    $ dialogue_choice = False
                    jump lab
        "Nevermind.":
            scene labstaticsansiggs
            $ Fr_exp = "gone"
            show monstersweetsmile at dialoguetwoleft
            show iggshappyo at dialoguetworight
            ig "Okay, Dr. Frank."
            show iggshappy at dialogueslidedissolveouttworight
            hide iggshappyo
            show monstersweetsmile at dialogueslidedissolveouttwoleft
            $ renpy.pause(0.2)
            $ dialogue_choice = False
            jump lab
             
                     
    jump lab









### SYLIOS DIALOGUE ###

label graveyarddialoguebranching:
    scene graveyardstaticsanssylios
    if use_grower:
        if sylios_route:
            scene graveyardstaticsanssylios
            show syliossad at dialogueslidedissolvein
            $ Fr_exp = "wearysado"
            dr "...Um. The, uh, the flowers inside."
            show syliossado at dialoguepos
            hide syliossad
            $ Fr_exp = "sad"
            syl "Should I go to them?"
            show syliossad at dialoguepos
            hide syliossado
            $ Fr_exp = "sidesado"
            dr "Yeah. There’s weeds in the box with them." 
            show syliossidesado at dialoguepos
            hide syliossad
            $ Fr_exp = "sidesad"
            syl "Thank you for telling me, Dr. Frank. "
            show syliossad at dialoguepos
            hide syliossidesado
            $ Fr_exp = "surprised"
            dr "..."
            show syliossupersado at dialoguepos
            hide syliossad
            $ Fr_exp = "wearysad"
            syl "...I didn’t mean anything, by asking you I mean-."
            show syliossad at dialoguepos
            hide syliossupersado
            $ Fr_exp = "angryneutralo"
            dr "Aren’t you leaving?"
            show syliossupersado at dialoguepos
            hide syliosad
            $ Fr_exp = "angryneutral"
            syl "I am. I... I’ll go now." 
            hide syliossupersado
            show syliossad at dialogueslidedissolveout
            $ Fr_exp = "gone"
            "He left."
            $ Fr_exp = "wearysadcry"
            dr "..." #(sad)
            $ Fr_exp = "gone"
            $ sylios_garden = False
            jump graveyard

        else:
            scene graveyardstaticsanssylios
            show syliosneutral at dialogueslidedissolvein
            $ Fr_exp = "crazedsurprisedyello"
            dr "Hey Sylios! I saw a whole bunch of weeds in the church! They were in that little box with your roses."
            if srsly_plz_leave_sylios:
                $ Fr_exp = "crazedhappy"
                hide syliosneutral
                show syliossweat at dialoguesadbobslow
                syl "..."
                show syliossurprisedo at dialoguepos
                hide syliossweat
                $ Fr_exp = "happyyell"
                syl "Well, then I suppose I need to leave this area completely unattended and go into the church!"
                hide syliossurprisedo
                show syliossurprisedsmile at dialoguecenterbob
                $ Fr_exp = "gone"
                "He winks at me and rushes off."
                show syliossurprisedsmile at dialogueslidedissolveout
                $ renpy.pause(0.2)
                $ sylios_garden = False
                jump graveyard
            else:
                $ Fr_exp = "crazedhappy"
                show syliossurprised at dialoguepos
                hide syliosneutral
                syl "!!!"
                hide syliossurprised
                show syliossadsurprisedo at dialoguesurprisebob
                syl "My flowers!"
                hide syliossadsurprisedo
                show syliossadsurprised at dialogueslidedissolveout
                $ Fr_exp = "gone"
                "He rushes off."
                $ sylios_garden = False
                jump graveyard
    if sylios_route:
        scene graveyardstaticsanssylios
        show syliossad at dialogueslidedissolvein
        $ Fr_exp = "nervousangry"
        dr "..."
        syl "..."
        show syliossadsurprisedo at dialoguepos
        hide syliossad
        $ Fr_exp = "closedangry"
        syl "...I'm sorry, Dr. Frank."
        show syliossad at dialoguepos
        hide syliossadsurprisedo
        $ Fr_exp = "angryneutralsideo"
        dr "I don't want to talk to you."
        show syliosclosedsad at dialoguepos
        hide syliossad
        $ Fr_exp = "angryneutralside"
        syl "..."
        show syliossado at dialoguepos
        hide syliosclosedsad
        $ Fr_exp = "wearysad"
        syl "Is there anything I can help you with?"
        show syliossad at dialoguepos
        hide syliossado
        $ Fr_exp = "gone"
        jump syliosdialogue
    if sylios_visit == 0:
        show syliossurprised at dialogueslidedissolvein
        "Crap! I made eye contact with him." 
        show syliosneutralsmile at dialoguepos
        hide syliossurprised
        $ Fr_exp = "crazedsurprisedo"
        dr "AAAH, um." 
        $ Fr_exp = "crazedsurprised"
        show syliossweetsmileo at dialoguecenterbob
        hide syliosneutralsmile
        syl "It's nice to see you again, Mr. Frank."
        show syliossweetsmile at dialoguepos
        hide syliossweetsmileo
        $ Fr_exp = "angryneutralo"
        dr "{size=+10}{i}Doctor{/i}{/size}!" with hpunch
        show syliossadsurprisedo at dialoguesurprisebob
        hide syliossweetsmile
        $ Fr_exp = "angryneutral"
        syl "Oh. Please forgive me. That was awfully rude, especially after you took the time to correct me the previous time."
        show syliosneutralsado at dialoguepos
        hide syliossadsurprisedo
        $ Fr_exp = "surprised"
        syl "Is there anything I can do to make it up to you?"
        show syliosneutralsad at dialoguepos
        hide syliosneutralsado
        $ Fr_exp = "crazedsidesad"
        dr "..."
        show syliossweat at dialoguepos
        hide syliosneutralsad
        $ Fr_exp = "crazedsurprised"
        syl "{w=0.3}.{w=0.3}.{w=0.3}."
        $ Fr_exp = "surprised"
        show syliosneutralsado at dialoguepos
        hide syliossweat
        syl "Ah, well."
        show syliossweetsmileo at dialoguepos
        hide syliosneutralsado
        $ Fr_exp = "crazedsadsidesweatfrown"
        syl "If you ever think of anything, feel free to let me know!"
        show syliossweetsmile at dialoguepos
        hide syliossweetsmileo
        $ Fr_exp = "crazedsad"
        dr "..."
        show syliossweetsmile at dialogueslidedissolveout
        $ Fr_exp = "gone"
        "SUSPICIOUS!"
        hide syliossweetsmile
        $ sylios_visit = 1
        jump graveyard
    if sylios_visit == 1:
        show syliossweetsmileo at dialogueslidedissolvein
        $ Fr_exp = "surprised"
        syl "Ah! Dr. Frank, you're back!"
        show syliossweetsmile at dialoguepos
        hide syliossweetsmileo
        $ Fr_exp = "crazedsidesad"
        dr "..."
        show syliosneutralo at dialoguepos
        hide syliossweetsmile
        $ Fr_exp = "surprisedside"
        syl "Did I get it right this time?"
        show syliosneutralsmile at dialoguepos
        hide syliosneutralo
        $ Fr_exp = "surprisedsideo"
        dr "Oh, uh, yes you did."
        show syliossweetsmileo at dialoguepos
        hide syliosneutralsmile
        $ Fr_exp = "surprised"
        syl "Is there anything I can help you with?"
        $ Fr_exp = "gone"
        show syliossweetsmile at dialoguepos
        hide syliossweetsmileo
        $ sylios_visit = 2
        jump syliosdialogue
    if sylios_visit == 2:
        show syliossweetsmileo at dialogueslidedissolvein
        syl "My! Do you like talking to me that much?"
        show syliosneutralsmile at dialoguepos
        hide syliossweetsmileo
        $ sylios_visit = 3
        jump syliosdialogue
    if sylios_visit == 3:
        show syliosclosedshyo at dialogueslidedissolvein
        $ Fr_exp = "surprised"
        syl "Stop, you're making me blush, Dr. Frank."
        show syliosclosedshy at dialoguepos
        hide syliosclosedshyo
        $ Fr_exp = "surprisedblush"
        dr "!?"
        show syliosneutralsmile at dialoguepos
        hide syliosclosedshy 
        $ Fr_exp = "comicshockblusho"
        dr "W-what?! I'm just visiting you to ask some questions!"
        show sylioshappyo at dialoguepos
        hide syliosneutralsmile
        $ Fr_exp = "surprisedsideblush"
        syl "Oh, is that what they're calling it nowadays?"
        hide sylioshappyo
        show syliossweetsmile at dialoguecenterbob
        "He winks at me."
        $ Fr_exp = "crazedsurprisedyellblush"
        show sylioshappyo at dialoguepos
        hide syliossweetsmile
        syl "So what is it that you want to ask me?"
        show sylioshappy at dialoguepos
        hide sylioshappyo
        $ Fr_exp = "gone"
        $ flirt_game = True
        $ sylios_visit = 4
        jump syliosdialogue
    if sylios_visit >= 4:
        show sylioshappyo at dialogueslidedissolvein
        $ Fr_exp = "surprisedside"
        syl "Hi there, Dr. Frank."
        show sylioshappy at dialoguepos
        hide sylioshappyo
        $ Fr_exp = "gone"
        $ sylios_visit += 1
        jump syliosdialogue
    jump graveyard
    
    
label syliosdialogue:
    $ dialogue_choice = True
    menu:
        "{size=-14}Are you f-f-flirting with me?!{/size}" if sylios_flirt == False and sylios_route == False and flirt_game == True:
            scene graveyardstaticsanssylios
            show syliosneutral at dialoguepos
            $ Fr_exp = "comicshockblusho"
            dr "Are you f-f-flirting with me?!"
            show sylioshappyo at dialoguesadbobslow
            hide syliosneutral
            $ Fr_exp = "surprisedblush"
            syl "Oh? Am I?"
            show sylioshappy at dialoguepos
            hide sylioshappyo
            $ Fr_exp = "gendou1angryblusho"
            dr "You keep telling me I’m cute!"
            show syliosclosedshyo at dialoguepos
            hide sylioshappy
            $ Fr_exp = "gendou1angryblush"
            syl "Forgive me if that is causing you any distress. I can stop if you want." 
            show syliosneutralsad at dialoguepos
            hide syliosclosedshyo
            $ Fr_exp = "surprisedblush"
            dr "!!!"
            $ Fr_exp = "sideblush"
            dr "..."
            show syliosconfusedo at dialoguepos
            hide syliosneutralsad
            syl "Dr. Frank? Would you like me to stop?"
            show syliosconfusedsmile at dialoguepos
            hide syliosconfusedo
            $ Fr_exp = "closedshyblusho"
            dr "Uh..."
            $ Fr_exp = "happyyellblusho"
            dr "I-I gotta go!"
            $ Fr_exp = "gone"
            show syliossweetsmileo at dialoguepos
            hide syliosconfusedsmile
            syl "Haha! Alright."
            hide syliossweetsmileo
            show syliossweetsmile at dialogueslidedissolveout
            $ renpy.pause(0.2)
            $ sylios_flirt = True
            $ dialogue_choice = False
            jump graveyard
            
        "{size=-15}This used to be a Cauldian church.{/size}" if seen_flowers == True and cauldian_church == False and sylios_route == False:
            scene graveyardstaticsanssylios
            show syliosneutral at dialoguepos
            $ Fr_exp = "confusedsideo"
            dr "The altar inside..."
            $ Fr_exp = "confusedo"
            dr "It has roses."
            $ Fr_exp = "confused"
            show syliossideneutralo at dialoguepos
            syl "Indeed. I worked hard to cultivate them, so I’m especially glad to see them blooming so beautifully."
            show syliosneutralsmile at dialoguepos 
            hide syliossideneutralo
            $ Fr_exp = "thinkingo"
            dr "Except roses are the symbol of the Atlin religion. And this used to be a Cauldian church." 
            $ Fr_exp = "neutral1side"
            hide syliosneutralsmile
            show syliosneutral at dialoguesadbobslow
            syl "..."
            $ Fr_exp = "surprisedside"
            dr "..."
            show syliosclosedneutralo at dialoguepos
            hide syliosneutral
            syl "Is that so?"
            $ Fr_exp = "surprisedyello"
            show syliossideneutral at dialoguepos
            hide syliosclosedneutralo
            dr "Wait, did you not know that?"
            $ Fr_exp = "surprised"
            show syliosneutralo at dialoguepos
            hide syliossideneutral
            syl "I’ll profess that I did not. The altar was barren when I arrived, so I simply planted flowers that I knew would thrive in that type of soil."
            $ Fr_exp = "surprisedside"
            show syliosneutral at dialoguepos
            hide syliosneutralo
            dr "..."
            $ Fr_exp = "gone"
            $ cauldian_church = True
            $ dialogue_choice = False
            jump syliosdialogue
            
        "{size=-12}Are you even a priest?{/size}" if seen_flowers == True and not_priest == False and cauldian_church == True and sylios_route == False:
            scene graveyardstaticsanssylios
            show syliossideneutral at dialoguepos
            $ Fr_exp = "angryneutralo"
            dr "How did you not know that this was a Cauldian church?"
            $ Fr_exp = "confusedo"
            show syliosneutral at dialoguepos
            hide syliossideneutral
            dr "Didn’t you say you took over the church from the last priest?"
            $ Fr_exp = "confused"
            show syliossideneutralo at dialoguepos
            hide syliosneutral
            syl "I did indeed. "
            $ Fr_exp = "confusedsideo"
            show syliossideneutral at dialoguepos
            hide syliossideneutralo
            dr "Then I mean- at the very least he would have mentioned the religious sect of the church you were inheriting, right?"
            $ Fr_exp = "neutral1"
            show syliossideneutralo at dialoguepos
            hide syliossideneutral 
            syl "He did not. Our... conversation was cut rather short." 
            $ Fr_exp = "surprised"
            show syliosneutral at dialoguepos
            hide syliossideneutralo
            "A chill suddenly runs up my spine."
            $ Fr_exp = "crazedsurprised2sado"
            dr "...cut short?"
            $ Fr_exp = "crazedsurprised"
            show syliosneutralpeevedo at dialoguepos
            hide syliosneutral
            syl "Hmm."
            show syliosneutralpeeved at dialoguepos
            hide syliosneutralpeevedo 
            $ Fr_exp = "closedsweato"
            dr "Uh... How was it cut short?"
            $ Fr_exp = "crazedsadsidesweatfrown"
            show syliossweetsmileo at dialoguepos
            hide syliosneutralpeeved
            syl "Well he had to leave in a hurry, I’m not sure about what. Our conversation was rather short, all in all." 
            $ Fr_exp = "crazedsurprised"
            show sylioshappy at dialoguepos
            hide syliossweetsmileo
            dr "..."
            syl "..."
            $ Fr_exp = "crazedsidesado"
            dr "Are you even a priest?"
            $ Fr_exp = "crazedsidesad"
            show syliosneutralpeevedo at dialoguepos
            hide sylioshappy
            syl "I do not believe I ever stated such." 
            $ Fr_exp = "comicshock"
            show syliosneutralpeeved at dialoguepos
            hide syliosneutralpeevedo
            dr "!!!" with hpunch
            $ Fr_exp = "crazedsurprisedo"
            dr "Then- then what are you?!"
            $ Fr_exp = "crazedsurprised"
            show sylioshappyo at dialoguepos
            hide syliosneutralpeeved
            syl "I’m a gardener."
            $ Fr_exp = "gone"
            hide sylioshappyo
            show syliossweetsmile at dialoguecenterbob
            "He gives me another smile. It’s kind of cute. Wait, what am I thinking?!" 
            $ Fr_exp = "surprised"
            show syliosneutralo at dialoguepos
            hide syliossweetsmile
            syl "I hope that won’t be an issue."
            $ Fr_exp = "crazedsidesad"
            show syliosneutralsmile at dialoguepos
            hide syliosneutralo
            dr "..."
            show syliosneutralsado at dialoguepos
            hide syliosneutralsmile
            syl "Dr. Frank?"
            show syliosneutralsad at dialoguepos
            hide syliosneutralsado
            $ Fr_exp = "crazedsado"
            dr "No, I uh." 
            $ Fr_exp = "sado"
            dr "I just assumed..."
            $ Fr_exp = "wearysado"
            dr "That you were a priest..."
            $ Fr_exp = "sidesado"
            dr "...Sorry." 
            $ Fr_exp = "sidesad"
            hide syliosneutralsad
            show syliossweetsmileo at dialoguecenterbob
            syl "Haha, Dr. Frank! Why are you apologizing?"
            show syliossadsurprisedo at dialoguepos
            hide syliossweetsmileo 
            syl "It was my own fault for not being clearer in my introductions." 
            $ Fr_exp = "surprised"
            show syliosneutralsado at dialoguepos
            hide syliossadsurprisedo
            syl "I’m afraid to say that I won’t be preaching any sermons here. I'm sorry if you frequented this church."
            $ Fr_exp = "angryneutralo"
            show syliosneutralsmile at dialoguepos
            hide syliosneutralsado
            dr "I wouldn’t attend a church even if you paid me."
            $ Fr_exp = "angryneutral"
            show syliossurprisedo at dialoguepos
            hide syliosneutralsmile
            syl "Oh, well then. My not giving any sermons should pose no issue. I know that a few of the villagers were sad to see the last priest go."
            $ Fr_exp = "neutral1"
            show syliossideneutralo at dialoguepos
            hide syliossurprisedo
            syl "But they won’t have to wait long before the next priest arrives."
            $ Fr_exp = "surprisedsideo"
            show syliosneutral at dialoguepos
            hide syliossideneutralo
            dr "Wait, what?"
            $ Fr_exp = "surprisedside"
            show syliosneutralo at dialoguepos
            hide syliosneutral
            syl "I’m just stopping through." 
            $ Fr_exp = "sidesado"
            show syliosneutral at dialoguepos
            hide syliosneutralo
            dr "Oh. You’re not staying?"
            $ Fr_exp = "gone"
            show syliosneutral at dialogueslidedissolveout
            "Why am I feeling sad all of a sudden...?"
            hide syliosneutral
            show syliossideneutralo at dialogueslidedissolvein
            $ Fr_exp = "sad"
            syl "Hmm. Well. That all depends on how things turn out. There’s a chance that I won’t be here for long." 
            $ Fr_exp = "confused"
            show syliossideneutral at dialoguepos
            hide syliossideneutralo
            dr "..."
            show syliosneutral at dialoguepos
            hide syliossideneutral
            syl "..."
            $ Fr_exp = "confusedo"
            dr "Why {i}are{/i} you even here?"
            $ Fr_exp = "confusedside"
            hide syliosneutral
            show syliossweetsmileo at dialoguecenterbob
            syl "Haha! So direct!"
            show syliosneutralpeevedo at dialoguepos
            hide syliossweetsmileo
            syl "Well, I heard a rumor. And I decided to investigate. That’s all." 
            $ Fr_exp = "crazedsurprised2sado"
            show syliosneutral at dialoguepos
            hide syliosneutralpeevedo
            dr "What rumor?"
            $ Fr_exp = "crazedsurprised"
            show sylioshappyo at dialoguepos
            hide syliosneutral
            syl "I love the way your glasses bring out the color of your eyes." 
            $ Fr_exp = "comicshockblusho"
            show sylioshappy at dialoguepos
            hide sylioshappyo
            dr "H-huh?!?!" with hpunch
            $ Fr_exp = "sideblush"
            hide sylioshappy
            show syliossurprisedo at dialoguecenterbob
            syl "Ah! Sorry, did I say that out loud? How embarrassing." 
            show syliossweetsmile at dialoguepos
            hide syliossurprisedo
            $ Fr_exp = "crazedsurprisedyellblush"
            dr "..." #(Blushing here)
            $ Fr_exp = "gone"
            $ flirt_game = True
            $ not_priest = True
            $ dialogue_choice = False
            jump syliosdialogue
            
        "{size=-12}Can I have your shovel?{/size}" if shovel_sylios == False and sylios_route == False and need_shovel == True:
            scene graveyardstaticsanssylios
            show syliosneutral at dialoguepos
            $ Fr_exp = "happyyello"
            show syliossurprised at dialoguepos
            hide syliosneutral
            dr "Can I have your shovel?"
            hide syliossurprised
            show syliosclosedblusho at dialoguesadbobslow
            $ Fr_exp = "neutral1smile"
            syl "My! At least take me out on a date first!"
            $ Fr_exp = "surprisedblush"
            show syliosclosedblush at dialoguepos
            hide syliosclosedblusho
            dr "!!!"
            $ Fr_exp = "surprisedblusho"
            show sylioshappy at dialoguepos
            hide syliosclosedblush
            dr "W-what?!"
            $ Fr_exp = "sidesado"
            dr "No I need it for-, for..."
            $ Fr_exp = "sidesad"
            hide sylioshappy 
            show syliossweetsmileo at dialoguecenterbob
            syl "For {i}what{/i}, Dr. Frank?"
            $ Fr_exp = "closedsweato"
            show syliossweetsmile at dialoguepos
            hide syliossweetsmileo 
            dr "To, you know...{w} dig up stuff."
            $ Fr_exp = "closedsweat"
            show sylioshappyo at dialoguepos
            hide syliossweetsmile
            syl "Well, I'm sorry to say that you'll have to use your own shovel to... dig up stuff."
            $ Fr_exp = "surprised"
            show syliosneutralo at dialoguepos
            hide sylioshappyo
            syl "I try not to lend my shovel around lightly, I wouldn't want it to get... dirty."
            $ Fr_exp = "surprisedblush"
            show sylioshappy at dialoguepos
            hide syliosneutralo
            dr "..."
            syl "..."
            $ Fr_exp = "surprisedblusho"
            dr "We're still talking about gardening equipment, right?"
            show syliosneutralsmile at dialoguepos
            hide sylioshappy
            $ Fr_exp = "gone"
            $ flirt_game = True
            $ shovel_sylios = True
            jump syliosdialogue
            
        "{size=-20}Wait a minute, you didn't answer my question!{/size}" if not_priest == True and sylios_avoidance == False and sylios_route == False:
            scene graveyardstaticsanssylios
            $ Fr_exp = "comicshockblusho"
            show syliosneutral at dialoguepos
            dr "Wait a minute! You never answered my question!"
            $ Fr_exp = "crazedsurprised"
            hide syliosneutral
            show syliossweetsmileo at dialoguecenterbob
            syl "Oh? How rude of me. What question was it?"
            $ Fr_exp = "confusedo"
            show sylioshappy at dialoguepos
            hide syliossweetsmileo
            dr "What rumor are you here investigating?"
            $ Fr_exp = "confused"
            show syliosneutralpeeved at dialoguepos
            hide sylioshappy
            syl "..."
            hide syliosneutralpeeved
            show syliossweetsmileo at dialoguecenterbob
            syl "My, your hair is such a cute shade of pink.{w} I wonder if it feels as fluffy as it looks."
            $ Fr_exp = "comicshockblusho"
            show syliossweetsmile at dialoguepos
            hide syliossweetsmileo
            dr "!!! {w} W-what?!" with hpunch
            $ Fr_exp = "crazedsurprisedyellblush"
            show syliossurprisedo at dialoguepos
            hide syliossweetsmile
            syl "Dr. Frank, are you feeling alright? You’re turning a strange shade of red."
            $ Fr_exp = "closedshyblusho"
            show syliossurprisedsmile at dialoguepos
            hide syliossurprisedo
            dr "GAH! S-SHUT UP!!"
            $ Fr_exp = "gone"
            hide syliossurprisedsmile
            show syliossweetsmile at dialoguecenterbob
            "He's too strong for me!"
            $ sylios_avoidance = True
            jump syliosdialogue
            
            
            
        "{size=-15}Have you met Dr. Oink?{/size}" if inventory.has_item(droink) and sylios_droink == False and sylios_route == False:
            scene graveyardstaticsanssylios
            show sylioshappy at dialoguepos
            $ Fr_exp = "gendou1o"
            dr "Have you met the esteemed Dr. Oink?"
            show syliossurprisedo at dialoguepos
            hide sylioshappy
            $ Fr_exp = "gendou1smile"
            syl "I don’t believe I have. "
            show syliossurprisedsmile at dialoguepos
            hide syliossurprisedo 
            show droinkbig at dialoguetworightslidedissolveinitem
            $ Fr_exp = "neutralhappy"
            "I pull out my trusty companion to show Sylios."
            show syliossweetsmileo at dialoguecenterbob
            hide syliossurprisedsmile
            syl "My! How utterly adorable!"
            show sylioshappy at dialoguepos
            hide syliossweetsmileo
            $ Fr_exp = "angryyello"
            dr  "Adorable?! GAH! She’s an industry veteran, show her some respect!"
            show syliossurprisedo at dialoguepos
            hide sylioshappy
            $ Fr_exp = "angryneutral"
            syl "Forgive me, I didn’t mean to come off so rude."
            show syliossweetsmileo at dialoguecenterbob
            hide syliossurprisedo
            $ Fr_exp = "neutral1"
            syl "I think her glasses give her a very sophisticated look. Definitely the scientist I would visit if I wanted good results." 
            show syliossideneutral at dialoguepos
            hide syliossweetsmileo
            $ Fr_exp = "neutral1smile"
            syl "Hmm..."
            $ Fr_exp = "confusedo"
            dr "What is it?"
            show sylioshappyo at dialoguepos
            hide syliossideneutral
            $ Fr_exp = "confused"
            syl "What with her glasses and all- The two of you look like siblings. Very cute indeed!"
            show sylioshappy at dialoguepos
            hide sylioshappyo
            $ Fr_exp = "comicshockblush"
            dr "!!!!" with hpunch
            show droinkbig at dialoguetworightslidedissolveoutitem
            show syliossweetsmile at dialoguepos
            hide sylioshappy
            $ Fr_exp = "surprisedblush"
            dr "..."
            $ Fr_exp = "gone"
            hide droinkbig
            $ flirt_game = True
            $ sylios_droink = True
            jump syliosdialogue
            
            
            
            
        "{size=-18}There are necromancy books in the church.{/size}" if seen_necromancy == True and sylios_avoidance == True and sylios_route == False:
            scene graveyardstaticsanssylios
            show syliosneutral at dialoguepos
            $ Fr_exp = "angryneutralo"
            dr "The books in the church, are those yours?"
            $ Fr_exp = "angryneutral"
            hide syliosneutral
            show syliossweetsmileo at dialoguecenterbob
            syl "Hmm, has anyone ever told you that you have very cute expressions?"
            show syliossweetsmile at dialoguepos
            hide syliossweetsmileo
            play sound "music/whoosh.ogg"
            $ Fr_exp = "crazedangrylinesyello"
            dr "{size=+25}STOP EVADING MY QUESTIONS!{/size}" with hpunch
            show syliosneutralpeeved at dialoguepos
            hide syliossweetsmile
            $ Fr_exp = "angryneutralo"
            dr "The books, are they yours?!"
            $ Fr_exp = "angryneutral"
            show syliossideneutral at dialoguepos
            hide syliosneutralpeeved
            syl "..."
            $ Fr_exp = "angryyell"
            show syliosneutral at dialoguepos
            hide syliossideneutral
            dr "..."
            syl "..."
            $ Fr_exp = "crazedangrylinesyello"
            hide syliosneutral
            show syliossurprised at dialoguecenterbob
            dr "Just answer the question." 
            $ Fr_exp = "crazedangrylinesyell"
            hide syliossurprised
            show syliossidesado at dialoguesadbobslow
            syl "Yes, I suppose they are."
            $ Fr_exp = "angryneutralo"
            show syliosneutral at dialoguepos
            hide syliossidesado
            dr "They’re necromancy texts." 
            $ Fr_exp = "angryneutral"
            show syliossideneutral at dialoguepos
            hide syliosneutral
            syl "Hmm."
            dr "..."
            $ Fr_exp = "crazedangrylinesyell"
            show syliosneutral at dialoguepos
            hide syliossideneutral
            syl "..."
            $ Fr_exp = "angryyello"
            dr "Which has been banned and widely persecuted. Where did you get them?"
            $ Fr_exp = "angryyell"
            show syliosangryo at dialoguepos
            hide syliosneutral
            syl "Have you any experience with the field?"
            $ Fr_exp = "crazedredhandedfrowno"
            show syliosangry at dialoguepos
            hide syliosangryo
            dr "GAH-!" with hpunch
            $ Fr_exp = "gone"
            show syliosangry at dialogueslidedissolveout
            "What a question!"
            hide syliosangry
            "It wasn’t like he hadn’t seen me in the graveyard the other night digging up bodies." 
            $ Fr_exp = "closedangry"
            show syliosangry at dialogueslidedissolvein
            dr "NHHHHGGHHH."
            hide syliosangry
            show sylioshappyo at dialoguecenterbob
            syl "You seem to be struggling there a bit, Dr. Frank."
            $ Fr_exp = "angryyello"
            show sylioshappy at dialoguepos
            hide sylioshappyo
            dr "Shut up!"
            $ Fr_exp = "angryneutral"
            show syliossidesado at dialoguepos
            hide sylioshappy
            syl "Pardon if I insulted you." 
            show syliossidesad at dialoguepos
            hide syliossidesado
            $ Fr_exp = "sad"
            dr "..."
            show syliossad at dialoguepos
            hide syliossidesad
            $ Fr_exp = "sidesado"
            dr "No, no you didn’t."
            $ Fr_exp = "sidesad"
            dr "..."
            $ Fr_exp = "sado"
            dr "You haven’t said anything, this whole time." 
            $ Fr_exp = "wearysad"
            show syliosneutralsado at dialoguepos
            hide syliossad
            syl "Of what?"
            $ Fr_exp = "wearysado"
            show syliosneutralsad at dialoguepos
            hide syliosneutralsado
            dr "Last night, you saw us digging up those bodies. But you haven’t said anything at all about that."
            $ Fr_exp = "crazedsad2o"
            show syliossideneutral at dialoguepos
            hide syliosneutralsad
            dr "I stole pants out of your donation box. I ripped someone’s arm off in front of you!"
            $ Fr_exp = "closedsad"
            show syliosneutral at dialoguepos
            hide syliossideneutral
            syl "..."
            $ Fr_exp = "sad"
            dr "..."
            show syliosclosedshyo at dialoguepos
            hide syliosneutral
            syl "Did you want me to make reference to that incident?"
            show syliosneutralsmile at dialoguepos
            hide syliosclosedshyo
            $ Fr_exp = "closedsado"
            dr "No! I didn’t!"
            $ Fr_exp = "sad"
            show syliossideneutralo at dialoguepos
            hide syliosneutralsmile
            syl "Then, I don’t see what the issue is."
            $ Fr_exp = "closedsado"
            show syliossideneutral at dialoguepos
            hide syliossideneutralo
            dr "GAAAH!!!"
            $ Fr_exp = "sado"
            show syliosneutral at dialoguepos
            hide syliossideneutral
            dr "Look! If you’re going to call the authorities on us, can you just DO IT?"
            $ Fr_exp = "sad"
            hide syliosneutral
            show syliossweetsmileo at dialoguecenterbob
            syl "I wouldn’t call the cops on you, Dr. Frank." 
            $ Fr_exp = "surprisedside"
            show syliossweetsmile at dialoguepos
            hide syliossweetsmileo
            dr "..."
            $ Fr_exp = "angryneutralsideo"
            dr "You’re infuriating to talk to, you know?"
            $ Fr_exp = "angrystraightwobfrown"
            show syliossurprised at dialoguepos
            hide syliossweetsmile
            syl "..."
            hide syliossurprised
            show syliossidesado at dialoguesadbobslow
            syl "I’m sorry to hear that."
            $ Fr_exp = "neutral1sad"
            show syliossidesad at dialoguepos
            hide syliossidesado
            dr "..."
            $ Fr_exp = "closedsado"
            dr "*Sigh*"
            $ Fr_exp = "sidesado"
            show syliosneutralsad at dialoguepos
            hide syliossidesad
            dr "If those books are yours, can I assume you’ve read them?"
            $ Fr_exp = "sidesad"
            show syliosneutralo at dialoguepos
            hide syliosneutralsad
            syl "You seem awfully interested in those books."
            $ Fr_exp = "confusedo"
            show syliosneutral at dialoguepos
            hide syliosneutralo
            dr "You’re never going to answer any of my questions, are you?"
            $ Fr_exp = "confused"
            hide syliosneutral
            show syliossweetsmile at dialoguecenterbob
            dr "..."  
            $ Fr_exp = "sado"
            show syliosneutralsmile at dialoguepos
            hide syliossweetsmile
            dr "I... My research is on something similar to necromancy. I never had any academic papers to go off of, not with what happened to them after the Edict of Tannenbury."
            $ Fr_exp = "sidesado"
            show syliosneutral at dialoguepos
            hide syliosneutralsmile
            dr "So seeing those books-." 
            $ Fr_exp = "sad"
            show syliossideneutralo at dialoguepos
            hide syliosneutral
            syl "You could have easily traveled outside of Gienel, to places where magic isn’t so strictly banned." 
            $ Fr_exp = "angryworriedyello"
            show syliosneutral at dialoguepos
            hide syliossideneutralo
            dr "HAH! Yeah right. Sure studying magic in Gienel is neigh to impossible, what with the form being banned, but necromancy has been banned everywhere. Even if I had left the country, it would have been the same." 
            $ Fr_exp = "angryneutral"
            show syliosconfusedsmile at dialoguepos
            hide syliosneutral
            syl "..."
            $ Fr_exp = "surprisedside"
            show syliosconfusedo at dialoguepos
            hide syliosconfusedsmile
            syl "Would it have?"
            $ Fr_exp = "gone"
            hide syliosconfusedo
            show syliosconfusedsmile at dialoguecenterbob
            "I look up at him. He has an interesting look on his face." 
            $ Fr_exp = "surprised"
            show syliossideneutralo at dialoguepos
            hide syliosconfusedsmile
            syl "Humans have a fascinating capacity to preserve their own pasts." 
            show syliossideangryo at dialoguepos
            hide syliossideneutralo
            syl "If a government says something must be destroyed, that will insure that someone out there will try to preserve it. For better or worse."  
            show syliossidesado at dialoguepos
            hide syliossideangryo
            $ Fr_exp = "sidesad"
            syl "It seems that the only things that truly die are those that invoke little feelings." 
            $ Fr_exp = "wearysad"
            show syliossidesad at dialoguepos
            hide syliossidesado
            syl "..."
            $ Fr_exp = "confused"
            dr "..."
            $ Fr_exp = "confusedo"
            dr "Sylios...?"
            $ Fr_exp = "confusedside"
            show syliossado at dialoguepos
            hide syliossidesad
            syl "Hmm? What is it?"
            $ Fr_exp = "sado"
            show syliossad at dialoguepos
            hide syliossado
            dr "You just seemed... sad."
            $ Fr_exp = "sidesad"
            hide syliossad
            show syliosclosedshyo at dialoguecenterbob
            syl "Forgive me, I didn’t realize that was how I was coming off." 
            show syliosneutral at dialoguepos
            hide syliosclosedshyo
            syl "..."
            show syliossado at dialoguepos
            hide syliosneutral
            syl "You are free to read those books, by the way. I know that the information they contain is incredibly rare, and it sounds like it would help your own personal research." 
            $ Fr_exp = "surprisedside"
            show syliosconfusedo at dialoguepos
            hide syliossado
            syl "Which..."
            hide syliosconfusedo
            show syliosconfused at dialogueslidedissolveout
            $ Fr_exp = "gone"
            "He leans in closer to me."
            $ Fr_exp = "surprised"
            show syliossweetsmileo at dialogueslidedissolvein
            hide syliosconfused
            syl "Can you tell me a little more about? I’m a bit curious to hear what sort of research you’re conducting." 
            $ Fr_exp = "gone"
            scene darkenedentryway
            show dominikhappyo
            with Dissolve(0.2)
            dom "Wow, your research sounds cool. Can you tell me a bit more about it?"
            scene graveyardstaticsanssylios
            show sylioshappy at dialoguepos
            $ Fr_exp = "crazedsurprised"
            dr "!!!" with hpunch
            $ Fr_exp = "crazedsidesado"
            show syliossurprised at dialoguepos
            hide sylioshappy
            dr "{size=+10}N-NO!{/size}"
            $ Fr_exp = "gone"
            hide syliossurprised with Dissolve(0.2)
            "I push him away."
            $ Fr_exp = "crazedangryyello"
            dr "Absolutely NOT!"
            $ Fr_exp = "crazedsurprised2sado"
            show syliossurprised at dialogueslidedissolvein
            dr "IS THAT WHY YOU’RE HERE?!"
            $ Fr_exp = "closedsado"
            show syliossad at dialoguepos
            hide syliossurprised
            dr "NO ONE CAN SEE MY RESEARCH!"
            $ Fr_exp = "crazedsad2o"
            dr "Not again. NOT AGAIN! I’m never going to let anyone see my research ever again!"
            $ Fr_exp = "crazedsad"
            show syliossado at dialoguepos
            hide syliossad
            syl "Dr. Frank- Please, I’m sorry!"
            $ Fr_exp = "screamcryo"
            show syliossurprised at dialoguepos
            hide syliossado
            dr "LEAVE ME ALONE!"
            scene streetstatic with Dissolve(0.2)
            $ Fr_exp = "wearysadcry"
            dr "..."
            $ Fr_exp = "gone"
            $ sylios_route = True
            $ dialogue_choice = False
            jump street
            
            
            
            
        "{size=-20}What would make you leave the garden?{/size}" if need_to_distract_sylios == True and please_leave_sylios == False:
            if sylios_route == False:
                scene graveyardstaticsanssylios
                show syliosneutral at dialoguepos
                $ Fr_exp = "closedsweato"
                dr "Haha!"
                $ Fr_exp = "closedsweat"
                show syliossweetsmileo at dialoguecenterbob
                hide syliosneutral
                syl "You have an interesting look on your face there, Dr. Frank."
                show syliossweetsmile at dialoguepos
                hide syliossweetsmileo
                $ Fr_exp = "crazedhappysweato"
                dr "Y-yeah, so.{w} Um."
                $ Fr_exp = "cockyo"
                dr "Hypothetically... If something big happened, would you leave?"
                show syliosneutralpeevedo at dialoguepos
                hide syliossweetsmile
                $ Fr_exp = "crazedhappy"
                syl "Excuse me?"
                show syliosneutralpeeved at dialoguepos
                hide syliosneutralpeevedo
                $ Fr_exp = "crazedsurprised"
                dr "..."
                $ Fr_exp = "surprisedo"
                dr "U-uh, I mean like-."
                $ Fr_exp = "confusedo"
                dr "If something happened, would you go check it out?"
                show syliossideconfusedo at dialoguepos
                hide syliosneutralpeeved
                $ Fr_exp = "confused"
                syl "Well, I suppose...?"
                show syliosconfused at dialoguepos
                hide syliossideconfusedo
                $ Fr_exp = "happyyello"
                dr "Great!"
                show syliossweat at dialoguepos
                hide syliosconfused
                $ Fr_exp = "happyyell"
                syl "..."
                $ Fr_exp = "neutralhappy"
                dr "..."
                show syliossurprised at dialoguepos
                hide syliossweat
                $ Fr_exp = "neutralhappyo"
                dr "{cps=*.5}So what things would you leave for?{/cps}"
                $ Fr_exp = "neutralhappy"
                show syliossadsurprisedo at dialoguepos
                hide syliossurprised
                syl "Dr. Frank, do you want me to leave?"
                show syliossadsurprised at dialoguepos
                hide syliossadsurprisedo
                $ Fr_exp = "surprisedblusho"
                dr "O-oh! N-no I’m not saying that at all!"
                show syliossadsurprisedo at dialoguepos
                hide syliossadsurprised
                $ Fr_exp = "surprisedblush"
                syl "Then why are you asking me this?"
                show syliossad at dialoguepos
                hide syliossadsurprisedo
                $ Fr_exp = "crazedhappysweato"
                dr "No reason! Absolutely no reason!"
                $ Fr_exp = "crazedhappy"
                hide syliossad
                show syliossweat at dialoguecenterbob
                syl "..."
                $ Fr_exp = "gone"
                $ please_leave_sylios = True
                $ dialogue_choice = False
                jump graveyard
            else:
                scene graveyardstaticsanssylios
                show syliossado at dialoguepos
                $ Fr_exp = "sad"
                syl "Dr. Frank, I’m sorry-."
                show syliossad at dialoguepos
                hide syliossado
                $ Fr_exp = "angrystraightwobo"
                dr "Look, I don’t really want to talk to you right now." 
                show syliosclosedsad at dialoguepos
                hide syliossad
                $ Fr_exp = "angryneutralo"
                dr "Just tell me, what would make you leave this area?"
                show syliossado at dialoguepos
                hide syliosclosedsad
                $ Fr_exp = "nervousangry"
                syl "Do you hate me that much?"
                show syliossidesad at dialoguepos
                hide syliossado
                $ Fr_exp = "surprisedsideo"
                dr "Ah-. No, just, just for a little while, is what I meant." 
                $ Fr_exp = "surprisedside"
                show syliossad at dialoguepos
                hide syliossidesad
                syl "..."
                $ Fr_exp = "surprised"
                show syliossado at dialoguepos
                hide syliossad
                syl "Well, I usually leave this area when I need to take care of the flowers on the other side of the church. Or even the altar roses." 
                show syliossidesado at dialoguepos
                hide syliossado
                syl "Those are my children, I’m especially proud of them- the altar roses." 
                $ Fr_exp = "sidesad"
                show syliossad at dialoguepos
                hide syliossidesado
                dr "..."
                $ Fr_exp = "wearysado"
                dr "I see. Thank you." 
                $ Fr_exp = "wearysad"
                show syliosneutralsadfrowno at dialoguepos
                hide syliossad
                syl "Of course, Dr. Frank. I always enjoy talking with you, about any topic." 
                $ Fr_exp = "surprisedside"
                hide syliosneutralsadfrowno
                show syliossupersado at dialoguecenterbob
                syl "Truly." 
                $ Fr_exp = "surprisedsideblush"
                show syliosneutralsad at dialoguepos
                hide syliossupersado
                dr "..." #blush
                hide syliosneutralsad
                show syliosneutralsad at dialogueslidedissolveout
                $ renpy.pause (0.3)
                $ Fr_exp = "gone"
                $ please_leave_sylios = True
                $ dialogue_choice = False
                jump graveyard
                
        "{size=-15}Seriously, what would you leave for?{/size}" if please_leave_sylios == True and sylios_route == False and srsly_plz_leave_sylios == False:
                scene graveyardstaticsanssylios
                show syliosneutral at dialoguepos
                $ Fr_exp = "crazedhappysweato"
                dr "HYPOTHETICALLY, OF COURSE-."
                $ Fr_exp = "neutral1sideo"
                show syliossweat at dialoguepos
                hide syliosneutral
                dr "I really gotta know what would make you leave this area." 
                show sylioshappyo at dialoguepos
                hide syliossweat
                $ Fr_exp = "neutralhappy"
                syl "Well then, hypothetically, I suppose if something happened to my flowers, maybe the altar roses, I would naturally have to rush to be with them." 
                $ Fr_exp = "happyyello"
                show sylioshappy at dialoguepos
                hide sylioshappyo
                dr "Oooh!"
                hide sylioshappy
                show sylioshappy at dialogueslidedissolveout
                $ renpy.pause(0.3)
                $ Fr_exp = "gone"
                $ srsly_plz_leave_sylios = True
                $ dialogue_choice = False
                jump graveyard


        
        "Nevermind.":
            if sylios_route == True:
                scene graveyardstaticsanssylios
                show syliossidesado at dialoguepos
                $ Fr_exp = "gendou2"
                syl "I'm... sorry Dr. Frank."
                show syliossad at dialoguepos
                hide syliossidesado
                $ Fr_exp = "sad"
                dr "..."
                $ Fr_exp = "gone"
                $ dialogue_choice = False
                jump graveyard
            if sylios_visit == 2:
                scene graveyardstaticsanssylios
                show syliossweetsmileo at dialoguecenterbob
                syl "It was nice meeting you, again."
                show sylioshappyo at dialoguepos
                hide syliossweetsmileo
                syl "Feel free to come back anytime."
                hide sylioshappyo
                show sylioshappy at dialogueslidedissolveout
                $ renpy.pause(0.2)
                $ dialogue_choice = False
                jump graveyard
            if sylios_visit == 3:
                scene graveyardstaticsanssylios
                show syliossweetsmileo at dialoguecenterbob
                syl "Come back anytime."
                hide syliossweetsmileo
                show syliossweetsmile at dialogueslidedissolveout
                $ renpy.pause(0.2)
                $ dialogue_choice = False
                jump graveyard
            if sylios_visit == 4:
                scene graveyardstaticsanssylios
                show sylioshappyo at dialoguepos
                syl "I await your return."
                hide sylioshappyo
                show sylioshappy at dialogueslidedissolveout
                $ renpy.pause(0.2)
                $ dialogue_choice = False
                jump graveyard
            if sylios_visit == 5:
                scene graveyardstaticsanssylios
                show sylioshappyo at dialoguepos
                syl "Feel free to come back anytime, Dr. Frank."
                hide sylioshappyo
                show syliossweetsmileo at dialoguecenterbob
                syl "I enjoy your company."
                show syliossweetsmile at dialoguepos
                hide syliossweetsmileo
                $ Fr_exp = "surprisedblush"
                dr "!!!"
                hide syliossweetsmile
                show syliossweetsmile at dialogueslidedissolveout
                $ renpy.pause(0.2)
                $ Fr_exp = "gone"
                $ dialogue_choice = False
                jump graveyard
            else:
                scene graveyardstaticsanssylios
                show syliosneutralo at dialoguepos
                syl "Very well! See you later."
                hide syliosneutralo
                show syliosneutral at dialogueslidedissolveout
                $ renpy.pause(0.2)
                $ dialogue_choice = False
                jump graveyard
    jump graveyard 