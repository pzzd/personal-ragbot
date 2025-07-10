import csv
import sys
import subprocess

# To call:
# python3 embed-list-of-docs.py document_dir csv_file_name
# eg:
# python3 embed-list-of-docs.py "/Users/pezzutidyer/Documents/AbqBackyardRefuge/" "AbqBackyardRefugeDocumentList.csv"

document_dir = sys.argv[1] # ends with /
csv_file_name = sys.argv[2]
chromadb_name = "abq_backyard_refuge"

file_path = document_dir + csv_file_name

try:
    with open(file_path, 'r', newline='') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file)

        for row in csv_dict_reader:
            # Each 'row' is a dictionary where keys are column headers
            print(row)
            subprocess.run(["python3", "make-one-embedding.py", document_dir, row['ID'], row['FileName'], chromadb_name], check=True)

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
