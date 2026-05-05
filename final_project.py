# ingrediant based recommender
import json
import string
import webbrowser
import time
from collections import Counter

# INGREDIENT CLEANING

def clean_ingredient(text):
    """Standardize ingredient text (lowercase, no punctuation, trimmed)."""
    text = text.strip().lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return " ".join(text.split())


def simplify_ingredient(ingredient):
    """
    Simplify ingredient for better matching:
    - handles plurals (tomatoes → tomato)
    """
    ingredient = clean_ingredient(ingredient)
    words = ingredient.split()
    simplified = []

    for word in words:
        if word.endswith("ies"):
            word = word[:-3] + "y"
        elif word.endswith("es") and len(word) > 3:
            word = word[:-2]
        elif word.endswith("s") and len(word) > 3:
            word = word[:-1]
        simplified.append(word)

    return " ".join(simplified)


def ingredients_match(recipe_ing, user_ingredients):
    """
    Check if a recipe ingredient matches user ingredients.
    Allows partial matches (e.g., 'cheddar cheese' vs 'cheese').
    """
    recipe_clean = simplify_ingredient(recipe_ing)

    for user_ing in user_ingredients:
        user_clean = simplify_ingredient(user_ing)

        if recipe_clean == user_clean:
            return True

        # partial match logic
        if recipe_clean in user_clean or user_clean in recipe_clean:
            return True

    return False


def clean_ingredient_list(items):
    """Clean list of ingredients and remove duplicates."""
    cleaned = []
    for item in items:
        item = clean_ingredient(item)
        if item and item not in cleaned:
            cleaned.append(item)
    return cleaned

# DATA LOADING

def load_recipes(filename):
    """Load recipes from JSON file."""
    with open(filename, "r") as file:
        return json.load(file)

# ANALYSIS + RANKING

def analyze_recipe(recipe, user_ingredients):
    """Compare a recipe against user ingredients."""
    matched = []
    missing = []

    for ing in recipe["ingredients"]:
        cleaned = clean_ingredient(ing)

        if ingredients_match(ing, user_ingredients):
            matched.append(cleaned)
        else:
            missing.append(cleaned)

    total = len(recipe["ingredients"])
    score = (len(matched) / total) * 100 if total else 0

    return {
        "name": recipe["name"],
        "category": recipe.get("category", "Uncategorized"),
        "matched": matched,
        "missing": missing,
        "matched_count": len(matched),
        "total_ingredients": total,
        "score": score
    }


def rank_recipes(recipes, user_ingredients):
    """
    Rank recipes:
    1. Highest score
    2. Most matches
    3. Fewest missing
    """
    results = [analyze_recipe(r, user_ingredients) for r in recipes]

    results.sort(
        key=lambda r: (r["score"], r["matched_count"], -len(r["missing"])),
        reverse=True
    )
    return results

# DISPLAY FUNCTIONS

def get_match_label(score):
    """Return label for match score."""
    if score == 100:
        return "Perfect Match"
    elif score >= 75:
        return "Great Match"
    elif score >= 50:
        return "Good Match"
    elif score >= 30:
        return "Possible Match"
    return "Low Match"


def explain_ranking(r):
    """Explain why recipe ranked where it did."""
    if r["score"] == 100:
        return "You have all ingredients."
    elif r["matched_count"] > len(r["missing"]):
        return "You have most ingredients."
    elif r["matched_count"] == len(r["missing"]):
        return "You have about half."
    return "You are missing many ingredients."


def display_results(results, top_n=10):
    """Print recipe recommendations."""
    print("\nRecipe Recommendations:\n")

    for i, r in enumerate(results[:top_n], start=1):
        print(f"{i}. {r['name']} ({r['category']})")
        print(f"   {get_match_label(r['score'])} - {r['score']:.0f}%")
        print(f"   You have: {', '.join(r['matched']) or 'None'}")
        print(f"   Missing: {', '.join(r['missing']) or 'None'}")
        print(f"   Why: {explain_ranking(r)}")

        if i == 1:
            print("   Best match")

        if r["score"] == 100:
            print("   You can make this now!")

        print()

# SHOPPING LIST

def build_shopping_list(results, top_n=3):
    """
    Build list using top recipes.
    Prioritizes ingredients that appear often.
    """
    counter = Counter()

    for r in results[:top_n]:
        for ing in r["missing"]:
            counter[ing] += 1

    return counter.most_common()


def display_shopping_list(items):
    print("Shopping List:\n")

    if not items:
        print("You have everything!")
        return

    for ing, count in items:
        print(f"- {ing}" if count == 1 else f"- {ing} ({count} recipes)")

# FUN FEATURES (Remy + Spotify)

def remy_says(msg, recipe=""):
    """Simple narrator for personality."""
    if msg == "welcome":
        print("Remy: Anyone can cook!")
    elif msg == "results":
        print("\nRemy: Let's see what we can make...")
    elif msg == "best":
        print(f"\nRemy: {recipe} looks promising.")
    elif msg == "error":
        print("Remy: I need at least one ingredient!")


def show_remy_gif():
    """Open Remy GIF page."""
    link = "https://giphy.com/stories/the-best-ratatouille-gifs-3e6334ee-0835"
    print("\nOpening Remy...")
    time.sleep(1)
    webbrowser.open(link)


def get_playlist():
    """Basic playlist options."""
    return [
        ("Chill Cooking", "https://open.spotify.com/playlist/37i9dQZF1DX4sWSpwq3LiO"),
        ("Lo-fi Beats", "https://open.spotify.com/playlist/6zCID88oNjNv9zx6puDHKj"),
        ("Feel Good Cooking", "https://open.spotify.com/playlist/37i9dQZF1DX2sUQwD7tbmL")
    ]


def choose_playlist():
    playlists = get_playlist()

    print("\nChoose a playlist:")
    for i, (name, _) in enumerate(playlists, 1):
        print(f"{i}. {name}")

    choice = input("Pick number or press Enter: ")

    if choice.isdigit():
        i = int(choice) - 1
        if 0 <= i < len(playlists):
            print("Opening playlist...")
            webbrowser.open(playlists[i][1])

# MAIN PROGRAM

def main():
    remy_says("welcome")
    show_remy_gif()

    user_input = input("\nEnter ingredients: ")
    user_ingredients = clean_ingredient_list(user_input.split(","))

    if not user_ingredients:
        remy_says("error")
        return

    recipes = load_recipes("recipes.json")
    results = rank_recipes(recipes, user_ingredients)

    remy_says("results")
    display_results(results)

    best = results[0]
    remy_says("best", best["name"])

    shopping = build_shopping_list(results)
    display_shopping_list(shopping)

    choose_playlist()


main()
