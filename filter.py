import argparse
import csv

def filter_csv(input_file, output_file, class_label = 2 , predict_label = 4 , confidence_column = 3, encoding='UTF-8', confidence_filter=0):
    with open(input_file, 'r', newline='', encoding=encoding) as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        filtered_rows = [row for row in reader if float(row[class_label]) == 0 and row[predict_label] == '1' and float(row[confidence_column]) >= confidence_filter]

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for row in filtered_rows:
            writer.writerow(row)

def main(args):
    filter_csv(args.input_file, args.output_file, args.encoding, args.confidence_filter)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter CSV novo positive prediction with confidence value (optional)")
    parser.add_argument("input_file", help="Input CSV file")
    parser.add_argument("output_file", help="Output CSV file")
    parser.add_argument("--class_label", type=int, default= 2, help="column of class_label")
    parser.add_argument("--predict_label", type=int, default= 4, help="Column of predict_label")
    parser.add_argument("--confidence_column", type=int, default= 3, help="Column of prediction confidence")
    parser.add_argument("--encoding", default="UTF-8", help="Encoding of the input CSV file (default: UTF-8). Optional. Use 'ISO-8859-1' for ISO-8859-1 encoding.")
    parser.add_argument("--confidence_filter", type=float, default=0, help="Confidence filter. e.g. Filtering out rows with confidence greater than 0.99999 (default: 0)")
    args = parser.parse_args()
    main(args)
