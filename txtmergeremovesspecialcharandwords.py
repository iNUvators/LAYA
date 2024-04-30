import os
import re

def merge_txt_files(input_folder, output_file):
    if not os.path.exists(input_folder):
        print("Input folder does not exist.")
        return

    files = [f for f in os.listdir(input_folder) if f.endswith('.txt')]

    if not files:
        print("No .txt files found in the input folder.")
        return

    with open(output_file, 'w', encoding='utf-8') as output_file:
        for filename in files:
            file_path = os.path.join(input_folder, filename)
            with open(file_path, 'r', encoding='utf-8') as input_file:
                content = input_file.read()
                output_file.write(content)
                output_file.write('\n')

    print(f"Merged {len(files)} .txt files into {output_file}.")

def remove_special_char(output_file):
    file_path = output_file

    with open(file_path, 'r', encoding='utf-8') as f:
     string = f.read()

    new_str = re.sub('[^a-zA-Z0-9\n.]', ' ', string)

    output_file_path = r'C:/Users/Admin/Downloads/1929-1960removedchar.txt'

    with open(output_file_path, 'w', encoding='utf-8') as f:
     f.write(new_str)
     
def removewords(output_file):
    word_to_remove = "The Lawphil Project   Arellano Law Foundation"

# Read the input file
    input_file_path = output_file
    with open(input_file_path, 'r', encoding='utf-8') as f:
     content = f.read()

# Remove the word
    content = re.sub(r'\b{}\b'.format(word_to_remove), "", content)

# Write the output to a new file
    output_file_path = r'C:/Users/Admin/Downloads/merge.txt'
    with open(output_file_path, 'w', encoding='utf-8') as f:
     f.write(content)
     

if __name__ == "__main__":
    input_folder = "C:/Users/Admin/Downloads/merge"
    output_file = "C:/Users/Admin/Downloads/jj.txt"
    output_files = "C:/Users/Admin/Downloads/1929-1960removedchar.txt"
    
    merge_txt_files(input_folder, output_file)
    remove_special_char(output_file)
    removewords(output_files)