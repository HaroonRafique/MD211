import os

master_dir = os.getcwd()

locations = []

# ~ locations.append('/00_00')
# ~ locations.append('/00_01')
# ~ locations.append('/00_02')
# ~ locations.append('/00_03')
# ~ locations.append('/00_04')

# ~ locations.append('/00_10')
# ~ locations.append('/00_11')
# ~ locations.append('/00_12')
# ~ locations.append('/00_13')
# ~ locations.append('/00_14')

locations.append('/NoSC_00')
locations.append('/NoSC_01')
locations.append('/NoSC_02')
locations.append('/NoSC_03')
locations.append('/NoSC_04')

locations.append('/NoSC_10')
locations.append('/NoSC_11')
locations.append('/NoSC_12')
locations.append('/NoSC_13')
locations.append('/NoSC_14')

for loc in locations:
	print '---------------------------------------------------------------------------'
	print '\t Submitting SLURM Job: MD211 Parabolic Sim ', loc[-2:]
	print '---------------------------------------------------------------------------'
	dir_ = master_dir + loc
	make_command = 'python Make_SLURM_submission_script.py'
	submit_command = 'sbatch SLURM_submission_script.sh'
	os.chdir(dir_)
	os.system(make_command)
	os.system(submit_command)
