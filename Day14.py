input = open("Day14-input.txt", "r")
lines = input.read().splitlines()
rows = [[character for character in line] for line in lines]
columns = []

SOUTH_EDGE = len(lines)

for i in range(len(rows[0])):
  column = []
  for j in range(len(rows)):
    column.append(rows[j][i])
  columns.append(column)

sortedColumns = []
for column in columns:
  columnString = "".join(column)
  columnSplit = columnString.split("#")
  columnSorted = [sorted(c, reverse=True) for c in columnSplit]
  joinedSubLists = ["".join(c) for c in columnSorted]
  sortedColumns.append("#".join(joinedSubLists))

# print(sortedColumns)

sumLoad = 0
for column in sortedColumns:
  for index, rock in enumerate(column):
    if rock == "O":
      sumLoad += SOUTH_EDGE - index

print(f"Total load: {sumLoad}")
