import os

NoSC_Scan = True
SC_Scan = True

master_dir = os.getcwd()

NoSC_locations = []
NoSC_locations.append('/0_00')
NoSC_locations.append('/0_01')
NoSC_locations.append('/0_02')
NoSC_locations.append('/0_03')
NoSC_locations.append('/0_04')
NoSC_locations.append('/0_10')
NoSC_locations.append('/0_11')
NoSC_locations.append('/0_12')
NoSC_locations.append('/0_13')
NoSC_locations.append('/0_14')

SC_locations = []
SC_locations.append('/1_00')
SC_locations.append('/1_01')
SC_locations.append('/1_02')
SC_locations.append('/1_03')
SC_locations.append('/1_04')
SC_locations.append('/1_10')
SC_locations.append('/1_11')
SC_locations.append('/1_12')
SC_locations.append('/1_13')
SC_locations.append('/1_14')



if NoSC_Scan:
	for loc in NoSC_locations:
		print '--------------------------------------------------------------------------------------------'
		print '\t Submitting HPC-Batch simulation:', loc
		print '--------------------------------------------------------------------------------------------'
		dir_ = master_dir + loc 
		make_command = 'python Make_SLURM_submission_script.py'
		submit_command = 'sbatch SLURM_submission_script.sh'
		os.chdir(dir_)
		os.system(make_command)
		os.system(submit_command)

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

