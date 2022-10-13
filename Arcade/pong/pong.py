import pygame, random

pygame.init()
wn = pygame.display.set_mode((1288, 839))
pygame.display.set_caption("PONG GAME")
pygame.display.flip()

def reset():
    wn.fill((200, 200, 200))
    for i in range(len(dust)):
        if len(dust[i].particles) > 0:
            dust[i].draw(wn)
            dust[i].update()
    wn.blit(barimg, bar)
    wn.blit(ballimg, ball)
    wn.blit(scoreCountTxt, scoreCountTxtRect)
    pygame.display.flip()

barimg = pygame.image.load("C:/Users/love_/Desktop/jay/Python/Games/Arcade/pong/pong bar.png")
ballimg = pygame.image.load("C:/Users/love_/Desktop/jay/Python/Games/Arcade/pong/ball.png")
bar = barimg.get_rect()
ball = ballimg.get_rect()
bar.center = (bar.x + bar.width / 2 - 40, bar.y + bar.height / 2 + 500)
ball.center = (random.randint(400, 600), random.randint(400, 600))
yspeed = 1
xspeed = -1
level = 0

font = pygame.font.Font("C:/Users/love_/Desktop/jay/Python/Games/Arcade/pong/Roboto-Black.ttf", 224)
font1 = pygame.font.Font("C:/Users/love_/Desktop/jay/Python/Games/Arcade/pong/Roboto-Black.ttf", 50)
text1 = font.render("LEVEL UP!", True, (220, 220, 220), (200, 200, 200))
textRect1 = text1.get_rect()
textRect1.center = (634, 500)

class Particle:
    def __init__(self, pos):
        self.x, self.y = pos[0], pos[1]
        self.vx, self.vy = -xspeed * 2, -yspeed * 2
        self.rad = 10

    def draw(self, win):
        pygame.draw.circle(win, (random.randrange(200, 255), random.randrange(100, 130), 50), (self.x, self.y), self.rad)
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        if random.randint(0, 100) < 40:
            self.rad -= 1

class Dust:
    def __init__(self, pos):
        self.pos = pos
        self.particles = []
        for i in range(10):
            self.particles.append(Particle(self.pos))

    def update(self):
        for i in self.particles:
            i.update()
            self.particles = [particle for particle in self.particles if particle.rad > 0]

    def draw(self, win):
        for i in self.particles:
            i.draw(win)

def draw(rect):
    dust.append(Dust(rect.center))

dust = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    scoreCountTxt = font1.render("score: " + str(level), True, (230, 230, 230), (200, 200, 200))
    scoreCountTxtRect = scoreCountTxt.get_rect()
    scoreCountTxtRect.center = (634, 200)
    
    wn.blit(scoreCountTxt, scoreCountTxtRect)
    
    if ball.bottom >= 839:
        yspeed = -yspeed
    if ball.top <= 0:
       yspeed = -yspeed
    if ball.right >= 1288:
        xspeed = -xspeed
    if ball.left <= 0:
        pygame.quit()
    
    if ball.colliderect(bar):
        level += 1
        xspeed = (level // 10 + 1) * abs(xspeed) / xspeed + abs(xspeed) / xspeed
        yspeed = (level // 10 + 1) * abs(yspeed) / yspeed + abs(yspeed) / yspeed
        xspeed = -xspeed
        ball.move_ip(xspeed, yspeed)
    
    ball.move_ip(xspeed, yspeed)
    bar.y = pygame.mouse.get_pos()[1] - bar.width / 2
    #bar.y = ball.y + ball.height / 2 - bar.height / 2
    reset()
    draw(ball)

    for i in range(len(dust)):
        if len(dust[i].particles) > 0:
            dust[i].draw(wn)
            dust[i].update()
    wn.blit(ballimg, ball)
    wn.blit(barimg, bar)
    pygame.display.update()