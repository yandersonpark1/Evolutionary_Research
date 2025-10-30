#!/bin/bash 

#SBATCH -p general 

source ~/.bashrc

conda activate proteinmpnn

python goldman_lab/software/ProteinMPNN/protein_mpnn_run.py