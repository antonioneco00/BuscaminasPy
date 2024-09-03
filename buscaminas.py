import random
from colorama import init, Fore

init()


class Buscaminas:
    def __init__(self, matriz, minas, isInitialized, gameOver, userChoices):
        self._matriz = matriz
        self._minas = minas
        self.isInitialized = isInitialized
        self._gameOver = gameOver
        self.userChoices = userChoices

    @property
    def matriz(self):
        return self._matriz

    @matriz.setter
    def matriz(self, value):
        unknownCells = 0
        lastChoice = self.userChoices[len(self.userChoices) - 1]
        msg = f"Has seleccionado las coordenadas [{lastChoice[1]}, {lastChoice[0]}]. Continua la partida"

        for i in range(len(self._matriz)):
            for j in range(len(self._matriz[0])):
                self._matriz[i][j] = self.nearbyMinas(i, j)

                if self.isUnknownCell(i, j) and [i, j] not in self.userChoices:
                    self._matriz[i][j] = f"{Fore.LIGHTBLACK_EX}?{Fore.RESET}"
                    unknownCells += 1

        if unknownCells == 3:
            self._gameOver = True

            msg = "Enhorabuena! Has ganado 🎉"

        for choice in self.userChoices:
            if choice in self._minas:
                self._matriz[choice[0]][choice[1]] = f"{Fore.RED}x{Fore.RESET}"
                self._gameOver = True

                msg = "Has explotado una mina ❌ Fin de la partida"

        if self.isInitialized:
            self.printScheme(msg)

        self.isInitialized = True

    @property
    def minas(self):
        return self._minas

    @minas.setter
    def minas(self, userChoice):
        userY, userX = userChoice

        for i in range(len(self._minas)):
            while True:
                newMina = [random.randint(0, 4), random.randint(0, 4)]

                if newMina not in self._minas and newMina != [userY, userX]:
                    self._minas[i] = newMina

                    break
                else:
                    print("La mina se repite o coincide con el usuario")

    @staticmethod
    def setCoord(message):
        while True:
            choice = input(message)

            if choice.isdigit() and int(choice) >= 0 and int(choice) < 5:
                break

            print("Por favor, introduzca coordenadas entre 0 y 4 (ambos incluidos)")
        return int(choice)

    def printScheme(self, msg):
        print()

        color = Fore.YELLOW

        for i in self._matriz:
            for j in i:
                match j:
                    case 0:
                        color = Fore.YELLOW
                    case 1:
                        color = Fore.BLUE
                    case 2:
                        color = Fore.GREEN
                    case _:
                        color = Fore.RED
                print(f"{color}{j}{Fore.RESET}", end=" ")

            print()

        print()
        print(msg)

    def nearbyMinas(self, x, y):
        minaCount = 0

        for mina in self._minas:
            distToMinaX = abs(mina[0] - x)
            distToMinaY = abs(mina[1] - y)

            if distToMinaX <= 1 and distToMinaY <= 1:
                minaCount += 1

        return minaCount

    def isUnknownCell(self, x, y):
        isUnknown = True

        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i >= 0 and j >= 0 and i < 5 and j < 5:
                    if self.matriz[i][j] == 0:
                        isUnknown = False

        return isUnknown
