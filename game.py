import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
width, height = 800, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Smilies Game")

# Font for emoji
font = pygame.font.SysFont("Segoe UI Emoji", 60)

# Smilies
smilies = [
    {"emoji": "😊", "x": 50, "y": 100, "speed": 3},
    {"emoji": "😢", "x": 50, "y": 200, "speed": 2},
    {"emoji": "😠", "x": 50, "y": 300, "speed": 4},
    {"emoji": "😲", "x": 50, "y": 400, "speed": 2.5},
]

clock = pygame.time.Clock()

# Game loop
while True:
    screen.fill((255, 255, 255))  # white background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move and draw smilies
    for s in smilies:
        s["x"] += s["speed"]

        # Bounce back from right edge
        if s["x"] > width - 50 or s["x"] < 0:
            s["speed"] *= -1

        text = font.render(s["emoji"], True, (0, 0, 0))
        screen.blit(text, (s["x"], s["y"]))

    pygame.display.update()
    clock.tick(60)