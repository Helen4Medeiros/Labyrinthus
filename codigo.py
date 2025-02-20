# Labyrinthus 
# Componentes: Kelvin e Helena
# Professor: Alexandre

import pygame
pygame.init()
janela=pygame.display.set_mode((640,640))
clock=pygame.time.Clock()

# VARIÁVEIS
inicio_bola= (200, 560)
vel_bola= 4

# BOLA
class BolaSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((35,35), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (235,255,20),(17.5,17.5), 8.75)
        self.rect=self.image.get_rect(topleft=inicio_bola)

    def mover_esq(self):
        self.rect.x-=vel_bola
    def mover_di(self):
        self.rect.x+=vel_bola
    def mover_cima(self):
        self.rect.y-=vel_bola
    def mover_baixo(self):
        self.rect.y+=vel_bola

    def reseta_pos(self):
        self.rect.topleft=inicio_bola

# LABIRINTO
class ParedesSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura):
        super().__init__()
        self.image= pygame.Surface((largura, altura))
        self.image.fill((0,0,0))
        self.rect= self.image.get_rect(topleft=(x, y))

# FIM
class RedSprite(pygame.sprite.Sprite):
    def __init__(self, x,y,largura,altura):
        super().__init__()
        self.image=pygame.Surface((largura,altura))
        self.image.fill((255,55,55))
        self.rect= self.image.get_rect(topleft=(x,y))

# SPRITES
bola = BolaSprite()
fim= RedSprite(440,40,80,40)

paredes= pygame.sprite.Group(
    ParedesSprite(0, 0, 640, 40),
    ParedesSprite(0, 40, 440, 240),
    ParedesSprite(520, 40, 120, 160),
    ParedesSprite(600, 40, 40, 600),
    ParedesSprite(0, 240, 560, 200),
    ParedesSprite(0, 440, 160, 280),
    ParedesSprite(280, 520, 320, 120)
)

todos_sprites = pygame.sprite.Group([paredes, fim, bola])

# LOOPING
running= True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running= False

    keys= pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bola.mover_esq()
    if keys[pygame.K_RIGHT]:
        bola.mover_di()
    if keys[pygame.K_UP]:
        bola.mover_cima()
    if keys[pygame.K_DOWN]:
        bola.mover_baixo()

    if pygame.sprite.spritecollide(bola, paredes, False):
        bola.reseta_pos()

    if pygame.sprite.collide_rect(bola,fim):
        running= False

    janela.fill((12, 192, 223))
    todos_sprites.draw(janela)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()