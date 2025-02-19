# Labyrinthus 
# Componentes: Kelvin e Helena
# Professor: Alexandre

import pygame
pygame.init()
janela=pygame.display.set_mode((640,640))
clock=pygame.time.Clock()

# VARIÁVEIS
inicio_bola= (200, 560)
vel_bola= 7

# BOLA
class BolaSprite(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image=pygame.Surface((50,50), pygame.SRCALPHA)
        pygame.draw.circle(self.image,(235,255,20),(25,25), 15)
        self.rect= self.image.get_rect(topleft=(x,y))
    
    def colisao(self, new_rect):
        return pygame.sprite.spritecollideany(self, paredes)

    def mover_para_esq(self, new_rect):
        new_rect.x -= vel_bola
    def mover_para_di(self, new_rect):
        new_rect.x += vel_bola 
    def mover_para_cima(self, new_rect):
        new_rect.y -= vel_bola
    def mover_para_baixo(self, new_rect):
        new_rect.y += vel_bola

    def mov(self, keys):
        new_rect= self.rect.copy()
        if keys[pygame.K_LEFT]:
            self.mover_para_esq(new_rect)
        if keys[pygame.K_RIGHT]:
            self.mover_para_di(new_rect)
        if keys[pygame.K_UP]:
            self.mover_para_cima(new_rect)
        if keys[pygame.K_DOWN]:
            self.mover_para_baixo(new_rect)

        if not self.colisao(new_rect):
            self.rect= new_rect
        else:
            self.rect.topleft= inicio_bola

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
bola = BolaSprite(inicio_bola[0], inicio_bola[1])
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
    bola.update(keys, paredes)

    if pygame.sprite.collide_rect(bola,fim):
        running= False

    janela.fill((95,255,202))
    todos_sprites.draw(janela)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()