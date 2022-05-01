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
    def update_l(self):
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
 
racket1 = Player('racket1.png', 30, 200, 4, 12, 120)
racket2 = Player('racket2.png', 550, 200, 4, 12, 120)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)
 
speed_x, speed_y = 3, 4
score1, score2 = 0, 0

font.init()
font = font.Font(None, 35)
score = font.render('0 : 0', True, (0, 0, 0))
lose = font.render('', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
 
    if not finish:
        window.fill(back)
 
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
 
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        if ball.rect.y < 0 or ball.rect.y > win_height - 50:
            speed_y *= -1    

        if ball.rect.x < 0:
            score2 += 1
            ball.rect.x, ball.rect.y = 200, 200
            speed_x, speed_y = 5, 6

        if ball.rect.x > win_width - 50:
            score1 += 1
            ball.rect.x, ball.rect.y = 200, 200
            speed_x, speed_y = 5, 6

        score = font.render(f'{score1} : {score2}', True, (0, 0, 0))
        window.blit(score, (285, 0))
        racket1.reset()
        racket2.reset()
        ball.reset()

        if score1 >= 5:
            lose = font.render('Player 2 lost!', True, (180, 0, 0))
            finish = True
            window.blit(lose, (250, 200))
        if score2 >= 5:
            lose = font.render('Player 1 lost!', True, (180, 0, 0))
            finish = True
            window.blit(lose, (250, 200))

    else:
        finish = False
        time.delay(5000)
        ball.rect.x, ball.rect.y = 200, 200
        speed_x, speed_y = 5, 6
        score1, score2 = 0, 0
        racket1.rect.y, racket2.rect.y = 200, 200

    display.update()
    clock.tick(FPS)
