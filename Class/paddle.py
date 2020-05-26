import pygame

BLACK = (0, 0, 0)


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, heigh):
        # Llama al constructor de la clase principal (Sprite)
        super().__init__()

        self.image = pygame.Surface([width, heigh])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # dibuja la paleta en forma de rectangulo
        pygame.draw.rect(self.image, color, [0, 0, width, heigh])

        # coloca el rectangulo con las dimenciones declaradas
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        # verificamos que no se sobrepasen los pixeles de la pantall
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        # verificamos que no se sobrepasen los pixeles de la pantall
        if self.rect.y > 400:
            self.rect.y = 400
