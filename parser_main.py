import argparse
import filter
import add_organism
import filter_organism

def main(args):
    if args.command == 'filter':
        filter.filter_csv(args.input_file, args.output_file, args.class_label ,args.predict_label ,args.confidence_column , args.encoding, args.confidence_filter)
    elif args.command == 'add_organism':
        add_organism.add_organism_to_csv(args.input_file, args.output_file)
    elif args.command == 'filter_organism':
        filter_organism.filter_homo_sapiens(args.input_file, args.output_file, args.receptor_organism, args.peptide_organism)

if __name__ == "__main__":
    top_parser = argparse.ArgumentParser(description="Main Command Line Interface")
    subparsers = top_parser.add_subparsers(dest='command', help='Available commands')

    # Parser for 'filter' command
    filter_parser = subparsers.add_parser('filter', help="Filter CSV novo positive prediction with confidence value (optional)")
    filter_parser.add_argument("input_file", help="Input CSV file")
    filter_parser.add_argument("output_file", help="Output CSV file")
    filter_parser.add_argument("--class_label", type=int, default= 2, help="column of class_label")
    filter_parser.add_argument("--predict_label", type=int, default= 4, help="Column of predict_label")
    filter_parser.add_argument("--confidence_column", type=int, default= 3, help="Column of prediction confidence")
    filter_parser.add_argument("--encoding", default="UTF-8", help="Encoding of the input CSV file (default: UTF-8). Optional: Try 'ISO-8859-1' for ISO-8859-1 encoding.")
    filter_parser.add_argument("--confidence_filter", type=float, default=0, help="Confidence filter. e.g. Filtering out rows with confidence greater than 0.99999 (default: 0)")

    # Parser for 'add_organism' command
    organism_parser = subparsers.add_parser('add_organism', help='Add organisms for receptor and peptide')
    organism_parser.add_argument("input_file", help="Input CSV file")
    organism_parser.add_argument("output_file", help="Output CSV file, with two extra columns of organisms")

    # Parser for 'filter_organism' command
    filter_organism_parser = subparsers.add_parser('filter_organism', help="Filter interactions with interested organism")
    filter_organism_parser.add_argument("input_file", help="Input CSV file")
    filter_organism_parser.add_argument("output_file", help="Output CSV file")
    filter_organism_parser.add_argument("--species_1", default="Homo sapiens", help="Species 1 (default: Homo sapiens)")
    filter_organism_parser.add_argument("--species_2", default="Homo sapiens", help="Species 2 (default: Homo sapiens)")

    # 解析命令行参数
    # args = parser.parse_args()
    args = top_parser.parse_args()
    
    # 如果命令为空或者用户输入 -h 或 --help，则显示全部帮助文档
    if not vars(args) or 'help' in vars(args):
        top_parser.print_help()
    # 如果命令行输入了 module 名称但没有参数，则显示该 module 的帮助文档
    elif 'command' in vars(args) and not vars(args)[args.command]:
        getattr(top_parser, args.command).print_help()
    else:
        main(args)