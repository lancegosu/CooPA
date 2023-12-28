# CooPA (Conversational Personal Assistant)

CooPA is a web-based application that leverages the power of OpenAI's GPT-3.5-turbo and Google's Custom Search API to provide a conversational and informative experience. It allows users to ask questions, and it responds by intelligently summarizing information from search results.

## Features

- **Smart Search**: CooPA performs a smart search using Google, aggregates content from relevant articles, and generates a comprehensive response.
  
- **Summarization**: The application utilizes OpenAI's GPT-3.5-turbo to summarize articles intelligently.

- **Source Citation**: CooPA provides source citations by extracting URLs from the search results, enhancing transparency and credibility.

- **Voice Interaction**: Users can input queries through both typing and speech recognition for a seamless conversational experience.

- **Text-to-Speech**: CooPA includes a text-to-speech feature, allowing users to listen to the generated responses.

## Dependencies

- OpenAI GPT-3.5-turbo
- Google Custom Search JSON API
- Flask
- Requests
- BeautifulSoup

## Getting Started

### 1. Clone the repository: `git clone https://github.com/lancerai/coopa.git`
### 2. Install dependencies: `pip install -r requirements.txt`
### 3. Set up environment variables in a `.env` file with your OpenAI API key, GSearch API key, and CSE ID.

- OPENAI_API_KEY=your_openai_api_key
- GSEARCH_API_KEY=your_gsearch_api_key
- CSE_ID=your_cse_id

### 4. Run the application: python coopa.py
### 5. Access the application in your browser at http://localhost:5000/

## Usage
1. Enter your query in the input field and click "Submit."
2. Explore the summarized response and source citations.
3. Use the text-to-speech feature for auditory feedback.

Feel free to ask questions, seek information, and enjoy a conversational experience with CooPA!
