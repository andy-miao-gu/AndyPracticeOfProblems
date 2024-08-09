import pygame as py
import random

py.init()

WIDTH, HEIGHT = 800, 600
win = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Rotating Cube")

WHITE = (255, 255, 255)

# Load the image (replace 'your_image_file.png' with the path to your image)
image = py.image.load('PART 2/Twelveth part/0F1176E2-22CE-4840-8B1D-6DC411FAC43A.png').convert_alpha()
original_width, original_height = image.get_width(), image.get_height()

# Initial position of the image
rect_x, rect_y = (WIDTH - original_width) // 2, (HEIGHT - original_height) // 2

# Rotation angle and speed
angle = 0
rotation_speed = 2

# Movement speed
movement_speed = 2

# Dictionary to store the state of each key
keys_pressed = {py.K_LEFT: False, py.K_RIGHT: False, py.K_UP: False, py.K_DOWN: False,
                py.K_w: False, py.K_a: False, py.K_s: False, py.K_d: False}

running = True
clock = py.time.Clock()

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN:
            if event.key in keys_pressed:
                keys_pressed[event.key] = True
        elif event.type == py.KEYUP:
            if event.key in keys_pressed:
                keys_pressed[event.key] = False

    # Rotate the image if left or right keys are held down
    if keys_pressed[py.K_LEFT]:
        angle += rotation_speed
    if keys_pressed[py.K_RIGHT]:
        angle -= rotation_speed

    # Move the image if WASD keys are held down
    if keys_pressed[py.K_w]:
        rect_y -= movement_speed
    if keys_pressed[py.K_s]:
        rect_y += movement_speed
    if keys_pressed[py.K_a]:
        rect_x -= movement_speed
    if keys_pressed[py.K_d]:
        rect_x += movement_speed

    win.fill(WHITE)

    # Rotate the image
    rotated_image = py.transform.rotate(image, angle)

    # Calculate the new position of the rotated image
    rect_x_rotated = rect_x + (original_width - rotated_image.get_width()) // 2
    rect_y_rotated = rect_y + (original_height - rotated_image.get_height()) // 2

    # Blit the rotated image onto the window surface
    win.blit(rotated_image, (rect_x_rotated, rect_y_rotated))

    py.display.flip()

    clock.tick(60)

py.quit()
