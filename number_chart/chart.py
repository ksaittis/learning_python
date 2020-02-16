import math
import os
import random
import sys
# 5
# 4             _
# 3          _  _
# 2       _  _  _
# 1    _  _  _  _
# 0 _  _  _  _  _
#   1  2  3  4  5
import time

# data = [1, 2, 3, 4, 5]

data = [random.randint(0, 99) for i in range(10)]
ROWS = 5
minimum = min(data)
maximum = max(data)

chart = []

for row in range(ROWS):
    chart.append([])
    chart[row].append(math.ceil(maximum / ROWS) * row)
    for d in data:
        chart[row].append('   ')

for row_idx, row in enumerate(chart):
    for col_idx, col in enumerate(data, start=1):
        if col >= row[0]:
            chart[row_idx][col_idx] = ' _ '

chart.reverse()

for row in chart:
    for column in row:
        sys.stdout.write(f'{str(column).rjust(3)} ')
    sys.stdout.write('\n')

sys.stdout.write('     ')
for i in data:
    sys.stdout.write(f'{str(i).ljust(4)}')
    time.sleep(1)

if __name__ == '__main__':
    while True:
        os.system('cls')
        os.system('python chart.py')
        pass
