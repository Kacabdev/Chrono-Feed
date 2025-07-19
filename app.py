from flask import Flask, render_template, request, jsonify
import requests
from config import NEWS_API_KEY

#creating a flask
app = Flask(__name__)

#Home page or route
@app.route('/')
def home():
    query = request.args.get("query", "Latest")
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
    
    response = requests.get(url) 
    
    news_data = response.json()
    articles = news_data.get('articles', []) # Hubi in 'articles' ay halkan ka timaaddo
    
    
   # filter_articles = [articles for article in articles if "Yahoo" not in article["source"]["name"] and 'removed'
    #not in article["title"].lower()]
    
    
    
    
    
    
    
    
    
    
    
    return render_template("index.html", articles=articles, query=query) # Halkan waxaan ku gudbinaynaa "articles"

















if __name__ == '__main__':
    app.run(debug=True)
