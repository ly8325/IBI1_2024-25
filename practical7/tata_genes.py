import re
input = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
#create a file to contain genes
tata=open("tata_genes.fa", "w")
#create a viable called a to contain gene's name
a=""
#create a viable called b to contain gene
b=""
for line in input:
    line = line.rstrip()
    #check if the line has gene's name
    if '>' in line:
        a=re.findall(r'gene:(\S+)',line)[0]
        #check if the gene has TATA box
        if re.search('TATAAAA',b) or re.search('TATAAAT',b) or re.search('TATATAA',b) or re.search('TATATAT',b):
            tata.write(f'>{a}\n{b}\n') 
        b=""
    else:
        #store a whole gene in b
        b+=line   
#check if the last gene has TATA box
if re.search('TATAAAA',b) or re.search('TATAAAT',b) or re.search('TATATAA',b) or re.search('TATATAT',b):
    a=re.findall(r'gene:(\S+)',line)[0]
    tata.write(f'>{a}\n{b}\n')       
tata.close()
input.close()