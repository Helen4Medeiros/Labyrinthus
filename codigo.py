# Labyrinthus 
# Componentes: Kelvin e Helena
# Professor: Alexandre Gomes de Lima

import pygame
pygame.init()
janela=pygame.display.set_mode((640,640))
clock=pygame.time.Clock()

# VARIÁVEIS
inicio_bola_um= (200, 560)
inicio_bola_dois= (490, 560)
vel_bola= 4
fase=1

# FONTES
fonte_titulo = pygame.font.Font("BryndanWriteBook-nGPM.ttf", 80)
fonte_texto = pygame.font.Font("ARIAL.TTF", 26)

# TELA INICIAL
def tela_inicial():
    running= True
    while running:
        janela.fill((0, 0, 0))

        ponto= pygame.Surface((35,35), pygame.SRCALPHA)
        pygame.draw.circle(ponto, (235,255,20),(17.5,17.5), 8.75)
        titulo= fonte_titulo.render("LABYRINTHUS", True, (12, 192, 223))
        enter= fonte_texto.render("Aperte ENTER para iniciar", True, (255, 255, 255))

        janela.blit(ponto, (300, 250))
        janela.blit(titulo, (320 - titulo.get_width()// 2, 270))
        janela.blit(enter, (320 - enter.get_width()// 2, 500))

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
        mensagem2= fonte_texto.render('Aperte ENTER para fechar o jogo', True, (255, 255, 255))

        janela.blit(titulo, (320 - titulo.get_width() // 2, 270)) 
        janela.blit(mensagem, (320 - mensagem.get_width() // 2, 350))    
        janela.blit(mensagem2, (320 - mensagem2.get_width() // 2, 500))   

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
        self.rect=self.image.get_rect(topleft=inicio_bola_um)

    def mover_esq(self):
        self.rect.x-=vel_bola
    def mover_di(self):
        self.rect.x+=vel_bola
    def mover_cima(self):
        self.rect.y-=vel_bola
    def mover_baixo(self):
        self.rect.y+=vel_bola
    def reseta_pos(self,fase):
        if fase==1:
            self.rect.topleft=inicio_bola_um
        else:
            self.rect.topleft=inicio_bola_dois

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

#FASE1
bola = BolaSprite()
fim_um= RedSprite(440,40,80,40)

paredes_um= pygame.sprite.Group(
    ParedesSprite(0, 0, 640, 40),
    ParedesSprite(0, 40, 440, 240),
    ParedesSprite(520, 40, 120, 160),
    ParedesSprite(600, 40, 40, 600),
    ParedesSprite(0, 240, 560, 200),
    ParedesSprite(0, 440, 160, 280),
    ParedesSprite(280, 520, 320, 120)
)

#FASE2
fim_dois= RedSprite(160, 40, 40, 40)
paredes_dois=pygame.sprite.Group(
    ParedesSprite(0, 0 , 640, 40), # 1
    ParedesSprite(0, 40, 160, 560), # 2
    ParedesSprite(200, 40, 280, 120), # 3
    ParedesSprite(480, 40, 120, 120), # 4
    ParedesSprite(560, 40, 80, 600), # 5 
    ParedesSprite(160, 200, 320, 80), # 6
    ParedesSprite(240, 320, 80, 240), # 7
    ParedesSprite(320, 320, 280, 120), # 8
    ParedesSprite(400, 480, 80, 160), # 9
    ParedesSprite(0, 600, 440, 40) # 10
)

paredes_atuais = paredes_um
fim_atual = fim_um
todos_sprites = pygame.sprite.Group(paredes_atuais, fim_atual, bola)

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

    if pygame.sprite.spritecollide(bola, paredes_atuais, False):
        bola.reseta_pos(fase)

    if pygame.sprite.collide_rect(bola, fim_atual):
        if fase == 1:
            fase = 2
            paredes_atuais = paredes_dois
            fim_atual = fim_dois
            bola.reseta_pos(fase)
        else:
            running = False

    janela.fill((12, 192, 223))
    todos_sprites = pygame.sprite.Group(paredes_atuais, fim_atual, bola)
    todos_sprites.draw(janela)
    pygame.display.flip()
    clock.tick(60)

tela_final()
pygame.quit()

