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

class NumberWithAdjacents:
    def __init__(self, value, adjacentCoordinates):
      self.value = value
      self.adjacentCoordinates = adjacentCoordinates

    def __repr__(self):
      return f"{self.value}"

    def isAdjacentToSymbol(self):
      for coordinate in self.adjacentCoordinates:
        if coordinate.x < 0 or coordinate.x >= LINE_LENGTH:
          continue
        if coordinate.y < 0 or coordinate.y >= LINES_NUM:
          continue
        if data[coordinate.y][coordinate.x] in symbols:
          return True
      return False

def getAdjacents(x, y):
  adjacents = set()

  # same row
  adjacents.add(Coordinates(x - 1, y + 0))
  adjacents.add(Coordinates(x + 1, y + 0))

  # top row
  adjacents.add(Coordinates(x - 1, y + 1))
  adjacents.add(Coordinates(x + 0, y + 1))
  adjacents.add(Coordinates(x + 1, y + 1))

  #bottom row
  adjacents.add(Coordinates(x - 1, y - 1))
  adjacents.add(Coordinates(x + 0, y - 1))
  adjacents.add(Coordinates(x + 1, y - 1))

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
  adjacents = set()
  for x, columnValue in enumerate(rowValue):
    if columnValue.isdigit():
      digits += columnValue
      for adjacent in getAdjacents(x, y):
        adjacents.add(adjacent)
    if not columnValue.isdigit() and digits != "":
      numbersWithAdjacents.append(
        NumberWithAdjacents(int(digits), adjacents)
      )
      digits = ""
      adjacents = set()

sum = 0

for number in numbersWithAdjacents:
  if number.isAdjacentToSymbol():
    print(number.value)
    sum += number.value

# print(symbols)
# print(numbersWithAdjacents)
# print(sum)

# print(*data, sep="\n")
