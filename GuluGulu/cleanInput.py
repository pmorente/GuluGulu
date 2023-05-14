import json
import sqlite3
from bisect import bisect_left

def find_matching_words(input_string, json_file_path):
    # Load the JSON file into a Python dictionary
    with open(json_file_path, 'r', encoding='utf-8') as f:
        word_dict = json.load(f)
    
    # Get the list of words from the JSON file
    words = word_dict['words']
    
    # Check if the list is sorted
    if word_dict.get('sorted', False):
        # Use binary search to find matching words
        input_words = input_string.split()
        matching_words = [word for word in input_words if bisect_left(words, word) != len(words) and words[bisect_left(words, word)] == word]
    else:
        # Use linear search to find matching words
        input_words = input_string.split()
        matching_words = [word for word in input_words if word in words]
    
    # Return the list of matching words
    return matching_words


def search_documents_by_tags(tags, file):
    # Load the JSON file
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Create a dictionary to store tag matches
    matches = {}

    # Iterate over documents in the data
    for document in data['documents']:
        # Compute the intersection of the document's tags with the search tags
        matching_tags = set(document['tags']).intersection(set(tags))

        # Store the number of matches in the dictionary
        matches[document['id']] = len(matching_tags)

    # Sort the results by number of matches in descending order
    results = sorted(matches.items(), key=lambda x: x[1], reverse=True)

    # Return the document ids with the most tag matches
    return [r[0] for r in results if r[1] > 0]

def get_pdf_data(ids):
    conn = sqlite3.connect('fib_gei.db')
    cursor = conn.cursor()

    data = []
    for id in ids: 
        cursor.execute("SELECT name, pdf_data FROM databasePDF WHERE id=?", (id,))
        result = cursor.fetchone()
        if result:
            data.append(result)

    conn.close()

    return data


#input_string = "Do you have any class notes related to biochemistry and cosmology"
#json_tags_path = "tags.json"
#json_documents_path = "documents.json"

#matching_words = find_matching_words(input_string, json_tags_path)

#list_documents = search_documents_by_tags(matching_words, json_documents_path)

#print(matching_words)