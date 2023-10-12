matrix = [[1, 1, 1, 1, 1, 1, 1] if i % 2 == 0 else [0, 0, 0, 0, 0, 0, 0] for I in range(7)]
for row in matrix:
  print (' '.join(map(str, row)))
