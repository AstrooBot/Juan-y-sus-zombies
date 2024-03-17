Propósito del código:

Este código simula un fondo desplazable para el videojuego juan y sus zombies, Crea el efecto de fondo en movimiento al copiar continuamente (dibujar) una imagen de fondo de izquierda a derecha a través de la pantalla.

Importaciones:

pygame: La biblioteca principal utilizada para crear juegos en Python.
sys: Proporciona acceso a parámetros y funciones específicos del sistema, utilizados aquí para salir del programa.
Constantes:

FPS: Establece los fotogramas deseados por segundo para la animación, con el objetivo de lograr 60 FPS suaves.
W: Define el ancho de la ventana del juego en píxeles (900 píxeles).
H: Define la altura de la ventana del juego en píxeles (490 píxeles).
Variables:

pantalla: Representa la ventana del juego creada usando pygame.display.setmode().
RELOJ: Una instancia de pygame.time.Clock() utilizada para controlar la velocidad de fotogramas y garantizar una animación fluida.
Función main():

Inicializa Pygame usando pygame.init().
Carga la imagen de fondo del archivo "imagenes/fondo.jpg" y la convierte a un formato más eficiente para su visualización usando pygame.image.load().convert().
Establece el título de la ventana del juego a "RESIDENT EVIL 3" con pygame.display.setcaption().
Bucle Principal:

El bucle while 1: asegura que el juego continúe ejecutándose hasta que el usuario lo cierre.
Dentro del bucle:
Procesa todos los eventos pendientes usando pygame.event.get().
Busca el evento QUIT (el usuario cierra la ventana) y sale del programa si se detecta usando sys.exit().
Calcula la posición x relativa de la imagen de fondo en función del valor actual de x y el ancho de la imagen:
xrelativa = x % backgroundimage.get_rect().width
Copia (blit) la imagen de fondo dos veces para crear un efecto de desplazamiento continuo:
Primero, copia la imagen comenzando desde la posición x_relativa calculada, asegurándose de que se envuelva hacia el lado izquierdo cuando llegue al final de la pantalla.
En segundo lugar, la vuelve a copiar comenzando desde x_relativa si aún no ha llegado al borde derecho de la ventana.
Actualiza la posición x restándole 1 para simular que el fondo se mueve hacia la izquierda.
Limita el valor de x para evitar que el fondo se mueva más allá de su ancho.
Actualiza la pantalla usando pygame.display.update() para mostrar los cambios realizados en la pantalla.
Usa RELOJ.tick(FPS) para mantener la velocidad de fotogramas deseada, asegurando una animación fluida.

Diagrama de flujo: 
