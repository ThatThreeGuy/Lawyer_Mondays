from bases import *

class dialogue_holder():
    def __init__(self):
        self.full_text = ''
        self.letter_on = 0
        self.writing_font = font.SysFont('verdana', 30)
        self.current_char = None
        self.char_on_rn = 1

        self.start = 0
        self.interval = 0.05
        self.new_t = tm()

        self.start_rotation = 0
        self.new_t_rotation = 0
        self.interval_rotation = 0.01

        self.rotated_version = []
        rotation = -20
        for i in range(20): ### Создание спрайтов для анимации появляения диалоговой бульбашки
            self.rotated_version.append(transform.rotate(image.load('images\\dlg_bubble.png'), rotation))
            rotation += 1
        self.rotated_version.append(transform.scale(image.load('images\\dlg_bubble.png'), (WND_SIZE[0], 150)))
        self.has_rotated = False

    ### Диалог который не останавливает все действия на заднем плане
    def dlg_no_stop(self, script):
        if self.has_rotated:
            if self.current_char == None: ### Проходит через список персов и выбирает нынешнего
                characters_passed = 1
                    ### Хз что это но оно работает
                for i in script:
                    self.current_char = i
                    if characters_passed == self.char_on_rn:
                        self.char_on_rn += 1
                        break
                    characters_passed += 1




            try:
                ###dialogue.sinewave_y(time.get_ticks()/ 3 % 1000, 10, 3)
                self.new_t = tm()
                if self.new_t - self.start > self.interval:
                    self.full_text += self.current_char[self.letter_on]
                    self.letter_on += 1
                    ####self.interval -= 0.05 пригодится #####
                    self.start = tm()
            except:
                pass
        elif self.has_rotated == False: ### Анимация появления
            self.new_t_rotation = tm()
            try:
                if self.new_t_rotation - self.start_rotation > self.interval_rotation:
                    self.interval_rotation -= 0.00025
                    dialogue.image = self.rotated_version[self.rotated_version.index(dialogue.image) + 1]
                    if dialogue.image == self.rotated_version[20]:
                        self.has_rotated = True
                        self.interval_rotation = 0.01
                    self.start_rotation = tm()
            except:
                dialogue.image = self.rotated_version[0]
        dialogue.render()
        try:
            #script[self.current_char].sinewave_y(time.get_ticks()/ 3 % 1000, 10, 10)
            script[self.current_char].render()
        except:
            pass

            ### Сам эффект диалогов
        if len(self.full_text) <= 27:
            wnd.blit(self.writing_font.render(self.full_text[0:27], True, BLACK), (215, 10))
                ##mixer.Sound.play(other_sfx['dlg_sfx'])
        elif len(self.full_text) > 27 and len(self.full_text) <= 57:
            wnd.blit(self.writing_font.render(self.full_text[0:27], True, BLACK), (215, 10))
            wnd.blit(self.writing_font.render(self.full_text[27:len(self.full_text)], True, BLACK), (200, 45))
                ##mixer.Sound.play(other_sfx['dlg_sfx'])
        elif len(self.full_text) > 57:
            wnd.blit(self.writing_font.render(self.full_text[0:27], True, BLACK), (215, 10))
            wnd.blit(self.writing_font.render(self.full_text[27:57], True, BLACK), (200, 45))
            wnd.blit(self.writing_font.render(self.full_text[57:len(self.full_text)], True, BLACK), (200, 80))
                ##mixer.Sound.play(other_sfx['dlg_sfx'])

    def dlg_with_stop(self, line, face, pos):
        global game
        whole_text = ''
        to_continue = False
        if pos == 'up':
            dialogue.rect.x = 0
            dialogue.rect.y = 0
            face.rect.y = 10
        if pos == 'down':
            dialogue.rect.y = WND_SIZE[1] - 150
            dialogue.rect.x = 0
            face.rect.y = 375


        dialogue.render()
        face.render()

        fontt = font.SysFont('verdana', 30)
        for i in line:
            whole_text += i
            if pos == 'up':
                if len(whole_text) <= 25:
                    wnd.blit(fontt.render(whole_text, True, BLACK), (210, 15))
                if len(whole_text) > 25:
                    wnd.blit(fontt.render(whole_text[25:len(whole_text)], True,BLACK), (200, 50))
            if pos == 'down':
                if len(whole_text) <= 25:
                    wnd.blit(fontt.render(whole_text, True, BLACK), (210, 375))
                if len(whole_text) > 25:
                    wnd.blit(fontt.render(whole_text[25:len(whole_text)], True,BLACK), (200, 410))
            clock.tick(15)
            display.update()
        while to_continue == False:
            game = True
            for ev in event.get():
                if ev.type == QUIT:
                    game = False
                if ev.type == KEYDOWN:
                    if ev.key == K_RETURN:
                        to_continue = True
            if game == False:
                break
            clock.tick(30)
            display.update()



