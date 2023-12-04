input = open("Day04-input-test.txt", "r")
lines = input.read().splitlines()

# print(*lines, sep="\n")

cards = []

class Card:
  def __init__(self, id, winningNumbers, numbers):
    self.id = id
    self.winningNumbers = winningNumbers
    self.numbers = numbers

  def getMatches(self):
    numMatches = 0
    for winningNumber in self.winningNumbers:
      numMatches += self.numbers.count(winningNumber)
    return numMatches

def removeEmptyElementsFromList(list):
  return [value for value in list if value != '']

for line in lines:
  lineSplit = line.split(":")
  cardId = int(lineSplit[0].replace("Card ", ""))

  cardsSplit = lineSplit[1].split("|")

  winningNumbers = cardsSplit[0].strip().split(" ")
  winningNumbers = removeEmptyElementsFromList(winningNumbers)
  winningNumbers = list(map(int, winningNumbers))

  numbers = cardsSplit[1].strip().split(" ")
  numbers = removeEmptyElementsFromList(numbers)
  numbers = list(map(int, numbers))

  cards.append(Card(cardId, winningNumbers, numbers))

card_1 = cards[0]
stack = {card_1: 1}
winning = True

print(card_1.getMatches())
