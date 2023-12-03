input = open("03-input.txt", "r")
lines = input.read().splitlines()

LINES_NUM = len(lines)
LINE_LENGTH = len(lines[0])

# build the 2D data array
data = []
symbols = set()
numbersWithAdjacents = []

class Coordinates:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return f"{x}:{y}"

  def __hash__(self):
    return hash(self.__repr__())

  def __eq__(self, other):
    if isinstance(other, Coordinates):
        return self.__repr__() == other.__repr__()
    else:
        return False

class NumberWithAdjacents:
    def __init__(self, value, adjacentCoordinates, startCoordinates):
      self.value = value
      self.adjacentCoordinates = adjacentCoordinates
      self.startCoordinates = startCoordinates

    def __repr__(self):
      return f"{self.value}"

    def isAdjacentToSymbol(self, symbol):
      for coordinate in self.adjacentCoordinates:
        if coordinate.x < 0 or coordinate.x > LINE_LENGTH - 1:
          continue
        if coordinate.y < 0 or coordinate.y > LINES_NUM -1:
          continue
        if data[coordinate.y][coordinate.x] == symbol:
          return True
      return False

    def getCoordinatesForAdjactentWithSymbol(self, symbol):
      for coordinate in self.adjacentCoordinates:
        if coordinate.x < 0 or coordinate.x > LINE_LENGTH - 1:
          continue
        if coordinate.y < 0 or coordinate.y > LINES_NUM -1:
          continue
        if data[coordinate.y][coordinate.x] == symbol:
          return coordinate


def getAdjacents(x, y):
  adjacents = []

  # same row
  adjacents.append(Coordinates(x - 1, y + 0))
  adjacents.append(Coordinates(x + 1, y + 0))

  # top row
  adjacents.append(Coordinates(x - 1, y + 1))
  adjacents.append(Coordinates(x + 0, y + 1))
  adjacents.append(Coordinates(x + 1, y + 1))

  #bottom row
  adjacents.append(Coordinates(x - 1, y - 1))
  adjacents.append(Coordinates(x + 0, y - 1))
  adjacents.append(Coordinates(x + 1, y - 1))

  return adjacents

# prepare data and extract symbols
for line in lines:
  lineData = []

  for character in line:
    lineData.append(character)
    if not character.isdigit() and character != ".":
      symbols.add(character)

  data.append(lineData)

# extract numbers and adjacent coordinates
for y, rowValue in enumerate(data):
  digits = ""
  adjacents = []
  startCoordinates = None

  for x, columnValue in enumerate(rowValue):
    if columnValue.isdigit():
      if digits == "":
        startCoordinates = Coordinates(x,y)
      digits += columnValue
      for adjacent in getAdjacents(x, y):
        adjacents.append(adjacent)

    if digits != "" and ((not columnValue.isdigit()) or x == LINE_LENGTH -1):
      numbersWithAdjacents.append(
        NumberWithAdjacents(int(digits), adjacents,startCoordinates))
      digits = ""
      adjacents = []

candidates = []
symbolCoordinates = set()
for number in numbersWithAdjacents:
  if number.isAdjacentToSymbol("*"):
    candidates.append(number)
    symbolCoordinates.add(number.getCoordinatesForAdjactentWithSymbol("*"))

print(len(candidates))
print(len(symbolCoordinates))
print(symbolCoordinates)
