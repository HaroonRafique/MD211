import os
import numpy as np

# Folder flags
########################################################################
# Folder name structure
# 0_312
# 0: space charge flag
# 312: Emittance case 3, Intensity=1, eps_z=2
# Limits: Intensity = {0,1}
# Limits: eps_z     = {0,4}
# Limits: Emittance case = {0.4}

Intensity_flag = int(os.getcwd()[-2]) # Intensity
Longitudinal_Emittance = int(os.getcwd()[-1]) # Longitudinal Emittance Case
Transverse_Emittance = int(os.getcwd()[-3]) # Transverse Emittance Case
sc = int(os.getcwd().split('/')[-1][0])

case = ['1p3', '1p6', '1p9', '2p3', '2p6']
eps_z = [1.3, 1.6, 1.9, 2.3, 2.6]
delta = [0.8E-3, 1.0E-3, 1.23E-3, 1.5E-3, 1.7E-3]
# voltages = [0.01225, 0.0189, 0.0304, 0.0455, 0.0591]
voltages_Low = [0.01475, 0.02157, 0.03311, 0.04821, 0.06172] # SC adjusted by empirical estimate low intensity
voltages_High = [0.01563, 0.02219, 0.03366, 0.04868, 0.06209] # SC adjusted by empirical estimate high intensity
    
# parameters
########################################################################       
parameters = {}

if Intensity_flag is 0:
        parameters['intensity']	= 1.6E12
        if Transverse_Emittance is 0: # Original
                parameters['epsn_x']	= 1.87E-6
                parameters['epsn_y']	= 1.83E-6
                
        elif Transverse_Emittance is 1: # Equal 1.8
                parameters['epsn_x']	= 1.8E-6
                parameters['epsn_y']	= 1.8E-6
        
        elif Transverse_Emittance is 2: # Equal 1.9
                parameters['epsn_x']	= 1.9E-6
                parameters['epsn_y']	= 1.9E-6
        
        elif Transverse_Emittance is 3: # Equal 2.0
                parameters['epsn_x']	= 2.0E-6
                parameters['epsn_y']	= 2.0E-6
        
        elif Transverse_Emittance is 4: # Equal 2.1
                parameters['epsn_x']	= 2.1E-6
                parameters['epsn_y']	= 2.1E-6
        str_intensity           = '1p6E12'
        parameters['rf_voltage']= voltages_Low[Longitudinal_Emittance]
        
else:
        parameters['intensity']	= 2.0E12
        if Transverse_Emittance is 0: # Original
                parameters['epsn_x']	= 2.3E-6
                parameters['epsn_y']	= 2.4E-6
                
        elif Transverse_Emittance is 1: # Equal 2.4
                parameters['epsn_x']	= 2.4E-6
                parameters['epsn_y']	= 2.4E-6
        
        elif Transverse_Emittance is 2: # Equal 2.5
                parameters['epsn_x']	= 2.5E-6
                parameters['epsn_y']	= 2.5E-6
        
        elif Transverse_Emittance is 3: # Equal 2.6
                parameters['epsn_x']	= 2.6E-6
                parameters['epsn_y']	= 2.6E-6
        
        elif Transverse_Emittance is 4: # Equal 2.7
                parameters['epsn_x']	= 2.7E-6
                parameters['epsn_y']	= 2.7E-6
        str_intensity           = '2E12'
        parameters['rf_voltage']= voltages_High[Longitudinal_Emittance]

parameters['Beam']		= case[Longitudinal_Emittance]
parameters['dpp_rms']		= delta[Longitudinal_Emittance]

if sc is 1:
        parameters['BLonD_file']='../BLonD_Files_SC/BLonD_Longitudinal_Distn_' + str_intensity + '_' + case[Longitudinal_Emittance] +  '_eVs.npz'
else:
        parameters['BLonD_file']='../BLonD_Files/BLonD_Longitudinal_Distn_' + str_intensity + '_' + case[Longitudinal_Emittance] +  '_eVs.npz'

        
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

switches = {
        'Dispersion_Mismatch':  True,
	'CreateDistn':		True,
	'Update_Twiss':		False,  # Needed to save optics turn-by-turn
	'GridSizeX': 128,
	'GridSizeY': 128,
	'GridSizeZ': 64
}

if sc is 1:
        switches['Space_Charge'] = True
else:
        switches['Space_Charge'] = False
        

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
