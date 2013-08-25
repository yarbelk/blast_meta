from collections import Counter
import re
import csv


_re_species = re.compile(r">(_R_)?(?P<species>\w+_\w+[ _]\d+)")


def run_counting(data_folder, output_file, ext, verbose=False):
    files = data_folder.files(ext)
    species_names = set()
    species_counts = {}
    for fasta_file in files:
        base = fasta_file.namebase
        species_counts[base] = Counter()
        with open(fasta_file, 'r') as data:
            for line in data:
                match = _re_species.search(line)
                if match:
                    gd = match.groupdict()
                    species_names.add(gd['species'])
                    species_counts[base][gd['species']] += 1
    header = list(species_names)
    header.sort()
    keys = species_counts.keys()
    keys.sort()
    with open(output_file, 'w') as results:
        csv_results = csv.writer(results,
                                 dialect='excel',
                                 delimiter=',')
        csv_results.writerow(['',] + header)
        for key in keys:
            data_row = [key,] + [species_counts[key][species] for species in header]
            csv_results.writerow(data_row)
