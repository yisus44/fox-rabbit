import pygame
import random
from keep_bound import keep_bound
from keep_separate import keep_separate


pygame.init()

# Set up the game window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Fox Hunt')

# Load the assets
forest_img = pygame.transform.scale(pygame.image.load('assets/forest.jpeg'), ( WINDOW_WIDTH, WINDOW_HEIGHT,))
fox_img = pygame.transform.scale(pygame.image.load('assets/fox.png'), (50, 50))
rabbit_img = pygame.transform.scale(pygame.image.load('assets/rabbit.png'), (50, 50))

# Set up the fox and rabbit initial positions
fox_rect = fox_img.get_rect(center=(250,250))
rabbit_rect = rabbit_img.get_rect(center=(350 , 250 ))

# Define the game loop
clock = pygame.time.Clock()
running = True
FOX_SPEED=50
RABBIT_SPEED=50
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
          
            distance = pygame.math.Vector2(fox_rect.center).distance_to(pygame.math.Vector2(rabbit_rect.center))
            is_near = distance < 100
            # Move the fox with the arrow keys
            if event.key == pygame.K_LEFT:
                    fox_rect.move_ip(-FOX_SPEED, 0)
                    if is_near:
                        rabbit_rect.move_ip(RABBIT_SPEED, 0)
            elif event.key == pygame.K_RIGHT:
                    fox_rect.move_ip(FOX_SPEED, 0)
                    if is_near:
                        rabbit_rect.move_ip(RABBIT_SPEED, 0)
            elif event.key == pygame.K_UP:
                    fox_rect.move_ip(0, -FOX_SPEED)
                    if is_near:
                        rabbit_rect.move_ip(0, -RABBIT_SPEED)
            elif event.key == pygame.K_DOWN:
                    fox_rect.move_ip(0, FOX_SPEED)
                    if is_near:
                        rabbit_rect.move_ip(0, RABBIT_SPEED)

            keep_separate(rabbit_rect, fox_rect)

            if rabbit_rect.left > WINDOW_WIDTH:
                print("0 right rabbit",)
                rabbit_rect.right = 50
            if rabbit_rect.right < 0:
                print("0 left rabbit",)
                rabbit_rect.left = WINDOW_WIDTH
            if rabbit_rect.top > WINDOW_HEIGHT:
                print("0 bottom rabbit",)
                rabbit_rect.top = 50
            if rabbit_rect.bottom < 0:
                print("0 top rabbit",)
                rabbit_rect.bottom = WINDOW_HEIGHT


            if fox_rect.left > WINDOW_WIDTH:
                print("0 right, fox")
                fox_rect.right = 0
            if fox_rect.right < 0:
                print("0 left, fox")
                fox_rect.left = WINDOW_WIDTH
            if fox_rect.top > WINDOW_HEIGHT:
                print("0 botto, foxm")
                fox_rect.top = 0
            if fox_rect.bottom < 0:
                print("0 top, ox"),
                fox_rect.bottom = WINDOW_HEIGHT
        
        
        clock.tick(60)
        # Draw the game objects
        window.blit(forest_img, (0, 0))
        window.blit(fox_img, fox_rect)
        window.blit(rabbit_img, rabbit_rect)
        pygame.display.update()
    
