#! /usr/bin/env python
import sys, json

for row in sys.stdin:
  obj = json.loads(row)
  content = obj['content']
  ner = obj['ner'].split()
  pos = obj['pos'].split()
  start_index = 0
  phrases = []

  # a position does not contain person
  if 'PERSON' in ner: continue

  # must end with noun
  if pos[-1][0] != 'N': continue

  # not the first row
  if obj['row'] == 0: continue

  position = 0
  # Output a tuple for each position
  print json.dumps({
    "mid": 'position_%s_%d' %(obj['cell_id'], position),
    "position": position,
    "cell_id": obj['cell_id'],
    "content": content,
    "filename": obj['filename'],
    "page": int(obj['page']),
    "table_id": int(obj['table_id']),
    "row": int(obj['row']),
    "column_start": int(obj['column_start']),
    "column_end": int(obj['column_end'])
  })