
def keep_bound(entity, WINDOW_HEIGHT, WINDOW_WIDTH):
    if entity.left > WINDOW_WIDTH:
        print("0 right")
        entity.right = 0
    if entity.right < 0:
        print("0 left")
        entity.left = WINDOW_WIDTH
    if entity.top > WINDOW_HEIGHT:
        print("0 bottom")
        entity.top = 0
    if entity.bottom < 0:
        print("0 top")
        entity.bottom = WINDOW_HEIGHT
