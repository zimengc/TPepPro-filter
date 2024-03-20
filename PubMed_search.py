import csv
import argparse
from Bio import Entrez

def search_pubmed_pdbid(pdb_id_1, pdb_id_2):
    Entrez.email = "your.email@example.com"
    query = f"({pdb_id_1}[PDB] AND {pdb_id_2}[PDB])"
    handle = Entrez.esearch(db="pubmed", term=query)
    record = Entrez.read(handle)
    pubmed_ids = record["IdList"]
    return pubmed_ids

def search_pubmed(gene_name_1, gene_name_2):
    Entrez.email = "your.email@example.com"
    query = f"({gene_name_1}[Gene name] AND {gene_name_2}[Gene name])"
    handle = Entrez.esearch(db="pubmed", term=query)
    record = Entrez.read(handle)
    pubmed_ids = record["IdList"]
    return pubmed_ids

def get_pubmed_id(input_file, output_file):
    try:
        with open(input_file, 'r', newline='') as input_csvfile:
            reader = csv.reader(input_csvfile)
            header = next(reader)

            # 读取原始的 CSV 文件内容，并添加 PubMed_IDs 列
            rows = []
            for row in reader:
                receptor_pdb_id = row[0][:-2]
                peptide_pdb_id = row[1][:-2]
                pubmed_ids = search_pubmed(receptor_pdb_id, peptide_pdb_id)
                row.append(', '.join(pubmed_ids) if pubmed_ids else 'No PubMed IDs found')
                rows.append(row)

        with open(output_file, 'w', newline='') as output_csvfile:
            writer = csv.writer(output_csvfile)
            # 写入原始的 CSV 文件内容
            writer.writerow(header + ['PubMed_IDs'])  # 添加 PubMed_IDs 列标题
            writer.writerows(rows)  # 写入原始数据及 PubMed_IDs 列

    except UnicodeDecodeError:
        with open(input_file, 'r', newline='', encoding='ISO-8859-1') as input_csvfile:
            reader = csv.reader(input_csvfile)
            header = next(reader)

            # 读取原始的 CSV 文件内容，并添加 PubMed_IDs 列
            rows = []
            for row in reader:
                receptor_pdb_id = row[0][:-2]
                peptide_pdb_id = row[1][:-2]
                pubmed_ids = search_pubmed(receptor_pdb_id, peptide_pdb_id)
                row.append(', '.join(pubmed_ids) if pubmed_ids else 'No PubMed IDs found')
                rows.append(row)

        with open(output_file, 'w', newline='') as output_csvfile:
            writer = csv.writer(output_csvfile)
            # 写入原始的 CSV 文件内容
            writer.writerow(header + ['PubMed_IDs'])  # 添加 PubMed_IDs 列标题
            writer.writerows(rows)  # 写入原始数据及 PubMed_IDs 列

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed IDs of papers that contain pairs of PDB IDs in CSV file")
    parser.add_argument("input_file", help="Input CSV file containing PDB IDs")
    parser.add_argument("output_file", help="Output CSV file with added PubMed IDs")
    args = parser.parse_args()

    get_pubmed_id(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
