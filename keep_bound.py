
def keep_bound(entity, WINDOW_HEIGHT, WINDOW_WIDTH):
    if entity.left > WINDOW_WIDTH:
        entity.right = 0
    if entity.right < 0:
        entity.left = WINDOW_WIDTH
    if entity.top > WINDOW_HEIGHT:
        entity.bottom = 0
    if entity.bottom < 0:
        entity.top = WINDOW_HEIGHT
