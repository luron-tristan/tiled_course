import pygame, sys
from pytmx.util_pygame import load_pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
tmx_data = load_pygame("data/tmx/basic.tmx")
print(dir(tmx_data))

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  screen.fill("black")
  pygame.display.update()