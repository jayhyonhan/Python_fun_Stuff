import pygame, random, time # import modules

#init pygame & clock & music
pygame.init()
pygame.font.init()
pygame.time.get_ticks()
pygame.mixer.music.load('Without Fear.ogg')
pygame.mixer.music.play(-1, 0.0, 5000)
Clock = pygame.time.Clock()

# set screen size 
screen_width = 1000
screen_height = 1000

#set classes
class Enemy1():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 44
        self.hp = 2
        self.img = enemy_img1

class Enemy2():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 52
        self.hp = 5
        self.img = enemy_img2

class Enemy3():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 67
        self.hp = 6
        self.img = enemy_img3

class Enemy4():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 68
        self.hp = 9
        self.img = enemy_img4

class Enemy5():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 67
        self.hp = 12
        self.img = enemy_img5

class Boss():
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.hp = hp

class missile():
    def __init__(self, x, y):
        self.x = x
        self.y = y

# load sound
Explosion = pygame.mixer.Sound("./explosion.mp3")
Laserblast = pygame.mixer.Sound("./LaserBlast.mp3")

screen = pygame.display.set_mode((screen_width, screen_height)) # uhh... it literally says 'screen' there...

# set variables
level = 1
bg_img = pygame.image.load("./spacebg.jpg")
player_x = 0
player_y = 0
player_img = pygame.image.load("./spaceship.png") # 101x77
player_bullet_count = 2
player_damage = 1
enemy_img1 = pygame.image.load("./normal spaceships/spaceship-1.png")
enemy_img2 = pygame.image.load("./normal spaceships/spaceship-2.png")
enemy_img3 = pygame.image.load("./normal spaceships/spaceship-3.png")
enemy_img4 = pygame.image.load("./normal spaceships/spaceship-4.png")
enemy_img5 = pygame.image.load("./normal spaceships/spaceship-5.png")
missile_img = pygame.image.load("missile (2).png")
laser_img = pygame.image.load("./laser.png")
boss_img = pygame.image.load("./boss.png") #670x390
explosion_img = pygame.image.load("./explosion.png")
my_font = pygame.font.Font("./MeowScript-Regular.ttf", 72)
my_font1 = pygame.font.Font("./DancingScript-Regular.ttf", 36)
enemies = []
laser_positions = []
play = True
time = 0
bg1_y = 0
bg2_y = -1000
score = 0
armor = 5
temp = 0
temp1 = False
BossSpawn = False
boss = Boss(screen_width//2 - 335, 195, 50)
mouse_is_down = False
dead_enemy = []
temp2 = []
missiles = []


# Particle system
class Particle:
    def __init__(self, pos):
        self.x, self.y = pos[0], pos[1]
        self.vx, self.vy = 0, 10
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

def draw():
    dust.append(Dust((player_x + 50, player_y + 77)))

dust = []

enemy_spawn_posibilities = [Enemy1, Enemy1, Enemy1, Enemy1, Enemy1, Enemy1, Enemy2, Enemy2, Enemy3, Enemy3, Enemy3, Enemy4, Enemy4, Enemy5]

# main game loop
while play:
    # set text
    scoretext = my_font.render("SCORE: %d"%score, True, (217, 74, 74))
    armortext = my_font.render("ARMOR: %d"%armor, True, (245, 206, 49))
    gameovertext = my_font.render("GAME OVER", True, (219, 46, 46))
    leveltext = my_font1.render("level: %d"%level, True, (252, 255, 92))

    level = score // 100 + 1 # level increases every 50 scores

    # background scrolling
    bg1_y += 0.5
    bg2_y += 0.5

    time += Clock.tick() # this is self-explanatory

    # this is for bosses. every 60000 milliseconds(1min) this code spawns the boss
    if -10 <= time % 60000 <= 10 and not BossSpawn:
        BossSpawn = True
        boss = Boss(screen_width//2 - 335, 195, 50)

    # spawn enemies
    if -10 <= time%(3000/level) <= 10 and not(BossSpawn):
        enemies.append(random.choice(enemy_spawn_posibilities)(random.randint(32, 968), -64))
        enemies[-1].x = random.randint(0, screen_width - 44)
    
    # get mouse positions
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]

    # event check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            c_time = time
            mouse_is_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_is_down = False
    if mouse_is_down and (-10 <= (time - c_time)% 250 <= 10):
        Laserblast.play()
        temp = time
        temp1 = True
        if int(player_bullet_count) % 2 == 0:
            for i in range(int(player_bullet_count) // 2):
                laser_positions.append([mouse_x + (i+1)*16, player_y])
            for i in range(int(player_bullet_count) // 2):
                laser_positions.append([mouse_x - (i+1)*16, player_y])
        elif int(player_bullet_count) % 2 == 1:
            for i in range(int(player_bullet_count) // 2):
                laser_positions.append([mouse_x + (i+1)*16, player_y])
            for i in range(int(player_bullet_count) // 2):
                laser_positions.append([mouse_x - (i+1)*16, player_y])
            laser_positions.append([mouse_x, player_y])
    
    # rifle-like shooting
    if time - temp >= 500 and temp1 == True:
        Laserblast.stop()
        temp1 = False
    
    # set the player position to mouse position
    player_x = mouse_x - 50
    player_y = mouse_y - 39

    # again, this is for backgound scrolling
    if bg1_y >= 1000:
        bg1_y = -1000
    if bg2_y >= 1000:
        bg2_y = -1000
    
    # you do have to draw the backgound.
    screen.blit(bg_img, (0, bg1_y))
    screen.blit(bg_img, (0, bg2_y))

    screen.blit(player_img, (player_x, player_y)) # do you want the player invisible? Actually, that would be pretty cool.

    if (BossSpawn):
        missiles.append(missile(boss.x+100, boss.y))
        missiles.append(missile(boss.x+50, boss.y))
        missiles.append(missile(boss.x, boss.y))
        missiles.append(missile(boss.x-50, boss.y))
        missiles.append(missile(boss.x-100, boss.y))

    # check for collisions with bullets and enemies
    for i in laser_positions:
        for j in enemies:
            if (0 <= (i[0] - j.x) <= j.size) & (abs(j.y - i[1]) <= j.size):
                j.hp -= player_damage
                try:
                    laser_positions.remove(i)
                except:
                    pass
                score += 1
        if BossSpawn:
            if (0 <= (i[0] - boss.x) <= 670) & (abs(boss.y - i[1]) <= 390):
                boss.hp -= 0.5
                if boss.hp <= 0:
                    BossSpawn = False
                    level += 1
                    score += 100
                    player_bullet_count += 1
                try:
                    laser_positions.remove(i)
                except:
                    pass
    
    # check collisions between player and enemies
    for i in enemies:
        if (i.hp <= 0):
            Explosion.play()
            dead_enemy.append(i)
            temp2.append(time)
            enemies.remove(i)
            player_bullet_count += 0.05
        if (0 <= (player_y - i.y) <= i.size):
            if ((player_x - i.x)>=0 and (player_x - i.x) <= i.size) or ((i.x - player_x)>=0 and (i.x - player_x) <= 101): # yeah, pretty hard huh? I was sooooo STUPID that I DIDN'T apply the rect object to the player.
                armor -= 1
                enemies.remove(i)
                if armor < 0:
                    screen.blit(gameovertext, (300, 500))
                    pygame.display.update()
                    pygame.time.delay(5000)
                    play = False
    
    # show explosion
    for i in dead_enemy:
        if (time-temp2[dead_enemy.index(i)]) <= 1000:
            screen.blit(pygame.transform.scale(explosion_img, (abs(i.size), abs(i.size))), (i.x, i.y))
    else:
        temp3 = False
    
    # draw enemies and bullets
    for i in enemies:
        i.y += 1
        screen.blit(i.img, (i.x, i.y))
        if i.y >= 1000:
            enemies.remove(i)
    for i in laser_positions:
        i[1] -= 8
        screen.blit(laser_img, (i[0], i[1]))
        if i[1] <= 0:
            laser_positions.remove(i)
    
    # draw the rocket flame
    draw()
    for i in range(len(dust)):
        if len(dust[i].particles) > 0:
            dust[i].draw(screen)
            dust[i].update()
    
    # score text and armor text
    screen.blit(scoretext, (100, 50))
    screen.blit(armortext, (500, 50))
    screen.blit(leveltext, (460, 0))

    # draw boss
    if BossSpawn:
        screen.blit(boss_img, (boss.x, boss.y))
        for i in missiles: 
            screen.blit(missile_img, (i.x, i.y))
    
    # this was for testing purposes
    print(player_bullet_count)

    pygame.display.update() # this is also self explanatory

pygame.quit() # uhh... seriously?