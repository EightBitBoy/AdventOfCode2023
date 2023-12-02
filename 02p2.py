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


input = open("02-input.txt", "r")
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

gamesPowerSum = 0

for game in games:
  maxRed = max(game.rounds, key=lambda x: x.numRed).numRed
  maxGreen = max(game.rounds, key=lambda x: x.numGreen).numGreen
  maxBlue = max(game.rounds, key=lambda x: x.numBlue).numBlue

  gamePower = maxRed * maxGreen * maxBlue
  gamesPowerSum += gamePower

print(gamesPowerSum)
