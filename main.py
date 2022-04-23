from pygame import *

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 120:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 120:
            self.rect.y += self.speed


back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
display.set_caption('Ping pong')

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('racket1.png', 30, 200, 4, 12, 150)
racket2 = Player('racket2.png', 550, 200, 4, 12, 150)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        if not finish:
            window.fill(back)

            racket1.update_1()
            racket2.update_r()

            racket1.reset()
            racket2.reset()


    display.update()
    clock.tick(FPS)
