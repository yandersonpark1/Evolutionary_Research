import webbrowser
import sys 
import os

class Scraper: 
    ''' homology -> input of homology folder 
        CATH_db -> root folder with database
        '''
    def __init__(self, dir_folder, homology): 
        self.dir_folder = dir_folder
        self.homology = homology
        self.path = f"{dir_folder}/{homology}/"
        
        self.pdb_link = "https://files.rcsb.org/view/"
        self.pdb_domains_res = []


    ''' Reads through a folder file '''
    def generate_pdb_link(self): 
        try:
            os.path.isdir(self.path)
            print(f"Base folder '{self.path}' ensured to exist.")
            print()
        except OSError as e:
            print(f"Error creating base folder '{self.path}': {e}")
            sys.exit(1)
        
        for dirpath, dirnames, filenames in os.walk(self.path): 
            for filename in filenames: 
                if filename.endswith(".txt"): 
                    full_file_path = os.path.join(dirpath, filename)
                
                try: 
                    with open(full_file_path, 'r') as parser: 
                        try: 
                            parser.readline()
                        except: 
                            print(f"File {full_file_path} is empty")
                            print()
                            continue 
                        
                        for line in parser: 
                            pdb_info = line.strip().split(',')
                            
                            
                            if len(pdb_info) < 2:
                                continue 
                            
                            pdb_id = pdb_info[0].strip().lower()
                            
                            if len(pdb_id) == 4: 
                                complete_pdb_url = (f"{self.pdb_link}{pdb_id}.pdb")
                                self.pdb_domains_res.append(complete_pdb_url)
                            
                            else: 
                                print(f'Malformed PDB {pdb_info}')
                except IOError as e: 
                    print(f"Error reading file {full_file_path}: {e}")


def main(): 
    if len(sys.argv) < 3: 
        print("Usage: python your_script_name.py <database_directory> <homology_directory>")
        print("Example: python scraper.py CATH_db ./1.10.10.10")
        sys.exit(1)
        
    db_dir = sys.argv[1]
    homology_dir = sys.argv[2]

    print(f"Initializing Scraper with homology directory: {db_dir}/{homology_dir}")
    print()

    # 1. Initialize the Scraper instance
    scraper = Scraper(db_dir, homology_dir)

    # 2. Call the method to generate the links
    scraper.generate_pdb_link()

    # 3. Optional: Summarize the results
    if scraper.pdb_domains_res:
        print(f"\n--- Process Complete ---")
        print(f"Successfully generated {len(scraper.pdb_domains_res)} PDB links.")
        
        print()
        for link in scraper.pdb_domains_res:
            print(f"- {link}")
        print() 
        print(f"Number of pdb links: {len(scraper.pdb_domains_res)}")
    else:
        print("\nNo valid PDB links were found.")


if __name__ == "__main__":
    main()


''' Need to get pdb file name from system args'''

''' 1. Need to take pdb '''