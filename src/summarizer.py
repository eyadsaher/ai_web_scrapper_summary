from openai import OpenAI
from .scraper import fetch_website_contents
from IPython.display import Markdown, display

OLLAMA_BASE_URL = "http://localhost:11434/v1"
ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama")
model = "deepseek-r1:1.5b"  # you can change this to any model you like that you have installed


system_prompt = """
You are an ai assistant that analyzes the contents of a website,
and provides a short summary and ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""

user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.
"""


def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website},
    ]


def summarize(url, model=model):
    website = fetch_website_contents(url)
    response = ollama.chat.completions.create(
        model=model, messages=messages_for(website)
    )
    return response.choices[0].message.content


def display_summary(url, model=model):
    summary = summarize(url, model)
    display(Markdown(summary))
