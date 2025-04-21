from flask import Flask, request, jsonify
from recipe_matching import suggest_recipes, score_recipes, fuzzy_match_score, filter_recipes
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


app = Flask(__name__)

# Load recipes from recipes.json file
with open("recipes.json", "r") as f:
    recipes = json.load(f)

@app.route("/")
def home():
    return "🍳 Recipe Matcher API is live!"

@app.route("/suggest", methods=["POST"])
def suggest():
    data = request.get_json()
    user_ingredients = data.get("ingredients", [])
    method = data.get("method", "exact")
    dietary = data.get("dietary", "any")
    max_time = data.get("max_time", 9999)

    # Filter recipes first
    filtered = filter_recipes(recipes, dietary, max_time)

    # Matching method
    if method == "exact":
        result = suggest_recipes(user_ingredients, filtered)
    elif method == "score":
        result = score_recipes(user_ingredients, filtered)
    elif method == "fuzzy":
        result = fuzzy_match_score(user_ingredients, filtered)
    else:
        return jsonify({"error": "Invalid method"}), 400

    return jsonify({"recipes": result})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)


