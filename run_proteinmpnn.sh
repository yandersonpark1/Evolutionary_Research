#!/bin/bash 

#SBATCH --job-name=proteinmpnn
#SBATCH --error=error.err
#SBATCH --mem=64G
#SBATCH --cpus-per-task=8
#SBATCH --partition=8core
#SBATCH --nodes=1


source ~/.bashrc

conda activate proteinmpnn

python goldman_lab/software/ProteinMPNN/protein_mpnn_run.py  \
    --pdb_path {folder_root_of_pdbs}/{homology_pdb_name} \
    --out_folder {folder_root_of_pdbs}/{homology_pdb_name}/output \
    --num_seq_per_target 10 \
    --batch_size 1 \