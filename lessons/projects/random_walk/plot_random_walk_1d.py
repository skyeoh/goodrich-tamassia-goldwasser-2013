import numpy as np
import matplotlib.pyplot as plt
import random_walk_1d as rw1d

# Plot random walk 1: Position vs. Step Number
N = 100
steps = rw1d.random_walk_1d(N)

x = np.arange(N+1)
y0 = 0.0
y = rw1d.calculate_trajectory_1d(y0, steps)

plt.plot(x, y)
plt.xlabel('Step Number')
plt.ylabel('Position')
plt.title('Position vs. Step Number')
plt.show()

# Plot random walk 2: Position vs. Step Number - All +ve steps
N = 100
dx = 0.5
p = 1.0
steps = rw1d.random_walk_1d(N, dx, p)

x = np.arange(N+1)
y0 = 0.0
y = rw1d.calculate_trajectory_1d(y0, steps)

plt.plot(x, y)
plt.xlabel('Step Number')
plt.ylabel('Position')
plt.title('Position vs. Step Number')
plt.show()

# Plot random walk 3: Position vs. Step Number - All -ve steps
N = 100
dx = 0.5
p = 0.0
steps = rw1d.random_walk_1d(N, dx, p)

x = np.arange(N+1)
y0 = 0.0
y = rw1d.calculate_trajectory_1d(y0, steps)

plt.plot(x, y)
plt.xlabel('Step Number')
plt.ylabel('Position')
plt.title('Position vs. Step Number')
plt.show()

# Plot random walk 4: Position vs. Step Number - Inclined towards +ve steps
N = 1000
dx = 1.0
p = 0.75
steps = rw1d.random_walk_1d(N, dx, p)

x = np.arange(N+1)
y0 = 0.0
y = rw1d.calculate_trajectory_1d(y0, steps)

plt.plot(x, y)
plt.xlabel('Step Number')
plt.ylabel('Position')
plt.title('Position vs. Step Number')
plt.show()

# Plot random walk 5: Position vs. Step Number - Inclined towards -ve steps
N = 1000
dx = 1.0
p = 0.25
steps = rw1d.random_walk_1d(N, dx, p)

x = np.arange(N+1)
y0 = 0.0
y = rw1d.calculate_trajectory_1d(y0, steps)

plt.plot(x, y)
plt.xlabel('Step Number')
plt.ylabel('Position')
plt.title('Position vs. Step Number')
plt.show()

# Plot random walk 6: Position vs. Step Number - 50/50 and many many steps
N = 10000
steps = rw1d.random_walk_1d(N)

x = np.arange(N+1)
y0 = 0.0
y = rw1d.calculate_trajectory_1d(y0, steps)

plt.plot(x, y)
plt.xlabel('Step Number')
plt.ylabel('Position')
plt.title('Position vs. Step Number')
plt.show()
