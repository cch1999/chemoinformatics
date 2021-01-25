from pdbe import pyPDBeREST
import json



def fetch_pdb_ligands(pdb_id, verbose=False):

    p = pyPDBeREST()

    data = p.PDB.getLigands(pdbid=pdb_id)
    
    if verbose:
        print(data)

    data = json.loads(data)
    data = data[pdb_id]
    
    if verbose:
        print()
        print(len(data), "ligands found in", pdb_id+":")

        for i, ligand in enumerate(data):
            print(" ",i+1,ligand["chem_comp_id"])

    return data

fetch_pdb_ligands("4hhb", verbose=True)