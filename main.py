import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("CONNECT4")
BLUE=(0,0,255)
FPS = 60

def main():
    clock=pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)                         #defining the speed of while loop so that it runs at same speed in all devices
        for event in pygame.event.get():            #checks for the events in pygame
            if event.type == pygame.QUIT:
                run=False

            WIN.fill(BLUE)
            pygame.display.update()             #we have to manually update the display when we change it

    pygame.quit()

# this allows the file only to run directly run not when it was imported ,basically tells this is the main file
if __name__ == "__main__":
    main()