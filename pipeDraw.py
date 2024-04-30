import pygame as pg
import pygame
import sys
''' Programmer: Ivan Zakharov '''
sc = pg.display.set_mode((990, 520))
pygame.display.set_caption("Отрисовка трубы")

programIcon = pygame.image.load('icon.png')

pygame.display.set_icon(programIcon)

from time import sleep

data = [] #variable with file 
with open("data.txt") as f:
    for line in f:
        data.append([float(x) for x in line.split()])
pg.display.update()
# Constant color value
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
y = 0 #temp coordinate
x = 0 #temp coordinate
pg.draw.rect(sc, WHITE, (0, 0, 1000, 250))
pg.draw.rect(sc, WHITE, (0, 270, 1000, 520))
clock = pygame.time.Clock()
def drawpixel(x, y):
  pg.draw.rect(sc, RED, (10*x, 10*y, 10, 10))
v = 0
pygame.init()
pygame.mixer.init()

print(data)
f.close()
print(x)
done = False
while not done:
  clock.tick(360)
  for event in pygame.event.get(): #leave if pressed escape 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  data = []
  with open("data.txt") as f:
      for line in f:
         data.append([float(x) for x in line.split()])
  f.close()
  for i in range(len(data)):  
    b = data[i] #current list from main list
    print('b', b)
    for n in range(len(b)):
      v = b[n] # value from current list of main list
      print('v', v)
     
      pg.display.update()
      drawpixel(i,  v-1)
  sleep(1)
  
pygame.quit()