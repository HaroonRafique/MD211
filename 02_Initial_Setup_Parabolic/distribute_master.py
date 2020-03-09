import shutil

pyorbit = False
simulation_parameters = False
flat_files = False
tune_files = False
distn_gen = True

master_directory = './00_Master'
pyorbit_file = master_directory + '/pyOrbit.py'
sim_params_file = master_directory + '/simulation_parameters.py'
flat_file = master_directory + '/Flat_file.madx'
tune_file = master_directory + '/tunes.str'
distn_generator = master_directory + '/lib/pyOrbit_GenerateInitialDistribution.py'

NoSC_Scan = True
SC_Scan = True

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

locations.append('NoSC_00')
locations.append('NoSC_01')
locations.append('NoSC_02')
locations.append('NoSC_03')
locations.append('NoSC_04')

locations.append('NoSC_10')
locations.append('NoSC_11')
locations.append('NoSC_12')
locations.append('NoSC_13')
locations.append('NoSC_14')

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
