from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

for record in SeqIO.parse("sample.fasta", "fasta"):
    sequence_id = record.id
    sequence_length = len(record.seq)
    gc_content = gc_fraction(record.seq) * 100

    print("Sequence ID:", sequence_id)
    print("Sequence Length:", sequence_length)
    print("GC Content: {:.2f}%".format(gc_content))
    print("----------------------")
