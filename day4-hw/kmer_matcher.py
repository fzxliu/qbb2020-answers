# note that shebang is omitted because I'm running this with python kmer_matcher.py
import sys
from fasta_iterator_class import FASTAReader

t_name = sys.argv[1]
q_name = sys.argv[2]
k = int(sys.argv[3])


dbseq = FASTAReader (open(t_name))
qseq = FASTAReader (open(q_name))

kmers = {} # initialize k-mer dictionary


for seq_id, sequence in dbseq:
    for i in range(0, len(sequence)-k+1):
        kmer = sequence[i:i + k]
        kmers.setdefault(kmer, [])
        kloc=(seq_id, i)
        kmers[kmer].append(kloc)
# for key in kmers:
#     print(key, kmers[key])
    
for seq_name, sequence in qseq:
    for key in kmers:
        if key in sequence:
            print(key, kmers[key], sequence.find(key))
