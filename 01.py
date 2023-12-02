input = open("01-input.txt", "r")

calibrationValues = []

for line in input:
  lineValue = line.strip()

  firstDigit = None
  lastDigit = None

  for character in lineValue:
    if character.isdigit():
      firstDigit = character
      break

  for character in reversed(lineValue):
    if character.isdigit():
      lastDigit = character
      break

  calibrationValues.append(int(firstDigit + lastDigit))

print(sum(calibrationValues))
