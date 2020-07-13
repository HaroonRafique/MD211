import os

SC_Scan = True

master_dir = os.getcwd()

SC_locations = []
SC_locations.append('/1_104')
SC_locations.append('/1_114')
SC_locations.append('/1_204')
SC_locations.append('/1_214')
SC_locations.append('/1_304')
SC_locations.append('/1_314')
SC_locations.append('/1_404')
SC_locations.append('/1_414')


if SC_Scan:
	for loc in SC_locations:
		print '--------------------------------------------------------------------------------------------'
		print '\t Submitting HPC-Batch simulation:', loc
		print '--------------------------------------------------------------------------------------------'
		dir_ = master_dir + loc 
		make_command = 'python Make_SLURM_submission_script.py'
		submit_command = 'sbatch SLURM_submission_script.sh'
		os.chdir(dir_)
		os.system(make_command)
		os.system(submit_command)

