import numpy as np

x1 = np.asarray([1, 2, 1, 2])
x2 = np.asarray([3, 0, -1, -4])

xz1 = np.asarray([1, 2, 1, 2, 0, 0, 0])
xz2 = np.asarray([3, 0, -1, -4, 0, 0, 0])
XZ1 = np.fft.fft(xz1)
XZ2 = np.fft.fft(xz2)

XZk = np.multiply(XZ1, XZ2)
print('XZk mult', XZk)
print('Inverse', np.fft.ifft(XZk))

print('XZ1', XZ1)
print('XZ2', XZ2)
print(np.convolve(x1, x2))

x1k = np.fft.fft(x1)
x2k = np.fft.fft(x2)
v1 = np.multiply(x1k, x2k)
print(np.fft.ifft(v1))
xn = x1k + x2k
x = x1 + x2
xk = np.fft.fft(x)
