import random
import textwrap

random.seed(101)
dna0 = ''.join(random.choices('ATCG', k=1000000))
dna = textwrap.fill(dna0, width=80)

with open('/workspaces/05-first-exam-ZhangZwaa/bioinformatics_project/data/random_sequence.fasta','w') as fasta:
    fasta.write(dna)
    print(f"Random DNA sequence generated and saved to {__file__}")