# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):
    default two_window = True

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window" xpos -20 ypos 505

                    text who:
                        id "who" size 80

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what" color "#D6F4D6" outlines [(1, "#13060d")]

    # If there's a side image, display it above the text.
#    if side_image:
#        add side_image
#    else:
#        add SideImage() xalign 0.0 yalign 1.0

    add "DrFrank_side" xpos -60 ypos 85 zoom 0.92
    
    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    if dialogue_choice == False:
        window:
            style "menu_window"
            xalign 0.5
            yalign 0.2
            at choice_move

            hbox:
                style "menu"
                
                spacing 150

                for caption, action, chosen in items:

                    if action:

                        button:
                            action action
                            style "menu_choice_button"

                            text caption style "menu_choice"

                    else:
                        text caption style "menu_caption"
    if dialogue_choice == True:
        window:
            style "menu_window"
            xalign 0.95
            yalign 0.5
            at choice_move2

            vbox:
                style "menu"
                
                spacing 5

                for caption, action, chosen in items:

                    if action:

                        button:
                            action action
                            style "menu_choice_button"

                            text caption style "menu_choice"

                    else:
                        text caption style "menu_caption"            
                        
init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.20)
        xmaximum int(config.screen_width * 0.20)
        #yminimum int(config.screen_width * 0.20)
        #ymaximum int(config.screen_width * 0.50)

##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    #use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu
screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu
    add "images/gui/mainmenu/endlessback.png" at demomenubackgroundanimation
    add "images/gui/mainmenu/endlessbackoverlay.png"
    add "images/gui/mainmenu/dominik_menu.png"
    add "images/gui/mainmenu/sylios_menu.png"
    add "images/gui/mainmenu/boxes.png"
    add "images/gui/mainmenu/monster.png"
    #add "hairmenu"
    add "images/gui/mainmenu/frankiggs.png"
    imagebutton auto "images/gui/mainmenu/start_%s.png" xpos -50 ypos 193 focus_mask True action [Play("sound", "music/chime11.ogg"), Start()] at menubuttonmove
    imagebutton auto "images/gui/mainmenu/extras_%s.png" xpos 1201 ypos 193 focus_mask True action ShowMenu("extrasmain") at menubuttonmove2
    imagebutton auto "images/gui/mainmenu/load_%s.png" xpos -50 ypos 343 focus_mask True action ShowMenu("load") at menubuttonmove
    imagebutton auto "images/gui/mainmenu/help_%s.png" xpos 1201 ypos 343 focus_mask True action Help() at menubuttonmove2
    imagebutton auto "images/gui/mainmenu/prefs_%s.png" xpos -50 ypos 493 focus_mask True action ShowMenu("preferences") at menubuttonmove
    imagebutton auto "images/gui/mainmenu/quit_%s.png" xpos 1201 ypos 493 focus_mask True action Quit() at menubuttonmove2
    add "images/gui/mainmenu/logo.png" at logomovein


    # The background of the main menu.
#    window:
#        style "mm_root"

#    # The main menu buttons.
#    frame:
#        style_group "mm"
#        xalign .98
#        yalign .98

#        has vbox

