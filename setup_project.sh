mkdir -p ./bioinformatics_project/data
mkdir -p ./bioinformatics_project/scripts
mkdir -p ./bioinformatics_project/results

cd ./bioinformatics_project
touch ./scripts/generate_fasta.py
touch ./scripts/dna_operations.py
touch ./scripts/find_cutsites.py

touch ./results/cutsite_summary.txt

touch ./data/random_sequence.fasta

echo "# Project Structure\n\n- **scripts**: Contains 3 Python scripts.\n- **results**: Contains a `.txt` file.\n- **data**: Contains a `.fasta` file." > README.md
