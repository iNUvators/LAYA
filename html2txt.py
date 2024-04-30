# Importing necessary libraries
import os # interacting with the operating system
from bs4 import BeautifulSoup # parsing HTML and XML files
import chardet # detecting the character encoding of a file


# opens a file in binary mode, reads its content, and uses chardet to detect the character encoding of the file. It returns the detected encoding.
def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
    return result['encoding']

# converts HTML files to text files. 
def convert_html_to_text(input_folder, output_folder):
    # checks if folder exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # loops html in the folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".html"):
            input_filepath = os.path.join(input_folder, filename)
            output_filepath = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")

            #opens the HTML file with the detected encoding, reads its content, and parses the HTML content
            encoding = detect_encoding(input_filepath)

            with open(input_filepath, "r", encoding=encoding, errors='replace') as html_file:
                html_content = html_file.read()
                soup = BeautifulSoup(html_content, 'html.parser')

            # extracts the text from the parsed HTML, writes the text to the output file, and prints a message indicating the completion of the conversion for the current file
            text_content = soup.get_text()

            with open(output_filepath, "w", encoding="utf-8") as txt_file:
                txt_file.write(text_content)

            print(f"Conversion complete: {filename} -> {os.path.basename(output_filepath)}")

# main execution block
if __name__ == "__main__":
    
    input_folder = "C:/Users/Admin/Downloads/Treaties"
    output_folder = "C:/Users/Admin/Downloads/merge"

    convert_html_to_text(input_folder, output_folder)