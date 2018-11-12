init:
    $ mods["rpgdsc"]=u"{font=battle_f.ttf}Файтинг для Летонька{/font}"

    $ mob_sec = 1

    $ style.esrpg_butt = Style(style.default)
    $ style.esrpg_butt.hover_color = (255, 255, 255)
    $ style.esrpg_butt.color = (25, 25, 112)
    $ style.esrpg_butt.outlines = [ (absolute(2), "#FFF", absolute(0), absolute(0)) ]
    $ style.esrpg_butt.size = 55
    $ style.esrpg_butt.font = "battle_f.ttf"
    $ style.esrpg_butt.text_align = 0.5

    $ style.esrpg_green = Style(style.esrpg_butt)
    $ style.esrpg_green.color = (0, 80, 0)
    $ style.esrpg_green.size = 48

    $ style.esrpg_greeni = Style(style.esrpg_green)
    $ style.esrpg_greeni.size = 128

    $ style.esrpg_greeny = Style(style.esrpg_greeni)
    $ style.esrpg_greeny.size = 32

    $ style.esrpg_un = Style(style.esrpg_butt)
    $ style.esrpg_un.color = (50, 50, 50)


    $ healed_h = ''
    $ if_heal = ''

    image prg_tolyan = 'tolyan.png'
    image win text = Text('Ты победил!', style = 'esrpg_butt')
    image lose text = Text('Ты проиграл..', style = 'esrpg_butt')
    image heal text = Text('Восстановлено ' + str(healed_h) + 'HP', style = 'esrpg_green')
    image dsc text = Text('Внимание! \n Данный мод не преследует цели унизить чью-нибудь вайфу, \n а также не призывает к насилию в реальной жизни. \n \n \n \n \n \n \n \n Я вас предупредил и теперь удаляюсь... \n Приятной игры!', style = 'esrpg_green')

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
            easeout 0.5 zoom 1.2
            easein 0.5 zoom 1.0
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5
        choice:
            easeout 0.5 xpos 1.1
            easein 0.5 xpos 0.5
            easeout 0.5 zoom 0.9
            easein 0.5 zoom 1.0
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5
        choice:
            easeout 0.5 xpos 1.2
            easein 0.5 xpos 0.5
            easeout 0.5 zoom 0.7
            easein 0.5 zoom 1.0
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5

    transform punch_2:
        choice:
            easeout 0.5 zoom 1.2
            easein 0.5 zoom 1.0
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5
        choice:
            easeout 0.5 zoom 1.4
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
        easein 0.5 zoom 1.0
        easein 0.1 xalign 0.5
        easein 0.1 yalign 0.5
        easein 0.1 rotate 0
        easein 2 ypos 0.9
        easein 0.75 rotate 5
        easein 0.75 rotate -5
        easein 0.75 rotate 15
        easein 0.75 rotate -15
        easein 0.75 rotate 90
        1.0
        easein 0.75 ypos 0.99

    transform punch_lose:
        easein 0.5 zoom 1.0
        easein 0.1 xalign 0.5
        easein 0.1 yalign 0.5
        easein 0.1 rotate 0
        easeout 0.5 zoom 2
        easein 2 ypos 0.8
        easein 0.75 rotate 5
        easein 0.75 rotate -5
        easein 0.75 rotate 15
        easein 0.75 rotate -15
        easein 0.75 rotate 90
        1.0
        easein 0.75 ypos 0.1



