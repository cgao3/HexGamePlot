#!/usr/bin/env python
import sys
maxmoves = 999 # print only this many
moves = 0
for line in sys.stdin:
  content = line.split('[')
  for x in content:
    if x[:4] == 'swap' or x[:4] == 'SWAP':
      moves += 1
      print('S'),
    if x[0].islower() and x[1].isdigit(): 
      moves += 1
      if x[2].isdigit(): print(x[:3],)
      else:              print(' ' + x[:2],)
      if moves == maxmoves: break
    if moves == maxmoves: break
  if moves == maxmoves: break
print('#')
