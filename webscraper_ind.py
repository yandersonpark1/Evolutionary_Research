import sys
#need to run python -m pip install requests 
import requests
import os

'''
pdb_id taken from main -> four character code 
chain taken from main -> single letter 
'''
def download_pdb(pdb_id): 
    pdb_url = f'https://files.rcsb.org/view/{pdb_id}.pdb'
    r = requests.get(pdb_url)
    
    #checks to make sure url is valid
    if r.ok: 
        print(f'Succesfully loaded url: {pdb_url}')
        return r.text
    else: 
        print(f'Error 400, could not load url: {pdb_url}')
        sys.exit(1)
    
    
''' Writes pdb file into output_folder as <pdb_id + chain + .pdb>'''
def output_pdb_contents(pdb_contents, out_dir, pdb_id, chain): 
    new_file_name = pdb_id + chain + '.pdb'
    out_dir = os.path.join(out_dir, new_file_name)
    
    try: 
        with open(out_dir, "w", encoding="utf-8") as f: 
            f.write(pdb_contents)
        print(f'File written successfully to {out_dir}')
    except Exception as e: 
        print(f'File could not be written: {e}')
        
def clean_for_chain(): 
    pass

def main(): 
    if len(sys.argv) < 4: 
        print("Usage: python3 your_script_name.py <output_directory> <pdbfile> <chains>")
        print("Example: python3 webscraper_ind.py /research/output_pdbs 1a5t 'a'")
        sys.exit(1)
    
    out_dir = sys.argv[1]
    
    out_dir = os.path.abspath(out_dir)
    if not os.path.isdir(out_dir):
        print(f'The directory {out_dir} is not a valid directory. Please make sure you set the correct path. If you want a folder in your cd simply write the folder name or follow with any /<other_folder>')
        sys.exit(1)
    print(f'Found directory {out_dir}')
    
    pdb_id = sys.argv[2].lower() 
    
    if len(pdb_id) != 4: 
        print(f'The pdb_file you are looking for {pdb_id} is invalid. Please enter a valid four character pdb id.')
        sys.exit(1)
    
    # right now assuming user wants to one chain from the pdb file
    chain = sys.argv[3].upper() 
    if not chain.isalpha(): 
        print(f'The chain you have entered {chain} is not valid. Please enter a valid character chain A-Z.')
        sys.exit(1)
    
    print(f'You are looking for chain {chain} on pdb file {pdb_id}.')
    
    '''Format should follow: https://files.rcsb.org/view/{pdb_id}.pdb'''
    pdb_contents = download_pdb(pdb_id)
    
    '''Output the pdb_contents from download_pdb to the correct directory'''
    output_pdb_contents(pdb_contents, out_dir, pdb_id, chain)
    
    
    
    
    
    

if __name__ == "__main__": 
    main()