#        textbutton _("Start Game") action Start()
#        textbutton _("Load Game") action ShowMenu("load")
#        textbutton _("Preferences") action ShowMenu("preferences")
#        textbutton _("Help") action Help()
#        textbutton _("Quit") action Quit(confirm=False)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"
#    image demomenuback = im.Composite(
#        (2732, 768),
#        (0, 0), "images/gui/demomenuback.png",
#        (1366, 0), "images/gui/demomenuback.png")
    transform demomenubackgroundanimation:
        ypos 0
        xpos 0
        linear 25 xpos -1366
        repeat
    transform menubuttonmove:
        on appear:
            xpos -100
            easein 0.5 xpos -50
        on hover:
            xpos -50
            easein 0.5 xpos -60
            easein 0.3 xpos -10
        on idle:
            xpos -10
            easein 0.3 xpos 0
            easein 0.5 xpos -50
    transform menubuttonmove2:
        on hover:
            xpos 1201
            easein 0.5 xpos 1209
            easein 0.3 xpos 1169
        on idle:
            xpos 1169
            easein 0.3 xpos 1159
            easein 0.5 xpos 1201    
    transform logomovein:
        parallel:
            alpha 0.0
            linear 1 alpha 1.0
        parallel:
            ypos -200
            easein 0.8 ypos 0
    transform extramainmove1:
        parallel:
            alpha 0.0
            linear 0.3 alpha 0.0
            linear 1.5 alpha 1.0
        parallel: 
            ypos 700
            easein 0.6 ypos -50
            easein 0.2 ypos 0
    transform extramainmove2:
            ypos -768
            easein 0.3 ypos 50
            easein 0.2 ypos 0
    transform extrabuttonfadein:
        alpha 0.0
        linear 0.7 alpha 0.0
        linear 0.5 alpha 1.0
    transform animesparklefadein:
        alpha 0.0
        pause 2.0
        linear 1.5 alpha 1.0
    transform titlemovein:
        parallel:
            alpha 0.0
            linear 0.3 alpha 1.0
        parallel:
            ypos -100
            easein 0.5 ypos 15
            easein 0.3 ypos 0
    transform menubuttonmovein1:
        parallel:
            alpha 0.0
            pause 0.8
            linear 1.0 alpha 1.0
        parallel:
            pause 0.8
            xpos -120
            easein 1.5  xpos 0
    transform menubuttonmovein2:
        parallel:
            alpha 0.0
            pause 0.8
            linear 1.5 alpha 1.0
        parallel:
            pause 1.0
            xpos 120
            easein 1.5  xpos 0
    image animesparkles:
        "images/gui/extrasfull/main/anime1.png"
        pause 0.7
        "images/gui/extrasfull/main/anime2.png"
        pause 0.7
        repeat
    $ show_elvine = True
    $ show_ma = False
    $ show_threads = False
    
    ##styles###
    style authornotesstyleheader:
        font "fonts/RIKY2VAMP.ttf"
        size 40
        xalign 0.5
        #color "#eccaf4"
    
    style authornotesstyle:
        font "fonts/goudy_bookletter_1911.otf"
        size 30
        color "#13060d" 
        outlines [(2, "#D6F4D6")]
        #text_align 0.5

##############################################################################
# Extras screen #

screen extrasmain():
    tag menu 
    add "images/gui/demomenuback2.png" at demomenubackgroundanimation
    add "images/gui/mainmenu/endlessbackoverlay.png"
    add "images/gui/extrasfull/main/back1.png" at extramainmove1
    add "images/gui/extrasfull/main/back2.png" at extramainmove2
    add "images/gui/extrasfull/main/title.png" at titlemovein
    imagebutton auto "images/gui/extrasfull/main/credits_%s.png" xpos 0 ypos 0 focus_mask True action ShowMenu("main_menu") at menubuttonmovein1
    imagebutton auto "images/gui/extrasfull/main/authornotes_%s.png" xpos 0 ypos 0 focus_mask True action ShowMenu("authorsnotes") at menubuttonmovein1
    imagebutton auto "images/gui/extrasfull/main/cgs_%s.png" xpos 0 ypos 0 focus_mask True at menubuttonmovein2
    imagebutton auto "images/gui/extrasfull/main/othergames_%s.png" xpos 0 ypos 0 focus_mask True action [ShowMenu("OtherGames"), SetVariable("show_elvine", True)] at menubuttonmovein2
    imagebutton auto "images/gui/extrasfull/main/return_%s.png" xpos 0 ypos 0 focus_mask True at extrabuttonfadein action ShowMenu("main_menu")
    add "animesparkles" at animesparklefadein

