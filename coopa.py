from flask import Flask, render_template, request, jsonify
from utils import smart_search, grab_urls, get_citation

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling form submission
@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input1']  # Retrieve user input from the form
    
    # Use the smart_search function to get relevant information
    # and grab_urls to extract URLs related to the user input
    urls = grab_urls(user_input, num_link=4)
    text = smart_search(user_input)
    
    citation = get_citation(urls)
    result = f"{text}\n\nSources:\n{citation}"
    return result

if __name__ == '__main__':
    app.run()
