input = open("Day06-input.txt", "r")
lines = input.read().splitlines()

for index, line in enumerate(lines):
  lines[index] = line.split(":")[1].strip()

def removeEmptyElementsFromList(list):
  return [value for value in list if value != '']

timeSplit = lines[0].split(" ")
distanceSplit = lines[1].split(" ")

times = removeEmptyElementsFromList(timeSplit)
distances = removeEmptyElementsFromList(distanceSplit)

times = list(map(int, times))
distances = list(map(int, distances))

result = 1
for index, time in enumerate(times):
  waysToBeatTheRecord = 0
  for i in range (0, time + 1):
    speed = i
    distanceTravalled = (time - i) * speed
    if distanceTravalled > 0 and distanceTravalled > distances[index]:
      waysToBeatTheRecord += 1
  result = result * waysToBeatTheRecord

print(result)
