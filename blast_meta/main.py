import argparse
import sys, os
from path import path

from counting import run_counting

def main(argv):
    arg_parser = argparse.ArgumentParser(prog="blast_meta",
            description="parses fasta files for counts of species hits")
    arg_parser.add_argument('--data_folder', '-d',
            required=True,
            help="data folder to search")
    arg_parser.add_argument('--output_file', '-o',
            required=True,
            help="where to save the results")
    arg_parser.add_argument('--extention', '-e',
            required=False,
            default='*.fasta',
            help="files to load, glob syntax, like *.fasta or *.fasta_out")
    arg_parser.add_argument('--verbose', '-v', action='store_true',
            required=False,
            default=False, help="print status and completion rate")
    if len(argv) == 1:
        argv.append('--help')
    args = arg_parser.parse_args(argv[1:])
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w',0)
    output_file = path(args.output_file)
    output_file = output_file.abspath()
    # check that the output folder exists
    if output_file.exists():
        print "{0} already exists".format(output_file)
        sys.exit()
    elif not output_file.dirname().exists():
        print "directory {0} does not exist, please make it".format(output.dirname())
        sys.exit()
    data_folder = path(args.data_folder)
    if not data_folder.exists():
        print "{0} does not exist, please chose a valid data folder".format(data_folder)
        sys.exit()
    run_counting(data_folder, output_file, args.extention, args.verbose)
    if args.verbose:
        print "\n\nDONE! :)"


if __name__ == "__main__":
    main(sys.argv)
