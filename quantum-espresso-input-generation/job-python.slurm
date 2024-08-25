#!/bin/bash
#SBATCH --qos=test
#SBATCH --ntasks=1               # total number of tasks across all nodes
#SBATCH --ntasks-per-node=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1       # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --mem-per-cpu=24G         # memory per cpu-core (4G is default)
#SBATCH --time=00:10:00          # total run time limit (HH:MM:SS)
#SBATCH --job-name="script"

pwd; hostname; date

module load Anaconda3

source /home/ppena/.venv/bin/activate	#python environment with ASE package 

python inputs.py

date
