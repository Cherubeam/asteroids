import pygame
from constants import *
from player import Player

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()

  Player.containers = (updatable, drawable)

  player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

  dt = 0

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return

    # Handle player input
    for update in updatable:
      update.update(dt)

    # Clear the screen and draw the player
    screen.fill("black")

    for draw in drawable:
      draw.draw(screen)
      
    pygame.display.flip()

    # Limit the framerate to 60 FPS
    dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
