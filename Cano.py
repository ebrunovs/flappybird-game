import pygame
import random
from flappybird import IMAGEM_CANO
from Passaro import Passaro

class Cano:
    DISTANCIA = 200
    VELOCIDADE = 5
    
    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True)
        self.CANO_BASE = IMAGEM_CANO
        self.passaro = False
        self.definir_altura()
        
    def definir_altura(self):
        self.altura = random.randint(50, 450)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
        self.pos_base = self.altura + self.DISTANCIA

    def mover(self):
        self.x -= self.VELOCIDADE
        
    def desenhar(self, tela):
        tela.blit(self.CANO_TOPO, (self.x, self.pos_topo))
        tela.blit(self.CANO_BASE, (self.x, self.pos_base))
        
    def colidir (self, passaro):
        pasaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.CANO_TOPO)
        base_mask = pygame.mask.from_surface(self.CANO_BASE)
        
        distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y)) 
        distancia_base = (self.x - passaro.x, self.pos_base - round(passaro.y)) 
        
        topo_ponto = pasa topo_mask = pasaro_mask.overlap(topo_mask, distancia_topo) topo_mask = pasaro_mask.overlap(topo_mask, distancia_topo)ro_mask.overlap(topo_mask, distancia_topo)
        base_ponto = pasaro_mask.overlap(base_mask, distancia_base)
        
        if base_ponto or topo_ponto:
            return True
        else:
            return False