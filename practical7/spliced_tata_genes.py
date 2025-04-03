import re
da=input("A splice donor/acceptor combination")
file=open(da+"_spliced_genes.fa", "w")
genes=open('tata_genes.fa', 'r')
name=""
a=""
#create pattern to cut introns
pattern = f"{re.escape(da[0:2])}.+?{re.escape(da[2:4])}"
for line in genes:
    line = line.rstrip()
    if '>' in line:
        #create a viable called name to contain gene' name
        name=line
    else:
        #cut intron with given donor and acceptor
        intron=re.findall(pattern,line)
        instance=0
        for i in range(len(intron)):
            #calculate the instance number
            if re.search('TATAAAA',intron[i]) or re.search('TATAAAT',intron[i]) or re.search('TATATAA',intron[i]) or re.search('TATATAT',intron[i]):
                instance+=1
        file.write(f'{name}  instance number:{instance}\n{line}\n')
file.close()
genes.close()