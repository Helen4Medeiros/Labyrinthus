# Labyrinthus 
# Componentes: Kelvin e Helena
# Professor: Alexandre

import pygame
pygame.init()
janela=pygame.display.set_mode((640,640))
clock=pygame.time.Clock()

# BOLA
# class BolaSprite(pygame.sprite.Sprite):
#    def __init__(self):
#        pygame.sprite.Sprite(self)
#    bola_img= pygame.image.load('bola.png').convert_alpha()
#    bola_img= pygame.transform.scale(bola_img, (10,10))
#    bola_rect= bola_img.get_rect()
#    bola_rect.bottomleft=(50, 500)

# FASE 1 - LABIRINTO
fase1_img= pygame.image.load('fase1.png').convert_alpha()
fase1_img= pygame.transform.scale(fase1_img,(640,640))
fase1_rect= fase1_img.get_rect()
fase1_rect.center=(0,0)

# bola= pygame.sprite.Sprite.add(BolaSprite())

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    janela.fill((95,255,202))
    
    janela.blit(fase1_img, fase1_rect.center)
#    bola.draw(janela)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()