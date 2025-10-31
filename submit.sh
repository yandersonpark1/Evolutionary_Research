#!/bin/bash 

#SBATCH --job-name=proteinmpnn
#SBATCH --output=/goldman_lab/mpnn/logs/pdb#.out
#SBATCH --mem=16G
#SBATCH --time=04:00:00
#SBATCH --cpus-per-task=8
#SBATCH --partition=8core
#SBATCH --nodes=1

source ~/.bashrc

conda activate proteinmpnn

python goldman_lab/software/ProteinMPNN/protein_mpnn_run.py  \
    --pdb_path \
    --out_folder \
    --num_seq_per_target 10 \
    --batch_size 1 \