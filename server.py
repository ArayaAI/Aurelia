from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TMDB_API_KEY = "TU_API_KEY_AQUÍ"

def interpret_query(query):
    # Simulamos una interpretación básica por ahora
    return "drama thriller ciencia ficción Matrix Snowpiercer"

def search_tmdb(query):
    url = "https://api.themoviedb.org/3/search/movie" 
    params = {
        "api_key": TMDB_API_KEY,
        "query": query,
        "language": "es"
    }
    response = requests.get(url, params=params).json()
    return response.get("results", [])[:5]

@app.route("/api/recommend", methods=["GET"])
def recommend():
    user_query = request.args.get("query")
    keywords = interpret_query(user_query)
    movies = search_tmdb(keywords)
    return jsonify(movies)

if __name__ == "__main__":
    app.run()
