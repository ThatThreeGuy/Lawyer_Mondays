import pygame
import math
from time import time as tm

'''
ТЕСТПЛЕЙС НА ЭКРАН 500х500, import pygame, И ЛИМИТАЦИИ ЛОГИКИ
'''

pygame.init()
pygame.font.init()

### Технические параметры
WND_SIZE = (500, 500)
#WND_SIZE_WITH_GAPS = (750, 750)
FPS = 60
###

working = True
game = False

wnd = pygame.display.set_mode(WND_SIZE)
clock = pygame.time.Clock()

pygame.display.set_caption('Lawyer Mondays')

### Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

### Важные для игрового процесса
screen_on = 'start'


class basicsprite():  ### Обычный спрайт
    def __init__(self, image_name, pos_x, pos_y, size):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image_name), size)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed = 0
        ### В основном только для ентера
        self.is_on_screen = False
        self.original_y = pos_y
        self.original_x = pos_x

    def render(self):
        wnd.blit(self.image, (self.rect.x, self.rect.y))

    def collpoint(self, x, y):  ### При прикосновении с точкой
        return self.rect.collidepoint(x, y)

    def sinewave_y(self, t, up, down):
        self.rect.y = math.sin(t / 50) * up + down

    def sinewave_x(self, t, right, left):
        self.rect.x = math.sin(t / 50) * right + left
class dialogue_holder():
    def __init__(self):
        self.full_text = ''
        self.letter_on = 0
        self.writing_font = pygame.font.SysFont('verdana', 30)
        self.current_char = None
        self.char_on_rn = 1

        self.start = 0
        self.interval = 0.05
        self.new_t = tm()


    ### Диалог который не останавливает все действия на заднем плане
    def dlg_no_stop(self, script):
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
        dialogue.render()
        try:
            #script[self.current_char].sinewave_y(time.get_ticks()/ 3 % 1000, 10, 10)
            script[self.current_char].render()
        except:
            pass

            ### Сам эффект диалогов
        if len(self.full_text) <= 20:
            wnd.blit(self.writing_font.render(self.full_text[0:20], True, BLACK), (150, 10))
                ##mixer.Sound.play(other_sfx['dlg_sfx'])
        elif len(self.full_text) > 20 and len(self.full_text) <= 40:
            wnd.blit(self.writing_font.render(self.full_text[0:20], True, BLACK), (150, 10))
            wnd.blit(self.writing_font.render(self.full_text[20:len(self.full_text)], True, BLACK), (150, 45))
                ##mixer.Sound.play(other_sfx['dlg_sfx'])
        elif len(self.full_text) > 40:
            wnd.blit(self.writing_font.render(self.full_text[0:20], True, BLACK), (150, 10))
            wnd.blit(self.writing_font.render(self.full_text[20:40], True, BLACK), (150, 45))
            wnd.blit(self.writing_font.render(self.full_text[40:len(self.full_text)], True, BLACK), (125, 80))
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

        fontt = pygame.font.SysFont('verdana', 30)
        for i in line:
            whole_text += i
            if pos == 'up':
                if len(whole_text) <= 25:
                    wnd.blit(fontt.render(whole_text, True, BLACK), (150, 15))
                if len(whole_text) > 25:
                    wnd.blit(fontt.render(whole_text[25:len(whole_text)], True,BLACK), (125, 50))
            if pos == 'down':
                if len(whole_text) <= 25:
                    wnd.blit(fontt.render(whole_text, True, BLACK), (150, 375))
                if len(whole_text) > 25:
                    wnd.blit(fontt.render(whole_text[25:len(whole_text)], True,BLACK), (125, 410))
            clock.tick(15)
            pygame.display.update()
        while to_continue == False:
            game = True
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    game = False
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_RETURN:
                        to_continue = True
            if game == False:
                break
            clock.tick(30)
            pygame.display.update()

### Главное меню
M = basicsprite('images\\M.png', 50, 350, (25, 30))
O = basicsprite('images\\O.png', M.rect.x + M.rect.width + 55, 350, (25, 30))
N = basicsprite('images\\N.png', O.rect.x + O.rect.width + 55, 350, (25, 30))
D = basicsprite('images\\D.png', N.rect.x + N.rect.width + 55, 350, (25, 30))
A = basicsprite('images\\A.png', D.rect.x + D.rect.width + 55, 350, (25, 30))
Y = basicsprite('images\\Y.png', A.rect.x + A.rect.width + 55, 350, (25, 30))
S = basicsprite('images\\S.png', Y.rect.x + Y.rect.width + 55, 350, (25, 30))
letters = [M, O, N, D, A, Y, S]

lawyer_title = basicsprite('images\\lawyer.png',  250, 0, (150, 50))

