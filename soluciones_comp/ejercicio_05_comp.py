import numpy as np 

steps_right = np.zeros(50000)
for i in range(50000):
    steps_right[i] = np.sum(np.int32(np.random.rand(100) < 0.8))

steps_right_squared = steps_right**2

expected_value_nd = steps_right.mean()
expected_value_nd2 = steps_right_squared.mean()
std_nd = np.sqrt(abs(expected_value_nd**2 - expected_value_nd2))

print(f"[nd] = {expected_value_nd}, [nd2] = {expected_value_nd2}, std_nd = {std_nd}")
