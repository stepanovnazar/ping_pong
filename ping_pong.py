#Создай собственный Шутер!
from pygame import *
from random import *
from time import time as tm

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Пинг понг')
background = transform.scale(image.load('background.jpg'), (700, 500))


clock = time.Clock()
FPS = 60
font.init()



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y>0:
            self.rect.y-= self.speed
        if keys_pressed[K_s] and self.rect.y<430:
           self.rect.y+= self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y>0:
            self.rect.y-= self.speed
        if keys_pressed[K_DOWN] and self.rect.y<430:
           self.rect.y+= self.speed





font = font.SysFont('Arial',35)
win = font.render('YOU WIN!', True, (0,255,0))
loose = font.render('YOU LOSE!', True, (255,0,0))
player_l = Player('racket.png', 10,400, 10, 30,70)
player_r = Player('racket.png',670,400,10,30,70)




game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        player_l.update_l()
        player_l.reset()
        player_r.update_r()
        player_r.reset()

    
    display.update()
    clock.tick(FPS)

