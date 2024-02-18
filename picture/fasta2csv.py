#!/usr/bin/python
#-*-coding:utf-8-*-

import sys, os


if len(sys.argv) <= 1:
    print('\nPlease provide input FASTA file.\n')
    print('Usage:\nfasta2csv.py input.fst output.csv\n')
    sys.exit()

if sys.argv[1] == '-h' or sys.argv[1] == 'help'or sys.argv[1] == '-help':
    print('\nUsage:\npython fasta2csv.py  input.fst  output.csv\n')
    sys.exit()

input = sys.argv[1] 
if not os.path.exists(input):
    print('\nError: File "%s" is not exist!\n' % input)
    sys.exit()

output = 'output.csv'
if len(sys.argv) > 2:
    output = sys.argv[2]
    
# Read in FASTA
file = open(input, 'r')
lines_i = file.readlines()
seq = ''

for l in lines_i:
    if l[0] == '>':
        'Fasta head line'
        seq_id = l.strip()
    else:
        'Sequence line'
        seq += l.strip()

file.close()

print('The Input file is: %s' %input)


# Convert FASTA to CSV
l = []
lines = [str(seq_id) + '\n']
for i, c in enumerate(seq):
    l.append(c)
    if i % 60 == 59:
        lines.append(','.join(l) + '\n')
        l = []

if l != []:
    lines.append(','.join(l) + '\n')
    
    
# Output CSV file
file = open(output, 'w')
file.writelines(lines)
file.close()
print('The Output file is: %s' %output)
