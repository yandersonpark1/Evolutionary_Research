# Evolutionary_Research
Computational Pipeline for Protein Sequencing and Analysis

Description 
-------------------------------------------------------------
All code down below is used for Evolutionary Research in the Goldman Lab 

- Cath_db parser: Used to download all the latest CATH proteins and organzie into a dictionary 
    - {homology: [pdb, chain], homology2: [pdb2, chain2], etc }
    - Create folder structure for entire CATH database: output folder with sub folder base/homology
        - Create file in output folder base/homology/homology.txt with number of domains, each row is a domain pdb file,  chain in pdb file

- Webscraper: Used to download PDBs from PDB website 
    - Works from CATH database downloading based on Homologies or manual input including chain and chain indices
