#create a string variable seq
seq='ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
import re
#find all the intron
intron=re.findall(r'(?=(GT.+?AG))',seq)
print(intron)
#report the length of that intron
largest=0
for i in range(len(intron)):
    if len(intron[i])>largest:
        largest=len(intron[i])
print(largest)