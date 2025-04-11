import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

color = BLACK
radius = 5
mode = 'free'
drawing = False
start_pos = None

screen.fill(WHITE)
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            if mode == 'free':
                pygame.draw.circle(screen, color, event.pos, radius)

        elif event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            drawing = False
            if mode == 'rect':
                rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                pygame.draw.rect(screen, color, rect, width=2)
            elif mode == 'circle':
                center = start_pos
                radius_c = int(((end_pos[0]-center[0])**2 + (end_pos[1]-center[1])**2) ** 0.5)
                pygame.draw.circle(screen, color, center, radius_c, width=2)

        elif event.type == pygame.MOUSEMOTION:
            if drawing and mode == 'free':
                pygame.draw.circle(screen, color, event.pos, radius)
            elif drawing and mode == 'eraser':
                pygame.draw.circle(screen, WHITE, event.pos, radius)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = 'rect'
            elif event.key == pygame.K_c:
                mode = 'circle'
            elif event.key == pygame.K_f:
                mode = 'free'
            elif event.key == pygame.K_e:
                mode = 'eraser'
            elif event.key == pygame.K_1:
                color = RED
            elif event.key == pygame.K_2:
                color = GREEN
            elif event.key == pygame.K_3:
                color = BLUE
            elif event.key == pygame.K_4:
                color = BLACK
            elif event.key == pygame.K_5:
                color = WHITE

    pygame.display.flip()

pygame.quit()