screen authorsnotes():
    tag menu
    add "images/gui/demomenuback2.png" at demomenubackgroundanimation
    add "images/gui/mainmenu/endlessbackoverlay.png"
    add "images/gui/extrasfull/othergames/base.png"
    vbox:
        style "authornotesstyle"
    frame:
        background None
        bottom_margin 100
        right_margin 174
        side "c r":
            area (149, 163, 1057, 536)
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            has vbox
            text _(
            "Wow! I can't believe you've made it this far! \n"
            "\n"
            "Like, how long did it take you to finish this?\n" "\n"
            "For me personally, it took me a really damn long time;;\n" "\n"
            "A year!\n" "\n"
            "Yikes!\n" "\n"
            "This is a really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really long line."
            "\n"
            ) text_align 0.5
            
            text _(
            "{font=fonts/RIKY2VAMP.ttf}{color=#eccaf4}Dr. Frank{/color}{/font}"
            ) text_align 0.3 size 60
            
            text _(
            "\n"
            "Uhhh is this working??"
            ) text_align 0.5 style "authornotesstyle"
            
            add "authornotes1":
                zoom 0.2
            
            text _(
            "\n"
            "Uhhh is this working??"
            ) text_align 0.5 style "authornotesstyle"
            
            text _(
            "Wow! I can't believe you've made it this far! \n"
            "\n"
            "Like, how long did it take you to finish this?\n" "\n"
            "For me personally, it took me a really damn long time;;\n" "\n"
            "A year!\n" "\n"
            "Yikes!\n" "\n"
            "This is a really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really long line."
            "\n"
            ) text_align 0.5
        xpos 160
        ypos 168
        xsize 1192
        ysize 620
    add "images/gui/extrasfull/authornotes/title.png"
    imagebutton auto "images/gui/extrasfull/othergames/extras_%s.png" xpos 0 ypos 0 focus_mask True action ShowMenu("extrasmain")
    imagebutton auto "images/gui/extrasfull/othergames/mainmenu_%s.png" xpos 0 ypos 0 focus_mask True action ShowMenu("main_menu")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""

#style about_label is gui_label
#style about_label_text is authornotesstyleheader
#style about_text is gui_text

#style about_label_text:
#    size gui.label_text_size

    


screen OtherGames:
    tag menu
    add "images/gui/demomenuback2.png" at demomenubackgroundanimation
    add "images/gui/mainmenu/endlessbackoverlay.png"
    add "images/gui/extrasfull/othergames/base.png"
    if show_elvine:
        add "images/gui/extrasfull/othergames/elvine.png"
        imagebutton auto "images/gui/extrasfull/othergames/elvinelink_%s.png" xpos 0 ypos 0 focus_mask True action OpenURL("https://lemmasoft.renai.us/forums/viewtopic.php?f=11&t=21419") # at othergameslidein
    if show_ma:
        add "images/gui/extrasfull/othergames/ma.png"
        imagebutton auto "images/gui/extrasfull/othergames/malink_%s.png" xpos 0 ypos 0 focus_mask True action OpenURL("https://lemmasoft.renai.us/forums/viewtopic.php?f=43&t=29838")
    if show_threads:
        add "images/gui/extrasfull/othergames/lifethreads.png"
        imagebutton auto "images/gui/extrasfull/othergames/lifethreadslink_%s.png" xpos 0 ypos 0 focus_mask True action OpenURL("http://cloudnovel.net/play?n=a4eac1c1937")
    add "images/gui/extrasfull/othergames/triangle.png"
    add "images/gui/extrasfull/othergames/othergamestitle.png"
    imagebutton auto "images/gui/extrasfull/othergames/elvinegame_%s.png" xpos 0 ypos 0 focus_mask True action [SetVariable("show_elvine", True), SetVariable("show_threads", False), SetVariable("show_ma", False)]
    imagebutton auto "images/gui/extrasfull/othergames/magame_%s.png" xpos 0 ypos 0 focus_mask True action [SetVariable("show_elvine", False), SetVariable("show_threads", False), SetVariable("show_ma", True)]
    imagebutton auto "images/gui/extrasfull/othergames/lifethreadsgame_%s.png" xpos 0 ypos 0 focus_mask True action [SetVariable("show_elvine", False), SetVariable("show_threads", True), SetVariable("show_ma", False)]
    add "images/gui/extrasfull/othergames/collabs.png"
    imagebutton auto "images/gui/extrasfull/othergames/helena_%s.png" xpos 0 ypos 0 focus_mask True action OpenURL("https://heiden.itch.io/helenas-flowers")
    imagebutton auto "images/gui/extrasfull/othergames/beyond_%s.png" xpos 0 ypos 0 focus_mask True action OpenURL("https://godline.itch.io/beyond")
    imagebutton auto "images/gui/extrasfull/othergames/extras_%s.png" xpos 0 ypos 0 focus_mask True action ShowMenu("extrasmain")
    imagebutton auto "images/gui/extrasfull/othergames/mainmenu_%s.png" xpos 0 ypos 0 focus_mask True action ShowMenu("main_menu")
    ##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():
    #add gravetop (0, 0)

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()
    #add gravetop (0, 0)
