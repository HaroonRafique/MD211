import os
import numpy as np

# Folder name structure
# 01_some_name_12
# 01: Simulation specific case
# 12: Intensity=1, eps_z=2
# Limits: Intensity = {0,1}
# Limits: eps_z     = {0,4}

a = int(os.getcwd()[-2])
b = int(os.getcwd()[-1])
c = int(os.getcwd().split('/')[-1][2:])

case = ['1p3', '1p6', '1p9', '2p3', '2p6']
eps_z = [1.3, 1.6, 1.9, 2.3, 2.6]
delta = [0.8E-3, 1.0E-3, 1.23E-3, 1.5E-3, 1.7E-3]
voltages = [0.01225, 0.0189, 0.0304, 0.0455, 0.0591]

parameters = {}

if a is 0:
        parameters['intensity']	= 1.6E12
        parameters['epsn_x']	= 0.#1.87E-6
        parameters['epsn_y']	= 0.#1.83E-6
        str_intensity           = '1p6E12'
else:
        parameters['intensity']	= 2.0E12
        parameters['epsn_x']	= 0.#2.3E-6
        parameters['epsn_y']	= 0.#2.4E-6
        str_intensity           = '2E12'

parameters['Beam']		= case[b]
parameters['dpp_rms']		= delta[b]
parameters['rf_voltage']	= voltages[b]
parameters['tomo_file']		='Tomo_Files/PyORBIT_Tomo_file_'+str_intensity+'_'+case[b]+'_eVs.mat'

parameters['tunex']		= '619'
parameters['tuney']		= '624'

parameters['lattice_start'] 	= 'BWSH65'
parameters['n_macroparticles']	= int(5E5)

# PS Injection 1.4 GeV
parameters['gamma'] 	        = 2.49038064
parameters['bunch_length']	= 210E-9
parameters['blength']		= 210E-9


parameters['beta'] 		= np.sqrt(parameters['gamma']**2-1)/parameters['gamma']
parameters['LongitudinalJohoParameter'] = 1.2
parameters['LongitudinalCut'] 	= 2.4
parameters['TransverseCut']	= 5
parameters['circumference']	= 2*np.pi*100
parameters['phi_s']		= 0
parameters['macrosize']		= parameters['intensity']/float(parameters['n_macroparticles'])
c 				= 299792458
parameters['sig_z'] 	= (parameters['beta'] * c * parameters['blength'])/4.

parameters['turns_max'] = int(2200)
tu1 = range(-1, parameters['turns_max'], 200)
tu2 = range(50, 100, 10) 
tu3 = range(1, 50)
tu = tu2 + tu1 + tu3 

parameters['turns_print'] = sorted(tu)
parameters['turns_update'] = sorted(tu)

sc = [False, True]

switches = {
	'CreateDistn':		True,
	'Update_Twiss':		False,  # Needed to save optics turn-by-turn
	'Space_Charge': 	sc[c],
	'GridSizeX': 128,
	'GridSizeY': 128,
	'GridSizeZ': 64
}

# PTC RF Table Parameters
harmonic_factors = [1] # this times the base harmonic defines the RF harmonics (for SPS = 4620, PS 10MHz 7, 8, or 9)
time = np.array([0,1,2])
ones = np.ones_like(time)
Ekin_GeV = 1.4*ones
RF_voltage_MV = np.array([parameters['rf_voltage']*ones]).T # in MV
RF_phase = np.array([np.pi*ones]).T

RFparameters = {
	'harmonic_factors': harmonic_factors,
	'time': time,
	'Ekin_GeV': Ekin_GeV,
	'voltage_MV': RF_voltage_MV,
	'phase': RF_phase
}
