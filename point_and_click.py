from bases import *
from cutscenes import dialogue_holder
from cutscenes import mikael, mikael_unknown, nikola, nikola_unknown, dialogue
from settings import *

dlg_holder1 = dialogue_holder()

arrow_go_forward = basicsprite('images\\go_forward_game.png', 300, 175, (100, 100))

arrow_go_right = basicsprite('images\\go_forward_game.png', 575, 275, (100, 100))
arrow_go_right.image = transform.scale(transform.rotate(image.load('images\\go_forward_game.png'), -90), (100, 100))


arrow_go_left = basicsprite('images\\go_forward_game.png', 25, 275, (100, 100))
arrow_go_left.image = transform.scale(transform.rotate(image.load('images\\go_forward_game.png'), 90), (100, 100))

inventory_button = basicsprite('images\\inventory.png', 600, 0, (100, 100))

inv_button__spin = []
inv_button_how_much_spin = 0

def first_point_and_click(inventory_button):
    global screen_on, inv_button__spin, inv_button_how_much_spin
    goofy_ahh_variable = 0
    for i in range(360):
        inv_button__spin.append(transform.rotate(transform.scale(image.load('images\\inventory.png'), (100, 100)), goofy_ahh_variable))
        goofy_ahh_variable += 1
    mixer.music.stop()
    all_bgs = [basicsprite('images\\lawplace_entrance.png', 0, 0, (700, 550)), basicsprite('images\\lawplace_hall.png', 0, 0, (700, 550)), basicsprite('images\\lawplace_free.png', 0, 0, (775, 550)), basicsprite('images\\lawplace_free.png', 0, 0, (775, 550))]
    current_bg = all_bgs[0]
    on_screen_objs = []
    script = None

    graffiti1 = basicsprite('images\\graffiti1.png', 50, 250, (100, 150))
    work_time = basicsprite('images\\work_time.png', 450, 100, (100, 150))
    worker_of_the_year = basicsprite('images\\worker_of_the_year.png', 100, 50, (150, 100))
    femida_art = basicsprite('images\\femida-art.jpg', 100, 50, (200, 170))
    nikola_door = basicsprite('images\\nikola_door.png', 10, 165, (125*1.5, 200*1.5))
    zaycev_door = basicsprite('images\\zaycev_door.png', 200, 165, (125*1.5, 200*1.5))
    zima_door = basicsprite('images\\zima_door.png', 390, 165, (125*1.5, 200*1.5))

    on_screen_objs = [graffiti1, arrow_go_forward]

    screen_on = 'point and click'
    working = True

    ###Для ентера
    enter_interval = 0.2
    start_enter = 0
    new_t_enter = 0

    spin_interval = 0.00000001
    start_spin = 0
    new_t_spin = 0

    while working:
        m_x, m_y = mouse.get_pos()
        for ev in event.get():
            if ev.type == QUIT: ### Выход
                working = False
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    screen_on = 'settings'
                    mixer.Sound.play(other_sfx['click'])
                if ev.key == K_RETURN and new_t_enter - start_enter > enter_interval and script != None:
                    start_enter = tm()
                    #print(dlg_holder1.char_on_rn,  dlg_holder1.current_char, dlg_holder1.full_text)
                    if dlg_holder1.char_on_rn == len(script) + 1: ### КОнец балаканья
                        script = None
                        dlg_holder1.char_on_rn = 1
                    dlg_holder1.current_char = None
                    dlg_holder1.letter_on = 0
                    dlg_holder1.full_text = ''
                    dlg_holder1.has_rotated = False
                    #print(dlg_holder1.char_on_rn,  dlg_holder1.current_char, dlg_holder1.full_text)
            if ev.type == MOUSEBUTTONDOWN:
                m_x, m_y = mouse.get_pos()
                if screen_on == 'settings':
                    screen_on = settings_properties(m_x, m_y, 'point and click')
                if screen_on == 'point and click':
                    if ev.button == 1:
                        if current_bg == all_bgs[0]: ### Вид с улицы
                            for i in on_screen_objs:
                                if i.collpoint(m_x, m_y):
                                    if i == graffiti1:
                                        script = {
                                            'Графити со времён динозавров':nikola_unknown,
                                            'Его бы по хорошему убрать надо, во имя профессионализма':nikola_unknown,
                                            'Но людям оно очень запало в душу':nikola_unknown,
                                            'Так что ,как говориться, что не сломано, чинить не надо':nikola_unknown
                                        }
                                    if i == arrow_go_forward: ### Переход на ресепшн
                                        current_bg = all_bgs[1]
                                        mixer.Sound.play(other_sfx['walk'])
                                        i.pressed_anim()
                                        on_screen_objs = [arrow_go_right, arrow_go_left, work_time, worker_of_the_year]
                        elif current_bg == all_bgs[1]: ### Ресепшн
                            for i in on_screen_objs:
                                if i.collpoint(m_x, m_y):
                                    if i == work_time:
                                        script = {
                                            'Расписание перерывов с очень специфичным временем':nikola_unknown,
                                            'Первый перерыв с 13:17 до 13:52':nikola_unknown,
                                            'И второй с 16:48 до 17:15':nikola_unknown,
                                            'Это что-то значит?':nikola_unknown
                                        }
                                    if i == worker_of_the_year:
                                        script = {
                                            'Рама с именем работника года':nikola_unknown,
                                            'Имя не моё, так что не интересует':nikola_unknown,
                                            'Правда бесит очень что рама не симметричная':nikola_unknown
                                        }
                                    if i == arrow_go_left: ### Переход на левый корридор
                                        current_bg = all_bgs[2]
                                        mixer.Sound.play(other_sfx['walk'])
                                        on_screen_objs = [arrow_go_right, nikola_door, zaycev_door, zima_door]
                                    if i == arrow_go_right: ### Переход на правый корридор
                                        current_bg = all_bgs[3]
                                        mixer.Sound.play(other_sfx['walk'])
                                        on_screen_objs = [femida_art, arrow_go_left]
                        elif current_bg == all_bgs[2]:
                            for i in on_screen_objs:
                                if i.collpoint(m_x, m_y):
                                    if i == arrow_go_right:
                                        current_bg = all_bgs[1]
                                        mixer.Sound.play(other_sfx['walk'])
                                        on_screen_objs = [arrow_go_right, arrow_go_left, work_time, worker_of_the_year]
                                        for i in on_screen_objs:
                                            i.rect.x = i.original_x
                                            i.rect.y = i.original_y
                                    if i == zima_door:
                                        script = {
                                            'Дверь в оффис к моему коллеге Джареду Зиме':nikola_unknown,
                                            'Очень скрытный парень, я почти никогда его не видел вне работы':nikola_unknown
                                        }
                                    if i == zaycev_door:
                                        script = {
                                            'Дверь в оффис к моему коллеге Антону Зайцеву':nikola_unknown,
                                            'Хороший тип, всегда приятно с ним иметь дело':nikola_unknown
                                        }
                                    if i == nikola_door:
                                        script = {
                                            'Дверь в мой оффис':nikola_unknown,
                                        }
                        elif current_bg == all_bgs[3]:
                            for i in on_screen_objs:
                                if i.collpoint(m_x, m_y):
                                    if i == femida_art:
                                        script = {
                                            'Рисунок богини правосудия - Фемиды':nikola_unknown,
                                            'Качественно сделанный':nikola_unknown
                                        }
                                    if i == arrow_go_left:
                                        current_bg = all_bgs[1]
                                        mixer.Sound.play(other_sfx['walk'])
                                        on_screen_objs = [arrow_go_right, arrow_go_left, work_time, worker_of_the_year]
                                        for i in on_screen_objs:
                                            i.rect.x = i.original_x
                                            i.rect.y = i.original_y
                        if inventory_button.collpoint(m_x, m_y):
                            script = {
                                'Мой инвентарь':nikola_unknown,
                                'Правый клик чтобы открыть':nikola_unknown
                            }
                    elif ev.button == 3:
                        if inventory_button.collpoint(m_x, m_y):
                            if inv_button_how_much_spin == 0:
                                inv_button_how_much_spin = 360
                            mixer.Sound.play(other_sfx['click'])

        
        if screen_on == 'settings':### Рендер
            settings(screen_on, time.get_ticks()/ 3 % 1000, m_x, m_y)
        elif screen_on == 'point and click': ### Рендер
            
            new_t_enter = tm()
            new_t_spin = tm()

            #print(all_bgs.index(current_bg))

            m_x, m_y = mouse.get_pos()
            current_bg.render()
            for i in on_screen_objs:
                i.rect.y = i.original_y + (m_y/10)*-1
                if current_bg.rect.width > 700:
                    i.rect.x = i.original_x + (m_x/10)*-1
                if i == arrow_go_forward:
                    i.hover_over(m_x, m_y)
                i.render()
            #current_bg.rect.y = ((m_y - current_bg.rect.height/2)/10)*-1 - 25
            current_bg.rect.y = current_bg.original_y + (m_y/10)*-1
            #print(current_bg.rect.width)
            if current_bg.rect.width > 700:
                #current_bg.rect.x = ((m_x - current_bg.rect.height/2)/10)*-1 - 25
                current_bg.rect.x = current_bg.original_x + (m_x/10)*-1

            if inv_button_how_much_spin > 0 and new_t_spin - start_spin > spin_interval:
                inv_button_how_much_spin -= 1
                start_spin = tm()
                inventory_button.image = inv_button__spin[inv_button_how_much_spin]

            inventory_button.render()
            inventory_button.hover_over(m_x, m_y)

        
        if script != None and screen_on != 'settings':
            dlg_holder1.dlg_no_stop(script)

        
        display.update()
        clock.tick(FPS)