init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.
screen load_save_slot:
    $ file_name = FileSlotName(number,3)
    $ file_time = FileTime(number, empty=_("Empty Slot."))
    text file_time xalign 0.5 ypos 200 size 30 color "eccaf4" font "fonts/RIKY2VAMP.ttf" outlines [ (2, "3d4b44") ]
    text file_name xalign 0.5 ypos 150 size 50 color "eccaf4" font "fonts/RIKY2VAMP.ttf" outlines [ (2, "3d4b44") ]
    add FileScreenshot(number) xpos -20 ypos -5

screen file_picker():
    imagemap:
        auto "images/gui/load/filepicker_%s.png"
        hotspot (240,543,26,59) clicked FilePage(1)
        hotspot (279,541,45,62) clicked FilePage(2)
        hotspot (1106,543,64,64) clicked FilePage(3)
        hotspot (1184,546,62,68) clicked FilePage(4)
        hotspot (274,252,239,242) clicked FileAction(1):
            use load_save_slot(number=1)
        hotspot (613,252,239,242) clicked FileAction(2):
            use load_save_slot(number=2)
        hotspot (952,252,239,242) clicked FileAction(3):
            use load_save_slot(number=3)

screen save():

    # This ensures that any other menu screen is replaced.
    add "images/gui/save/base.png"
    add "images/gui/load/lines.png"
    imagebutton auto "images/gui/load/return_%s.png" focus_mask True action [Return(), Hide("save")]
    imagebutton auto "images/gui/save/load_%s.png" focus_mask True action [ShowMenu("load"), Hide("save")]
    imagebutton auto "images/gui/load/prefs_%s.png" focus_mask True action [ShowMenu("preferences"), Hide("save")]
    use file_picker
    #use navigation
    #use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    add "images/gui/load/base.png"
    add "images/gui/load/lines.png"
    imagebutton auto "images/gui/load/return_%s.png" focus_mask True action [Return(), Hide("load")]
    imagebutton auto "images/gui/load/save_%s.png" focus_mask True action [ShowMenu("save"), Hide("load")]
    imagebutton auto "images/gui/load/prefs_%s.png" focus_mask True action [ShowMenu("preferences"), Hide("load")]
    #use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text

init -2 python:
    
    config.thumbnail_width = 273.2
    config.thumbnail_height = 153.6


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    # Include the navigation.
    #use navigation
    add "images/gui/prefs/base.png"
    imagemap:
        auto "images/gui/prefs/options_%s.png"
        alpha False
    
        hotspot (652, 198, 155, 55) action Preference ("display", "window")
        hotspot (929, 203, 198, 55) action Preference ("display", "fullscreen")
        hotspot (604, 273, 237, 53) action Preference ("skip", "all")
        hotspot (903, 270, 250, 53) action Preference ("skip", "seen")
        hotspot (644, 350, 169, 53) action Preference ("transitions", "all")
        hotspot (925, 352, 203, 49) action Preference ("transitions", "none")
        hotspot (599, 434, 247, 53) action Preference ("after choices", "skip")
        hotspot (907, 430, 230, 57) action Preference("after choices", "stop")
        bar pos(640, 510) value MixerValue('sfx') style "pref_slider"
        bar pos(640, 575) value MixerValue('music') style "pref_slider"
    
    imagebutton auto "images/gui/prefs/load_%s.png" focus_mask True action [ShowMenu("load"), Hide("preferences")]
    imagebutton auto "images/gui/prefs/save_%s.png" focus_mask True action [ShowMenu("save"), Hide("preferences")]
    imagebutton auto "images/gui/prefs/menu_%s.png" focus_mask True action [MainMenu (), Hide("preferences")]
    imagebutton auto "images/gui/prefs/return_%s.png" focus_mask True action [Return(), Hide("preferences")]
    
init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        left_bar "images/gui/prefs/bar_full.png"
        right_bar "images/gui/prefs/bar_empty.png"
        thumb "images/gui/prefs/thumb.png"
        xmaximum 502
        ymaximum 47
        

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
#    hbox:
#        style_group "quick"

#        xalign 1.0
#        yalign 1.0

