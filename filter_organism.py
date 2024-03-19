import argparse
import csv

def filter_species(input_file, output_file, species_1='Homo sapiens', species_2='Homo sapiens'):
    with open(input_file, 'r', newline='') as input_csvfile, \
            open(output_file, 'w', newline='') as output_csvfile:
        reader = csv.DictReader(input_csvfile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(output_csvfile, fieldnames=fieldnames)
        writer.writeheader()

        if species_1 == species_2:
            for row in reader:
                if row['receptor_organism'] == species_1 and row['peptide_organism'] == species_2:
                    writer.writerow(row)
        else:
            for row in reader:
                if row['receptor_organism'] == species_1 and row['peptide_organism'] == species_2:
                    writer.writerow(row)
                elif row['receptor_organism'] == species_2 and row['peptide_organism'] == species_1:
                    writer.writerow(row)

def main():
    parser = argparse.ArgumentParser(description="Filter interactions with interested organism")
    parser.add_argument("input_file", help="Input CSV file")
    parser.add_argument("output_file", help="Output CSV file")
    parser.add_argument("--species_1", default="Homo sapiens", help="Species 1 (default: Homo sapiens)")
    parser.add_argument("--species_2", default="Homo sapiens", help="Species 2 (default: Homo sapiens)")

    args = parser.parse_args()
    filter_species(args.input_file, args.output_file, args.species_1, args.species_2)

if __name__ == "__main__":
    main()
