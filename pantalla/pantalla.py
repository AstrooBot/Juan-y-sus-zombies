import pygame
import sys

FPS = 60

x = 0

W, H = 900, 490

screen = pygame.display.set_mode((W, H))

# Reloj para controlar la velocidad de actualización del juego
RELOJ = pygame.time.Clock()


def main():
    x = 0
    pygame.init()

    background_image = pygame.image.load("../imagenes/fondo.jpg").convert()

    # Titulo del juego cuando se ejecuta
    pygame.display.set_caption("RESIDENT EVIL 3")

    # Bucle principal del juego
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Calcula la posición relativa del fondo para hacer un desplazamiento continuo
        x_relativa = x % background_image.get_rect().width

        # Dibuja la imagen de fondo en la pantalla
        screen.blit(background_image, (x_relativa -
                    background_image.get_rect().width, 0))
        pygame.display.update()

        # Dibuja la imagen de fondo nuevamente para hacer el desplazamiento continuo
        if x_relativa < W:
            screen.blit(background_image, (x_relativa, 0))

        # Desplazamiento horizontal del fondo
        x -= 1

        # Controla la velocidad del juego
        RELOJ.tick(FPS)


if __name__ == '__main__':
    main()
