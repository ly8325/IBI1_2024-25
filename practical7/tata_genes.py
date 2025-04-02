import re
input = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
tata=open("tata_genes.fa", "w")
a=""
b=""
for line in input:
    line = line.rstrip()
    if '>' in line:
        if re.search('TATAAAA',b) or re.search('TATAAAT',line) or re.search('TATATAA',line) or re.search('TATATAT',line):
            a=re.findall(r'gene:(\S+)',header)[0]
            tata.write(f'>{a}\n{b}\n')
        header=line 
        b=""
    else:
        b+=line   
if re.search('TATAAAA',b) or re.search('TATAAAT',line) or re.search('TATATAA',line) or re.search('TATATAT',line):
    a=re.findall(r'gene:(\S+)',line)[0]
    tata.write(f'>{a}\n{b}\n')       
tata.close()
input.close()