from Bio.Blast.NCBIWWW import qblast
from pdbe import pyPDBeREST
import json

def find_uniprot_ligands(uniprot_id):
    return 1

def blast_pdb(uniprot_id, verbose=False):

    results_handle = qblast("blastp", "pdb", uniprot_id)
    blast_results = NCBIXML.read(result_handle)

    if verbose:
        for blast_result in blast_results:
            print(blast_result)

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

blast_pdb("P69905", verbose=True)