start_button = basicsprite('images\\begin.png', WND_SIZE[0]/2 - 100, 175, (150, 150))
settings_button = basicsprite('images\\settings.png', WND_SIZE[0]/2 - 100, 400, (150, 50))
keys_constitution = basicsprite('images\\keys_constitution.png', 350,175, (150, 150))
constitution_pages = [basicsprite('images\\constitution_page1.png', 0, 0, (550, 550)), basicsprite('images\\constitution_page2.png', 0, 0, (550, 550))] ###750, 550
constitution_page_on = 0
constitution_forward = basicsprite('images\\go_forward.png', 450, 250, (150, 45))


music_setting = basicsprite('images\\music_setting.png', 0, 50, (150, 75))
other_setting = basicsprite('images\\others_setting.png', 0, 300, (150, 75))
go_back = basicsprite('images\\go_back.png', 0, 0, (150, 45))
volume_changes = {
    'music':
    [basicsprite('images\\sound_plus.png', 0, 125, (75, 75)), basicsprite('images\\sound_minus.png', 150, 125, (75, 75))],
    'other':
    [basicsprite('images\\sound_plus.png', 0, 375, (75, 75)), basicsprite('images\\sound_minus.png', 150, 375, (75, 75))]
}



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

def settings(screen_on, t):


    wnd.fill(BLACK)
    music_setting.render()
    other_setting.render()
    go_back.render()
    for types in volume_changes:
        for button in volume_changes[types]:
            button.render()
    
    #music_setting.sinewave_y(t, -5, 50)
    #other_setting.sinewave_y(t, -5, 300)

    go_back.sinewave_x(t, -10, 10)


def settings_properties(m_x, m_y, go_back_where):
    screen_on = 'settings'
    if go_back.collpoint(m_x, m_y):
        screen_on = go_back_where
    return screen_on



def menu_screen():
    global game, working, screen_on, other_sfx, constitution_page_on
    sinewave_go_back_var = 10
    while game == False and working:
        wnd.fill(BLACK)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT: ### Выход
                working = False
            if ev.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                if screen_on == 'start':
                    if settings_button.collpoint(m_x, m_y):
                        screen_on = 'settings'
                    if start_button.collpoint(m_x, m_y):
                        game = True
                    if keys_constitution.collpoint(m_x, m_y):
                        screen_on = 'constitution'
                elif screen_on == 'settings':
                    screen_on = settings_properties(m_x, m_y, 'start')
                elif screen_on == 'constitution':
                    if go_back.collpoint(m_x, m_y):
                        screen_on = 'start'
                        constitution_page_on = 0
                        go_back.rect.y = 0
                        sinewave_go_back_var = 10
                    if constitution_forward.collpoint(m_x, m_y) and constitution_page_on == 0:
                        constitution_page_on += 1
                        sinewave_go_back_var = 250
                        go_back.rect.y = 400

        t = pygame.time.get_ticks() / 3 % 1000

        if screen_on == 'start':  # Рендер
            lawyer_title.render()

            for i in letters:
                i.render()

            start_button.render()
            settings_button.render()
            keys_constitution.render()

            lawyer_title.sinewave_x(t, -5, 100)
            for i in letters:
                i.sinewave_y(t, 30, 75)
            start_button.sinewave_y(t, -10, 200)
            keys_constitution.sinewave_y(t, -5, 200)

        elif screen_on == 'settings':  # Рендер
            settings(screen_on, t)

        elif screen_on == 'constitution':  # Рендер
            m_x, m_y = pygame.mouse.get_pos()

            # constitution_pages[constitution_page_on].rect.x = ((m_x - constitution_pages[constitution_page_on].rect.width/2)/10)*-1 - 25
            # constitution_pages[constitution_page_on].rect.y = ((m_y - constitution_pages[constitution_page_on].rect.height/2)/10)*-1 - 25

            constitution_pages[constitution_page_on].rect.x = constitution_pages[constitution_page_on].original_x + (
                        m_x / 13) * -1
            constitution_pages[constitution_page_on].rect.y = constitution_pages[constitution_page_on].original_y + (
                        m_y / 10) * -1

            constitution_pages[constitution_page_on].render()
            go_back.render()
            if constitution_page_on == 0:
                constitution_forward.render()
                constitution_forward.sinewave_x(t, -10, 350)
            go_back.sinewave_x(t, -10, sinewave_go_back_var)

        pygame.display.update()
        clock.tick(FPS)
def starting_cutscene():
    global working

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
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT: ### Выход
                working = False
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN and new_t_enter - start_enter > enter_interval:
                    start_enter = tm()
                    dlg_holder1.current_char = None
                    dlg_holder1.letter_on = 0
                    dlg_holder1.full_text = ''
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
                

        pygame.display.update()
        clock.tick(FPS)

menu_screen()
starting_cutscene()
