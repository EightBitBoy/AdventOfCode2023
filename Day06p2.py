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

time = int("".join(times))
distance = int("".join(distances))

waysToBeatTheRecord = 0
min = time
max = 0
for i in range (0, time + 1):
  speed = i
  distanceTravalled = (time - i) * speed
  if distanceTravalled > 0 and distanceTravalled > distance:
    waysToBeatTheRecord += 1
    if i < min:
      min = i
    if i > max:
      max = i

print(f"min@{min} max@{max}")
print(waysToBeatTheRecord)
