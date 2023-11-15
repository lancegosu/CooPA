import openai
import requests
from bs4 import BeautifulSoup
import fitz  # PyMuPDF
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Access your environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')
gsearch_api_key = os.getenv('GSEARCH_API_KEY')
cse_id = os.getenv('CSE_ID')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def google_search(query, api_key, cse_id):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": gsearch_api_key,
        "cx": cse_id,
        "q": query
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None

def grab_urls(query, num_link=5):

    search_results = google_search(query, gsearch_api_key, cse_id)

    urls = []
    if search_results:
        for item in search_results.get("items", []):
            urls.append(item["link"])
          # print(item["title"])
          # print(item["link"])
          # print(item.get("snippet", ""))
          # print("-----")
    return urls[:num_link]

def download_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        # Assuming the content is text-based, you can access it using response.text
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while downloading the URL: {e}")
        return None

def extract_visible_text(html_content):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        # Get the visible text content using .get_text() method of BeautifulSoup
        visible_text = soup.get_text()
        return visible_text
    except Exception as e:
        print(f"An error occurred while extracting text: {e}")
        return None

def url_aggregated(urls):
    visible_text = ""
    for url in urls:
        # url_to_download = "https://apnews.com/article/hawaii-wildfire-maui-lahaina-f5a7047d407f836f89e90dd7f10faa94"  # Replace this with your desired URL
        html_content = download_url(url)

        if html_content:
            visible_text += extract_visible_text(html_content) + "\n\n" + "------"
            #if visible_text:
                #print(visible_text)
    return visible_text

def get_citation(urls):
    source_urls = "\n".join(urls)
    return source_urls

def smart_search(query):
    urls = grab_urls(query, num_link=4)
    articles = url_aggregated(urls)[:4000]
    prompt = f"""
    From the list of articles: {articles}\n
    Answer the question in a minimum of 3 sentences: {query}
    """
    # # Create a list of source URLs
    # source_urls = "Sources:\n" + "\n".join(urls)
    response = get_completion(prompt) #+ "\n\n" + source_urls
    return response
    # Create a list of source URLs
    # source_urls = "\n".join(urls)
    # 
    # text_result = get_completion(prompt)
    # 
    # combined_response = f"{text_result}\n\nSources:\n{source_urls}"
    # 
    # return combined_response
