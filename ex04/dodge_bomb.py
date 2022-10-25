import pygame as pg
import sys
from random import randint

def check_bound(obj_rct, scr_rct):
    """
    obj_rct:こうかとんrct,または,爆弾rct
    scr_rct:スクリーンrct
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko,tate

# def key_down(event):
#     global key
#     key = event.keysym

def bomb():
    global scrn_rct
    global bomb_sfc
    global bomb_rct
    bomb_sfc = pg.Surface((20, 20))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)

def main():
    #背景
    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    #こうかとん
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    #爆弾
    bomb_sfc = pg.Surface((20, 20))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)
    
    #爆風
    blow_sfc = pg.image.load("fig/blow.png")
    blow_sfc = pg.transform.rotozoom(blow_sfc, 0, 1.0)
    blow_rct = blow_sfc.get_rect()
    

    vx, vy = +1, +1

    clock = pg.time.Clock()
    #clock.schdule_unique(bomb,3)
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)   

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        #こうかとんの移動処理
        #左右上下のキーで移動
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:tori_rct.centery -=1#こうかとんの縦座標を-1
        if key_states[pg.K_DOWN]:tori_rct.centery +=1#こうかとんの縦座標を+1
        if key_states[pg.K_LEFT]:tori_rct.centerx -=1
        if key_states[pg.K_RIGHT]:tori_rct.centerx +=1
        #こうかとんが外に行かないための処理
        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_states[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        if tate == -1:
            if key_states[pg.K_UP]:
                tori_rct.centery += 1
            if key_states[pg.K_DOWN]:
                tori_rct.centery -= 1
        scrn_sfc.blit(tori_sfc, tori_rct)

        # if key_states[pg.K_0]:
        #     bomb
        #爆弾の跳ね返り
        yoko, tate = check_bound(bomb_rct, scrn_rct)   
        vx *= yoko
        vy *= tate     

        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct)

        #爆弾とこうかとんが接触時に爆破
        global touch
        #touch = 0
        if tori_rct.colliderect(bomb_rct):
            blow_rct.center = bomb_rct.center
            scrn_sfc.blit(blow_sfc, blow_rct)
            #3回まで接触可能にする(爆弾の色も変える)
            # if touch == 0:
            #     bomb_sfc = pg.Surface((20, 20))
            #     bomb_sfc.set_colorkey((0, 0, 0))
            #     pg.draw.circle(bomb_sfc, (255, 250, 0), (bomb_rct.centerx, bomb_rct.centery), 10)
            #     bomb_rct = bomb_sfc.get_rect()
            # else:
            #touch+=1
            #return
            
        pg.display.update() 
        clock.tick(1000)

if  __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()