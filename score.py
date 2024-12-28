import pygame
from constants import *

class Score():
    def __init__(self):
        self.value = 0
        self.time = 0
        self.font = pygame.font.Font(None, 35) # None uses the default font, and 50 is the font size.

    def update(self, dt):
        self.value += dt

    def increase(self, hit):
        if hit == ASTEROID_MIN_RADIUS: # define these
            self.value += 10
        if hit == ASTEROID_MIN_RADIUS * 2:
            self.value += 5
        if hit == ASTEROID_MAX_RADIUS:
            self.value += 3

    def draw(self, screen):
        score_text = self.font.render(f"Score:  {int(self.value)}", True, WHITE)
        screen.blit(score_text, (585, 10))  # Draw text at the top-left corner