init python:

    rpg_help = 0
    not_av = 0
    haction = ""
    if_heal = ''
    mob_sec = renpy.random.randint (1, 3)
    hero_hmax = 100
    hero_hmax = 101
    hero_h = 100
    hero_heal = 50
    mob_hmax = 100
    mob_h = 100
    hero_state = True
    mob_life = True
    mob_name = ''
    mob_mxp = 3
    mob_speed_min = 1
    mob_speed_max = 3


    def pnch(hero_state):
        if_heal = ''
        global if_heal
        mob_sec = renpy.random.randint (mob_speed_min, mob_speed_max)
        global mob_sec
        hero_bonus = renpy.random.randint (1, 2)
        hero_pow = renpy.random.randint (5, 10) * hero_bonus
        defrand = renpy.random.randint (1, 2)
        if defrand == 1:
            global mob_h
            mob_h -= hero_pow
            haction = "Я ударил противника " + mob_nmn + " и отнял " + str(hero_pow) + " HP"
            global haction
            renpy.play('PUNCH.mp3', channel = 'sound')
            renpy.show(mob_name, [punch_1])
            renpy.show(randbg, [punch_bg])
            renpy.jump('check')

        else:
            not_av = renpy.random.randint (0, 1)
            global not_av
            global mob_h
            mob_h -= 0
            haction = "Промазал"
            global haction
            renpy.play('PUNCH.mp3', channel = 'sound')
            renpy.show(mob_name, [punch_2])
            renpy.show(randbg, [punch_bg])
            renpy.jump('check')

    def defn(hero_state):
        not_av = 0
        global not_av
        if_heal = ''
        global if_heal
        mob_sec = renpy.random.randint (4, 10)
        global mob_sec
        mob_pow = (renpy.random.randint (0, 4) * renpy.random.randint (1, 3))
        defrand = renpy.random.randint (1, 2)
        if defrand == 2:
            global hero_h
            hero_h -= mob_pow
            haction = "Я уклонился, но потерял " + str(mob_pow) + " HP"
            global haction
            renpy.play('defend.mp3', channel = 'sound')
            renpy.show(mob_name, [punch_me])
            renpy.show(randbg, [punch_bg_def])
            renpy.jump('check')
        else:
            global hero_h
            hero_h -= 0
            haction = "Я уклонился"
            global haction
            renpy.play('defend.mp3', channel = 'sound')
            renpy.show(randbg, [punch_bg_def])
            renpy.jump('check')


    def noth(hero_state):
        if_heal = ''
        global if_heal
        mob_sec = renpy.random.randint (mob_speed_min, mob_speed_max)
        global mob_sec
        mob_pow = (renpy.random.randint (5, 10) * renpy.random.randint (1, mob_mxp))
        defrand = renpy.random.randint (1, 2)
        if defrand == 2:
            not_av = 1
            global hero_h
            hero_h -= mob_pow
            haction = "Я потерял " + str(mob_pow) + " HP"
            global haction
            renpy.play('attack.mp3', channel = 'sound')
            renpy.show(mob_name, [punch_me])
            renpy.show(randbg, [punch_me_bg])
            renpy.jump('check')
        else:
            global hero_h
            hero_h -= 0
            haction = "Я уклонился"
            global haction
            renpy.play('attack.mp3', channel = 'sound')
            renpy.show(mob_name, [punch_me])
            renpy.show(randbg, [punch_me_bg])
            renpy.jump('check')



    def heal(hero_state):
        if_heal = ''
        global if_heal
        mob_sec = renpy.random.randint (mob_speed_min, mob_speed_max)
        global mob_sec
        defrand = renpy.random.randint (1, 2)
        if defrand == 2:
            global hero_h
            healed_h = (renpy.random.randint (10, 30))
            hero_h = hero_h + healed_h
            global healed_h
            if_heal = "+" + str(healed_h) + " HP"
            global if_heal
            haction = "Я восстановил " + str(healed_h) + " HP"
            global haction
            renpy.play('defend.mp3', channel = 'sound')
            renpy.jump('check')
        else:
            global hero_h
            global mob_h
            healed_h = (renpy.random.randint (5, 15))
            healed_m = (renpy.random.randint (0, 10))
            hero_h = hero_h + healed_h
            global healed_h
            if_heal = "+" + str(healed_h) + " HP"
            global if_heal
            mob_h += healed_m
            haction = "Я восстановил " + str(healed_h) + " HP"
            global haction
            renpy.play('defend.mp3', channel = 'sound')
            renpy.jump('check')

    def runaway():
        renpy.jump('prep')

    def helpsme():
        if rpg_help == 0:
            rpg_help = 1
            global rpg_help
        else:
            rpg_help = 0
            global rpg_help
        renpy.jump('check')



label rpgdsc:
    play music music_list["into_the_unknown"] fadein 2
    show dsc text at truecenter with dissolve
    $ renpy.pause(5, hard = True)
    hide dsc text with dissolve
    jump prep




