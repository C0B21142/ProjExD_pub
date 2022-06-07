import pygame as pg
import sys
import random

key_delta = {pg.K_UP   : [0, -1],
             pg.K_DOWN : [0, +1],
             pg.K_LEFT : [-1, 0],
             pg.K_RIGHT: [+1, 0],}

def main():
    clock = pg.time.Clock()
    
    # 練習1
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))      # 画面用のSurface
    sc_rect= screen.get_rect()                     # 画面用のRect
    bg_img = pg.image.load("fig/pg_bg.jpg")        # 背景画像用のSurface
    bg_rect= bg_img.get_rect()                     # 背景画像用のRect
    #bg_rect.center = (1500,500)
    screen.blit(bg_img, bg_rect)                   # 背景画像用Surfaceを画面用Surfaceに貼り付ける

    # 練習3
    tori_img = pg.image.load("fig/3.png")          # こうかとん画像用のSurface
    tori_img = pg.transform.rotozoom(tori_img, 0, 2)
    tori_rect= tori_img.get_rect()                 # こうかとん画像用のRect
    tori_rect.center = 900, 400                    # こうかとん画像の中心座標を設定する
    screen.blit(tori_img, tori_rect)               # こうかとん画像用のSurfaceを画面用Surfaceに貼り付ける

    # 練習5
    bomb = pg.Surface((20,20))                     # 爆弾用のSurface
    bomb.set_colorkey((0,0,0))                     # 黒色部分を透過する
    pg.draw.circle(bomb, (255,0,0), (10,10), 10)   # 爆弾用Surfaceに円を描く
    bomb_rect = bomb.get_rect()                    # 爆弾用Rect
    bomb_rect.centerx = random.randint(0, sc_rect.width)
    bomb_rect.centery = random.randint(0, sc_rect.height)
    screen.blit(bomb, bomb_rect)                   # 爆弾用のSurfaceを画面用Surfaceに貼り付ける
    vx, vy = +2, +2

    while True:
        # 練習2
        screen.blit(bg_img, bg_rect)
        for event in pg.event.get():
            if event.type == pg.QUIT: return       # ✕ボタンでmain関数から戻る

        # 練習4
        key_states = pg.key.get_pressed()
        for key, delta in key_delta.items():
            if key_states[key] == True:
                tori_rect.centerx += delta[0]
                tori_rect.centery += delta[1]
                # 練習7
                if check_bound(sc_rect, tori_rect) != (1,1): 
                    tori_rect.centerx -= delta[0]
                    tori_rect.centery -= delta[1]
        screen.blit(tori_img, tori_rect)

        # 練習6
        bomb_rect.move_ip(vx, vy)
        screen.blit(bomb, bomb_rect)
        # 練習7
        x, y = check_bound(sc_rect, bomb_rect)
        vx *= x # 横方向に画面外なら，横方向速度の符号反転
        vy *= y # 縦方向に画面外なら，縦方向速度の符号反転

        # 練習8
        if tori_rect.colliderect(bomb_rect): return        # こうかとん用のRectが爆弾用のRectと衝突していたらreturn

        pg.display.update()  # 画面の更新
        clock.tick(1000) 
    
# 練習7
def check_bound(sc_r, obj_r): # 画面用Rect, ｛こうかとん，爆弾｝Rect
    # 画面内：+1 / 画面外：-1
    x, y = +1, +1
    if obj_r.left < sc_r.left or sc_r.right  < obj_r.right : x = -1
    if obj_r.top  < sc_r.top  or sc_r.bottom < obj_r.bottom: y = -1
    return x, y


if __name__ == "__main__":
    pg.init() 
    main()
    pg.quit()
    sys.exit()
