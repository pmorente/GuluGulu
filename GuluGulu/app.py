from flask import Flask, render_template, request
from cleanInput import find_matching_words, search_documents_by_tags, get_pdf_data
from flask_bootstrap import Bootstrap
import sqlite3
import json

from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_string = request.form['transcription']
        
        # Call the desired functions with the input data
        json_tags_path = "tags.json"
        json_documents_path = "documents.json"
        matching_words = find_matching_words(input_string, json_tags_path)
        list_documents = search_documents_by_tags(matching_words, json_documents_path)
        tuple_data = get_pdf_data(list_documents)
        
        # Create a list of download links for each PDF file
       
        
        # Render a template to show the results
        return render_template('results.html', documents=tuple_data)
    
    # If the request method is GET, show the form
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
    



