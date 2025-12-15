PDB Chain & Sequence Range Parser

A lightweight Python utility for downloading Protein Data Bank (PDB) files and extracting specific chains and residue ranges for downstream protein redesign workflows.

This parser was built to support large-scale protein domain redesign using protein sequence or structure-based models.

The parser is designed for exporting chains from PDB files for protein redesign using sequencing or structure-based models

Only ATOM records are retained

Non-atomic entries (e.g. REMARK, HETATM, metadata) are skipped

The output is a minimal, clean PDB suitable for downstream modeling

If the requested residue range does not exactly exist, the script will:

Extract the closest valid range

Report the actual residue indices used

This tool automates that process by:

Downloading a PDB file from the RCSB

Removing non-atomic records

Selecting a specific chain

Extracting a user-defined residue range

Writing a cleaned PDB file ready for redesign or modeling

Structured Terminal Input: 
python PDB_WebParser/webscraper_ind.py <output_directory> <pdb_id> <chain> <start:end>

Example Terminal Input:
python PDB_WebParser/webscraper_ind.py ./output_pdbs 1a5t A 2:90