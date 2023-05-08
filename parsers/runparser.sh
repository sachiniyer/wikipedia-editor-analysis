#!/bin/bash
#
##SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=64
#SBATCH --time=2:00:00:00
#SBATCH --mem=128GB
#SBATCH --job-name=parsers
#SBATCH --mail-type=END
#SBATCH --mail-user=si2073@nyu.edu
#SBATCH --output=slurm_%j.out

input_dir="/scratch/si2073/data"
output_dir="/scratch/si2073/output"
temp_dir="/scratch/si2073/temp"

for input_file in $input_dir/*.7z; do
    filename=$(basename -- "${input_file%.*}")
    srun python3 xmlparser.py "$filename" "$input_dir" "$output_dir" "$temp_dir" &
done

wait
