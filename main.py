import pygame
from random import randint
FPS = 60
pygame.init()

points = 0

lost = 0

wind_w = 600
wind_h = 500
window = pygame.display.set_mode((wind_w, wind_h))
pygame.display.set_caption('Doodle Jump')
clock = pygame.time.Clock()
#задай фон сцени
backgroung = pygame.image.load("background.png")
backgroung = pygame.transform.scale(backgroung, (600, 500))
pygame.mixer.music.load("canary.ogg")
pygame.mixer.music.play(-1)
exp_s = pygame.mixer.Sound("Jump 1.wav")
bullet_image = pygame.image.load("wing.png")
platforms_image = pygame.image.load("platform.png")


with open("record.txt","r",encoding="Utf-8") as file:
    record = int(file.read())

print(record)

class Sprite:

    def __init__(self, x, y,w ,h, image):
        self.rect = pygame.Rect(x, y, w, h)
        image = pygame.transform.scale(image, (w, h))
        self.image = image


    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite):
    def __init__(self, x, y,w ,h, image, speed):
        self.speed = speed
        super().__init__(x, y, w, h, image)
        self.max_jumps = 50
        self.jump_count = 0
        self.jump_power = 5
    
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, a, d):

        keys = pygame.key.get_pressed()
        if keys[d]:
            if self.rect.right < wind_w:
                self.rect.x += self.speed
        if keys[a]:
            if self.rect.left > 0:
                self.rect.x -= self.speed
    def fire(self):
        exp_s.play()
        (self.rect.x, self.rect.y,10,10,bullet_image,10)

    def jump(self):
        if self.jump_count < self.max_jumps:
            self.rect.y -= self.jump_power
            self.jump_count += 1
        else:
            pass


class Platform(Sprite):
    def __init__(self, x, y, width, height,image):
        super().__init__(x,y,width,height,image)
        platforms.append(self)

        


class Enemy(Sprite):
    def __init__(self, x , y , w , h , image , speed):
        super().__init__(x, y, w, h, image)
        self.speed = speed
        self.image_right = self.image
    def ruh(self):
        self.rect.y += self.speed
        if self.rect.y >= wind_h:
            self.rect.x = randint(0,wind_w-50)
            self.rect.y = randint(-350, -50)

# a = randint(50, 550)
# enemies = []
# for i in range(5):
#     enemies.append(Enemy(randint(0,wind_w-50), randint(-250, -50), 70, 50, meteorit_image, randint(5, 10)))

platforms = []
platforms.append(Platform(0,470,wind_w,40,platforms_image))

platform_y = 370
for i in range(4):
    platforms.append(Platform(randint(0,500),platform_y,150,40,platforms_image))
    platform_y -= 100

font = pygame.font.SysFont("Arial",50)
lose = font.render("Lose",True, (0,255,255) )

spaceship_image = pygame.image.load("wing.png")
spaceship = Player(300, 420, 50, 50, spaceship_image, 5)
game = True
finish = False
while game:
    if not finish:
        window.blit(backgroung, (0,0))
        spaceship.draw()
                            

        for platform in platforms:
            platform.draw()

        # for enemy in enemies:

        #     enemy.draw()
        #     enemy.ruh()
                  

        # if spaceship.rect.colliderect(enemy.rect):
        #      finish = True
        #      window.blit(lose,(200,150))

        spaceship.move(pygame.K_a, pygame.K_d)

        # if lost >= 5:
        #     finish = True 
        #     window.bitle(lose,(200,200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            spaceship.fire()
        
    

    pygame.display.update()
    clock.tick(FPS)