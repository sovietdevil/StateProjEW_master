from Fittings import *
from Peaks import *
from StateProj import *
from StateProjEW import *
import numpy as np
import scipy

def energy2wavelength(energy):
    c = 299792458
    h = 6.62607015e-34
    e = 1.602176634e-19
    me = 9.10938356e-31
    momentum = (2 * me * energy * e * (1 + energy*e/(2*me*c**2))) ** 0.5
    wavelength = h / momentum
    return wavelength*1e10

def select_freq_range(exitwave, gmin, gmax, sampling):
    exitwave = np.array(exitwave)
    m, n = exitwave.shape
    ft_exitwave = scipy.fft.fft2(exitwave)
    freq_gx = np.fft.fftfreq(m, sampling)
    freq_gy = np.fft.fftfreq(n, sampling)
    gx, gy = np.meshgrid(freq_gx, freq_gy)
    g2 = gx ** 2 + gy ** 2
    ft_exitwave[g2 < gmin ** 2] = 0
    ft_exitwave[g2 > gmax ** 2] = 0
    ew = scipy.fft.ifft2(ft_exitwave)
    return ew

def propagation(waves, distance, sampling, energy):
    wavelength = energy2wavelength(energy)
    waves = np.array(waves)
    m, n = waves.shape
    kx = np.fft.fftfreq(m, sampling)
    ky = np.fft.fftfreq(n, sampling)
    Kx, Ky = np.meshgrid(kx, ky)
    k2 = Kx ** 2 + Ky ** 2
    kernel = np.exp(- 1.j * k2 * np.pi * wavelength * distance)
    waves = scipy.fft.ifft2(scipy.fft.fft2(waves)*kernel)
    return waves