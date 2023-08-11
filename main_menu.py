from bases import *
from settings import *
mixer.init()

mixer.music.load('sfx+music\\better-call-saul.mp3')
mixer.music.set_volume(0.45)

#other_sfx = [click_sfx, hi_im_saul]

'''TBA
Книга персов - открывается только по завершению игры/демки
'''


M = basicsprite('images\\M.png', 50, 350, (40, 70))
O = basicsprite('images\\O.png', M.rect.x + M.rect.width + 55, 350, (40, 70))
N = basicsprite('images\\N.png', O.rect.x + O.rect.width + 55, 350, (40, 70))
D = basicsprite('images\\D.png', N.rect.x + N.rect.width + 55, 350, (40, 70))
A = basicsprite('images\\A.png', D.rect.x + D.rect.width + 55, 350, (40, 70))
Y = basicsprite('images\\Y.png', A.rect.x + A.rect.width + 55, 350, (40, 70))
S = basicsprite('images\\S.png', Y.rect.x + Y.rect.width + 55, 350, (40, 70))
letters = [M, O, N, D, A, Y, S]

lawyer_title = basicsprite('images\\lawyer.png',  250, 0, (250, 63))

start_button = basicsprite('images\\begin.png', WND_SIZE[0]/2 - 100, 175, (150, 150))
settings_button = basicsprite('images\\settings.png', WND_SIZE[0]/2 - 100, 400, (150, 50))
keys_constitution = basicsprite('images\\keys_constitution.png', 500,175, (200, 250))
constitution_pages = [basicsprite('images\\constitution_page1.png', 0, 0, (750, 550)), basicsprite('images\\constitution_page2.png', 0, 0, (750, 550))] ###750, 550
constitution_page_on = 0
constitution_forward = basicsprite('images\\go_forward.png', 550, 250, (215,45))

def menu_screen():
    global game, working, screen_on, other_sfx, constitution_page_on, to_quit
    sinewave_go_back_var = 10
    mixer.music.play()
    while game == False and working:
        if mixer.music.get_busy() == False:
            mixer.music.play()
        wnd.fill(BLACK)
        m_x, m_y = mouse.get_pos()
        for ev in event.get():
            if ev.type == QUIT: ### Выход
                working = False
                to_quit = True
            if ev.type == MOUSEBUTTONDOWN:
                m_x, m_y = mouse.get_pos()
                if screen_on == 'start':
                    if settings_button.collpoint(m_x, m_y):
                        screen_on = 'settings'
                        mixer.Sound.play(other_sfx['click'])
                        settings_button.pressed_anim()
                    if start_button.collpoint(m_x, m_y):
                        game = True
                        mixer.Sound.play(other_sfx['click'])
                        start_button.pressed_anim()
                        mixer.music.stop()
                    if keys_constitution.collpoint(m_x, m_y):
                        screen_on = 'constitution'
                        mixer.Sound.play(other_sfx['page turn'])
                        keys_constitution.pressed_anim()
                elif screen_on == 'settings':
                    screen_on = settings_properties(m_x, m_y, 'start')

                elif screen_on == 'constitution':
                    if go_back.collpoint(m_x, m_y):
                        screen_on = 'start'
                        constitution_page_on = 0
                        go_back.rect.y = 0
                        sinewave_go_back_var = 10
                        mixer.Sound.play(other_sfx['click'])
                        go_back.pressed_anim()
                    if constitution_forward.collpoint(m_x, m_y) and constitution_page_on == 0:
                        mixer.Sound.play(other_sfx['page turn'])
                        constitution_forward.pressed_anim()
                        constitution_page_on += 1
                        sinewave_go_back_var = 450
                        go_back.rect.y = 400
        
        t = time.get_ticks()/ 3 % 1000

        if screen_on == 'start': ### Рендер
            lawyer_title.render()

            for i in letters:
                i.render()

            start_button.render()
            start_button.hover_over(m_x, m_y)
            settings_button.render()
            settings_button.hover_over(m_x, m_y)
            keys_constitution.render()
            keys_constitution.hover_over(m_x, m_y)
            
            lawyer_title.sinewave_x(t, -5, 100)
            for i in letters:
                i.sinewave_y(t, 30, 75)
            start_button.sinewave_y(t, -10, 200)
            keys_constitution.sinewave_y(t, -5, 200)






        elif screen_on == 'settings': ### Рендер
            settings(screen_on, t, m_x, m_y)

        elif screen_on == 'constitution': ### Рендер
            m_x, m_y = mouse.get_pos()



            #constitution_pages[constitution_page_on].rect.x = ((m_x - constitution_pages[constitution_page_on].rect.width/2)/10)*-1 - 25
            #constitution_pages[constitution_page_on].rect.y = ((m_y - constitution_pages[constitution_page_on].rect.height/2)/10)*-1 - 25
            
            constitution_pages[constitution_page_on].rect.x = constitution_pages[constitution_page_on].original_x + (m_x/13)*-1
            constitution_pages[constitution_page_on].rect.y = constitution_pages[constitution_page_on].original_y + (m_y/10)*-1

            constitution_pages[constitution_page_on].render()
            go_back.render()
            go_back.hover_over(m_x, m_y)
            if constitution_page_on == 0:
                constitution_forward.render()
                constitution_forward.hover_over(m_x, m_y)
                constitution_forward.sinewave_x(t, -10, 450)
            go_back.sinewave_x(t, -10, sinewave_go_back_var)
            



        display.update()
        clock.tick(FPS)
    return game