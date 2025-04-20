import pygame
import sys

#inicializa o game
pygame.init()

#define as dimenções da tela
WIDTH, HEIGHT = 1200, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dia 2 - Pong")


#Define as cores
WHITE = (230,230,255)
BLACK = (10, 10, 40)

#Cria as paddles e a bola
paddle_width, paddle_height = 15, 100
ball_size = 30

#Posições iniciais
player1 = pygame.Rect(30, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
player2 = pygame.Rect(WIDTH - 45, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2, ball_size, ball_size)

#Velocidade das paddles e da bola
player_speed = 8
ball_speed_x = 6
ball_speed_y = 6

# Fonte para pontuação
font = pygame.font.SysFont("Arial", 36)
score1 = 0
score2 = 0

#loop principal
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    #Eventos do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Movimentação dos jogadores
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= player_speed
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += player_speed
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= player_speed
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += player_speed

    #Movimento da bola
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #Colisão com o topo e base
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    #Colisão com os jogadores
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1.05
        


    #Verifica Pontuação
    if ball.left <= 0:
        score2 += 1
        ball.center = (WIDTH //2, HEIGHT //2)
        pygame.time.delay(1000)
        ball_speed_x = -6
        ball_speed_y = 6
    if ball.right >= WIDTH:
        score1 += 1
        ball.center = (WIDTH //2, HEIGHT //2)
        pygame.time.delay(1000)
        ball_speed_x = 6
        ball_speed_y = 6

    #Desenho dos Elementos
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    #Renderiza a pontuação
    text1 = font.render(str(score1), True, WHITE)
    text2 = font.render(str(score2), True, WHITE)
    screen.blit(text1, (WIDTH //4, 20))
    screen.blit(text2, (WIDTH *3 //4, 20))

    #Atualiza a tela
    pygame.display.flip()
    clock.tick(60)

    #define tecla para encerrar o jogo
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

pygame.quit()
sys.exit()