import scipy

wave = scipy.fromfile('samples.dat', dtype=scipy.int16)
samples = [complex(i, q) for i, q in zip(wave[::2], wave[1::2])]

from matplotlib import pyplot as plt

fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
ax[0].plot([s.real for s in samples[:500]], '-bo')
ax[1].plot([ abs( sum( [samples[i+j] * samples[i+j+16].conjugate() for j in range(0, 48)]) ) /
             sum( [abs(samples[i+j])**2 for j in range(0, 48)]) for i in range(0, 500)], '-ro')
plt.show(block=False)