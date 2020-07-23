# codon_lookup.py
#From Hill scientific Python programming
#https://scipython.com/book/chapter-5-ipython-and-ipython-notebook/examples/rna-codons/

bases = ['U', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

#doing same thing with cards
numbers = ['1','2','3','4','5','6','7','8','9','10','K','Q','J']
palos = ['H','D','S','C']
cards = [a+b for a in palos for b in numbers]

