import streamlit as st
import pygame
import random

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clase para la pelotita
class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = 5
        self.speed_y = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x - self.radius > 0:
            self.x -= self.speed_x
        if keys[pygame.K_RIGHT] and self.x + self.radius < WIDTH:
            self.x += self.speed_x
        if keys[pygame.K_UP] and self.y - self.radius > 0:
            self.y -= self.speed_y
        if keys[pygame.K_DOWN] and self.y + self.radius < HEIGHT:
            self.y += self.speed_y

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)

# Clase para los cuadritos
class Square:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = WHITE

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

def run_game():
    # Configuración de la pantalla
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pelotita y Cuadritos")

    # Reloj para controlar la velocidad del juego
    clock = pygame.time.Clock()

    # Crear la pelotita
    ball = Ball(WIDTH // 2, HEIGHT // 2, 15)

    # Crear cuadritos aleatorios
    squares = [Square(random.randint(0, WIDTH - 30), random.randint(0, HEIGHT - 30), 30) for _ in range(10)]

    # Bucle principal del juego
    running = True
    while running:
        screen.fill(BLACK)

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Mover y dibujar la pelotita
        ball.move()
        ball.draw(screen)

        # Dibujar y comprobar colisiones de los cuadritos
        for square in squares[:]:
            square.draw(screen)
            # Detectar colisión
            if (square.x < ball.x < square.x + square.size and
                    square.y < ball.y < square.y + square.size):
                squares.remove(square)

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad del juego
        clock.tick(60)

    # Salir de Pygame
    pygame.quit()

# Streamlit interfaz
st.title("Juego de la Pelotita y los Cuadritos")
st.write("Haz clic en el botón para iniciar el juego.")

if st.button("Iniciar Juego"):
    run_game()
