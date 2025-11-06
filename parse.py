#Class for parser to get pdbs from the necessary C.A.T.H database 
class Parser: 
    def __init__(self, file): 
        self.file = file 
        
    def parse_by_pdbs(self, file, cath_id): 
        
            