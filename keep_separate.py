import random

# Check if the fox catches the rabbit

def keep_separate(rabbit, fox):
    if fox.colliderect(rabbit):
        rand_x = random.randint(1, 500)
        rand_y = random.randint(1, 500)
        fox.move_ip(rand_x, rand_y)
        keep_separate(rabbit, fox)