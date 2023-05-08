#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --time=4:00:00
#SBATCH --mem=8GB
#SBATCH --job-name=download_files
#SBATCH --mail-type=END
#SBATCH --mail-user=si2073@nyu.edu
#SBATCH --output=slurm_%j.out

cd /scratch/$USER || exit

# Read URLs from the file and download each one with wget
while read url; do
  srun wget -P data "$url" -q
done <file_links
