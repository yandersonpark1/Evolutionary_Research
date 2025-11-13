import sys 
import json 
from collections import defaultdict 
import os

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
    
    if not os.path.isfile(input_file):
        print(f"Error: Input file '{input_file}' not found in current directory.")
        sys.exit(1)

    # ⚠️ Check if output file exists
    if os.path.exists(output_file):
        response = input(f"⚠️ Output file '{output_file}' already exists. Overwrite? (y/n): ").strip().lower()
        if response not in ["y", "yes"]:
            print("Operation cancelled.")
            sys.exit(0)
    
    cath_organized = parse_file(input_file)
    
    with open(output_file, "w") as output: 
        json.dump(cath_organized, output, indent=4)
        
    print(f"Parse {input_file} and saved results in {output_file}")


if __name__ == "__main__": 
    main()
