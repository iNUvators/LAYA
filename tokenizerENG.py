import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load the Excel file
df = pd.read_excel("C:/Users/Admin/Downloads/MergedDatasets.xlsx")

# Define a function to tokenize a cell, remove stopwords, special characters, and punctuations, and convert to lowercase
def process_cell(cell):
    # Tokenize the cell
    tokens = word_tokenize(str(cell))
    
    # Remove stopwords from English and Tagalog
    english_stopwords = set(stopwords.words('english'))
    filtered_tokens = [token.lower() for token in tokens if token.lower() not in english_stopwords]
    
    # Remove special characters and punctuations
    cleaned_tokens = [token for token in filtered_tokens if token.isalnum()]
    
    # Convert to lowercase
    lowercase_tokens = [token.lower() for token in cleaned_tokens]
    
    return lowercase_tokens

# Apply the function to the DataFrame
df = df.map(process_cell)

# Save the processed DataFrame back to Excel
df.to_excel("ty.xlsx", index=False)