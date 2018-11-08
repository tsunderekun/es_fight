init:
    $ mods["prep"]=u"ES Battle Game"
    $ mob_sec = 1
    $ style.esrpg_butt = Style(style.default)
    $ style.esrpg_butt.hover_color = (255, 255, 255)
    $ style.esrpg_butt.color = (80, 0, 0)
    $ style.esrpg_butt.outlines = [ (absolute(2), "#FFF", absolute(0), absolute(0)) ]
    $ style.esrpg_butt.size = 55
    $ style.esrpg_butt.font = "battle_f.ttf"
    $ style.esrpg_butt.text_align = 0.5

    image win text = Text('You win!', style = 'esrpg_butt')
    image lose text = Text('You lose!', style = 'esrpg_butt')

    transform textrp:
        easeout_back .25 zoom 0.1
        easein_back .50 zoom 1
        easeout_back .75 zoom 2
        1.0
        easein_back .25 zoom 0


    transform esrpg_butt_t():
        on idle:
            easeout_back 0.25 zoom 1.0
        on hover:
            easein_back 0.25 zoom 1.25
        on update:
            easeout_back 0.25 zoom 1.0

    transform punch_1:
        choice:
            easeout 0.5 zoom 0.8
            easein 0.5 zoom 1.0
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5
        choice:
            easeout 0.5 xpos 0.8
            easein 0.5 xpos 0.5
            easeout 0.5 zoom 0.9
            easein 0.5 zoom 1.0
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5
        choice:
            easeout 0.5 xpos 0.1
            easein 0.5 xpos 0.5
            easeout 0.5 zoom 0.7
            easein 0.5 zoom 1.0
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5

    transform punch_2:
        choice:
            easeout 0.5 zoom 0.9
            easein 0.5 zoom 1.0
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5
        choice:
            easeout 0.5 zoom 0.7
            easein 0.5 zoom 1.0
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5

    transform punch_me:
        choice:
            easeout 0.5 zoom 1.2
            easein 0.5 zoom 1.0
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5

        choice:
            easeout 0.5 zoom 1.2
            easein 0.5 zoom 1.0
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5

    transform punch_me_bg:
        choice:
            easeout 0.5 zoom 1.2
            easeout 0.5 rotate 30
            easein 0.5 zoom 1.0
            easein 0.1 rotate 0
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5
        choice:
            easeout 0.5 zoom 1.2
            easeout 0.5 rotate 15
            easein 0.5 zoom 1.0
            easein 0.1 rotate 0
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5

    transform punch_bg:
        choice:
            easeout 0.5 zoom 1.5
            easein 0.5 zoom 1.0
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5
            easein 0.1 rotate 0
        choice:
            easeout 0.5 zoom 1.5
            easein 0.5 zoom 1.0
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5
            easein 0.1 rotate 0

    transform punch_bg_def:
        choice:
            easeout 0.5 zoom 1.1
            easeout 0.5 xpos 0.6
            easein 0.5 zoom 1.0
            easein 0.5 xpos 0.5
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5
            easein 0.1 rotate 0
        choice:
            easeout 0.5 zoom 1.2
            easeout 0.5 xpos 0.4
            easein 0.5 zoom 1.0
            easein 0.5 xpos 0.5
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5
            easein 0.1 rotate 0
    transform punch_win:
        easein 2 ypos 0.9
        easein 0.75 rotate 5
        easein 0.75 rotate -5
        easein 0.75 rotate 15
        easein 0.75 rotate -15
        easein 0.75 rotate 90
        1.0
        easein 0.75 ypos 0.99

    transform punch_lose:
        easeout 0.5 zoom 2
        easein 2 ypos 0.8
        easein 0.75 rotate 5
        easein 0.75 rotate -5
        easein 0.75 rotate 15
        easein 0.75 rotate -15
        easein 0.75 rotate 90
        1.0
        easein 0.75 ypos 0.99



