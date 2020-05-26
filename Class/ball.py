import pygame
from random import randint

BLACK = (0, 0, 0)


# Esta clase es de tipo Ball, que hereda los datos de la clase Sprite de pygame
class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Se dibuja la pelota en la pantalla como un cuadrado, pasandole las caract: color, tipo, alto, ancho
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # se obtiene la velocidad con sus vectores correspondientes
        self.velocity = [randint(4, 8), randint(-8, 8)]

        self.rect = self.image.get_rect()

        # actualizacion de las coordenadas para el movimiento de la pelota
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
