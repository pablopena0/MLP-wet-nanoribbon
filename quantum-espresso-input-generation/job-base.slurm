#!/bin/bash
#SBATCH --qos=regular
#SBATCH --time=01:00:00
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=48
#SBATCH --cpus-per-task=1
#SBATCH --constraint=icelake
##SBATCH --constraint=cascadelake
#SBATCH --mem=105G
#SBATCH --job-name=wet-ribbon-NUMBER

date

# Cargar el módulo de Quantum ESPRESSO
module purge
module load QuantumESPRESSO/7.1-intel-2022a

# Ejecutar Quantum ESPRESSO con srun
srun pw.x -nk 4 < wet-ribbon-conf-NUMBER.in > wet-ribbon-conf-NUMBER.out

echo Calculation successful.

date
