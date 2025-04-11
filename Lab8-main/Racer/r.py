import pygame
import random

pygame.init()

WIDTH = 400
HEIGHT = 600
FPS = 60
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

background = pygame.image.load("C:\pp2\Lab8-main\Street.png")
player_img = pygame.image.load("C:\pp2\Lab8-main\Player.png")
enemy_img = pygame.image.load("C:\pp2\Lab8-main\Enemy.png")
coin_img = pygame.image.load("C:\pp2\Lab8-main\coin.png")
coin_img = pygame.transform.scale(coin_img, (30, 30))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 80)
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 40:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH - 40:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)
        self.speed = 5

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), -random.randint(100, 300))
        self.speed = 4

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.rect.top = -random.randint(100, 300)
            self.rect.center = (random.randint(40, WIDTH - 40), self.rect.top)

player = Player()
enemy = Enemy()
coin1 = Coin()
coin2 = Coin()

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coin1, coin2)
enemies.add(enemy)
coins.add(coin1, coin2)

font = pygame.font.SysFont("Verdana", 20)
coin_count = 0

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.move()
    enemy.move()
    for coin in coins:
        coin.move()

    if pygame.sprite.spritecollideany(player, enemies):
        collision_sound.play()
        pygame.quit()
        print("Game Over")
        break

    collected_coins = pygame.sprite.spritecollide(player, coins, False)
    for coin in collected_coins:
        coin_count += 1
        coin.rect.top = -random.randint(100, 300)
        coin.rect.center = (random.randint(40, WIDTH - 40), coin.rect.top)

    win.blit(background, (0, 0))
    for entity in all_sprites:
        win.blit(entity.image, entity.rect)

    score_text = font.render(f"Coins: {coin_count}", True, BLACK)
    win.blit(score_text, (WIDTH - 120, 10))

    pygame.display.update()

pygame.quit()
