import json

def clean_ingredient(text):
    """
    Convert one ingredient to lowercase and remove extra spaces.
    Example: " Milk " becomes "milk"
    """
    return text.strip().lower()


def clean_ingredient_list(items):
    """
    Clean all ingredients in a list.
    Also removes empty items and duplicates.
    """
    cleaned = []

    for item in items:
        cleaned_item = clean_ingredient(item)

        if cleaned_item != "" and cleaned_item not in cleaned:
            cleaned.append(cleaned_item)

    return cleaned


def load_recipes(filename):
    """
    Load recipe data from a JSON file.
    The JSON file should be in the same folder as this Python file.
    """
    with open(filename, "r") as file:
        return json.load(file)


def analyze_recipe(recipe, user_ingredients):
    """
    Compare one recipe to the user's ingredients.
    Count matches, missing ingredients, and calculate a percentage score.
    """
    matched = []
    missing = []

    for ingredient in recipe["ingredients"]:
        clean_recipe_ingredient = clean_ingredient(ingredient)

        if clean_recipe_ingredient in user_ingredients:
            matched.append(clean_recipe_ingredient)
        else:
            missing.append(clean_recipe_ingredient)

    matched_count = len(matched)
    total_ingredients = len(recipe["ingredients"])
    score = (matched_count / total_ingredients) * 100

    return {
        "name": recipe["name"],
        "category": recipe.get("category", "Uncategorized"),
        "matched_count": matched_count,
        "total_ingredients": total_ingredients,
        "matched": matched,
        "missing": missing,
        "score": score
    }


def rank_recipes(recipes, user_ingredients):
    """
    Compare all recipes to the user's ingredients
    and sort them from best match to worst match.
    """
    results = []

    for recipe in recipes:
        result = analyze_recipe(recipe, user_ingredients)
        results.append(result)

    results.sort(key=lambda recipe: (recipe["score"], recipe["matched_count"]), reverse=True)
    return results


def get_match_label(score):
    """
    Give each recipe a label based on its percentage match score.
    """
    if score == 100:
        return "Perfect Match"
    elif score >= 75:
        return "Great Match"
    elif score >= 50:
        return "Good Match"
    elif score >= 30:
        return "Possible Match"
    else:
        return "Low Match"


def display_results(results, top_n=10):
    """
    Display the top recipe recommendations in a clean format.
    """
    print("\nRecipe Recommendations:\n")

    if len(results) == 0:
        print("No recipes found.")
        return

    for i, result in enumerate(results[:top_n], start=1):
        label = get_match_label(result["score"])

        if len(result["matched"]) == 0:
            matched_text = "None"
        else:
            matched_text = ", ".join(result["matched"])

        if len(result["missing"]) == 0:
            missing_text = "None"
        else:
            missing_text = ", ".join(result["missing"])

        print(f"{i}. {result['name']} ({result['category']})")
        print(f"   Match Level: {label}")
        print(f"   Ingredients Matched: {result['matched_count']}/{result['total_ingredients']}")
        print(f"   Match Score: {result['score']:.0f}%")
        print(f"   Ingredients You Have: {matched_text}")
        print(f"   Missing Ingredients: {missing_text}")

        if result["score"] == 100:
            print("   You can make this right now!")

        print()


def build_shopping_list(results, top_n=3):
    """
    Build a shopping list using missing ingredients
    from the top few recipe matches.
    """
    shopping_list = []

    for result in results[:top_n]:
        for ingredient in result["missing"]:
            if ingredient not in shopping_list:
                shopping_list.append(ingredient)

    return shopping_list


def display_shopping_list(shopping_list):
    """
    Display a suggested shopping list.
    """
    print("Suggested Shopping List:\n")

    if len(shopping_list) == 0:
        print("You already have everything you need for the top recipes!")
        return

    for item in shopping_list:
        print(f"- {item}")


def main():
    """
    Main program:
    1. Ask the user for ingredients
    2. Clean the input
    3. Load recipes
    4. Rank recipes
    5. Display results
    6. Display a shopping list
    """
    print("Welcome to the Ingredient-Based Recipe Recommender")
    print("Enter the ingredients you have, separated by commas.")
    print("Example: egg, milk, butter, bread")

    user_input = input("\nYour ingredients: ")
    raw_ingredients = user_input.split(",")
    user_ingredients = clean_ingredient_list(raw_ingredients)

    if len(user_ingredients) == 0:
        print("You did not enter any valid ingredients.")
        return

    recipes = load_recipes("recipes.json")
    results = rank_recipes(recipes, user_ingredients)

    display_results(results, top_n=10)

    shopping_list = build_shopping_list(results, top_n=3)
    print()
    display_shopping_list(shopping_list)


main()
