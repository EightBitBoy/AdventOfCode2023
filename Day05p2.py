input = open("Day05-input.txt", "r")
lines = input.read().splitlines()

class Mapping:
  def __init__(self, sourceStart, destinationStart, range) -> None:
    self.sourceStart = sourceStart
    self.destinationStart = destinationStart
    self.range = range
  def __repr__(self) -> str:
    return f"dest@{self.destinationStart} src@{self.sourceStart} rng@{self.range}"


class Map:
  def __init__(self, source: int, destination: int) -> None:
    self.source = source
    self.destination = destination
    self.mappings = []
  def __repr__(self) -> str:
    return f"{self.source}->{ self.destination}"


class Seed:
  def __init__(self, number: int) -> None:
    self.number = number
  def __repr__(self) -> str:
    return f"S+{self.number}"
  def transform(self, map: Map) -> None:
    for mapping in map.mappings:
      #if self.number in range(mapping.sourceStart, mapping.sourceStart + mapping.range - 1):
      if mapping.sourceStart <= self.number <= mapping.sourceStart + mapping.range - 1:
        difference = self.number - mapping.sourceStart
        # print(difference)
        self.number = mapping.destinationStart + difference
        break


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

  if line != "":
    lineSplit = line.split(" ")
    mapping = Mapping(int(lineSplit[1]), int(lineSplit[0]), int(lineSplit[2]))
    map.mappings.append(mapping)

  if index == len(lines) - 1 and map != None:
    maps.append(map)


for seed in seeds:
  for map in maps:
    seed.transform(map)

print(seeds)
print(min(seeds, key=lambda x: x.number))
