# CooPA - Contextualized Search with Language Models

CooPA is a Flask web application that leverages OpenAI's language model and the Google Custom Search API to provide contextually relevant answers to user queries based on aggregated article content.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (3.6 or higher)
- Flask
- Requests library (`pip install requests`)
- BeautifulSoup library (`pip install beautifulsoup4`)
- OpenAI Python library (`pip install openai`)
- Python-dotenv library (`pip install python-dotenv`)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/lancerai/CooPA.git
    cd CooPA
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your OpenAI API key, Google Custom Search API key, and Custom Search Engine ID in the `.env` file:

    ```env
    OPENAI_API_KEY=your-openai-api-key
    GSEARCH_API_KEY=your-google-search-api-key
    CSE_ID=your-custom-search-engine-id
    ```

## Usage

1. Start the Flask application:

    ```bash
    python coopa.py
    ```

2. Open your web browser and go to [http://localhost:5000/](http://localhost:5000/) to access CooPA.

3. Enter your query in the input field and submit the form to receive contextually relevant answers based on aggregated article content.

## Project Structure

- **`utils.py`**: Contains utility functions for interacting with OpenAI's language model, performing Google searches, and aggregating content from articles.

- **`coopa.py`**: Flask application handling web requests, user input processing, and result rendering.

- **`index.html`**: HTML template for the user interface, including the input form, result container, and buttons for text-to-speech functionality.

## Configuration

- **OpenAI API Key**: Obtain your API key from the [OpenAI API](https://beta.openai.com/signup/) and set it in `OPENAI_API_KEY` in the `.env` file.

- **Google Custom Search API Key and CSE ID**: Set up a Custom Search Engine on [Google Custom Search](https://programmablesearchengine.google.com/about/) and obtain the API key and CSE ID. Set them in `GSEARCH_API_KEY` and `CSE_ID` in the `.env` file.
