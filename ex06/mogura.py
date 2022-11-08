import pygame as pg
import sys
from random import randint

class Screen:
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title) #モグラたたき
        self.sfc = pg.display.set_mode(wh) #(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) #"fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

class hole:
    def __init__(self,color, x, y, width, height):
        
                self.sfc = pg.Surface((x*2, y*2)) # 空のSurface
                self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
                pg.draw.ellipse(self.sfc, color, (x, y, width, height)) # 円を描く
                self.rct = self.sfc.get_rect()
                self.rct.center = (x, y) # 900, 400

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr:Screen):
        self.blit(scr)

class mogra:
    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) 
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) 
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
        
        self.up = False
        self.appearing = False
        self.hiting = True 

    def appear(self):
        '''モグラを穴から出す'''
        self.appearing = True

    def update(self, scr:Screen):
        '''更新'''
        if self.appearing:
            self.blit(scr)
        else:
            pass
        if self.hiting:
            self.appearing = False
            not self.blit(scr)
    
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def hit():
        pass

def main():
    for event in pg.event.get():
            if (event.type == pg.MOUSEBUTTONDOWN) and (event.button == 1) :
                if moguradata.rect.collidepoint(event.pos):
                    mogra.update
                    pass
    # スクリーン生成
    scr = Screen("モグラたたき", (1600, 900), "fig/pg_bg.jpg") # スクリーン名、サイズ、読み込む画像
    moguradata = []
    
    clock = pg.time.Clock()
    scr.blit()
    for i in range(5):
            for j in range(4):
                hl = hole((1, 0, 0), 150+(i)*300, 300+(j-1)*200, 150, 100)
                hl.update(scr)
                moguradata.append(mogra("fig/mogura.png", 0.2, (hl.rct.centerx+75, hl.rct.centery+30)))
    while True:
        
        for i in range(20):
            a = randint(1,1000)
            if a == 1:
                moguradata[i].appear()
                moguradata[i].update(scr)


        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return
        pg.display.update() #練習2
        clock.tick(1000)

if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()