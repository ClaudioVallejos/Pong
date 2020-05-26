import pygame
from Class.paddle import Paddle
from Class.ball import Ball

pygame.init()

BLACK = (0, 0, 0)
WHITE = (225, 225, 225)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_mode()

# atributos de la paletaB
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

# atributos de la paletaA
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

start = True

# el reloj y tiempo de la libreria de pygame
clock = pygame.time.Clock()

scoreA = 0
scoreB = 0

while start:
    # loop principal que ejecuta el juego.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
        elif event.type == pygame.K_x:
            start = False

    # instanciar y guardar la funcion que obtiene la tecla que se presiona.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)
    # logica principal del juego
    all_sprites_list.update()

    # Se verifica si la pelota rebota con cualquiera de las paredes
    if ball.rect.x >= 690:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]
    # detecta si la pelota colisiona con alguna de las paletas
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    screen.fill(BLACK)
    # Dibujar la malla
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    # pintamos las paletas
    all_sprites_list.draw(screen)

    # colocar marcador en la pantalla
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420, 10))

    # recargar la pantalla para pintar en ella
    pygame.display.flip()
    # loop para los frames
    clock.tick(60)

pygame.quit()
