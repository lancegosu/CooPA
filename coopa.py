from flask import Flask, render_template, request, jsonify
from utils import smart_search, grab_urls, get_citation

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input1']
    urls = grab_urls(user_input, num_link=4)
    print(user_input)
    text = smart_search(user_input)
    citation = get_citation(urls)
    result = f"{text}\n\nSources:\n{citation}"
    print(result)
    return result

if __name__ == '__main__':
    app.run()
