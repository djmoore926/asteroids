import pygame
import json
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score

'''
-- track high scores
-- display time
-- make player hitbox triangular
'''
user = ""

with open("highscores.json", "r") as file:
    highscores = json.load(file)

highscores = sorted(highscores, key=lambda x: list(x.values())[0], reverse=True)

def check_highscores(score):
    global user, highscores
    for entry in highscores:
        for v in entry.values():
            if score > v:
                print("You set a new highscore!")
                highscores.append({user: score})
                highscores = sorted(highscores, key=lambda x: list(x.values())[0], reverse=True)
                save_highscores()
                return
            
def save_highscores():
    global highscores
    while len(highscores) > 3:
        lowest_score = min(highscores, key=lambda x: list(x.values())[0])
        highscores.remove(lowest_score)
    print("Highscores:")
    for entry in highscores:
        for key, value in entry.items():
            print(f"{key} - {value}")
    with open("highscores.json", "w") as file:
        json.dump(highscores, file)

def game_over(score):
    print("Game over!")
    print(f"You scored: {int(score)}")
    check_highscores(score)
    

def main():
    global user
    print("Highscores:")
    for entry in highscores:
        for key, value in entry.items():
            print(f"{key} - {value}")
    user = input("Please enter your name (This is for highscore tracking): ")
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    score = Score()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over(int(score.value))
                return
        
        for _ in updateable:
            _.update(dt)


        for asteroid in asteroids:
            if asteroid.collide(player):
                game_over(int(score.value))
                return
            
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()
                    score.increase(asteroid.radius)

        screen.fill("black")

        score.update(dt)
        score.draw(screen)

        for _ in drawable:
            _.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60fps
        dt = clock.tick(60) / 1000
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()