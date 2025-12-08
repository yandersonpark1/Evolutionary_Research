import sys 

'''
pdb_id taken from main -> four character code 
chain taken from main -> single letter 
'''
def download_pdb(pdb_id, chain): 
    print(f'Looking for pdb file and chain at https://files.rcsb.org/view/{pdb_id}.pdb')

def main(): 
    if len(sys.argv) < 4: 
        print("Usage: python3 your_script_name.py <output_directory> <pdbfile> <chains>")
        print("Example: python3 webscraper_ind.py /research/output_pdbs 1a5t 'a'")
        sys.exit(1)
    
    out_dir = sys.argv[1]
    pdb_id = sys.argv[2].lower() 
    
    if len(pdb_id) != 4: 
        print(f'The pdb_file you are looking for {pdb_id} is invalid. Please enter a valid four character pdb id.')
        sys.exit(1)
    
    # right now assuming user wants to one chain from the pdb file
    chain = sys.argv[2].upper() 
    if not chain.isalpha(): 
        print(f'The chain you have entered {chain} is not valid. Please enter a valid character chain A-Z.')
        sys.exit(1)
    
    print(f'You are looking for chain {chain} on pdb file {pdb_id}.')
    
    '''Format should follow: https://files.rcsb.org/view/{pdb_id}.pdb'''
    download_pdb(pdb_id, chain)
    
    
    

if __name__ == "__main__": 
    main()