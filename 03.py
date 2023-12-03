input = open("03-input-test.txt", "r")
lines = input.read().splitlines()

LINE_LENGTH = len(lines[0])

# build the 2D data array
data = []
symbols = []

for line in lines:
  lineData = []

  for character in line:
    lineData.append(character)

    if not character.isdigit() and character != ".":
      symbols.append(character)

  data.append(lineData)

print(*data, sep="\n")

numbers = []

for y, rowValue in enumerate(data):
  digits = ""
  for x, columnValue in enumerate(rowValue):
    if columnValue.isdigit():
      digits += columnValue
    if not columnValue.isdigit() and digits != "":
      numbers.append(int(digits))
      digits = ""

print(numbers)
