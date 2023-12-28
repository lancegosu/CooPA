# CooPA - Contextualized Personal Assistant

CooPA is a Flask web application that leverages OpenAI's ChatGPT API and the Google Custom Search API to deliver contextually informed answers by aggregating relevant content from online articles based on user queries.

## Table of Contents

- [Purpose](#purpose)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Note](#note)

## Purpose

CooPA is designed to redefine the interaction between users and information. Utilizing OpenAI's GPT-3.5-turbo, CooPA seamlessly integrates natural language processing and web scraping to enable users to ask questions or seek information by conversing with the system. By leveraging a cutting-edge language model and Google's Custom Search API, CooPA empowers users to obtain concise and relevant answers from aggregated article content, enhancing the efficiency and accessibility of information retrieval. Whether through voice or text input, CooPA aims to provide an intuitive interface for users to effortlessly access knowledge and deliver insightful responses.

## Features

- **Smart Search**: Perform intelligent searches using Google Custom Search and aggregate content from relevant articles to generate comprehensive answers.

- **Language Model Interaction**: Utilize OpenAI's GPT-3.5-turbo for generating contextually informed responses to user queries.

- **Speech Recognition and Synthesis**: Enable users to input queries through speech and listen to the synthesized responses.

- **Source Attribution**: Automatically include source URLs when presenting the aggregated content, offering transparency and credibility.

## Installation

1. Clone the repository:

    ```bash
    git clone https://lancerai/CooPA.git
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

## Note

Make sure to comply with OpenAI's use-case policies and guidelines when using this app.
