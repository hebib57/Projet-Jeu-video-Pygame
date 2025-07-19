import pygame
import sys

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.position = [100, 600]
        self.velocity = [0, 0]  # Déplacement 
        self.image = pygame.image.load("./sprite/stop1.png") 
        self.image = pygame.transform.scale(self.image, (80, 100))  
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position  # Position initiale du rectangle

        self.walk_left = [
            pygame.image.load("./sprite/walkL1.png"),
            pygame.image.load("./sprite/walkL2.png"),
            pygame.image.load("./sprite/walkL3.png"),
            pygame.image.load("./sprite/walkL4.png")
        ]
        self.walk_right = [
            pygame.image.load("./sprite/walkR1.png"),
            pygame.image.load("./sprite/walkR2.png"),
            pygame.image.load("./sprite/walkR3.png"),
            pygame.image.load("./sprite/walkR4.png")
        ]
        self.current_walk_frame = 0  # Frame actuelle de l'animation

    def update(self):
        # Met à jour la position en fonction de la vélocité
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.rect.topleft = self.position  # Met à jour le rect pour correspondre à la position

        # Animation de marche (changer l'image selon le sens)
        if self.velocity[0] < 0:  # Si le joueur se déplace vers la gauche
            self.image = self.walk_left[self.current_walk_frame]
        elif self.velocity[0] > 0:  # Si le joueur se déplace vers la droite
            self.image = self.walk_right[self.current_walk_frame]
        else:  # Si le joueur ne bouge pas
            self.image = pygame.image.load("./sprite/stop1.png")
        
        self.image = pygame.transform.scale(self.image, (80, 100)) 
        
        # Changer de frame pour l'animation
        self.current_walk_frame += 1
        if self.current_walk_frame >= len(self.walk_left):
            self.current_walk_frame = 0  # Retour à la première image

    def move_left(self):
        self.velocity[0] = -5  # Vitesse gauche

    def move_right(self):
        self.velocity[0] = 5  # Vitesse vers la droite

    def stop(self):
        self.velocity[0] = 0  # stop le mouvement horizontal

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

ciel = pygame.image.load("./template/background.jpg")
plate_forme = pygame.image.load("./template/Texture/ground9.png")

player = Player()

running = True
while running:
    screen.blit(ciel, (0, 0))  
    
    screen.blit(player.image, player.rect.topleft)  
    pygame.display.flip()  # Met à jour l'affichage

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.move_left()
    elif keys[pygame.K_RIGHT]:
        player.move_right()
    else:
        player.stop()

    
    player.update()

    pygame.time.Clock().tick(30)  # 30 images par seconde dans la boucles

pygame.quit()
sys.exit()