init python:

    hero_hmax = 100
    hero_h = 100
    mob_hmax = 100
    mob_h = 100
    hero_state = True
    mob_life = True
    haction = "Nothing"

    def pnch(hero_state):
        mob_sec = renpy.random.randint (1, 3)
        global mob_sec
        hero_bonus = renpy.random.randint (1, 2)
        hero_pow = renpy.random.randint (5, 10) * hero_bonus
        defrand = renpy.random.randint (1, 2)
        if defrand == 1:
            global mob_h
            mob_h -= hero_pow
            haction = "I pwnd " + mob_nmn + ", and it lost " + str(hero_pow) + " HP"
            global haction
            renpy.play('PUNCH.mp3', channel = 'sound')
            renpy.show(mob_name, [punch_1])
            renpy.show(randbg, [punch_bg])
            renpy.jump('check')

        else:
            global mob_h
            mob_h -= 0
            haction = "I pwnd " + mob_nmn + ", and it lost  0  HP"
            global haction
            renpy.play('PUNCH.mp3', channel = 'sound')
            renpy.show(mob_name, [punch_2])
            renpy.show(randbg, [punch_bg])
            renpy.jump('check')


    def defn(hero_state):
        mob_sec = renpy.random.randint (1, 3)
        global mob_sec
        mob_pow = (renpy.random.randint (0, 4) * renpy.random.randint (1, 3))
        defrand = renpy.random.randint (1, 2)
        if defrand == 2:
            global hero_h
            hero_h -= mob_pow
            haction = "Defended, but i lost " + str(mob_pow) + " HP"
            global haction
            renpy.play('defend.mp3', channel = 'sound')
            renpy.show(mob_name, [punch_me])
            renpy.show(randbg, [punch_bg_def])
            renpy.jump('check')
        else:
            global hero_h
            hero_h -= 0
            haction = "Defended."
            global haction
            renpy.play('defend.mp3', channel = 'sound')
            renpy.show(randbg, [punch_bg_def])
            renpy.jump('check')


    def noth(hero_state):
        mob_sec = renpy.random.randint (1, 3)
        global mob_sec
        mob_pow = (renpy.random.randint (0, 20) * renpy.random.randint (1, 3))
        defrand = renpy.random.randint (1, 2)
        if defrand == 2:
            global hero_h
            hero_h -= mob_pow
            haction = "I lost " + str(mob_pow) + " HP"
            global haction
            renpy.play('attack.mp3', channel = 'sound')
            renpy.show(mob_name, [punch_me])
            renpy.show(randbg, [punch_me_bg])
            renpy.jump('check')
        else:
            global hero_h
            hero_h -= 0
            haction = "I lost  0  HP"
            global haction
            renpy.play('attack.mp3', channel = 'sound')
            renpy.show(mob_name, [punch_me])
            renpy.show(randbg, [punch_me_bg])
            renpy.jump('check')

    def heal(hero_state):
        mob_sec = renpy.random.randint (1, 3)
        global mob_sec
        defrand = renpy.random.randint (1, 2)
        if defrand == 2:
            global hero_h
            healed_h = (renpy.random.randint (0, 10))
            hero_h = hero_h + healed_h
            haction = "I healed " + str(healed_h) + " HP"
            global haction
            renpy.play('defend.mp3', channel = 'sound')
            renpy.show(mob_name, [punch_me])
            renpy.show(randbg, [punch_me_bg])
            renpy.jump('check')
        else:
            global hero_h
            global mob_h
            healed_h = (renpy.random.randint (0, 2))
            healed_m = (renpy.random.randint (0, 25))
            hero_h = hero_h + healed_h
            mob_h += healed_m
            haction = "I healed " + str(healed_h) + " HP"
            global haction
            renpy.play('defend.mp3', channel = 'sound')
            renpy.show(mob_name, [punch_me])
            renpy.show(randbg, [punch_me_bg])
            renpy.jump('check')


    def runaway():
        renpy.return_statement()


label prep:
    $mob_sec = renpy.random.randint (1, 3)
    $hero_hmax = 100
    $hero_h = 100
    $mob_hmax = 100
    $mob_h = 100
    $hero_state = True
    $mob_life = True
    $mob_name = 'pi normal'
    scene anim prolog_1 with dspr
    menu:
        "{b}Choose a enemy:{/b}"
        "Пионер":
            $mob_name = 'pi normal'
            $mob_nmn = 'Пионер'
        "Алиса":
            $mob_name = 'dv rage pioneer far'
            $mob_nmn = 'Алиса'
        "Славя":
            $mob_name = 'sl angry pioneer far'
            $mob_nmn = 'Славя'
        "Лена":
            $mob_name = 'un rage pioneer far'
            $mob_nmn = 'Лена'
        "Мику":
            $mob_name = 'mi rage pioneer far'
            $mob_nmn = 'Мику'
        "Шурик":
            $mob_name = 'sh rage pioneer far'
            $mob_nmn = 'Шурик'
    $ randscene = renpy.random.randint (0, 2)
    if randscene == 0:
        $day_time()
        $persistent.sprite_time = "day"
        show bg ext_square_day with dissolve
        $randbg = "bg ext_square_day"
    if randscene == 1:
        $sunset_time()
        $persistent.sprite_time = "sunset"
        show bg ext_polyana_sunset with dissolve
        $randbg = "bg ext_polyana_sunset"
    if randscene == 2:
        $night_time()
        $persistent.sprite_time = "night"
        show bg int_mine_room with dissolve
        $randbg = "bg int_mine_room"

    $ renpy.show(mob_name, [center])
    $ renpy.with_statement(dspr, always=False)
    $ randmus = renpy.random.choice([music_list["doomed_to_be_defeated"], music_list["awakening_power"] , music_list["scarytale"]])
    play music randmus
    jump prep_1


