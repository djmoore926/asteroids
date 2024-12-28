import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score

'''
-- add scoring:
-- small asteroids are worth 5pts, med asteroids worth 3pts, large asteroids worth 1pt
-- increment 1 point for every second survived
-- display time
-- display score
-- make player hitbox triangular
'''

def main():
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
                return
        
        for _ in updateable:
            _.update(dt)


        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                print(f"You scored: {int(score.value)}")
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