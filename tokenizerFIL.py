import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# Load the Excel file
df = pd.read_excel("C:/Users/Admin/Downloads/Training_File FIL.xlsx")

# Define a function to tokenize a cell, remove stopwords, special characters, and punctuations, and convert to lowercase
def process_cell(cell):
    # Tokenize the cell
    tokens = word_tokenize(str(cell))
    
    # Remove stopwords from Tagalog
    with open('stopwords-tl.txt', 'r') as f:
     stop_words = f.read().splitlines()
    filtered_tokens = [token.lower() for token in tokens if token.lower() not in stop_words]
    
    # Remove special characters and punctuations
    cleaned_tokens = [token for token in filtered_tokens if token.isalnum()]
    
    # Convert to lowercase
    lowercase_tokens = [token.lower() for token in cleaned_tokens]
    
    return lowercase_tokens

# Apply the function to the DataFrame
df = df.map(process_cell)

# Save the processed DataFrame back to Excel
df.to_excel("TrainingFIL.xlsx", index=False)