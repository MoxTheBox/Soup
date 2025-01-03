#imports
import pygame
import sys
import os

#initializations
pygame.init()
pygame.mixer.init()

#Directory List
base_path = os.path.dirname(__file__)
image_path = os.path.join(base_path, "Assets", "Soup.png")
sound_path = os.path.join(base_path, "Assets", "Soup.wav")

#Variables
image = pygame.image.load(image_path)
sound = pygame.mixer.Sound(sound_path)
screen = pygame.display.set_mode(image.get_size())
pygame.display.set_caption("Soup")
ksp = 0

#script
screen.blit(image,(0, 0))
pygame.display.flip()

sound.play(loops=-1)

#loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sound.stop()
            ksp = 0
            running = False
            pygame.quit()
            sys.exit()
        if ksp == 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ksp = 1
        if ksp == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SEMICOLON:
                    ksp = 2
        if ksp == 2:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    sound.stop()
                    ksp = 0
                    running = False
                    pygame.quit()
                    sys.exit()
#exit
pygame.quit() 
sys.exit()