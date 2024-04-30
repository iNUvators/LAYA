import csv
import json

# Convert CSV file to JSONL
def csv_to_jsonl(csv_file, jsonl_file):
    with open(csv_file, 'r', encoding='latin-1') as csvfile, open(jsonl_file, 'w', encoding='utf-8') as jsonlfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row if exists

        for row in csvreader:
            user = row[0]  # First column is user's message
            assistant = ','.join(row[1:])  # Join remaining columns into assistant's response
            messages = [
                {"role": "user", "content": user.strip()},
                {"role": "assistant", "content": assistant.strip()}
            ]
            json_entry = {"messages": messages}
            jsonlfile.write(json.dumps(json_entry) + '\n')

# Example usage:
csv_to_jsonl(r'C:\Users\Angel Micaela\Documents\Official_LAYA_Question_and_Answer_DataSet.csv', 'laya.jsonl')