#        textbutton _("Back") action Rollback()
#        textbutton _("Save") action ShowMenu('save')
#        textbutton _("Q.Save") action QuickSave()
#        textbutton _("Q.Load") action QuickLoad()
#        textbutton _("Skip") action Skip()
#        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
#        textbutton _("Auto") action Preference("auto-forward", "toggle")
#        textbutton _("Prefs") action ShowMenu('preferences')
    $ x = 1040
    imagebutton auto "images/gui/textbox/back_%s.png" xpos x ypos 715 focus_mask True action Rollback() at gravemove
    $ x += 40
    imagebutton auto "images/gui/textbox/save_%s.png" xpos x ypos 710 focus_mask True action ShowMenu('save') at gravemove2
    $ x += 40
    imagebutton auto "images/gui/textbox/qsave_%s.png" xpos x ypos 720 focus_mask True action QuickSave() at gravemove3 
    $ x += 40
    imagebutton auto "images/gui/textbox/qload_%s.png" xpos x ypos 715 focus_mask True action QuickLoad() at gravemove 
    $ x += 40
    imagebutton auto "images/gui/textbox/skip_%s.png" xpos x ypos 710 focus_mask True action Skip() at gravemove2
    $ x += 40
    imagebutton auto "images/gui/textbox/fskip_%s.png" xpos x ypos 720 focus_mask True action Skip(fast=True, confirm=True) at gravemove3
    $ x += 40
    imagebutton auto "images/gui/textbox/auto_%s.png" xpos x ypos 715 focus_mask True action Preference("auto-forward", "toggle") at gravemove 
    $ x += 40
    imagebutton auto "images/gui/textbox/prefs_%s.png" xpos x ypos 710 focus_mask True action ShowMenu('preferences') at gravemove2
    add "gravetop"

##############################################################################
#### CREDITS ######
screen creditscreen():
    tag menu
    add "images/gui/extras/fences.png" at fadeinmenu
    add "images/gui/extras/creditswords.png" at fadeinmenu
    imagebutton auto "images/gui/extras/return_%s.png" focus_mask True action Return() at fadeinmenu
    imagebutton auto "images/gui/extras/guestartbutton_%s.png" focus_mask True action[Hide ("creditscreen"), Show ("guestartscreen")] at fadeinmenu
    imagebutton auto "images/gui/extras/dontclick_%s.png" focus_mask True action[Play("sound", "music/fart.ogg")] at fadeinmenu
        
screen guestartscreen():
    tag menu
    add "images/gui/extras/fences.png" at fadeinmenu
    add "images/gui/extras/guestartwords.png" at fadeinmenu
    imagebutton auto "images/gui/extras/return_%s.png" focus_mask True action Return() at fadeinmenu
    imagebutton auto "images/gui/extras/creditsbutton_%s.png" focus_mask True action[Hide ("guestartscreen"), Show("creditscreen")] at fadeinmenu
    imagebutton auto "images/gui/extras/dontclick_%s.png" focus_mask True action[Play("sound", "music/fart.ogg")] at fadeinmenu
    imagebutton auto "images/gui/extras/amiralolink_%s.png" focus_mask True action[OpenURL("http://amiralo.deviantart.com/")]
    imagebutton auto "images/gui/extras/kyolink_%s.png" focus_mask True action[OpenURL("http://kyokyo866.deviantart.com/")]

## ■██▓▒░ CUSTOM SOUND CHANNEL ░▒▓██████████████████████████■
# This is the block where we declare the individual sound channels. This enables us to play several sound FX's without overlapping
init python:
    renpy.music.register_channel("doublemusic", "music", False)
    renpy.music.register_channel("doublesound", "sound", False)
    renpy.music.register_channel("triplesound", "sound", False)

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"
        
    transform gravemove:
        on idle:
            easein 0.5 yoffset 0
        on hover:
            parallel:
                easein 0.5 yoffset -92
            parallel:
                easein 0.1 xoffset -2
                easein 0.1 xoffset 2
                easein 0.1 xoffset -2
                easein 0.1 xoffset 2
                easein 0.1 xoffset 0
    transform gravemove2:
        on idle:
            easein 0.5 yoffset 0
        on hover:
            parallel:
                easein 0.5 yoffset -89
            parallel:
                easein 0.1 xoffset -2
                easein 0.1 xoffset 2
                easein 0.1 xoffset -2
                easein 0.1 xoffset 2
                easein 0.1 xoffset 0
    transform gravemove3:
        on idle:
            easein 0.5 yoffset 0
        on hover:
            parallel:
                easein 0.5 yoffset -100
            parallel:
                easein 0.1 xoffset -2
                easein 0.1 xoffset 2
                easein 0.1 xoffset -2
                easein 0.1 xoffset 2
                easein 0.1 xoffset 0
                
    transform fadeinmenu:
        alpha 0.0
        linear 1.5 alpha 1.0
        

