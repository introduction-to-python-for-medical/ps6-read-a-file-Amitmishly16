def create_codon_dict(file):
    
    dictionary = {}
    for row in rows:
      cells = row.strip().split('\t')
      codon = cells[0]
      amino_acid = cells[2]
      dictionary[codon] = amino_acid
    return dictionary

file = open("data/codons.txt")
rows = file.readlines()
file.close()

