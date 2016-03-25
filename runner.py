import os

if not os.path.exists("slurm_logs"):
    os.makedirs("slurm_logs")

if not os.path.exists("slurm_scripts"):
    os.makedirs("slurm_scripts")

jobs = [
    {
        'eps_endt': 1000000,
        'lr': 0.00025,
        'port': 8000,
        'use_distance': 'true'
    },
    {
        'eps_endt': 1000000,
        'lr': 0.00025,
        'port': 8001,
        'use_distance': 'true'
    },
    {
        'eps_endt': 1000000,
        'lr': 0.00025,
        'port': 8002,
        'use_distance': 'true'
    },
    {
        'eps_endt': 1000000,
        'lr': 0.00025,
        'port': 8003,
        'use_distance': 'true'
    },
    {
        'eps_endt': 1000000,
        'lr': 0.00025,
        'port': 8004,
        'use_distance': 'true'
    },
]

for job in jobs:
    jobname = "scratch_metanet_"
    savedir_prefix = "saved_networks/"
    exp_name = 'scratch_lower=200k_meta=50k_eps_endt=' + str(job['eps_endt']) + "_lr=" + str(job['lr']) + '_port=' + str(job['port']) + '_usedist=' + str(job['use_distance'])
    flagstring = "./run_exp.sh " + exp_name + " " + str(job['port']) + " 12 " + str(job['use_distance']) + " " + str(job['eps_endt']) + " " + str(job['lr'])
    print(flagstring)
    jobname = jobname + exp_name

    with open('slurm_scripts/' + jobname + '.slurm', 'w') as slurmfile:
        slurmfile.write("#!/bin/bash\n")
        slurmfile.write("#SBATCH --job-name"+"=" + jobname + "\n")
        slurmfile.write("#SBATCH --output=slurm_logs/" + jobname + ".out\n")
        slurmfile.write("#SBATCH --error=slurm_logs/" + jobname + ".err\n")
        slurmfile.write(flagstring)

    if True:
        os.system("sbatch --mem=50000 -N 1 -c 2 --gres=gpu:1 --time=6-23:00:00 slurm_scripts/" + jobname + ".slurm &")
