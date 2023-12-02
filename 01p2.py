input = open("01-input.txt", "r")

calibrationValues = []

textDigits = {
  "1": "one",
  "2": "two",
  "3": "three",
  "4": "four",
  "5": "five",
  "6": "six",
  "7": "seven",
  "8": "eight",
  "9": "nine"
}

for line in input:
  lineValue = line.strip()

  # replace all numeric values by textual representation
  for number, textNumber in textDigits.items():
    lineValue = lineValue.replace(number, textNumber)

  lowestFirstIndex = 1000
  lowestFirstIndexKey = ""

  lowestLastIndex = -1
  lowestLastIndexKey = ""
  
  # search from the begining
  for number, textNumber in textDigits.items():
    found = lineValue.find(textNumber)
    if (found >= 0 and found < lowestFirstIndex):
      lowestFirstIndex = found
      lowestFirstIndexKey = number
  
  # search from the end
  for number, textNumber in textDigits.items():
    found = lineValue.rfind(textNumber)
    if (found >= 0 and found > lowestLastIndex):
      lowestLastIndex = found
      lowestLastIndexKey = number
  
  calibrationValues.append(int(lowestFirstIndexKey + lowestLastIndexKey))

print(sum(calibrationValues))