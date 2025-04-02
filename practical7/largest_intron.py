#create a string variable seq
seq='ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
import re
#find the longest intron
intron=re.findall(r'GT.+?AG',seq)
print(intron)
#report the length of that intron
intron=intron[0]
print(len(intron))