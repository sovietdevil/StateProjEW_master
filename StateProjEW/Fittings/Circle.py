import circle_fit as cf
import numpy as np

def generate_continious_phase(complex_series):
    '''
    Generate a continious phase from a complex series
    :param complex_series: complex series
    :return: continious phase
    '''
    output_phase = np.angle(complex_series)
    for n in range(len(complex_series)-1):
        if (output_phase[n]-output_phase[n+1])>np.pi:
            output_phase[n+1:] = output_phase[n+1:] + 2*np.pi
        elif (output_phase[n+1]-output_phase[n])>np.pi:
            output_phase[n+1:] = output_phase[n+1:] - 2*np.pi
    return output_phase



def circle_fit(profile_lists):
    '''
    Fit a circle to a list of profiles
    :param profile_lists: list of profiles
    :return: xc, yc, R
    '''
    xc_list = []
    yc_list = []
    R_list = []
    for profile in profile_lists:
        if len(profile) == 0:
            return None, None, None
        # Fit circle
        xc, yc, R, _ = cf.least_squares_circle(profile)
        xc_list.append(xc)
        yc_list.append(yc)
        R_list.append(R)
    xc_list = np.array(xc_list)
    yc_list = np.array(yc_list)
    R_list = np.array(R_list)
    return xc_list, yc_list, R_list


