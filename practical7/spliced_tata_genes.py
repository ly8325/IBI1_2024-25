import re
da=input("A splice donor/acceptor combination")
file=open(da+"_spliced_genes.fa", "w")
genes=open('tata_genes.fa', 'r')
name=""
a=""
for line in genes:
    line = line.rstrip()
    if '>' in line:
        name=line
    else:
        a=line
        intron=re.findall(r'(?=(da[0:2].+?da[2:4]))',a)
        instance=0
        for i in range(len(intron)):
            if re.search('TATAAAA',intron[i]) or re.search('TATAAAT',intron[i]) or re.search('TATATAA',intron[i]) or re.search('TATATAT',intron[i]):
                instance+=1
        file.write(f'{name}  instance number:{instance}\n{a}\n')