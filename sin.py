import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 200)
y1 = np.sin((np.pi * 2) * t)
y2 = np.sin((np.pi * t))
y3 = np.sin((3 * np.pi * 2) * t)

plt.subplot(221)
plt.title('sin((pi/2)*t)')
plt.plot(t, y1)
plt.subplot(222)
plt.title('sin((pi*t))')
plt.plot(t, y2)
plt.subplot(223)
plt.title('sin((3pi/2)*t)')
plt.plot(t, y3)
