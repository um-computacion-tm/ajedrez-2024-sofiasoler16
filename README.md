# ajedrez-2024-sofiasoler16

# 

# CircleCI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-sofiasoler16/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-sofiasoler16/tree/main)


# Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/7a6c7d161292b5366766/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-sofiasoler16/maintainability)

# Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/7a6c7d161292b5366766/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-sofiasoler16/test_coverage)


## Descripción

Este proyecto es una implementación del juego de ajedrez utilizando Python, ejecutable mediante Docker, se han modificado algunas reglas tradicionales del juego, las cuales se describen a continuación.

## Reglas del Juego

El ajedrez es un juego de estrategia para dos jugadores, que se juega sobre un tablero de 8x8 casillas alternas en colores claros y oscuros. 
Cada jugador controla 16 piezas con el objetivo de capturar al rey del oponente. Sin embargo, en esta versión del juego se han implementado algunas reglas adicionales:

### Reglas Tradicionales

1. **Objetivo del Juego**: 
En esta versión del juego, el objetivo es eliminar todas las piezas del oponente.

2. **Movimiento de las Piezas**:
   - **Peón**: Avanza una casilla hacia adelante, pero captura en diagonal. Puede moverse dos casillas hacia adelante en su primer movimiento.
   - **Torre**: Se mueve horizontal o verticalmente cualquier número de casillas.
   - **Caballo**: Se mueve en forma de "L", dos casillas en una dirección y una en perpendicular.
   - **Alfil**: Se mueve diagonalmente cualquier número de casillas.
   - **Dama**: Combina los movimientos de la torre y el alfil.
   - **Rey**: Se mueve una casilla en cualquier dirección.

3. **Captura**: Una pieza se captura moviéndose a la casilla que ocupa la pieza del oponente. La pieza capturada es retirada del tablero.

5. **Coronación del Peón**: Cuando un peón alcanza la última fila, puede intercambiar un apieza comida por el oponente

### Reglas Personalizadas

1. **Finalización del Juego**:
   - Los jugadores pueden optar por terminar la partida cuando uno de ellos responda "no" a la pregunta `Do You Want to continue playing?`. Si un jugador decide finalizar la partida voluntariamente, el juego termina en empate.
   - El juego también puede terminar cuando un jugador captura las 16 piezas del oponente. 

2. **Promoción de Peón**:
   - Cuando un peón alcanza la última fila, puede intercambiarse por una pieza previamente capturada por el oponente.

## Instrucciones para Ejecutar el Juego

Este proyecto está preparado para ejecutarse mediante Docker. A continuación, se detallan los pasos para su correcta ejecución:

### Requisitos Previos

Asegúrate de tener instalado Docker en tu sistema. Puedes consultar la documentación oficial de Docker para su instalación: [Docker Installation Guide](https://docs.docker.com/get-docker/).

### Clonación del Repositorio

Clona el repositorio en tu máquina local usando el siguiente comando:

git clone https://github.com/tu-usuario/ajedrez-2024-sofiasoler16.git
cd ajedrez-2024-sofiasoler16

### Para construir la imagen Docker del juego, ejecuta el siguiente comando:
docker buildx build -t ajedrez-2024-sofiasoler16 .

### Una vez construida la imagen, puedes ejecutar el juego con el siguiente comando:
docker run -i ajedrez-2024-sofiasoler16

