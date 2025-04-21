from fuzzywuzzy import fuzz

def suggest_recipes(user_ingredients, recipes):
    user_set = set(user_ingredients)
    suggestions = []

    for recipe in recipes:
        recipe_set = set(recipe["ingredients"])
        if recipe_set.issubset(user_set):
            suggestions.append(recipe["name"])

    return suggestions

def score_recipes(user_ingredients, recipes):
    user_set = set(user_ingredients)
    results = []

    for recipe in recipes:
        recipe_set = set(recipe["ingredients"])
        num_have = len(recipe_set & user_set)
        score = num_have / len(recipe_set)
        results.append((recipe["name"], score))

    results.sort(key=lambda x: x[1], reverse=True)
    return results

def is_similar(word1, word2):
    return fuzz.token_sort_ratio(word1, word2) > 85

def fuzzy_match_score(user_ingredients, recipes):
    results = []

    for recipe in recipes:
        match_count = 0
        for ing in recipe["ingredients"]:
            for user_ing in user_ingredients:
                if is_similar(ing, user_ing):
                    match_count += 1
                    break
        score = match_count / len(recipe["ingredients"])
        results.append((recipe["name"], score))

    results.sort(key=lambda x: x[1], reverse=True)
    return results

def filter_recipes(recipes, dietary="any", max_time=9999):
    return [
        r for r in recipes
        if (dietary in r["dietary"] or dietary == "any")
        and r["time_minutes"] <= max_time
    ]
