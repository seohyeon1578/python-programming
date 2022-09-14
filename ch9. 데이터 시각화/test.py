import matplotlib.pyplot as plt
import random

integar = [random.randint(1,9) for _ in range(10)]

plt.hist(integar, bins=10)

plt.show()