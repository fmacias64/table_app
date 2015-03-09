#! /usr/bin/env python
import sys, json

for row in sys.stdin:
  obj = json.loads(row)
  content = obj['content'].split()
  ner = obj['ner'].split()
  start_index = 0
  phrases = []
  # sys.stderr.write(' '.join(content) + '\n')
  # sys.stderr.write(str(len(content)) + '\n')
  # sys.stderr.write(' '.join(ner) + '\n')
  # sys.stderr.write(str(len(ner)) + '\n')


  while start_index < len(content):
    # Checking if there is a PERSON phrase starting from start_index
    index = start_index
    while index < len(content) and ner[index] == "PERSON":
      index += 1
    if index != start_index:   # found a person from "start_index" to "index"
      text = ' '.join(content[start_index:index])
      phrases.append((start_index, text))
    start_index = index + 1

  # Output a tuple for each PERSON phrase
  for position, text in phrases:
    print json.dumps({
      "mid": '%s_%d' %(obj['cell_id'], position),
      "position": position,
      "cell_id": obj['cell_id'],
      "content": text,
      "filename": obj['filename'],
      "page": int(obj['page']),
      "table_id": int(obj['table_id']),
      "row": int(obj['row']),
      "column_start": int(obj['column_start']),
      "column_end": int(obj['column_end'])
    })