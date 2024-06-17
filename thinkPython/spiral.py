import numpy as np
import matplotlib.pyplot as plt

# Define theta range
theta = np.linspace(0, 4 * np.pi, 1000)  # 2 full rotations

# Nautilus shell spiral parameters
a1 = 5
b1 = 0.5
r1 = a1 * np.exp(b1 * theta)

# Spiral galaxy parameters
a2 = 1000
b2 = 0.1
r2 = a2 * np.exp(b2 * theta)

# Convert to Cartesian coordinates for plotting
x1 = r1 * np.cos(theta)
y1 = r1 * np.sin(theta)
x2 = r2 * np.cos(theta)
y2 = r2 * np.sin(theta)

# Plotting the spirals
plt.figure(figsize=(12, 6))

# Nautilus shell spiral
plt.subplot(1, 2, 1)
plt.plot(x1, y1)
plt.title('Nautilus Shell Spiral')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')

# Spiral galaxy
plt.subplot(1, 2, 2)
plt.plot(x2, y2)
plt.title('Spiral Galaxy')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')

plt.tight_layout()
plt.show()
