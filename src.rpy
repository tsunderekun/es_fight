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

    if persistent.method_an == 'new':
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
            easeout 0.5 zoom 1.2
            easein 0.5 zoom 1.0
            easein 0.5 zoom 1.0
            easein 0.5 xpos 0.5
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5
            easein 0.1 rotate 0



        transform punch_me:
            easeout 0.5 zoom 1.2
            easein 0.5 zoom 1.0
            easein 0.5 zoom 1.0
            easein 0.5 xpos 0.5
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5
            easein 0.1 rotate 0

        transform punch_me_bg:
            easeout 0.5 zoom 1.2
            easeout 0.5 rotate 10
            easeout 0.5 zoom 1.2
            easeout 0.5 rotate -10
            easein 0.5 zoom 1.0
            easein 0.5 xpos 0.5
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5
            easein 0.1 rotate 0

        transform punch_bg:
            easeout 0.5 zoom 1.5
            easein 0.5 zoom 1.0
            easein 0.5 zoom 1.0
            easein 0.5 xpos 0.5
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5
            easein 0.1 rotate 0


        transform punch_bg_def:
            easeout 0.5 zoom 1.1
            easeout 0.5 xpos 0.6
            easeout 0.5 zoom 1.2
            easeout 0.5 xpos 0.4
            easein 0.5 zoom 1.0
            easein 0.5 xpos 0.5
            easein 0.1 xalign 0.5
            easein 0.1 yalign 0.5
            easein 0.1 rotate 0


        transform punch_moving:
            choice:
                easein 0.5 zoom 1.0
                easein 2 xpos 0.5
                easeout 2 xpos 0.6
                easein 2 xpos 0.5
                easeout 2 xpos 0.4
                easein 2 xpos 0.5
                repeat
            choice:
                easein 0.5 zoom 1.0
                easein 2 xpos 0.5
                easeout 2 xpos 0.7
                easein 2 xpos 0.5
                easeout 2 xpos 0.3
                easein 2 xpos 0.5
                repeat

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
            easein 0.2 zoom 0.5
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

    if persistent.method_an == 'old':
        transform textrp:
            easeout_back .25 zoom 0.1
            easein_back .50 zoom 1
            easeout_back .75 zoom 2
            1.0
            easein_back .25 zoom 0

        transform punch_moving:
            pass

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


    if persistent.method_an == 'none':
            transform textrp:
                pass
            transform punch_moving:
                pass
            transform esrpg_butt_t():
                pass
            transform punch_1:
                pass
            transform punch_2:
                pass
            transform punch_me:
                pass
            transform punch_me_bg:
                pass
            transform punch_bg:
                pass
            transform punch_bg_def:
                pass
            transform punch_win:
                pass
            transform punch_lose:
                pass



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
    cnt_pnch = 10
    pnch_ver = 1


    def pnch(hero_state):
        if_heal = ''
        global if_heal
        mob_sec = renpy.random.randint (mob_speed_min, mob_speed_max)
        global mob_sec
        hero_bonus = renpy.random.randint (1, hero_mul)
        hero_pow = renpy.random.randint (4, 11) * hero_bonus
        defrand = renpy.random.randint (1, 2)
        if defrand == 1:
            global mob_h
            mob_h -= hero_pow
            haction = "Я ударил противника " + mob_nmn + " и отнял " + str(hero_pow) + " HP"
            global haction

        else:
            not_av = renpy.random.randint (0, 1)
            global not_av
            global mob_h
            mob_h -= 0
            haction = "Промазал"
            global haction

        renpy.play('PUNCH.mp3', channel = 'sound')
        renpy.show(mob_name, [punch_1, punch_moving])
        renpy.show(randbg, [punch_bg])
        renpy.jump('check')

    def pnch_v2(hero_state):
        if_heal = ''
        global if_heal
        mob_sec = renpy.random.randint (mob_speed_min, mob_speed_max)
        global mob_sec
        hero_pow = renpy.random.randint (int (8 * hero_hard), int (22 * hero_hard))
        defrand = renpy.random.randint (1, 2)
        if defrand == 1:
            global mob_h
            mob_h -= hero_pow
            haction = "Я ударил противника " + mob_nmn + " и отнял " + str(hero_pow) + " HP"
            global haction
            cnt_pnch -= 1
            global cnt_pnch

        else:
            cnt_pnch -= 1
            global cnt_pnch
            global mob_h
            mob_h -= 0
            haction = "Промазал"
            global haction

        renpy.play('PUNCH.mp3', channel = 'sound')
        renpy.show(mob_name, [punch_1, punch_moving])
        renpy.show(randbg, [punch_bg])
        renpy.jump('check')

    def defn(hero_state):
        if pnch_ver == 2:
            cnt_pnch = cnt_pnch_all
            global cnt_pnch
        not_av = 0
        global not_av
        if_heal = ''
        global if_heal
        if pnch_ver == 2:
            mob_sec = renpy.random.randint (int (mob_speed_max * 1.25), int (mob_speed_max * 1.75))
        else:
            mob_sec = renpy.random.randint (4, 7)
        global mob_sec
        mob_pow = (renpy.random.randint (0, 3) * renpy.random.randint (1, int (mob_mxp * hero_hard)))
        defrand = renpy.random.random()
        if defrand < 0.33:
            global hero_h
            hero_h -= mob_pow
            haction = "Я уклонился, но потерял " + str(mob_pow) + " HP"
            global haction
            renpy.show(mob_name, [punch_me, punch_moving])

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
        mob_sec = renpy.random.randint (mob_speed_min, mob_speed_max + 1)
        global mob_sec
        mob_pow = (renpy.random.randint (5, 6) * renpy.random.randint (1, int (mob_mxp * hero_hard)))
        defrand = renpy.random.random()
        if defrand > (0.20 * hero_hard) :
            not_av = 1
            if pnch_ver == 2:
                cnt_pnch = 0
                global cnt_pnch
            global hero_h
            hero_h -= mob_pow
            haction = "Я потерял " + str(mob_pow) + " HP"
            global haction

        else:
            global hero_h
            hero_h -= 0
            haction = "Я уклонился"
            global haction

        renpy.play('attack.mp3', channel = 'sound')
        renpy.show(mob_name, [punch_me, punch_moving])
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
            healed_h = (renpy.random.randint (int (hero_heal / 3), int (hero_heal / 2)))
            hero_h = hero_h + healed_h
            global healed_h
            if_heal = "+" + str(healed_h) + " HP"
            global if_heal

        else:
            global hero_h
            global mob_h
            healed_h = (renpy.random.randint (int (hero_heal / 3), int (hero_heal / 2)))
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
    show dsc text at truecenter with dissolve
    $ renpy.pause(5, hard = True)
    hide dsc text with dissolve
    jump prep




