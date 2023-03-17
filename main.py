import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Zfight")
BLUE=(0,0,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)
PURPLE=(255,0,255)
FPS = 60
SPRITE_DIM = 55
VEL = 5
BLAST_VEL=8
BORDER=pygame.Rect(WIDTH//2 -5, 0, 10, HEIGHT)
MAX_BLAST = 3

GOKU_HIT = pygame.USEREVENT +1
VEGETA_HIT = pygame.USEREVENT +2

GOKU = pygame.image.load(os.path.join('assets','goku.png'))
GOKU = pygame.transform.scale(GOKU,(SPRITE_DIM,SPRITE_DIM))             #resizing the sprites
VEGETA = pygame.image.load(os.path.join('assets','vegeta.png'))
VEGETA = pygame.transform.scale(VEGETA,(SPRITE_DIM,SPRITE_DIM))


def draw_win(gok, veg, gok_blast, veg_blast):
    WIN.fill(BLUE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(GOKU,(gok.x,gok.y))                #adding the sprites to the display, every object is called a surface in python
    WIN.blit(VEGETA,(veg.x,veg.y))

    for blast in gok_blast:
          pygame.draw.rect(WIN, YELLOW, blast)
    for blast in veg_blast:
          pygame.draw.rect(WIN, PURPLE, blast)

    pygame.display.update()                 #we have to manually update the display when we change it

def move_goku(keys_pressed,gok):
    if(keys_pressed[pygame.K_a]) and gok.x - VEL >0:    #move goku left
            gok.x -= VEL
    if(keys_pressed[pygame.K_d]) and gok.x + VEL < WIDTH/2 -60:    #move goku right
            gok.x += VEL
    if(keys_pressed[pygame.K_w]) and gok.y -VEL >0:    #move goku up
            gok.y -= VEL
    if(keys_pressed[pygame.K_s]) and gok.y + VEL <500 -55:    #move goku down
            gok.y += VEL

def move_vegeta(keys_pressed,veg):
    if(keys_pressed[pygame.K_LEFT]) and veg.x - VEL > WIDTH/2 +5:    #move vegeta left
            veg.x -= VEL
    if(keys_pressed[pygame.K_RIGHT]) and veg.x + VEL < 900 -55:    #move vegeta right
            veg.x += VEL
    if(keys_pressed[pygame.K_UP]) and veg.y - VEL > 0:    #move vegeta up
            veg.y -= VEL
    if(keys_pressed[pygame.K_DOWN]) and veg.y - VEL < 500 -55:    #move vegeta down
            veg.y += VEL

def blast_handle(gok_blast, veg_blast, gok, veg):
      for blast in gok_blast:
            blast.x += BLAST_VEL
            if veg.colliderect(blast):
                  pygame.event.post(pygame.event.Event(VEGETA_HIT))
                  gok_blast.remove(blast) 
            elif blast.x>= WIDTH:
                  gok_blast.remove(blast)
                      
      for blast in veg_blast:
            blast.x -= BLAST_VEL
            if gok.colliderect(blast):
                  pygame.event.post(pygame.event.Event(GOKU_HIT))
                  veg_blast.remove(blast)
            elif blast.x<= 0:
                  veg_blast.remove(blast)

def main():
    gok = pygame.Rect(200, 250, SPRITE_DIM, SPRITE_DIM)
    veg = pygame.Rect(WIDTH-200, 250, SPRITE_DIM, SPRITE_DIM)

    gok_blast = []
    veg_blast = []

    clock=pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)                             #defining the speed of while loop so that it runs at same speed in all devices
        for event in pygame.event.get():            #checks for the events in pygame
            if event.type == pygame.QUIT:
                run=False

            if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_LCTRL and len(gok_blast) <=MAX_BLAST:
                        blast = pygame.Rect(gok.x + gok.width, gok.y + gok.height//2 -2 ,10,5)
                        gok_blast.append(blast)
                  if event.key == pygame.K_RCTRL and len(veg_blast) <=MAX_BLAST :
                        blast = pygame.Rect(veg.x, veg.y + veg.height//2 -2 ,10,5)
                        veg_blast.append(blast)

        print(gok_blast,veg_blast)
        keys_pressed = pygame.key.get_pressed()
        move_goku(keys_pressed,gok)
        move_vegeta(keys_pressed,veg)
        blast_handle(gok_blast,veg_blast,gok,veg)

        draw_win(gok,veg,gok_blast,veg_blast)

    pygame.quit()

# this allows the file only to run directly run not when it was imported ,basically tells this is the main file
if __name__ == "__main__":
    main()