label prep:
    $rpg_help = 0
    $not_av = 0
    $haction = ""
    $if_heal = ''
    $mob_sec = renpy.random.randint (1, 3)
    $hero_hmax = 100
    $hero_hmax = 101
    $hero_h = 100
    $hero_heal = 50
    $mob_hmax = 100
    $mob_h = 100
    $hero_state = True
    $mob_life = True
    $mob_name = ''
    $mob_mxp = 3
    $mob_speed_min = 1
    $mob_speed_max = 3
    scene anim prolog_1 with dspr
    menu:
        "{size=40}{font=battle_f.ttf}{b}Выбери кол-во здоровья:{/b}{/font}"
        "{font=battle_f.ttf}Легкий{/font}":
            $hero_hmax = 200
            $hero_hmaxi = 201
            $hero_h = 200
            $hero_heal = 100
        "{font=battle_f.ttf}Средний{/font}":
            $hero_hmax = 100
            $hero_hmaxi = 101
            $hero_h = 100
            $hero_heal = 50
        "{font=battle_f.ttf}Сложный{/font}":
            $hero_hmax = 75
            $hero_hmaxi = 76
            $hero_h = 75
            $hero_heal = 25
        "{font=battle_f.ttf}{color=#f00}Даже не пытайся{/color}{/font}":
            $hero_hmax = 50
            $hero_hmaxi = 51
            $hero_h = 50
            $hero_heal = 25
    menu:
        "{size=40}{font=battle_f.ttf}{b}Выбери противника:{/b}{/font}"
        "{size=40}{font=battle_f.ttf}{b}Легкие:{/b}{/font}{/size}"
        "{font=battle_f.ttf}Ульяна{/font}":
            $mob_name = 'us angry pioneer far'
            $mob_nmn = 'Ульяна'
            $mob_hmax = 50
            $mob_h = 50
            $mob_speed_min = 1
            $mob_speed_max = 2
            $mob_mxp = 2
        "{font=battle_f.ttf}Женя{/font}":
            $mob_name = 'mz rage pioneer far'
            $mob_nmn = 'Женя'
            $mob_hmax = 80
            $mob_h = 80
            $mob_speed_min = 2
            $mob_speed_max = 3
            $mob_mxp = 4
        "{font=battle_f.ttf}Юля{/font}":
            $mob_name = 'uv rage far'
            $mob_nmn = 'Юля'
            $mob_hmax = 85
            $mob_h = 85
            $mob_speed_min = 1
            $mob_speed_max = 2
            $mob_mxp = 5
        "{font=battle_f.ttf}Электроник{/font}":
            $mob_name = 'el angry pioneer far'
            $mob_nmn = 'Электроник'
            $mob_hmax = 90
            $mob_h = 90
            $mob_speed_min = 1
            $mob_speed_max = 4
            $mob_mxp = 3
        "{size=40}{font=battle_f.ttf}{b}Средние:{/b}{/font}{/size}"
        "{font=battle_f.ttf}Мику{/font}":
            $mob_name = 'mi rage pioneer far'
            $mob_nmn = 'Мику'
            $mob_hmax = 95
            $mob_h = 95
            $mob_speed_min = 1
            $mob_speed_max = 2
            $mob_mxp = 6
        "{font=battle_f.ttf}Пионер{/font}":
            $mob_name = 'pi normal'
            $mob_nmn = 'Пионер'
            $mob_hmax = 100
            $mob_h = 100
            $mob_speed_min = 1
            $mob_speed_max = 3
            $mob_mxp = 4
        "{font=battle_f.ttf}Шурик{/font}":
            $mob_name = 'sh rage pioneer far'
            $mob_nmn = 'Шурик'
            $mob_hmax = 110
            $mob_h = 110
            $mob_speed_min = 1
            $mob_speed_max = 2
            $mob_mxp = 6
        "{font=battle_f.ttf}Алиса{/font}":
            $mob_name = 'dv rage pioneer far'
            $mob_nmn = 'Алиса'
            $mob_hmax = 115
            $mob_h = 115
            $mob_speed_min = 1
            $mob_speed_max = 2
            $mob_mxp = 7
        "{font=battle_f.ttf}Лена{/font}":
            $mob_name = 'un rage pioneer far'
            $mob_nmn = 'Лена'
            $mob_hmax = 120
            $mob_h = 120
            $mob_speed_min = 1
            $mob_speed_max = 1
            $mob_mxp = 8
        "{size=40}{font=battle_f.ttf}{b}Сложные:{/b}{/font}{/size}"
        "{font=battle_f.ttf}Славя{/font}":
            $mob_name = 'sl angry pioneer far'
            $mob_nmn = 'Славя'
            $mob_hmax = 150
            $mob_h = 150
            $mob_speed_min = 1
            $mob_speed_max = 1
            $mob_mxp = 7
        "{font=battle_f.ttf}Ольга Дмитриевна{/font}":
            $mob_name = 'mt rage pioneer far'
            $mob_nmn = 'Ольга Дмитриевна'
            $mob_hmax = 200
            $mob_h = 200
            $mob_speed_min = 1
            $mob_speed_max = 1
            $mob_mxp = 8
        "{size=40}{font=battle_f.ttf}{b}Сверхсложные:{/b}{/font}{/size}"
        "{font=battle_f.ttf}Толян{/font}":
            $mob_name = 'prg_tolyan'
            $mob_nmn = 'Толян'
            $mob_hmax = 1000
            $mob_h = 1000
            $mob_speed_min = 1
            $mob_speed_max = 1
            $mob_mxp = 9
        "{size=40}{font=battle_f.ttf}{b}Покинуть поле боя{/b}{/font}{/size}":
            jump splashscreen
    stop music fadeout 2
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
    play music randmus fadein 2
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
        if hero_h > 201:
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

                text "Мое здоровье:":
                    style "esrpg_butt"
                null width 10
                text "[hero_h]/[hero_hmax] HP" at esrpg_butt_t:
                    style "esrpg_butt"
            null width 25
            hbox:
                text "Здоровье [mob_nmn]:":
                    style "esrpg_butt"
                null width 10
                text "[mob_h]/[mob_hmax] HP" at esrpg_butt_t:
                    style "esrpg_butt"

    text '[if_heal]' xpos 0.5 ypos 0.5 at esrpg_butt_t:
        style 'esrpg_greeni'

    frame:
        background Frame("frame.png", 40, 40, 40, 40)
        xpadding 10
        ypadding 10
        xfill
        xalign 0.5
        ypos .80
        vbox:
            hbox:
                if not_av == 1:
                    textbutton "*Недоступно*" at esrpg_butt_t:
                        style "esrpg_un"
                        text_style "esrpg_un"
                else:
                    textbutton "Атаковать" action [Function(renpy.hide_screen, 'bat_gui'), Function(pnch, hero_state)] at esrpg_butt_t:
                        style "esrpg_butt"
                        text_style "esrpg_butt"

                null width 25

                textbutton "Защита" action [Function(renpy.hide_screen, 'bat_gui'), Function(defn, hero_state)] at esrpg_butt_t:
                    style "esrpg_butt"
                    text_style "esrpg_butt"

                null width 25

                textbutton "Ничего" action [Function(renpy.hide_screen, 'bat_gui'),Function(noth, hero_state)] at esrpg_butt_t:
                    style "esrpg_butt"
                    text_style "esrpg_butt"

                null width 25
                if hero_h < hero_heal:
                    textbutton "Лечиться" action Function(heal, hero_state) at esrpg_butt_t:
                        style "esrpg_butt"
                        text_style "esrpg_butt"
                else:
                    textbutton "*Недоступно*" at esrpg_butt_t:
                        style "esrpg_un"
                        text_style "esrpg_un"

                null width 25

                textbutton "Помощь" action Function(helpsme) at esrpg_butt_t:
                    style "esrpg_butt"
                    text_style "esrpg_butt"
                null width 25

                textbutton "Убежать" action Function(runaway) at esrpg_butt_t:
                    style "esrpg_butt"
                    text_style "esrpg_butt"

                null width 25

            text '[haction]' text_align 0.5 at esrpg_butt_t:
                style "esrpg_butt"
    if rpg_help == 1:
        frame:
            background Frame("frame.png", 40, 40, 40, 40)
            xpadding 10
            ypadding 10
            xfill
            xalign 0.8
            ypos .5
            vbox:
                text "Атака может быть недоступна из-за того, что вас ударили. \n Чтобы её восстановить нажмите \"Защита\". \n Восстановление здоровье возможно, если оно ниже 50 пунктов."  at esrpg_butt_t:
                        style "esrpg_greeny"

                textbutton "Закрыть" action Function(helpsme) at esrpg_butt_t:
                    style "esrpg_butt"
                    text_style "esrpg_butt"

    timer mob_sec action Function(noth, hero_state)
