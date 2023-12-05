input = open("Day05-input-test.txt", "r")
lines = input.read().splitlines()

class Seed:
  def __init__(self, number) -> None:
    self.number = number

  def __repr__(self) -> str:
    return f"S+{self.number}"

class Map:
  def __init__(self, source, destination) -> None:
    self.source = source
    self.destination = destination

  def __repr__(self) -> str:
    return f"{self.source}->{ self.destination}"

seeds = []
maps = []

seedsLine = lines[0].replace("seeds: ", "")
seedsSplit = seedsLine.split(" ")
for item in seedsSplit:
    seeds.append(Seed(int(item)))

lines.pop(0)
lines.pop(0)

map = None
for index, line in enumerate(lines):
  if "map:" in line:
    if map != None:
      maps.append(map)


    line = line.replace(" map:", "")
    lineSplit = line.split("-to-")
    map = Map(lineSplit[0], lineSplit[1])
    continue

  if index == len(lines) - 1 and map != None:
    maps.append(map)




print(type(lines))
print(lines[2])
print(seeds)
print(maps)
