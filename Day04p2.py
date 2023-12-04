input = open("Day04-input.txt", "r")
lines = input.read().splitlines()


cards = []


class Card:
  def __init__(self, id, winningNumbers, numbers):
    self.instances = 1
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
  cardsSplit = lineSplit[1].split("|")

  cardId = int(lineSplit[0].replace("Card ", ""))

  winningNumbers = cardsSplit[0].strip().split(" ")
  winningNumbers = removeEmptyElementsFromList(winningNumbers)
  winningNumbers = list(map(int, winningNumbers))

  numbers = cardsSplit[1].strip().split(" ")
  numbers = removeEmptyElementsFromList(numbers)
  numbers = list(map(int, numbers))

  cards.append(Card(cardId, winningNumbers, numbers))


for card in cards:
  numWinning = card.getMatches()

  for n in range(card.id + 1, card.id + 1 + numWinning):
    if n <= len(cards):
      cards[n - 1].instances += card.instances


sumCards = 0
for card in cards:
  sumCards += card.instances

print(f"Sum: {sumCards}")
