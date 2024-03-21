import pygame
from pygame.locals import *

class Menu(pygame.sprite.Sprite):
    def __init__(self, fondo_img):
        super().__init__()
        self.fondo_menu = pygame.image.load("../imagenes/fondo_menu.png").convert()  # Carga la imagen de fondo
        self.image = self.fondo_menu
        self.rect = self.image.get_rect()


def pipe():
    pygame.init()
    Tamaño_pantalla = (914, 514)  # Define el tamaño de la pantalla
    screen = pygame.display.set_mode(Tamaño_pantalla)
    pygame.display.set_caption("Pantalla de Inicio")

    # Ruta de la imagen de fondo
    fondo_img = pygame.image.load("../imagenes/fondo_menu.png").convert()

    # Crear una instancia del menú con la imagen de fondo
    menu_inicio = Menu(fondo_img)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(menu_inicio.image, menu_inicio.rect)
        pygame.display.update()

        tecla = pygame.key.get_pressed()
        if tecla [K_RETURN]: 
            return True



if __name__ == "__main__":
    pipe()
