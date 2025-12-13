''' A few things to Note: 
The parser is mainly for exporting chains from a pdb in order to redesign using a protein sequencing model 
Will skip over non atoms listed in pdb (i.e. Remarks atoms)
'''
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
    
    
''' 
Writes pdb file into output_folder as <pdb_id + chain + .pdb>
Returns -> out_dir path to file 
'''
def output_pdb_contents(pdb_contents, out_dir, pdb_id, chain): 
    new_file_name = pdb_id + chain + '.pdb'
    out_dir = os.path.join(out_dir, new_file_name)
    
    try: 
        with open(out_dir, "w", encoding="utf-8") as f: 
            f.write(pdb_contents)
        print(f'File written successfully to {out_dir}')
    except Exception as e: 
        print(f'File could not be written: {e}')
        
    return out_dir


''' Writes pdb for all chains in the pdb file'''
def clean_for_all_chain(path_location): 
    filtered = []
    
    writing = False
    
    try: 
        with open(path_location, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.split()
                if parts and parts[0] == "ATOM":
                    filtered.append(line)
                    writing = True
                    
                
                elif parts and parts[0] == "TER": 
                    filtered.append(line)
                    writing = False
                     
                
                elif writing: 
                    filtered.append(line)
                    
                    
            print(f'Successfully opened file at {path_location}')
    
    except Exception as e: 
        print(f'Could not access file at {path_location}')
        
    try: 
        with open(path_location, "w", encoding="utf-8") as out:
            out.writelines(filtered)
        print(f'Successfully rewrote file at {path_location}')
    except Exception as e: 
        print(f'Could not rewrite file at {path_location}: {e}')
        
    return path_location


'''Looks for specific chain in pdb file'''
def clean_specific_chain(pdb_chains_location, chain): 
    filtered = []
    writing = False
    
    try: 
        with open(pdb_chains_location, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.split()
                if parts and parts[4] == chain:
                    filtered.append(line)
                    writing = True
                    
                
                elif parts and parts[0] == "TER": 
                    filtered.append(line)
                    writing = False
                     
                
                elif writing: 
                    filtered.append(line)
                    
                    
            print(f'Successfully opened file at {pdb_chains_location}')
    
    except Exception as e: 
        print(f'Could not access file at {pdb_chains_location}')
        
    try: 
        with open(pdb_chains_location, "w", encoding="utf-8") as out:
            out.writelines(filtered)
        print(f'Successfully rewrote file for chain {chain} at {pdb_chains_location}')
    except Exception as e: 
        print(f'Could not rewrite file at {pdb_chains_location} for chain {chain}: {e}')
    
    return pdb_chains_location

'''Looks for specific pdb chain: given as x:y includinhg both x and y'''
def clean_for_seq(pdb_chain_specific_location, seq_range): 
    start = seq_range.partition(':')[0]
    end = seq_range.partition(':')[2]
    print(f'You are looking for seq range: {start} to {end}' )
    
    
    filtered = []
    writing = False
    true_idx = []
    correct_idx = True
    last_idx = 0
    
    try: 
        with open(pdb_chain_specific_location, "r", encoding="utf-8") as f:
            
            for line in f:
                parts = line.split()
                
                # check to make sure there is at least 5 elemnents in the list if not will crash while reading file
                # cannot access index element 5 if not present -> will throw index out of error 
                if parts and parts[0] == "TER": 
                    filtered.append(line)
                    writing = False
                    if int(last_idx) < int(end): 
                        true_idx.append(last_idx)
                        correct_idx = False
                    else: 
                        true_idx.append(last_idx)
                
                
                #check to make sure starting residue if not start at first residue number 
                elif parts and len(true_idx) == 0 and int(parts[5]) > int(start):
                    filtered.append(line)
                    writing = True
                    true_idx.append(parts[5])
                    correct_idx = False
                    
                    
                elif parts and parts[5] and parts[5] == start:
                    filtered.append(line)
                    writing = True
                    if len(true_idx) == 0:
                        true_idx.append(parts[5])
                    
                
                elif parts and parts[5] and parts[5] == end: 
                    filtered.append(line)
                    writing = False
                    last_idx = parts[5]        

                
                elif writing: 
                    filtered.append(line)
                    last_idx = parts[5]
                    
                    
                    
            print(f'Successfully opened file at {pdb_chain_specific_location}')
    
    except Exception as e: 
        print(f'Could not access file at {pdb_chain_specific_location}: {e}')

    try: 
        with open(pdb_chain_specific_location, "w", encoding="utf-8") as out:
            out.writelines(filtered)
        
        if correct_idx: 
            print(f'Successfully rewrote file for seq range {true_idx[0]} to {true_idx[1]} at {pdb_chain_specific_location}')
        else: 
            print(f'Successfully rewrote file. Invalid initial range, actual range is {true_idx[0]} to {true_idx[1]} at {pdb_chain_specific_location}')
    except Exception as e: 

        print(f'Could not rewrite file at {pdb_chain_specific_location} for seq range {start} to {end}: {e}')
    
    return pdb_chain_specific_location
    


def main(): 
    if len(sys.argv) < 4: 
        print("Usage: python3 your_script_name.py <output_directory> <pdbfile> <chains> <seqs #>")
        print("Example: python3 webscraper_ind.py /research/output_pdbs 1a5t 'a' 2:90")
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
    
    #looking for chain number
    
    seq_range = str(sys.argv[4])
    
    
    print(f'You are looking for chain {chain} on pdb file {pdb_id}.')
    
    '''Format should follow: https://files.rcsb.org/view/{pdb_id}.pdb'''
    pdb_contents = download_pdb(pdb_id)
    
    '''Output the pdb_contents from download_pdb to the correct directory'''
    path_location = output_pdb_contents(pdb_contents, out_dir, pdb_id, chain)
    
    '''cleans pdb files for chains only'''
    pdb_chains_location = clean_for_all_chain(path_location)
    
    pdb_chain_specific_location = clean_specific_chain(pdb_chains_location, chain)
    
    final_pdb_file_path = clean_for_seq(pdb_chain_specific_location, seq_range)
    
    return final_pdb_file_path

    
    
    

if __name__ == "__main__": 
    main()