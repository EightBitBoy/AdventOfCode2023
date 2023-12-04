input = open("Day04-input.txt", "r")
lines = input.read().splitlines()

# print(*lines, sep="\n")

cards = []

class Card:
    def __init__(self, id, winningNumbers, numbers):
        self.id = id
        self.winningNumbers = winningNumbers
        self.numbers = numbers

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

pointsSum = 0
for card in cards:
    numMatches = 0

    for winningNumber in card.winningNumbers:
        numMatches += card.numbers.count(winningNumber)

    if numMatches > 0:
        pointsSum += 2**(numMatches - 1)

print(pointsSum)

# print(*cards, sep="\n")
