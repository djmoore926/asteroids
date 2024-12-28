import pygame
from constants import *

class Score():
    def __init__(self):
        self.value = 0
        self.seconds = 0
        self.minutes = 0
        self.score_font = pygame.font.Font(None, 35) # None uses the default font, and 50 is the font size.
        self.time_font = pygame.font.Font(None, 25)

    def update(self, dt):
        self.value += dt * 2
        self.seconds += dt
        if self.seconds > 60:
            self.minutes += 1
            self.seconds %= 60


    def increase(self, hit):
        if hit == ASTEROID_MIN_RADIUS: # define these
            self.value += 10
        if hit == ASTEROID_MIN_RADIUS * 2:
            self.value += 5
        if hit == ASTEROID_MAX_RADIUS:
            self.value += 3

    def draw(self, screen):
        score_text = self.score_font.render(f"Score:  {int(self.value)}", True, "white")
        screen.blit(score_text, (585, 10))  # Draw text at the top-left corner

        time_text = self.time_font.render(f"Time:  {int(self.minutes)}:{self.seconds:05.2f}", True, "white")
        screen.blit(time_text, (585, 690))

    def get_time(self):
        return f"{int(self.minutes)}:{self.seconds:05.2f}"