label prep_1:
    window hide
    jump check
    call screen bat_gui(hero_state) with dspr


label check:

    python:
        renpy.hide_screen("bat_gui")
        if hero_h <= 0:
            hero_state = False
        if hero_h > 0:
            hero_state = True
        if hero_state == False:
            renpy.play('lose.mp3', channel = 'sound')
            renpy.music.stop(channel='music', fadeout=2)
            renpy.show('lose text', [truecenter, textrp])
            renpy.show(randbg, [punch_lose])
            renpy.show(mob_name, [punch_lose])
            renpy.pause(10, hard = True)
            renpy.hide(mob_name)
            renpy.hide(randbg)
            renpy.show('anim prolog_1')
            renpy.with_statement(dissolve2, always=False)
            renpy.jump('prep')
        if mob_h <= 0:
            mob_life = False
            renpy.play('win.mp3', channel = 'sound')
            renpy.music.stop(channel='music', fadeout=2)
            renpy.show('win text', [truecenter, textrp])
            renpy.show(mob_name, [punch_win])
            renpy.pause(10, hard = True)
            renpy.hide(mob_name)
            renpy.show('anim prolog_1')
            renpy.with_statement(dissolve2, always=False)
            renpy.jump('prep')
        if hero_h > 101:
            renpy.play('lose.mp3', channel = 'sound')
            renpy.music.stop(channel='music', fadeout=2)
            renpy.show('lose text', [truecenter, textrp])
            renpy.show(randbg, [punch_lose])
            renpy.show(mob_name, [punch_lose])
            renpy.pause(10, hard = True)
            renpy.hide(randbg)
            renpy.hide(mob_name)
            renpy.show('anim prolog_1')
            renpy.with_statement(dissolve2, always=False)
            renpy.jump('prep')
        else:
            renpy.call_screen("bat_gui", hero_state)

    # "hero_state = [hero_state] \n mob_h = [mob_h] \n mob_life = [mob_life] "

screen bat_gui(hero_state):
    modal False
    frame:
        background Frame("frame.png", 40, 40, 40, 40)

        xpadding 10
        ypadding 10
        xfill
        xalign 0.5
        ypos 0.025

        hbox xalign 0.5 ypos 0.1:

            hbox:

                text "My HP:":
                    style "esrpg_butt"
                null width 10
                text "[hero_h]/[hero_hmax] HP" at esrpg_butt_t:
                    style "esrpg_butt"
            null width 25
            hbox:
                text "[mob_nmn]'s HP:":
                    style "esrpg_butt"
                null width 10
                text "[mob_h]/[mob_hmax] HP" at esrpg_butt_t:
                    style "esrpg_butt"
    frame:
        background Frame("frame.png", 40, 40, 40, 40)
        xpadding 10
        ypadding 10
        xfill
        xalign 0.5
        ypos .80
        vbox:
            hbox:

                textbutton "Punch" action [Function(renpy.hide_screen, 'bat_gui'), Function(pnch, hero_state)] at esrpg_butt_t:
                    style "esrpg_butt"
                    text_style "esrpg_butt"

                null width 25

                textbutton "Defend" action [Function(renpy.hide_screen, 'bat_gui'), Function(defn, hero_state)] at esrpg_butt_t:
                    style "esrpg_butt"
                    text_style "esrpg_butt"

                null width 25

                textbutton "Nothing" action [Function(renpy.hide_screen, 'bat_gui'),Function(noth, hero_state)] at esrpg_butt_t:
                    style "esrpg_butt"
                    text_style "esrpg_butt"

                null width 25

                textbutton "Heal" action Function(heal, hero_state) at esrpg_butt_t:
                    style "esrpg_butt"
                    text_style "esrpg_butt"

                null width 25

                textbutton "Run Away" action Function(runaway) at esrpg_butt_t:
                    style "esrpg_butt"
                    text_style "esrpg_butt"

                null width 25

            text '\"[haction]\"' text_align 0.5 :
                style "esrpg_butt"

    timer mob_sec action Function(noth, hero_state)
