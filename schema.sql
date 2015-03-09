DROP TABLE IF EXISTS table_cells CASCADE;
CREATE TABLE table_cells(
  cell_id bigint,
  filename text,
  page int,
  table_id int,
  row int,
  column_start int,
  column_end int,
  content text,
  ner text,
  pos text
);

create table people_mentions(
  mid text,
  cell_id bigint,
  filename text,
  page int,
  table_id int,
  row int,
  column_start int,
  column_end int,
  position int,
  content text);

create table position_mentions(
  mid text,
  cell_id bigint,
  filename text,
  page int,
  table_id int,
  row int,
  column_start int,
  column_end int,
  position int,
  content text);

create table person_position(
  mid1 text,
  mid2 text,
  description text,
  relation_id bigint,
  is_true boolean);