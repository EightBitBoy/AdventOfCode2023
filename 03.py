input = open("03-input-test.txt", "r")
lines = input.read().splitlines()

# build the 2D data array
data = []
symbols = set()
numbers = []

class Coordinates:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class NumberWithAdjacents:
    def __init__(self, value, adjacents):
      self.value = value
      self.adjacents = adjacents

for line in lines:
  lineData = []
  for character in line:
    lineData.append(character)
    if not character.isdigit() and character != ".":
      symbols.add(character)
  data.append(lineData)

print(*data, sep="\n")

for y, rowValue in enumerate(data):
  digits = ""
  for x, columnValue in enumerate(rowValue):
    if columnValue.isdigit():
      digits += columnValue
    if not columnValue.isdigit() and digits != "":
      numbers.append(int(digits))
      digits = ""

print(symbols)
print(numbers)
