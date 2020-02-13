#!/usr/bin/env python

import bibtexparser
import sys

with open(sys.argv[1], 'r') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

for idx, entry in enumerate(bib_database.entries):
#     print(entry['title'])
    if 'url' in entry:
        if ' ' in entry['url']:
            entry['url'] = entry['url'].split(' ')[0]
        entry['title'] = '\href{' + entry['url'] + '}{' + entry['title'] + '}'
        del entry['url']
    bib_database.entries[idx] = entry

with open(sys.argv[2], 'w') as bibtex_file:
    bibtexparser.dump(bib_database, bibtex_file)