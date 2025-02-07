from StateProjEW import *

def gerchberg_saxton(exitwave, probe, distance, energy, sampling, iterations):
    exitwave = np.array(exitwave)
    probe = np.array(probe)
    m, n = exitwave.shape
    exitwave = select_freq_range(exitwave, 0, 1 / (2 * sampling), sampling)
    probe = select_freq_range(probe, 0, 1 / (2 * sampling), sampling)
    for i in range(iterations):
        exitwave = propagation(probe, distance, sampling, energy) * np.exp(1.j * np.angle(exitwave))
        probe = propagation(exitwave, distance, sampling, energy) * np.exp(1.j * np.angle(probe))
    return exitwave, probe