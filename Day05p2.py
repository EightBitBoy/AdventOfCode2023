import sys


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
  def transform(map: Map, value) -> None:
    for mapping in map.mappings:
      if mapping.sourceStart <= value <= mapping.sourceStart + mapping.range - 1:
        difference = value - mapping.sourceStart
        return mapping.destinationStart + difference
    return value


maps = []


print("# creating seeds")
seedsLine = lines[0].replace("seeds: ", "")
seedsSplit = seedsLine.split(" ")
seedPairs = list(map(int, seedsSplit))

lines.pop(0)
lines.pop(0)

print("# creating maps")
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

print("# transforming seeds")
# numSeeds = len(seeds)
# for index, seed in enumerate(seeds):
#   if index % 1000 == 0:
#     print(f"{index} of {numSeeds}")
#   for map in maps:
#     seed.transform(map)

processed = 0
minimum = sys.maxsize
print(minimum)
for i in range(0, len(seedPairs), 2):
  for seedNumber in range(seedPairs[i], seedPairs[i] + seedPairs[i+1]):
    number = seedNumber
    for map in maps:
      number = Seed.transform(map, number)
    if number < minimum:
      minimum = number
      print(f"New min: {minimum}")
    processed += 1
    if processed % 100000 == 0:
      print(f"# {processed}")


print("####")
print(minimum)
