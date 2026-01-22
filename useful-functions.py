# example DNA sequence
seq = 'ATGCGTACCTGAACTGGTACGATTCGAGTTAACCGT'

# complementary base-pairing
def complement(seq):
    # capitalise template seq
    seq = seq.upper()
    # watson-crick base-pairing
    seq = seq.replace('A','t')
    seq = seq.replace('T','a')
    seq = seq.replace('G','c')
    seq = seq.replace('C','g')
    # capitalise template seq
    seq = seq.upper()
    return seq

print(complement(seq))

# transcription
def transcribe(seq):
    # capitalise template seq
    seq = seq.upper()
    # transcription
    seq = seq.replace('A','u')
    seq = seq.replace('T','a')
    seq = seq.replace('G','c')
    seq = seq.replace('C','g')
    # capitalise template seq
    seq = seq.upper()
    return(seq)

print(transcribe(seq))
