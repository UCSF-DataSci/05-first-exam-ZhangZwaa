import sys
import re

def break_seq(seq, pos,cut_point):
    seq1 = []
    for i in range(len(pos)):
        if i == 0:
            piece = seq[:pos[i]+cut_point]
        else:
            piece = seq[pos[i-1]+cut_point:pos[i]+cut_point]
        seq1.append(piece)
    seq1.append(seq[pos[-1]+cut_point+1:])
    new_seq = '|'.join(seq1)

    with open("/workspaces/05-first-exam-ZhangZwaa/bioinformatics_project/results/cutsite_summary.txt",'w') as file:
        file.write(new_seq)

def pair(position, d_low, d_high):
    match_list = []
    for pt in position:
        num_in_range = [num for num in position if pt + d_low <= num <= pt + d_high]
        for pair in num_in_range:
            pair_list = [pt, pair]
            match_list.append(pair_list)
    num = len(match_list)
    return num, match_list[:5]


def cut(dna_seq, find_seq, cut_point):
    d_low = 80000
    d_high = 120000
    # len_seq = len(dna_seq)
    position = []
    for match in re.finditer(find_seq,dna_seq):
        position.append(match.start())
    break_seq(dna_seq, position, cut_point)
    cut_site_num = len(position)
    pair_num, match_list = pair(position, d_low, d_high)

    return cut_site_num, pair_num, match_list


def dna_cut():
    if len(sys.argv) !=3:
        print("should input one sequence")
        sys.exit()
    
    input_path = sys.argv[1]
    with open(input_path,'r+') as f:
        # need to omit the line with identification code
        new_seq = [pt for row in f if not row[0]=='>' for pt in row.strip()]
        new_seq = ''.join(new_seq) # long match sequence

    input_seq = sys.argv[2]
    input_seq = input_seq.upper()
    invalid_check1 = [pt for pt in input_seq if pt not in ["A","G","C","T","|"]]
    invalid_check2 = [pt for pt in new_seq if pt not in ["A","G","C","T","|"]]
    if invalid_check1 or invalid_check2 or "|" not in input_seq:
        print("Something out of AGCT is occur in given sequence")
        sys.exit()
    cut_place = input_seq.find("|") # index of | in cut sequence
    cut_seq = [pt for pt in input_seq if not pt == "|"]
    cut_seq = ''.join(cut_seq) # remove | from cut sequence
    cut_site_num, pair_num, match_list = cut(new_seq, cut_seq, cut_place)

    print(f"Analyzing cut site: {cut_seq}")
    print(f"Total cut sites found: {cut_site_num}")
    print(f"Cut site pairs 80-120 kbp apart: {pair_num}")
    print("First 5 pairs:")
    row_pair = 1
    for pair in match_list:
        print(f"{row_pair}. {pair[0]} - {pair[1]}")
        row_pair += 1


if __name__ == "__main__":
    dna_cut()