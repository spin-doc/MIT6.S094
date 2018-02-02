from os.path import expanduser, isfile

to_tbl = expanduser('~/cs/mit6.s094/references.tsv')
md = ''

with open(expanduser(to_tbl), 'r') as f:
    header = f.readline().rstrip().split('\t')
    atl_col = ['Brief Author', 'Brief Title', 'Link']
    atl_ind = list(map(lambda x: header.index(x), atl_col))
    for line in f.readlines():
        cols = line.rstrip().split('\t')
        if len(cols) < (max(atl_ind)+1):
            continue
        a, t, l = list(map(lambda x: cols[x], atl_ind))
        if a == '':
            md += f"- [{t}]({l})\n"
        else:
            md += f"- {a} ⠶ [{t}]({l})\n"

out_tbl = to_tbl.rstrip('erences.tsv') + '-list.md'
with open(out_tbl, 'w') as f:
    f.write(md)
