import sys 
import json 
from collections import defaultdict 
import os

''' base_folder -> output base folder you want to create, cath_db -> defualtdict(list) '''
def create_output_folder(base_folder, cath_db): 
    try:
        os.makedirs(base_folder, exist_ok=True)
        print(f"Base folder '{base_folder}' ensured to exist.")
    except OSError as e:
        print(f"Error creating base folder '{base_folder}': {e}")
        return False 

    for cath_family, pdb_domain_list in cath_db.items():
        
        # --- Create Sub-Folder for the Key (cath_family) ---
        # The full path to the new sub-folder: base_folder/cath_family/
        sub_folder_path = os.path.join(base_folder, cath_family)
        
        try:
            # Create the sub-folder
            os.makedirs(sub_folder_path, exist_ok=True)
            print(f"  Created sub-folder: {sub_folder_path}")
        except OSError as e:
            print(f"Error creating sub-folder {sub_folder_path}: {e}")
            continue # Skip this key and move to the next one
            
        # --- Create File inside the Sub-Folder ---
        file_name = f"{cath_family}.txt"
        # The full path to the new file: base_folder/cath_family/cath_family.txt
        full_path = os.path.join(sub_folder_path, file_name)

        num_entries = len(pdb_domain_list)

        try:
            with open(full_path, 'w') as f:
                # a. Print the length of the list
                f.write(f"{num_entries}\n")

                # b. Iterate through the list of (pdb, domain) tuples
                for pdb, domain_in_pdb in pdb_domain_list:
                    f.write(f"{pdb}, {domain_in_pdb}\n")

            print(f"  Successfully created and wrote to: {full_path}")

        except IOError as e:
            print(f"Error writing to file {full_path}: {e}")

    return True # Indicate success

def parse_file(input_file): 
    cath_organized = defaultdict(list)
    
    with open(input_file) as file: 
        for line in file: 
            parts = line.strip().split()
            if len(parts) >= 4: 
                cath_family = parts[2]
                pdb = parts[0][:4]
                domain_in_pdb = parts[3]
                cath_organized[cath_family].append((pdb, domain_in_pdb))
    
    return cath_organized

def main(): 
    if len(sys.argv) < 3: 
        print('Format: python parse_cathdb.py <input_file.name> <output_file_name.json>')
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    output_folder = sys.argv[3]
    
    if not os.path.isfile(input_file):
        print(f"Error: Input file '{input_file}' not found in current directory.")
        sys.exit(1)

    # ⚠️ Check if output file exists
    if os.path.exists(output_file):
        response = input(f"⚠️ Output file '{output_file}' already exists. Overwrite? (y/n): ").strip().lower()
        if response not in ["y", "yes"]:
            print("Operation cancelled.")
            sys.exit(0)
    
    # create dict for CATH
    cath_organized = parse_file(input_file)
    
    # create JSON CATH file as HashMap
    with open(output_file, "w") as output: 
        json.dump(cath_organized, output, indent=4)
        
    print(f"Parse {input_file} and saved results in {output_file}")
    
    
    ''' Output Folder Structure '''
    print(f"\nStarting hierarchical folder and file creation in '{output_folder}'...")
    success = create_output_folder(output_folder, cath_organized)
    
    if success:
        print("\nOperation complete.")
    else:
        print("\nOperation finished with errors in file creation.")


if __name__ == "__main__": 
    main()
