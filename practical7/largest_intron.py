#create a string variable seq
seq='ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
import re
intron=re.findall(r'GT.+AG',seq)
print(intron)
intron=intron[0]
print(len(intron))