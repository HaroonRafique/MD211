import os

master_dir = os.getcwd()

locations = []

locations.append('/00_00')
locations.append('/00_01')
locations.append('/00_02')
locations.append('/00_03')
locations.append('/00_04')

locations.append('/01_00')
locations.append('/01_01')
locations.append('/01_02')
locations.append('/01_03')
locations.append('/01_04')

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
