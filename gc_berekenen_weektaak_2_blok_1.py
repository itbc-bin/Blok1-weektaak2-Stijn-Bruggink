#!/usr/bin/env python
Seq = ''
Bestand = open("/home/stijn/Documents/Bio-informatica/blok_1/rna_data_weektaak_2/Zea_mays_mRNA.txt", "r")
for line in Bestand:
    if not line.startswith(">"):
        Seq = Seq + line
GC_percentage = (((Seq.count('G') + (Seq.count('C'))) / len(Seq)) * 100)
print(len(Seq))
print('Zea mays GC percentage is',GC_percentage, '%')
#GC% whole organism = 46.8248

Seq1 = ''
Bestand1 = open("/home/stijn/Documents/Bio-informatica/blok_1/rna_data_weektaak_2/Gallus_gallus_mRNA.txt", "r")
for line in Bestand1:
    if not line.startswith(">"):
        Seq1 = Seq1 + line
GC_percentage1 = (((Seq1.count('G') + (Seq1.count('C'))) / len(Seq1)) * 100)
print(len(Seq1))
print('Gallus gallus GC percentage is',GC_percentage1, '%')
#GC% whole organism = 41.9137

Seq2 = ''
Bestand2 = open("/home/stijn/Documents/Bio-informatica/blok_1/rna_data_weektaak_2/Mus_musculus_mRNA.txt", "r")
for line in Bestand2:
    if not line.startswith(">"):
        Seq2 = Seq2 + line
GC_percentage2 = (((Seq2.count('G') + (Seq2.count('C'))) / len(Seq2)) * 100)
print(len(Seq2))
print('Mus musculus GC percentage is',GC_percentage2, '%')
#GC% whole organism = 42.5

Seq3 = ''
Bestand3 = open("/home/stijn/Documents/Bio-informatica/blok_1/rna_data_weektaak_2/Saccharomyces_cerevisiae_mRNA.txt", "r")
for line in Bestand3:
    if not line.startswith(">"):
        Seq3 = Seq3 + line
GC_percentage3 = (((Seq3.count('G') + (Seq3.count('C'))) / len(Seq3)) * 100)
print(len(Seq3))
print('Saccharomyces cerevisiae GC percentage is',GC_percentage3, '%')
#GC% whole organism = 38.3758

Seq4 = ''
Bestand4 = open("/home/stijn/Documents/Bio-informatica/blok_1/rna_data_weektaak_2/Pseudomonas_syringae_mRNA.txt", "r")
for line in Bestand4:
    if not line.startswith(">"):
        Seq4 = Seq4 + line
GC_percentage4 = (((Seq4.count('G') + (Seq4.count('C'))) / len(Seq4)) * 100)
print(len(Seq4))
print('Pseudomonas syringae GC percentage is',GC_percentage4, '%')
#GC% whole organism = 58.7
