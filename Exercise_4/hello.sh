#!/bin/sh
#SBATCH --job-name=hello_slurm
#SBATCH --output=hello.log
#SBATCH --time=01:00:00
#SBATCH --ntasks=1

echo hello world

