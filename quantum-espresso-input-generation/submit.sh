#!/bin/bash -l

for number in {1..100}

do
	 sed "s/NUMBER/$number/g" job-base.slurm > job.slurm
	 sbatch < job.slurm
done
