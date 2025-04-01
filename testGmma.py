import numpy as np
import matplotlib.pyplot as plt

x = np.random.gamma(3, 0.5, 1000)
plt.hist(x, bins=30, density=True, alpha=0.6, color='g')
plt.title('Gamma Distribution')
plt.show()