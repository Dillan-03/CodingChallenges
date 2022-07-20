def dna_to_rna(dna):
   letter  = list(dna)
   for i in range(0,len(letter)):
    if (letter[i] == "T"):
        letter[i] = "U"

   return ''.join(letter)
   

   
print(dna_to_rna("TTTT"))