from buscaminas import Buscaminas

while True:
    size = input('Seleccione el tamaño del tablero: ')

    if size.isdigit() and int(size) > 3 and int(size) < 10:
        break
matriz = []
for i in range(int(size)):
    row = [0] * int(size)
    matriz.append(row)

minas = [[0, 0] for _ in range(int(size))]
game = Buscaminas(matriz, minas, int(size), False, False, [])

while not game._gameOver:
    userX = game.setCoord("Introduce una coordenada X: ")
    userY = game.setCoord("Introduce una coordenada Y: ")

    game.userChoices.append([userY, userX])

    if not game.isInitialized:
        game.minas = (userY, userX)
        game.matriz = game.matriz

    game.matriz = game.matriz
