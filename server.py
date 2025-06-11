from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TMDB_API_KEY = "TU_API_KEY_AQUÍ"

def interpret_query(query):
    # Aquí simulamos una interpretación básica de IA
    if "como" in query.lower():
        # Si dice "películas como X", buscamos X
        parts = query.lower().split("como")
        if len(parts) > 1:
            keyword = parts[1].strip().replace("?", "").replace(".", "")
            return keyword
    return query  # Si no entiende, devuelve lo mismo

def search_tmdb(query):
    url = "https://api.themoviedb.org/3/search/movie" 
    params = {
        "api_key": TMDB_API_KEY,
        "query": query,
        "language": "es"
    }
    try:
        response = requests.get(url, params=params).json()
        return response.get("results", [])[:5]
    except Exception as e:
        print("Error al buscar en TMDB:", e)
        return []

@app.route("/api/recommend", methods=["GET"])
def recommend():
    user_query = request.args.get("query")
    keywords = interpret_query(user_query)
    movies = search_tmdb(keywords)
    return jsonify(movies)

if __name__ == "__main__":
    app.run()
