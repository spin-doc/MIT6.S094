from os.path import expanduser, isfile

to_tbl = expanduser('~/cs/mit6.s094/references.tsv')
md = ''

with open(expanduser(to_tbl), 'r') as f:
    header = f.readline().rstrip().split('\t')
    md += f"|{'|'.join(header)}|\n"
    md += f"|{'|'.join(['---'] * len(header))}|\n"
    ncol = len(header)
    for line in f.readlines():
        cols = line.rstrip().split('\t')
        md += f"|{'|'.join(cols + [''] * (ncol-len(cols)))}|\n"

out_tbl = to_tbl.rstrip('tsv') + 'md'
with open(out_tbl, 'w') as f:
    f.write(md)
