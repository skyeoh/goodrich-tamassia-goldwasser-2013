import math
import numpy as np

def random_walk_1d(N, dx=1.0, p=0.5):
    """Generate a series of steps in a 1-D random walk.

         Input
         N:     Number of steps (int)
         dx:    Step size (float)
         p:      Probability of step in +ve direction (float)
         1-p:   Probability of a step in -ve direction (float)

         Output
         Series of steps (NumPy float array)
    """

    randarr = np.random.rand(N)
    steps = np.array([+dx if randnum < p else -dx for randnum in randarr])

    return steps

def calculate_trajectory_1d(x0, steps):
    """Calculate a 1-D trajectory.

         Input
         x0:        Starting point (float)
         steps:     Series of steps (NumPy float array)

         Output
         Positions (Numpy float array)
    """

    pos = [x0]
    x = x0
    for step in steps:
        x = x + step
        pos.append(x)

    return np.array(pos)


if __name__ == "__main__":

    # Test step size 1 - Specified value
    N = 12
    dx = 0.87
    steps = random_walk_1d(N, dx)
    print('\nTest step size 1 - Specified value')
    print(steps)

    # Test step size 2 - Default value (dx = 1.0)
    N = 8
    steps = random_walk_1d(N)
    print('\nTest step size 2 - Default value (dx = 1.0)')
    print(steps)

    # Test probability 1 - Specified value
    N = 10000
    dx = 1.0
    p = 0.27
    steps = random_walk_1d(N, dx, p)
    pos, neg = 0, 0
    for step in steps:
        if step > 0.0:
            pos+=1
        else:
            neg+=1
    print('\nTest probability 1 - Specified value')
    print('Percentage of positive steps:', 100.0*pos/N)
    print('Percentage of negative steps:', 100.0*neg/N)

    # Test probability 2 - Default value (p = 0.5)
    N = 10000
    steps = random_walk_1d(N)
    pos, neg = 0, 0
    for step in steps:
        if step > 0.0:
            pos+=1
        else:
            neg+=1
    print('\nTest probability 2 - Default value (p = 0.5)')
    print('Percentage of positive steps:', 100.0*pos/N)
    print('Percentage of negative steps:', 100.0*neg/N)

    # Test trajectory calculation 1 - Constant positive step size
    x0 = 0.0
    steps = np.full(10, 0.5)
    pos = calculate_trajectory_1d(x0, steps)

    print('\nTest trajectory calculation 1 - Constant positive step size')
    print(pos)

    # Test trajectory calculation 2 - Constant negative step size
    x0 = 1.0
    steps = np.full(10, -0.5)
    pos = calculate_trajectory_1d(x0, steps)

    print('\nTest trajectory calculation 2 - Constant negative step size')
    print(pos)

    # Test trajectory calculation 3 - Variable step size
    x0 = -1.0
    steps = np.array([1.0, -2.5, -0.5, 1.5, 10.0, -4.5, 8.0, -8.0, 3.5, -4.0])
    pos = calculate_trajectory_1d(x0, steps)

    print('\nTest trajectory calculation 3 - Variable step size')
    print(pos)

    # Test average distance from initial position after N steps
    # Theoretically, it should approach sqrt(N) as no. of samples approaches infinity
    # for unit step size and 50/50 probability.
    N = 100
    NumSamples = 10**5

    y0, AvgDist = 0.0, 0.0
    for sample in range(NumSamples):
        steps = random_walk_1d(N)
        y = calculate_trajectory_1d(y0, steps)
        AvgDist = AvgDist + (y[N] - y0)**2

    AvgDist = math.sqrt(AvgDist/NumSamples)

    print('\nAverage distance from initial position after', N, 'steps is', AvgDist)
