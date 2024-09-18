# Connect 4 Bot

Este proyecto es una implementación del clásico juego **Conecta 4**, donde una persona juega contra un bot que utiliza el algoritmo **Minimax** con poda alfa-beta para tomar decisiones óptimas.


## Requisitos

Para ejecutar el proyecto necesitarás:

- **Python 3.x**
- **Numpy**


## Cómo jugar

Para iniciar el juego, simplemente ejecuta el archivo `game.py`:

```bash
python game.py
```

El juego se desarrolla en la terminal, donde el jugador selecciona una columna para colocar su ficha, y el bot responde con su movimiento calculado usando el algoritmo Minimax.

### Controles

1. El juego te pedirá que ingreses el número de la columna (del 0 al 6) en la que deseas colocar tu ficha.
2. Después de cada turno, el bot hará su movimiento y se mostrará el tablero actualizado.
3. El juego termina cuando uno de los jugadores consigue alinear 4 fichas (horizontal, vertical o diagonalmente).
