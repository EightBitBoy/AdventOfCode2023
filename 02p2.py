NUM_RED = 12
NUM_GREEN = 13
NUM_BLUE = 14

class Game:
    def __init__(self, id):
        self.id = id
        self.rounds = []
    
    def __repr__(self):
        return f"Game {self.id}: {self.rounds}"


class Round:
    def __init__(self, numRed = 0, numGreen = 0, numBlue = 0):
        self.numRed = numRed
        self.numGreen = numGreen
        self.numBlue = numBlue
    
    def __repr__(self):
        return f"r{self.numRed} g{self.numGreen} b{self.numBlue}"


input = open("02-input-test.txt", "r")
lines = input.read().splitlines()

games = []

for line in lines:
    splits = line.split(":")
    
    gamePart = splits[0]
    gameId = gamePart.replace("Game", "").strip()
    game = Game(int(gameId))

    roundsPart = splits [1]
    roundsSplit = roundsPart.split(";")

    for round in roundsSplit:
        cubes = round.split(",")

        numRed = 0
        numGreen = 0
        numBlue = 0

        for cube in cubes:
            if "red" in cube:
                numRed = int(cube.replace("red", "").strip())
            if "green" in cube:
                numGreen = int(cube.replace("green", "").strip())
            if "blue" in cube:
                numBlue = int(cube.replace("blue", "").strip())
        
        game.rounds.append(Round(numRed, numGreen, numBlue))

    games.append(game)

# print(*games, sep="\n")

possibleGamesSum = 0

for game in games:
    isGamePossible = True

    if max(game.rounds, key=lambda x: x.numRed).numRed > NUM_RED:
        isGamePossible = False
    if max(game.rounds, key=lambda x: x.numGreen).numGreen > NUM_GREEN:
        isGamePossible = False
    if max(game.rounds, key=lambda x: x.numBlue).numBlue > NUM_BLUE:
        isGamePossible = False
    
    if isGamePossible:
        possibleGamesSum += game.id

print(possibleGamesSum)