label prep:
    play music music_list["into_the_unknown"] fadein 2
    $hero_hard = 0.50
    $cnt_pnch = 10
    $cnt_pnch_all = 10
    $pnch_ver = 0
    $rpg_help = 0
    $not_av = 0
    $haction = ""
    $if_heal = ''
    $mob_sec = renpy.random.randint (1, 3)
    $hero_hmax = 100
    $hero_hmaxi = 101
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
    $hero_mul = 2
    $disp_cnt_pnch = ''
    $prolog_time()
    scene anim prolog_1 with dspr
    if persistent.method_an is None:
        $ frs_anim = 1
        $ frs_txt = 'Первый запуск. Требуется перезапуск'
    if persistent.method_an is not None:
        $ frs_anim = 0
        $ frs_txt = 'Смена анимации будет произведена после ручного перезапуска'

    menu:

        "{size=40}{font=battle_f.ttf}{b}Выбери режим анимаций:{/b}{/font}"


        "{font=battle_f.ttf}[frs_txt]{/font}"

        "{font=battle_f.ttf}Кривой новый{/font}":
            $persistent.method_an = 'new'

        "{font=battle_f.ttf}Кривой старый{/font}":
            $persistent.method_an = 'old'

        "{font=battle_f.ttf}Отключить{/font}":
            $persistent.method_an = 'none'

        "{font=battle_f.ttf}Далее{/font}":
            pass


    if frs_anim == 1:
        $renpy.utter_restart()


    menu:
        "{size=40}{font=battle_f.ttf}{b}Выбери метод восстановления:{/b}{/font}"
        "{font=battle_f.ttf}Радном{/font}":
            $pnch_ver = 1
        "{font=battle_f.ttf}Защита{/font}":
            $pnch_ver = 2
    menu:
        "{size=40}{font=battle_f.ttf}{b}Выбери сложность:{/b}{/font}"
        "{font=battle_f.ttf}Легкий{/font}":
            $hero_hard = 0.50
            $cnt_pnch = 7
            $cnt_pnch_all = 7
            $hero_hmax = 200
            $hero_hmaxi = 201
            $hero_h = 200
            $hero_heal = 100
            $hero_mul = 4
        "{font=battle_f.ttf}Средний{/font}":
            $hero_hard = 0.75
            $cnt_pnch = 5
            $cnt_pnch_all = 5
            $hero_hmax = 100
            $hero_hmaxi = 125
            $hero_h = 100
            $hero_heal = 76
            $hero_mul = 3
        "{font=battle_f.ttf}Сложный{/font}":
            $hero_hard = 1.25
            $cnt_pnch = 3
            $cnt_pnch_all = 3
            $hero_hmax = 75
            $hero_hmaxi = 100
            $hero_h = 75
            $hero_heal = 51
            $hero_mul = 2
        "{font=battle_f.ttf}{color=#f00}Даже не пытайся{/color}{/font}":
            $hero_hard = 1.50
            $cnt_pnch = 2
            $cnt_pnch_all = 2
            $hero_hmax = 50
            $hero_hmaxi = 75
            $hero_h = 50
            $hero_heal = 36
            $hero_mul = 2
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
        "{font=battle_f.ttf}Электроник{/font}":
            $mob_name = 'el angry pioneer far'
            $mob_nmn = 'Электроник'
            $mob_hmax = 90
            $mob_h = 90
            $mob_speed_min = 1
            $mob_speed_max = 4
            $mob_mxp = 3
        "{size=40}{font=battle_f.ttf}{b}Средние:{/b}{/font}{/size}"
        "{font=battle_f.ttf}Женя{/font}":
            $mob_name = 'mz rage pioneer far'
            $mob_nmn = 'Женя'
            $mob_hmax = 80
            $mob_h = 80
            $mob_speed_min = 2
            $mob_speed_max = 3
            $mob_mxp = 4
        "{font=battle_f.ttf}Пионер{/font}":
            $mob_name = 'pi normal'
            $mob_nmn = 'Пионер'
            $mob_hmax = 100
            $mob_h = 100
            $mob_speed_min = 1
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
        "{size=40}{font=battle_f.ttf}{b}Сложные:{/b}{/font}{/size}"
        "{font=battle_f.ttf}Мику{/font}":
            $mob_name = 'mi rage pioneer far'
            $mob_nmn = 'Мику'
            $mob_hmax = 95
            $mob_h = 95
            $mob_speed_min = 1
            $mob_speed_max = 2
            $mob_mxp = 6
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
        "{font=battle_f.ttf}Славя{/font}":
            $mob_name = 'sl angry pioneer far'
            $mob_nmn = 'Славя'
            $mob_hmax = 150
            $mob_h = 150
            $mob_speed_min = 1
            $mob_speed_max = 1
            $mob_mxp = 7
        "{font=battle_f.ttf}Лена{/font}":
            $mob_name = 'un rage pioneer far'
            $mob_nmn = 'Лена'
            $mob_hmax = 120
            $mob_h = 120
            $mob_speed_min = 1
            $mob_speed_max = 1
            $mob_mxp = 8
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
        "{size=40}{font=battle_f.ttf}{b}Особые:{/b}{/font}{/size}"
        "{font=battle_f.ttf}Случайная Конфигурация Противника{/font}":
            $mob_name = renpy.random.choice(['prg_tolyan', 'mt rage pioneer far', 'sl angry pioneer far', 'un rage pioneer far', 'us angry pioneer far', 'mz rage pioneer far', 'uv rage far' ,'el angry pioneer far', 'mi rage pioneer far', 'pi normal' ,'sh rage pioneer far', 'dv rage pioneer far'])
            $mob_nmn = 'СКП'
            $mob_hmax = renpy.random.randint (50, 1000)
            $mob_h = mob_hmax
            $mob_speed_min = renpy.random.randint (1, 2)
            $mob_speed_max = renpy.random.randint (2, 9)
            $mob_mxp = randscene = renpy.random.randint (4, 8)
        "{size=40}{font=battle_f.ttf}{b}Покинуть поле боя{/b}{/font}{/size}":
            jump splashscreen

    menu:
        "{size=40}{font=battle_f.ttf}{b}Выбери локацию{/b}{/font}{/size}"
        "{font=battle_f.ttf}Случайно{/font}":
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
        "{font=battle_f.ttf}Площадь{/font}":
            $day_time()
            $persistent.sprite_time = "day"
            show bg ext_square_day with dissolve
            $randbg = "bg ext_square_day"
        "{font=battle_f.ttf}Поляна{/font}":
            $sunset_time()
            $persistent.sprite_time = "sunset"
            show bg ext_polyana_sunset with dissolve
            $randbg = "bg ext_polyana_sunset"
        "{font=battle_f.ttf}Катакомбы{/font}":
            $night_time()
            $persistent.sprite_time = "night"
            show bg int_mine_room with dissolve
            $randbg = "bg int_mine_room"


    $ renpy.show(mob_name, [center, punch_moving])
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
        disp_cnt_pnch = ' * ' * cnt_pnch
        if cnt_pnch == 0:
            not_av == 1
        if cnt_pnch == cnt_pnch_all:
            not_av == 0
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
        if hero_h > hero_hmaxi:
            hero_h = hero_hmax
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
            vbox:
                hbox:
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
                if pnch_ver == 2:
                    text "Удары: [disp_cnt_pnch]" at esrpg_butt_t:
                        style "esrpg_butt"
                else:
                    pass

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
                    if pnch_ver == 1:
                        textbutton "Атаковать" action [Function(renpy.hide_screen, 'bat_gui'), Function(pnch, hero_state)] at esrpg_butt_t:
                            style "esrpg_butt"
                            text_style "esrpg_butt"
                    if pnch_ver == 2:
                        if cnt_pnch == 0:
                            textbutton "*Недоступно*" at esrpg_butt_t:
                                style "esrpg_un"
                                text_style "esrpg_un"
                        else:
                            textbutton "Атаковать" action [Function(renpy.hide_screen, 'bat_gui'), Function(pnch_v2, hero_state)] at esrpg_butt_t:
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
                if pnch_ver == 1:
                    text "Атака может быть недоступна из-за того, что вас ударили. \n Чтобы её восстановить нажмите \"Защита\". \n Восстановление здоровье возможно, если оно ниже [hero_heal] пунктов."  at esrpg_butt_t:
                            style "esrpg_greeny"

                if pnch_ver == 2:
                    text " \n Чтобы восстановить пункты атаки нажмите \"Защита\". \n Восстановление здоровье возможно, если оно ниже [hero_heal] пунктов."  at esrpg_butt_t:
                            style "esrpg_greeny"


                textbutton "Закрыть" action Function(helpsme) at esrpg_butt_t:
                    style "esrpg_butt"
                    text_style "esrpg_butt"

    timer mob_sec action Function(noth, hero_state)
