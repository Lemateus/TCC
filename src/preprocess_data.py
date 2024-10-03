import csv
import os

def filter_data(file_path):
    input_file = file_path  # Replace with your input file name
    output_file = '/home/lemateus/TCC/cintilacao/data/'
    output_file += file_path.split('/')[-1].split('.')[0] + 'EDITADO.csv'  # Replace with your desired output file name

    # Define the columns to extract
    columns_to_extract = ['time_utc', ' svid', ' azim', ' elev', ' s4']

    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=columns_to_extract)
        
        # Write the header
        writer.writeheader()
        
        # Extract the specified fields and write to the output file
        for row in reader:
            writer.writerow({col: row[col] for col in columns_to_extract})

    print(f"Data extracted and saved to {output_file}")

directory = '/home/lemateus/TCC/cintilacao/raw_data'

for file_name in os.listdir(directory):
    if(file_name.endswith('.ismr')):
        file_path = os.path.join(directory, file_name)
        filter_data(file_path)