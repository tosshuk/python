matrix = []

for i in range (7):
  if i % 2 ==0:
    row = [1,1,1,1,1,1,1]
  else:
    row = [0,0,0,0,0,0,0]
  matrix.append(row)
for row in matrix:
  print (' '.join(map(str, row)))