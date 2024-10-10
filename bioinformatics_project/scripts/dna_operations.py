import sys

def complement(dna):
    dict_dna = {65:84, 71:67, 67:71, 84:65}
    new_seq = dna.translate(dict_dna)
    return new_seq

def reverse(dna):
    return dna[::-1]

def reverse_complement(dna):
    dna_complement = complement(dna)
    return(reverse(dna_complement))

def dna_operation():
    if len(sys.argv) !=2:
        print("should input one sequence")
        sys.exit()
    
    dna_seq = str(sys.argv[1])
    dna_seq = dna_seq.upper()
    
    invalid_check = [pt for pt in dna_seq if pt not in ["A","G","C","T"]]
    if invalid_check:
        print("Something out of AGCT is occur in given sequence")
        sys.exit()

    print(f"The original sequence: {dna_seq}")
    print(f"Its complement: {complement(dna_seq)}")
    print(f"Its reverse: {reverse(dna_seq)}")
    print(f"Its reverse complement: {reverse_complement(dna_seq)}")

if __name__ == "__main__":
    dna_operation()