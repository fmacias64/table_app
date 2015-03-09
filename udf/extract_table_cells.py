#! /usr/bin/env python

import fileinput
import json
import os
import glob
import sys
import json
from table_cell import TableCell
from nltk.tag.stanford import NERTagger
import nltk

def debug(str):
  sys.stderr.write("%s\n" % str)

BASE_FOLDER = os.path.split(os.path.realpath(__file__))[0]
BASE_FOLDER = BASE_FOLDER + "/.."
OUTPUT_DIR = BASE_FOLDER + "/pdf_rawtables"
TMP_DIR = BASE_FOLDER + "/tables_tmp"

# Create the temporary output directory if it does not exist
if not os.path.exists(OUTPUT_DIR):
  os.makedirs(OUTPUT_DIR)
if not os.path.exists(TMP_DIR):
  os.makedirs(TMP_DIR)

# ner tagger
st = NERTagger('/Users/feiran/workspace/stanford-ner-2014-08-27/classifiers/english.all.3class.distsim.crf.ser.gz',
               '/Users/feiran/workspace/stanford-ner-2014-08-27/stanford-ner.jar') 

cell_id = 0
# Process each file
for filename in [os.path.abspath(f) for f in glob.glob("%s/data/*.pdf" % BASE_FOLDER)]:
  debug("Processing %s" % filename)
  OUTPUT_FILE = "%s/%s.xml" %(OUTPUT_DIR, os.path.basename(filename))
  # os.system("java -jar %s/lib/totable.jar %s %s >| %s" %(BASE_FOLDER, filename, TMP_DIR, OUTPUT_FILE))
  # Read the table cells
  with open(OUTPUT_FILE) as f:
    cells = [TableCell.parse(x) for x in f.readlines()]
  # Output one tuple for each table cell
  for tc in [c for c in cells if c != None]:
    ners = st.tag(tc.content.split())
    content = [w[0] for w in ners]
    ner = ' '.join([n[1] for n in ners])
    pos = ' '.join([w[1] for w in nltk.pos_tag(content)])
    print json.dumps({
      "filename": os.path.basename(filename),
      "page": tc.page,
      "table_id": tc.table_id,
      "row": tc.row,
      "column_start": tc.column_from,
      "column_end": tc.column_to,
      "content": ' '.join(content),
      "ner": ner,
      "pos": pos,
      "cell_id": cell_id
    })
    cell_id += 1

