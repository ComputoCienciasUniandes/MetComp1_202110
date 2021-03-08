import numpy as np

counts_same = 0
counts_consecutive = 0
for i in range(10000):
  numbers = np.random.randint(1, 7, 3)
  if numbers[0] == numbers[1] and numbers[0] == numbers[2] and numbers[1] == numbers[2]:
    counts_same += 1
  numbers.sort()
  if numbers[0] == numbers[1] - 1 and numbers[1] == numbers[2] - 1:
    counts_consecutive += 1

prob_same = counts_same/10000
prob_consecutive = counts_consecutive/10000

print(f"Prob Alice = {prob_same}, Prob Bob = {prob_consecutive}")