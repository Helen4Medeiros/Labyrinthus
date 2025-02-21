# Labyrinthus 
# Componentes: Kelvin e Helena
# Professor: Alexandre Gomes de Lima

import pygame
pygame.init()
janela=pygame.display.set_mode((640,640))
clock=pygame.time.Clock()

# VARIÁVEIS
inicio_bola= (200, 560)
vel_bola= 4

# FONTES
fonte_titulo = pygame.font.Font("BryndanWriteBook-nGPM.ttf", 80)
fonte_texto = pygame.font.Font("ARIAL.TTF", 20)

# TELA INICIAL
def tela_inicial():
    running= True
    while running:
        janela.fill((0, 0, 0))
        pygame.display.set_caption("Labyrinthus")
        
        fase = fonte_texto.render('Fase 1', True, 'White')
        titulo= fonte_titulo.render("LABYRINTHUS", True, (12, 192, 223))
        enter= fonte_texto.render("Aperte ENTER para iniciar", True, (255, 255, 255))

        janela.blit(fase, (29,5))
        janela.blit(titulo, (320 - titulo.get_width()// 2, 270))
        janela.blit(enter, (320 - enter.get_width()// 2, 400))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()

            if event.type==pygame.KEYDOWN and event.key==pygame.K_RETURN:
                running = False

# TELA FINAL
def tela_final():
    rodando = True
    while rodando:
        janela.fill((0, 0, 0))

        titulo = fonte_titulo.render("PARABÉNS!", True, (235, 255, 20))
        mensagem = fonte_texto.render("Você zerou o jogo!", True, (255,255,255))
        
        janela.blit(titulo, (320 - titulo.get_width() // 2, 270)) 
        janela.blit(mensagem, (320 - mensagem.get_width() // 2, 380))    

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.KEYDOWN and event.key==pygame.K_RETURN:
                return

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

tela_inicial()

# LOOPING DO JOGO
running= True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running= False

    # MOVENDO A BOLA
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

tela_final()
pygame.quit()

