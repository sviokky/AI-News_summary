import requests
from send_email import send_email
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


url = ("https://newsapi.org/v2//top-headlines?"
       "category=business&"
       "language=en&"
       "pageSize=8&"
       "sortBy=publishedAt&apiKey=" + NEWS_API_KEY
       )


request = requests.get(url)
content = request.json()
articles = content.get("articles", [])

articles_text = ""

for i, a in enumerate(articles, 1):
    articles_text += f"""
Article {i}
Title: {a.get('title')}
Description: {a.get('description')}
Content: {a.get('content')}
Source: {a.get('source', {}).get('name')}
URL: {a.get('url')} """

model = init_chat_model(model="gemini-3-flash-preview",
                        model_provider="google-genai",
                        api_key=GOOGLE_API_KEY)

prompt = f"""
You are a professional news analyst.

Task:
1. Write 1 paragraph summarizing all the news.
2. Write 1 paragraph explaining how it may affect stock markets.

Return ONLY plain text.

News:
{articles_text}
"""

response = model.invoke(prompt)

response_str = response.content[0]["text"]

body = "Subject: News Summary\n\n" + response_str + "\n\n"
body = body.encode("utf-8")
send_email(message=body)
