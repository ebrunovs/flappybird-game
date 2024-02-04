import pygame
import os
#from flappybird import IMAGEM_PASSARO

IMAGEM_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird3.png')))
]

class Passaro:
    IMGS = IMAGEM_PASSARO
    
    # Animações da rotação
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5
    
    def __init__(self, x, y) -> None:
        self.x = x;
        self.y = y;
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]
        
    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y
    
    def mover(self):
        # calcular o deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo
        
        # restringir o deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2
        
        self.y += deslocamento
        
        # angulo do passaro
        if deslocamento < 0 or self.y <  (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO

    def desenhar(self, tela):
        # defini qual imagem do passaro usar
        self.contagem_imagem += 1
        
        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem >= self.TEMPO_ANIMACAO*4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0
            
        #se o passaro estiver caindo nao bater asas
        if self.angulo <= -80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO
        
        # desenhar imagem
        imagem_rotacioanda = pygame.transform.rotate(self.imagem, self.angulo)
        posicao_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacioanda.get_rect(center=posicao_centro_imagem)
        tela.blit(imagem_rotacioanda, retangulo.topleft)
        
    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)