import numpy as np
import matplotlib.pyplot as plt

samples = np.fromfile('/tmp/gqrx_20170218_023225_131832200_1800000_fc.raw', np.complex64) # Read in file.  We have to tell it what format it is
print(samples)

# Plot constellation to make sure it looks right
plt.plot(np.real(samples), np.imag(samples), '.')
plt.grid(True)
plt.show()