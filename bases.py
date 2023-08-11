from pygame import *
import math
from time import sleep as sl
from time import time as tm
init()
font.init()

### Технические параметры
WND_SIZE = (700,500)
WND_SIZE_WITH_GAPS = (750, 750)
FPS = 60
###

working = True
game = False



wnd = display.set_mode(WND_SIZE)
clock = time.Clock()

display.set_caption('Lawyer Mondays')


### Цвета
BLACK = (0,0,0)
WHITE = (255, 255, 255)

### Важные для игрового процесса
screen_on = 'start'







class basicsprite(sprite.Sprite): ### Обычный спрайт
    def __init__(self, image_name, pos_x, pos_y, size):
        super().__init__()
        self.image = transform.scale(image.load(image_name), size)
        self.just_image = image.load(image_name)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed = 0
        self.cur_size = size
        self.orig_size = size
        ### В основном только для ентера
        self.is_on_screen = False
        self.original_y = pos_y
        self.original_x = pos_x
    def render(self):
        wnd.blit(self.image, (self.rect.x, self.rect.y))
    def collpoint(self, x, y): ### При прикосновении с точкой
        return self.rect.collidepoint(x,y)
    def sinewave_y(self, t, up, down):
        self.rect.y = math.sin(t/50)* up + down
    def sinewave_x(self, t, right, left):
        self.rect.x = math.sin(t/50)* right + left
    def default_settings(self):
        self.rect.x = self.original_x
        self.rect.y = self.original_y
        self.image = transform.scale(self.just_image, self.orig_size)
        self.cur_size = self.orig_size
    def pressed_anim(self):
        tparency = 255
        for i in range(25):
            wnd.fill(BLACK)
            self.image = transform.scale(self.just_image, self.cur_size)
            self.image.set_alpha(tparency)

            self.rect.x -= self.rect.width / 50 / 3
            self.rect.y -= self.rect.height/50 / 3
            self.cur_size = list(self.cur_size)
            self.cur_size[0] += self.rect.width / 50
            self.cur_size[1] += self.rect.height/50
            self.cur_size = tuple(self.cur_size)

            tparency -= 10.2

            
            self.render()
            
            clock.tick(FPS)
            display.update()
        self.default_settings()
    def hover_over(self, m_x, m_y):
        if self.collpoint(m_x, m_y):
            if list(self.cur_size)[0] < list(self.orig_size)[0] + 15:
                self.image = transform.scale(self.just_image, self.cur_size)
                self.cur_size = list(self.cur_size)
                self.cur_size[0] += self.rect.width / 50
                self.cur_size[1] += self.rect.height/50
                self.cur_size = tuple(self.cur_size)
                self.rect.x -= 1
        elif not self.collpoint(m_x, m_y) and list(self.cur_size)[0] > list(self.orig_size)[0]:
            self.image = transform.scale(self.just_image, self.cur_size)
            self.cur_size = list(self.cur_size)
            self.rect.x += 1
            self.cur_size[0] -= self.rect.width / 50
            self.cur_size[1] -= self.rect.height/50
            self.cur_size = tuple(self.cur_size)
        

### Для геймплея
plr_inventory = []


### Звук
click_sfx = mixer.Sound('sfx+music\\click_sfx.mp3')
click_sfx.set_volume(2)
hi_im_saul = mixer.Sound('sfx+music\\did_you_know_rights.mp3')
med = mixer.Sound('sfx+music\\med.mp3')
page_turn = mixer.Sound('sfx+music\\page_flip.mp3')
walk = mixer.Sound('sfx+music\\walk.mp3')
#dialogue_sfx = mixer.Sound('sfx+music\\dlg_sfx.mp3')

other_sfx = {
    'hi im saul': hi_im_saul,
    'med': med,
    'click': click_sfx,
    'page turn':page_turn,
    'walk':walk
    #'dlg_sfx':dialogue_sfx
}
volume_changes = {
    'music':
    [basicsprite('images\\sound_plus.png', 0, 125, (75, 75)), basicsprite('images\\sound_minus.png', 150, 125, (75, 75))],
    'other':
    [basicsprite('images\\sound_plus.png', 0, 375, (75, 75)), basicsprite('images\\sound_minus.png', 150, 375, (75, 75))]
}