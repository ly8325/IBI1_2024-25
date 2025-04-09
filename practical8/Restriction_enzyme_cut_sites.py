def search(sequence,nucleotide):
   for i in range(len(sequence)) :
      for a in range(len(nucleotide)):
        if sequence[i+a]==nucleotide[a] :
           if nucleotide=="ACGT":
            return True
           else:
              return sequence[i]
        else:
           return False
DNA=input("the DNA sequence to be cut")
restriction=input("the sequence recognised	by the	restriction enzyme")
canonical="ACGT"	
#check if the DNA sequence contain canonical (‘ACGT’) nucleotide	
if not search(DNA,canonical):
   print("the DNA sequence doesn't have canonical nucleotide")
#check if the  sequence recognised by the restriction enzyme contain canonical (‘ACGT’) nucleotide
elif not search(restriction,canonical):
   print("the sequence recognised by the restriction enzyme doesn't have canonical nucleotide")
else:
   print(search(DNA,restriction))