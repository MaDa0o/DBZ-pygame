import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("CONNECT4")

def main():
    run = True
    while run:
        for event in pygame.event.get():            #checks for the events in pygame
            if event.type == pygame.QUIT:
                run=False

#while loop ends here
                pygame.quit()

# this allows the file only to run directly run not when it was imported ,basically tells this is the main file
if __name__ == "__main__":
    main()