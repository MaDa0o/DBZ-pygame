import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Zfight")
BLUE=(0,0,255)
FPS = 60
SPRITE_DIM = 55

GOKU = pygame.image.load(os.path.join('assets','goku.png'))
GOKU = pygame.transform.scale(GOKU,(SPRITE_DIM,SPRITE_DIM))
VEGETA = pygame.image.load(os.path.join('assets','vegeta.png'))
VEGETA = pygame.transform.scale(VEGETA,(SPRITE_DIM,SPRITE_DIM))


def draw_win():
    WIN.fill(BLUE)
    WIN.blit(GOKU,(200,250))
    WIN.blit(VEGETA,(WIDTH-200,250))
    pygame.display.update()             #we have to manually update the display when we change it

def main():
    clock=pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)                         #defining the speed of while loop so that it runs at same speed in all devices
        for event in pygame.event.get():            #checks for the events in pygame
            if event.type == pygame.QUIT:
                run=False
        
        draw_win()

    pygame.quit()

# this allows the file only to run directly run not when it was imported ,basically tells this is the main file
if __name__ == "__main__":
    main()