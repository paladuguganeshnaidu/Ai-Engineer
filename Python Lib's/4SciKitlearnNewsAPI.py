import requests

import json



API_KEY = "1f0349cbd2cf40dc941afcb15911976c"



url = (

    f"https://newsapi.org/v2/top-headlines?"

    f"country=us&pageSize=20&apiKey={API_KEY}"

)



response = requests.get(url)

data = response.json()



if data["status"] != "ok":

    print(data)

    exit()



news = []



for article in data["articles"]:

    news.append({

        "title": article.get("title"),

        "description": article.get("description"),

        "content": article.get("content"),

        "author": article.get("author"),

        "source": article["source"]["name"],

        "published_at": article.get("publishedAt"),

        "url": article.get("url")

    })



with open("news.json", "w", encoding="utf-8") as file:

    json.dump(news, file, indent=4, ensure_ascii=False)



print(f"Saved {len(news)} articles to news.json")