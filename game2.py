import pygame
import sys
import random

pygame.init()
pygame.mixer.init()

# Screen
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Emoji Sound Game")

# Font
font = pygame.font.SysFont("Segoe UI Emoji", 60)

# Load sounds
sounds = {
    "😊": pygame.mixer.Sound("happy.wav"),
    "😢": pygame.mixer.Sound("sad.wav"),
    "😠": pygame.mixer.Sound("angry.wav"),
    "😲": pygame.mixer.Sound("surprise.wav")
}

# Set volume (0 to 1)
for s in sounds.values():
    s.set_volume(0.5)

# Background music
pygame.mixer.music.load("bg_music.wav")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)  # loop forever

# Emoji list
emoji_list = list(sounds.keys())

# Smiley
smiley = {"emoji": "😊", "x": 300, "y": 200}

clock = pygame.time.Clock()

# Game loop
while True:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Click → change emoji + play sound
        if event.type == pygame.MOUSEBUTTONDOWN:
            smiley["emoji"] = random.choice(emoji_list)
            sounds[smiley["emoji"]].play()

        # Volume control using keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pygame.mixer.music.set_volume(1.0)   # high
            if event.key == pygame.K_DOWN:
                pygame.mixer.music.set_volume(0.1)   # low

    # Draw emoji
    text = font.render(smiley["emoji"], True, (0, 0, 0))
    screen.blit(text, (smiley["x"], smiley["y"]))

    pygame.display.update()
    clock.tick(60)