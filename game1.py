import pygame
import sys
import random

pygame.init()

# Screen
width, height = 800, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Interactive Smilies")

# Font
font = pygame.font.SysFont("Segoe UI Emoji", 60)

# Load sound (optional)
try:
    sound = pygame.mixer.Sound("click.wav")  # add any .wav file
except:
    sound = None

# Emoji list
emoji_list = ["😊", "😢", "😠", "😲"]

# Smiley object
smiley = {
    "emoji": "😊",
    "x": 300,
    "y": 100,
    "vy": 0,   # vertical speed (gravity)
    "dragging": False
}

gravity = 0.5
clock = pygame.time.Clock()

# Game loop
while True:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 🖱️ Mouse click → change emoji + sound
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            if abs(mouse_x - smiley["x"]) < 40 and abs(mouse_y - smiley["y"]) < 40:
                smiley["emoji"] = random.choice(emoji_list)

                if sound:
                    sound.play()

                smiley["dragging"] = True

        if event.type == pygame.MOUSEBUTTONUP:
            smiley["dragging"] = False

        if event.type == pygame.MOUSEMOTION:
            if smiley["dragging"]:
                smiley["x"], smiley["y"] = event.pos

    # 🌍 Gravity effect
    if not smiley["dragging"]:
        smiley["vy"] += gravity
        smiley["y"] += smiley["vy"]

    # Bounce from bottom
    if smiley["y"] > height - 50:
        smiley["y"] = height - 50
        smiley["vy"] *= -0.7

    # Draw emoji
    text = font.render(smiley["emoji"], True, (0, 0, 0))
    screen.blit(text, (smiley["x"], smiley["y"]))

    pygame.display.update()
    clock.tick(60)