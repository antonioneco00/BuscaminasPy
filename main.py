from buscaminas import Buscaminas

GAME_SIZE = 5

matriz = []
for i in range(GAME_SIZE):
    row = [0] * GAME_SIZE
    matriz.append(row)

minas = [[0, 0] for _ in range(3)]
game = Buscaminas(matriz, minas, False, False, [])

while not game._gameOver:
    userX = Buscaminas.setCoord("Introduce una coordenada X: ")
    userY = Buscaminas.setCoord("Introduce una coordenada Y: ")

    game.userChoices.append([userX, userY])

    if not game.isInitialized:
        game.minas = (userX, userY)
        game.matriz = game.matriz

    game.matriz = game.matriz
