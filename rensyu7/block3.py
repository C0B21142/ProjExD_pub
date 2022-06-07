import pygame
from pygame.locals import *
import sys
import math
import pygame.mixer

# 画面サイズ
SCREEN = Rect(0, 0, 1600, 900)

# パドルクラス
class Paddle(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert()
        self.image = pygame.transform.rotozoom(self.image,0,2)
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN.bottom - 20          # パドルのy座標

    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]  # マウスのx座標をパドルのx座標に
        self.rect.clamp_ip(SCREEN)                     # ゲーム画面内のみで移動

# ボールクラス
class Ball(pygame.sprite.Sprite):
    def __init__(self, filename, paddle, blocks, speed,angle_left, angle_right):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert()
        self.image = pygame.transform.rotozoom(self.image,0,0.2)
        self.image.set_colorkey((255, 255, 255))    #C0B21094 colorkeyを設定
        self.rect = self.image.get_rect()
        self.dx = self.dy = 0  # ボールの速度
        self.paddle = paddle  # パドルへの参照
        self.blocks = blocks  # ブロックグループへの参照
        self.update = self.start # ゲーム開始状態に更新
        self.speed = speed # ボールの初期速度
        self.angle_left = angle_left # パドルの反射方向(左端:135度）
        self.angle_right = angle_right # パドルの反射方向(右端:45度）


    # ゲーム開始状態（マウスを左クリック時するとボール射出）
    def start(self):
        # ボールの初期位置(パドルの上)
        self.rect.centerx = self.paddle.rect.centerx
        self.rect.bottom = self.paddle.rect.top

        # 左クリックでボール射出
        if pygame.mouse.get_pressed()[0] == 1:
            self.dx = 0
            self.dy = -self.speed
            self.update = self.move
    

    # ボールの挙動
    def move(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        hp =3

        # 壁との反射
        
        if self.rect.left < SCREEN.left:    # 左側
            self.rect.left = SCREEN.left
            self.dx = -self.dx              # 速度を反転
        if self.rect.right > SCREEN.right:  # 右側
            self.rect.right = SCREEN.right
            self.dx = -self.dx
        if self.rect.top < SCREEN.top:      # 上側
            self.rect.top = SCREEN.top
            self.dy = -self.dy
        if self.rect.colliderect(self.paddle.rect) and self.dy > 0:
            self.dy = -self.dy
            self.hit = 0
            (x1, y1) = (self.paddle.rect.left - self.rect.width, self.angle_left)
            (x2, y2) = (self.paddle.rect.right, self.angle_right)
            x = self.rect.left                                      # ボールが当たった位置
            y = (float(y2-y1)/(x2-x1)) * (x - x1) + y1              # 線形補間
            angle = math.radians(y)                                 # 反射角度
            self.dx = self.speed * math.cos(angle)
            self.dy = -self.speed * math.sin(angle)

        if self.rect.top > SCREEN.bottom:
            self.update = self.start                    # ボールを初期状態に
            hp -= 1
            if hp == 0:
                return


        # ボールと衝突したブロックリストを取得（Groupが格納しているSprite中から、指定したSpriteと接触しているものを探索）
        blocks_collided = pygame.sprite.spritecollide(self, self.blocks, True)
        if blocks_collided:  # 衝突ブロックがある場合
            oldrect = self.rect
            for block in blocks_collided:
                # ボールが左からブロックへ衝突した場合
                if oldrect.left < block.rect.left and oldrect.right < block.rect.right:
                    self.rect.right = block.rect.left
                    self.dx = -self.dx
                    
                # ボールが右からブロックへ衝突した場合
                if block.rect.left < oldrect.left and block.rect.right < oldrect.right:
                    self.rect.left = block.rect.right
                    self.dx = -self.dx

                # ボールが上からブロックへ衝突した場合
                if oldrect.top < block.rect.top and oldrect.bottom < block.rect.bottom:
                    self.rect.bottom = block.rect.top
                    self.dy = -self.dy

                # ボールが下からブロックへ衝突した場合
                if block.rect.top < oldrect.top and block.rect.bottom < oldrect.bottom:
                    self.rect.top = block.rect.bottom
                    self.dy = -self.dy
        return self.dx,self.dy

       # 反転




# ブロッククラス
class Block(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert()
        self.image = pygame.transform.rotozoom(self.image,0,0.3)
        self.image.set_colorkey((255, 255, 255))    # C0B21094 ブロックにcolorkeyを設定
        self.rect = self.image.get_rect()
        # ブロックの左上座標
        self.rect.left = SCREEN.left + x * self.rect.width
        self.rect.top = SCREEN.top + y * self.rect.height


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN.size)
    #C0B21094 背景画像を設定
    bg_img = pygame.image.load("fig/toQtorisakjuR.jpg")
    bg_rect = bg_img.get_rect()
    screen.blit(bg_img, bg_rect)

    # 描画用のスプライトグループ
    group = pygame.sprite.RenderUpdates()  

    # 衝突判定用のスプライトグループ
    blocks = pygame.sprite.Group()   

    # スプライトグループに追加    
    Paddle.containers = group
    Ball.containers = group
    Block.containers = group, blocks

    # パドルの作成
    paddle = Paddle("fig/8.png")

    # ブロックの作成
    for x in range(1, 28):
        for y in range(1, 5):
            Block("fig/block2.png", x, y)


    # ボールを作成
    Ball("fig/ダウンロード.jpg",paddle, blocks,  15, 135, 45)
    
    clock = pygame.time.Clock()
    

    while (1):
        clock.tick(60)      # フレームレート(60fps)
        # 背景真っ白から鳥取砂丘に
        # screen.fill((255,255,255))
        screen.blit(bg_img, bg_rect)
        # 全てのスプライトグループを更新
        group.update()
        # 全てのスプライトグループを描画       
        group.draw(screen)
        # 画面更新 
        pygame.display.update()
        # キーイベント（終了）
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


            

if __name__ == "__main__":
    main()