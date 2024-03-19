import argparse
import csv
import requests

def extract_organism_from_pdb(pdb_id):
    try:
        response = requests.get(f"https://data.rcsb.org/rest/v1/core/polymer_entity/{pdb_id}/1")
        if response.status_code == 200:
            data = response.json()
            organism_list = data.get("rcsb_entity_source_organism", [])
            for organism in organism_list:
                if "ncbi_scientific_name" in organism:
                    return organism["ncbi_scientific_name"]
            return ""
        else:
            print(f"Warning: Failed to retrieve data for PDB ID {pdb_id}")
            return None
    except Exception as e:
        print(f"Error processing PDB {pdb_id}: {e}")
        return None


def add_organism_to_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='ISO-8859-1') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        rows = list(reader)

    header.extend(['receptor_organism', 'peptide_organism'])

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for row in rows:
            receptor_pdb_id = row[0][:-2]  # remove subchain
            peptide_pdb_id = row[1][:-2]   
            receptor_organism = extract_organism_from_pdb(receptor_pdb_id)
            peptide_organism = extract_organism_from_pdb(peptide_pdb_id)
            row.extend([receptor_organism, peptide_organism])
            writer.writerow(row)

def main(args):
    add_organism_to_csv(args.input_file, args.output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add organism information to CSV file")
    parser.add_argument("input_file", help="Input CSV file")
    parser.add_argument("output_file", help="Output CSV file")
    args = parser.parse_args()
    main(args)
