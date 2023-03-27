import pygame
import random
from keep_bound import keep_bound
from keep_separate import keep_separate


pygame.init()

# Set up the game window
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Fox Hunt')

# Load the assets
forest_img = pygame.transform.scale(pygame.image.load('assets/forest.jpeg'), ( WINDOW_WIDTH, WINDOW_HEIGHT,))
fox_img = pygame.transform.scale(pygame.image.load('assets/fox.png'), (50, 50))
rabbit_img = pygame.transform.scale(pygame.image.load('assets/rabbit.png'), (50, 50))

# Set up the fox and rabbit initial positions
fox_rect = fox_img.get_rect(center=(250,250))
rabbit_rect = rabbit_img.get_rect(center=(350 , 350 ))

# Define the game loop
clock = pygame.time.Clock()
running = True
FOX_SPEED=15
RABBIT_SPEED=15
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

            # Wrap the fox and rabbit around the screen
            keep_bound(fox_rect, WINDOW_HEIGHT, WINDOW_WIDTH)
            keep_bound(rabbit_rect, WINDOW_HEIGHT, WINDOW_WIDTH)
            keep_separate(rabbit_rect, fox_rect)
        
        # Draw the game objects
        window.blit(forest_img, (0, 0))
        window.blit(fox_img, fox_rect)
        window.blit(rabbit_img, rabbit_rect)
        pygame.display.update()
    
