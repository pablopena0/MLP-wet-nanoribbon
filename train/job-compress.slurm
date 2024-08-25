#!/bin/bash
#SBATCH --ntasks=1               # total number of tasks across all nodes
#SBATCH --ntasks-per-node=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1       # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --mem-per-cpu=24G         # memory per cpu-core (4G is default)
#SBATCH --time=1-00:00:00          # total run time limit (HH:MM:SS)
#SBATCH --job-name="Compress"
##SBATCH --gres=gpu:1        # number of gpus per node
##SBATCH --constraint=a100
#SBATCH --qos=regular

pwd; hostname; date

module purge
module load Python DeePMD/2.2.10-cpu CUDA

export OMP_NUM_THREADS=2
export TF_INTRA_OP_PARALLELISM_THREADS=2
export TF_INTER_OP_PARALLELISM_THREADS=2

export KMP_BLOCKTIME=0
export KMP_AFFINITY=granularity=fine,verbose,compact,1,0


dp compress -t input-compress.json -i frozen_model.pb -o frozen_model_compressed.pb


date