car_sprites = [basicsprite('images\\silver_car1.png', 250, 250, (288, 150)), basicsprite('images\\silver_car2.png', 250, 250, (288, 150))]
bgs_starter = [basicsprite('images\\bg_start1.jpg', 0,0, (WND_SIZE)), basicsprite('images\\bg_start2.png', WND_SIZE[0]*-1,0, (WND_SIZE))]

transition = basicsprite('images\\transition.png', 0, -500, (WND_SIZE))
transition.speed = 5

dialogue = basicsprite('images\\dlg_bubble.png', 0,0, (WND_SIZE[0], 150))
nikola = basicsprite('images\\nikola.png', 30, 15, (130,110))
nikola_unknown = basicsprite('images\\nikola_unknown.png', 30, 15, (130,110))
mikael = basicsprite('images\\mikael.png', 30, 15, (145,110))
mikael_unknown = basicsprite('images\\mikael_unknown.png', 30, 15, (145, 110))
phone_gps = basicsprite('images\\telephone_gps.png', 30, 15, (130, 110))
sprites_mainly_for_dlg = (dialogue, nikola, nikola_unknown,mikael, mikael_unknown)

dlg_holder1 = dialogue_holder()
script = {
    'Нам ещё долго?':nikola_unknown,
    'Достаточно.':mikael_unknown,
    'Достаточно много или мало?':nikola_unknown,
    'достаточно.':mikael_unknown,
    'А просто сказать не можешь?': nikola_unknown,
    'Это было бы слишком легко': mikael_unknown,
    'Так твоя работа - облегчать мне работу': nikola_unknown,
    'Ты уже достиг ежедневнего лимита облегчения': mikael_unknown,
    'Тч, тебе просто нравится меня донимать?': nikola_unknown,
    'Йа йа': mikael_unknown,
    'через':phone_gps,
    '100':phone_gps,
    'метров':phone_gps,
    'поверните':phone_gps,
    'на':phone_gps,
    'право':phone_gps,
    'до':phone_gps,
    'конечной остановки':phone_gps,
    '1 км':phone_gps,
    'и':phone_gps,
    '250 м':phone_gps,
    'Почему даже телефон отвечает, а ты нет?':nikola_unknown,
    'Потому что он - всего лишь машина, имитация человека':mikael_unknown,
    'Робот сочинит симфонию? Робот нарисует шедевр из ничего?':mikael_unknown,
    'Я бы не сказал что ты тоже это сделаешь':nikola_unknown,
    '...':mikael_unknown,
    'Робот расскажет анекдот про колобка?':mikael_unknown,
    'Ох, ну ты конечно его уделал':nikola_unknown,
    'А как же иначе.':mikael_unknown}




