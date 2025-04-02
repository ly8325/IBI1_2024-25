import re
input = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
tata=open("tata_genes.fa", "w")
a=""
b=""
for line in input:
    line = line.rstrip()
    if '>' in line:
        a=re.findall(r'gene:(\S+)',line)[0]
        if re.search('TATAAAA',b) or re.search('TATAAAT',b) or re.search('TATATAA',b) or re.search('TATATAT',b):
            tata.write(f'>{a}\n{b}\n') 
        b=""
    else:
        b+=line   
if re.search('TATAAAA',b) or re.search('TATAAAT',b) or re.search('TATATAA',b) or re.search('TATATAT',b):
    a=re.findall(r'gene:(\S+)',line)[0]
    tata.write(f'>{a}\n{b}\n')       
tata.close()
input.close()