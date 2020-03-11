import shutil

pyorbit                 = False
simulation_parameters   = False
flat_files              = False
tune_files              = False
distn_gen               = False
tomo_files              = False
bunch_plotting          = True

master_directory        = './00_Master'
pyorbit_file            = master_directory + '/pyOrbit.py'
sim_params_file         = master_directory + '/simulation_parameters.py'
flat_file               = master_directory + '/Flat_file.madx'
tune_file               = master_directory + '/tunes.str'
distn_generator         = master_directory + '/lib/pyOrbit_GenerateInitialDistribution.py'
tomo_file               = master_directory + '/Tomo_Files/'
bunch_plotter           = master_directory + '/Plot_Tune_and_Distn_Footprints.py'

tomo_list = [
        'PyORBIT_Tomo_file_2E12_1p3_eVs.mat',
        'PyORBIT_Tomo_file_2E12_1p6_eVs.mat',
        'PyORBIT_Tomo_file_2E12_1p9_eVs.mat',
        'PyORBIT_Tomo_file_2E12_2p3_eVs.mat',
        'PyORBIT_Tomo_file_2E12_2p6_eVs.mat',
        'PyORBIT_Tomo_file_1p6E12_2p6_eVs.mat',
        'PyORBIT_Tomo_file_1p6E12_2p3_eVs.mat',
        'PyORBIT_Tomo_file_1p6E12_1p9_eVs.mat',
        'PyORBIT_Tomo_file_1p6E12_1p6_eVs.mat',
        'PyORBIT_Tomo_file_1p6E12_1p3_eVs.mat',
]

locations = []

locations.append('00_00')
locations.append('00_01')
locations.append('00_02')
locations.append('00_03')
locations.append('00_04')

locations.append('00_10')
locations.append('00_11')
locations.append('00_12')
locations.append('00_13')
locations.append('00_14')

locations.append('01_00')
locations.append('01_01')
locations.append('01_02')
locations.append('01_03')
locations.append('01_04')

locations.append('01_10')
locations.append('01_11')
locations.append('01_12')
locations.append('01_13')
locations.append('01_14')

if pyorbit:
	for loc in locations:
		newPath = shutil.copy(pyorbit_file, loc)
		print pyorbit_file, ' copied to ', loc

if simulation_parameters:
	for loc in locations:
		newPath = shutil.copy(sim_params_file, loc)
		print sim_params_file, ' copied to ', loc

if flat_files:
	for loc in locations:
		newPath = shutil.copy(flat_file, loc)
		print flat_file, ' copied to ', loc

if tune_files:
	for loc in locations:
		newPath = shutil.copy(tune_file, loc)
		print flat_file, ' copied to ', loc

if distn_gen:
	for loc in locations:
		loc_ = loc + '/lib/'
		newPath = shutil.copy(distn_generator, loc_)
		print distn_generator, ' copied to ', loc_

if tomo_files:
        for loc in locations:
                for f in tomo_list:
                        tomo_f = tomo_file + f 
                        loc_ = loc + '/Tomo_Files/'
                        newPath = shutil.copy(tomo_f, loc_)
                        print tomo_file, ' copied to ', loc_

if bunch_plotting:
	for loc in locations:
		newPath = shutil.copy(bunch_plotter, loc)
		print bunch_plotter, ' copied to ', loc
