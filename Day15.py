input = open("Day15-input.txt", "r")

# input should be a single line
lines = input.read().splitlines()
assert len(lines) == 1

line: list[str] = lines[0]
elements: list[str] = line.split(",")

def hash(input: str) -> int:
  value = 0
  for character in input:
    value = value + ord(character)
    value = value * 17
    value = value % 256
  return value


hashSum = 0
for element in elements:
  hashSum += hash(element)

print(f"Sum: {hashSum}")
