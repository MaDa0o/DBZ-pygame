import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Zfight")
BLUE=(0,0,255)
FPS = 60
SPRITE_DIM = 55
VEL = 5

GOKU = pygame.image.load(os.path.join('assets','goku.png'))
GOKU = pygame.transform.scale(GOKU,(SPRITE_DIM,SPRITE_DIM))             #resizing the sprites
VEGETA = pygame.image.load(os.path.join('assets','vegeta.png'))
VEGETA = pygame.transform.scale(VEGETA,(SPRITE_DIM,SPRITE_DIM))


def draw_win(gok, veg):
    WIN.fill(BLUE)
    WIN.blit(GOKU,(gok.x,gok.y))                #adding the sprites to the display, every object is called a surface in python
    WIN.blit(VEGETA,(veg.x,veg.y))
    pygame.display.update()                 #we have to manually update the display when we change it

def main():
    gok = pygame.Rect(200, 250, SPRITE_DIM, SPRITE_DIM)
    veg = pygame.Rect(WIDTH-200, 250, SPRITE_DIM, SPRITE_DIM)

    clock=pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)                             #defining the speed of while loop so that it runs at same speed in all devices
        for event in pygame.event.get():            #checks for the events in pygame
            if event.type == pygame.QUIT:
                run=False
        keys_pressed = pygame.key.get_pressed()

        if(keys_pressed[pygame.K_a]):    #move goku left
            gok.x -= VEL
        if(keys_pressed[pygame.K_d]):    #move goku left
            gok.x += VEL
        if(keys_pressed[pygame.K_w]):    #move goku left
            gok.y -= VEL
        if(keys_pressed[pygame.K_s]):    #move goku left
            gok.y += VEL

        draw_win(gok,veg)

    pygame.quit()

# this allows the file only to run directly run not when it was imported ,basically tells this is the main file
if __name__ == "__main__":
    main()