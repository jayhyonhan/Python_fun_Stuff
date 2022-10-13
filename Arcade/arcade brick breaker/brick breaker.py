import pygame

pygame.init()
screen = pygame.display.set_mode((1300, 1000), 0, 32)
brickimg = pygame.image.load("C:/Users/love_/Desktop/jay/Python/Games/Arcade/arcade brick breaker/brick.png")
squareimg = pygame.image.load("C:/Users/love_/Desktop/jay/Python/Games/Arcade/arcade brick breaker/square.png")
paddleimg = pygame.image.load("C:/Users/love_/Desktop/jay/Python/Games/Arcade/arcade brick breaker/paddle.png")
paddle = paddleimg.get_rect()
bricks = [brickimg.get_rect(), brickimg.get_rect(), brickimg.get_rect(), brickimg.get_rect(), brickimg.get_rect(), brickimg.get_rect(), brickimg.get_rect(), brickimg.get_rect(), brickimg.get_rect(), brickimg.get_rect(), brickimg.get_rect(), brickimg.get_rect(), brickimg.get_rect()]
for i in range(len(bricks)):
    bricks[i].center = (i * 100 + 50, 30)
square = squareimg.get_rect()
square.center = (500, 100)
paddle.center = (650, 1000)
yspeed = 1
xspeed = -1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if square.bottom >= 1000:
        pygame.quit()
    if square.colliderect(paddle) or square.top <= 0:
       yspeed = -yspeed
    if square.left <= 0 or square.right >= 1300:
        xspeed = -xspeed
    a = []
    for i in bricks:
        if square.colliderect(i):
            yspeed = -yspeed
            a.append(i)
    for i in a:
        bricks.remove(i)
    square.move_ip(xspeed, yspeed)
    paddle.move_ip(pygame.mouse.get_pos()[0] - paddle.x, 0)
    screen.fill((200, 200, 200))
    for i in range(len(bricks)):
        screen.blit(brickimg, bricks[i])
    screen.blit(squareimg, square)
    screen.blit(paddleimg, paddle)
    pygame.display.flip()
    if len(bricks) == 0:
        pygame.quit()