'''
def dlg(t, face_sprite = mc_face_sprites[0], pos = 'up'):
    global game, should_do_dialogue_sfx
    whole_text = ''
    to_continue = False
    dialogue_face.image = face_sprite
    if pos == 'up':
        dialogue.rect.x = 0
        dialogue.rect.y = 0
        dialogue_face.rect.y = 30
    if pos == 'down':
        dialogue.rect.y = WND_SIZE[1] - 150
        dialogue.rect.x = 0
        dialogue_face.rect.y = 375


    dialogue.render()
    dialogue_face.render()

    fontt = font.SysFont('verdana', 30)
    for i in t:
        music_control()
        if should_do_dialogue_sfx:
            mixer.Sound.play(current_dialogue_sfx)
        whole_text += i
        if pos == 'up':
            if len(whole_text) <= 25:
                wnd.blit(fontt.render(whole_text, True, WHITE), (210, 15))
            if len(whole_text) > 25:
                wnd.blit(fontt.render(whole_text[25:len(whole_text)], True,WHITE), (200, 50))
        if pos == 'down':
            if len(whole_text) <= 25:
                wnd.blit(fontt.render(whole_text, True, WHITE), (210, 375))
            if len(whole_text) > 25:
                wnd.blit(fontt.render(whole_text[25:len(whole_text)], True,WHITE), (200, 410))
        clock.tick(15)
        display.update()
    while to_continue == False:
        music_control()
        for ev in event.get():
            if ev.type == QUIT:
                game = False
            if ev.type == KEYDOWN:
                if ev.key == K_RETURN:
                    to_continue = True
        if game == False:
            break
        clock.tick(30)
        display.update()'''



def dlg(t, pos = 'up'):
    global game, should_do_dialogue_sfx
    '''Сюда сразу будет засовываться дофига данных по типу 
    Кто говорит : Фраза : Лицо
    '''
    clock.tick(30)
    display.update()



def starting_cutscene():
    global working

    mixer.music.load('sfx+music\\starting_cutscene_music.mp3')

    car_change_sprite = 1
    ### Для машини и заднего фона
    interval = 0.1
    start = 0
    new_t = 0

    ###Для нажатий enter
    enter_interval = 0.2
    start_enter = 0
    new_t_enter = 0


    while working:
        for ev in event.get():
            if ev.type == QUIT: ### Выход
                working = False
            if ev.type == KEYDOWN:
                if ev.key == K_RETURN and new_t_enter - start_enter > enter_interval:
                    start_enter = tm()
                    dlg_holder1.current_char = None
                    dlg_holder1.letter_on = 0
                    dlg_holder1.full_text = ''
                    dlg_holder1.has_rotated = False
                    if dlg_holder1.char_on_rn == len(script) + 1:
                        dlg_holder1.char_on_rn += 1

        for background in bgs_starter:
            if transition.rect.y < 500:
                transition.render()
                transition.rect.y += transition.speed
                if dlg_holder1.char_on_rn > len(script) + 1 and transition.rect.y >= 500:
                    dlg_holder1.dlg_with_stop('Приехали, вываливайся', mikael_unknown, 'up')
                    dlg_holder1.dlg_with_stop('Благодарю', nikola_unknown, 'up')
                    working = False
                    
            else:
                if mixer.music.get_busy() == False:
                    mixer.music.play()
                background.rect.x += 5
                background.render()
                if background.rect.x >= WND_SIZE[0]:
                    background.rect.x = -700

                new_t = tm()
                new_t_enter = tm()
                for car in car_sprites:
                    if car_change_sprite == 1 and car == car_sprites[0]:
                        car.render()
                    elif car_change_sprite == -1 and car == car_sprites[1]:
                        car.render()
                    if new_t - start > interval:
                        car_change_sprite *= -1
                        start = tm()
                
                
                if dlg_holder1.char_on_rn <= len(script) + 1:
                    dlg_holder1.dlg_no_stop(script)
                else:
                    for i in car_sprites:
                        i.rect.x -= 0.1
                        if i.rect.x <= 0:
                            transition.rect.y = -500
                

        display.update()
        clock.tick(FPS)