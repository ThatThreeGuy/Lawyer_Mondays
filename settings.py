from bases import *

music_setting = basicsprite('images\\music_setting.png', 0, 50, (150, 75))
other_setting = basicsprite('images\\others_setting.png', 0, 300, (150, 75))
go_back = basicsprite('images\\go_back.png', 0, 0, (215, 45))

### КВАРТЕТ СОЛА
SAUL = basicsprite('images\\saul_goodman.jpg',500, 0, (150, 100))
saul_orig_image = SAUL.image
saul_spin = 1
saul_cd = 0

WALTUH = basicsprite('images\\waltuh.jpg', 500, 200, (150, 100))
waltuh_orig_image = WALTUH.image



def settings(screen_on, t, m_x, m_y):
    global saul_cd, saul_spin, saul_orig_image


    wnd.fill(BLACK)
    music_setting.render()
    other_setting.render()
    go_back.render()
    go_back.hover_over(m_x, m_y)
    if saul_cd <= 0:
        SAUL.image = transform.rotate(saul_orig_image, saul_spin)
        WALTUH.image = transform.rotate(waltuh_orig_image, saul_spin)
        saul_spin += 1
        saul_cd = 1
    SAUL.render()
    WALTUH.render()
    for types in volume_changes:
        for button in volume_changes[types]:
            button.render()
            button.hover_over(m_x, m_y)
    
    #music_setting.sinewave_y(t, -5, 50)
    #other_setting.sinewave_y(t, -5, 300)

    saul_cd -= 1
    go_back.sinewave_x(t, -10, 10)


def settings_properties(m_x, m_y, go_back_where):
    screen_on = 'settings'
    if go_back.collpoint(m_x, m_y):
        screen_on = go_back_where
        mixer.Sound.play(other_sfx['click'])
        go_back.pressed_anim()
                    
    if SAUL.collpoint(m_x, m_y):
        mixer.Sound.play(other_sfx['hi im saul'])

    if WALTUH.collpoint(m_x, m_y):
        mixer.Sound.play(other_sfx['med'])

    for types in volume_changes: ### Все типы в словаре (музыка, прочее...)
        for button in volume_changes[types]:### проверяет все кнопки в словаре
            if button.collpoint(m_x, m_y):
                if button == volume_changes[types][0]: ### если кнопка равна кнопке увеличения звука
                                    ### Потом здесь будет if type == 'music'/ elif type == 'other' и т.д.
                    if types == 'music':
                        curr_volume = mixer.music.get_volume()
                        mixer.music.set_volume(curr_volume + 0.033)
                        mixer.Sound.play(other_sfx['click'])
                    if types == 'other':
                        for sound in other_sfx:
                            curr_volume = other_sfx[sound].get_volume()
                            other_sfx[sound].set_volume(curr_volume + 0.033)
                            mixer.Sound.play(other_sfx['click'])
                            print('up', types)
                elif button == volume_changes[types][1]: ### если кнопка равна кнопке уменьшения звука
                                    ### Потом здесь будет if type == 'music'/ elif type == 'other' и т.д.
                    if types == 'music':
                        curr_volume = mixer.music.get_volume()
                        mixer.music.set_volume(curr_volume - 0.033)
                        mixer.Sound.play(other_sfx['click'])
                    if types == 'other':
                        for sound in other_sfx:
                            curr_volume = other_sfx[sound].get_volume()
                            other_sfx[sound].set_volume(curr_volume - 0.033)
                            mixer.Sound.play(other_sfx['click'])
                            print('down', types)
    return screen_on