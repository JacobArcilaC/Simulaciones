import random, math

class CrapsGame():
	def __init__(self):
		self.statusOfGame = True
		self.winGame = ""
		self.releases = []
		self.game()

	def game(self):
		while(self.statusOfGame):
			throwDice = random.randint(1,6) + random.randint(1, 6)
			self.releases.append(throwDice)
			if((throwDice in [7, 11]) and len(self.releases) == 1):
				self.winGame = True
				self.statusOfGame = False
			elif((throwDice in [4 ,5, 6, 8, 9, 10]) and  
				(throwDice== self.releases[0]) and (len(self.releases ) > 1)):
				self.winGame = True
				self.statusOfGame = False
			elif(throwDice in [2, 3, 12] and len(self.releases) == 1):
				self.winGame = False
				self.statusOfGame = False
			elif(throwDice == 7 and len(self.releases) > 1):
				self.winGame = False
				self.statusOfGame = False

	def getNumberOfReleases(self):
		return len(self.releases) 

	def isWinGame(self):
		return self.winGame

	def getReleases(self):
		return self.releases	
 
def  runSimulation(numberOfGames):
	listOfCrapsGames = []
	for i in range(0, numberOfGames):
		game = CrapsGame()
		listOfCrapsGames.append(game)
	return listOfCrapsGames

def getStaticsOfSimulation(listOfCrapsGames):
	numberOfWins = 0
	totalOfReleases = 0
	for game in listOfCrapsGames:
		if(game.isWinGame()):
			totalOfReleases += len(game.getReleases())
			numberOfWins += 1
	probWin = numberOfWins/len(listOfCrapsGames)
	promReleasesToWin = totalOfReleases/numberOfWins
	print("La Probabilidad de Ganar el Juego es de: ", probWin)
	print("La Probabilidad de Perder el Juego es de: ", 1 - probWin)
	print("El numero Promedio de lanzamientos antes de Ganar es: ", math.ceil(promReleasesToWin))

numberOfGames = int(input("Ingrese el numero de Simulaciones a realizar del juego "))
listOfGames = runSimulation(numberOfGames)
getStaticsOfSimulation(listOfGames)	