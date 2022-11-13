from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.Seq import Seq
from Bio import SeqIO

seq_1NOS = next(SeqIO.parse(
    open('./Fasta_templates/rcsb_pdb_1NOS.fasta'), 'fasta'))
seq_2BHJ = next(SeqIO.parse(
    open('./Fasta_templates/rcsb_pdb_2BHJ.fasta'), 'fasta'))
seq_3NOS = next(SeqIO.parse(
    open('./Fasta_templates/rcsb_pdb_3NOS.fasta'), 'fasta'))
seq_3NSE = next(SeqIO.parse(
    open('./Fasta_templates/rcsb_pdb_3NSE.fasta'), 'fasta'))


alignments = pairwise2.align.globalxx(seq_3NOS.seq, seq_3NSE.seq)

for i in alignments:
  print(format_alignment(*i))
