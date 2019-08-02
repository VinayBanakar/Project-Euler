import math

def computeRectangles(row, col):  
  total = 0  
  for r in range(1, row + 1):  
    for c in range(1, col + 1):  
      total += (row - r + 1) * (col - c + 1)  
  return total

smallestDiff = 2000000  
area = -1  
finalRow = -1  
finalCol = -1  
for row in range(1,101):  
  for col in range(1,101):  
    rectangles = computeRectangles(row, col)  
    diff = math.fabs(rectangles - 2000000)  
    if (diff < smallestDiff):  
      area = row * col  
      smallestDiff = diff  
      finalRow = row  
      finalCol = col  
print("Result: [%s]x[%s] with area of %s" %(finalRow, finalCol, area))