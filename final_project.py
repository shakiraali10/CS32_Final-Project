# Ingredient-Based Recipe Recommender

This project suggests recipes based on ingredients a user already has.

## Features
- Input a list of ingredients
- Finds matching recipes
- Shows missing ingredients
- Ranks recipes by match score

# Simple Ingredient-Based Recipe Recommender

# Ingredient-Based Recipe Recommender

# Step 1: Recipe dataset
recipes = [
    {"name": "Pancakes", "ingredients": ["egg", "milk", "flour"]},
    {"name": "Omelette", "ingredients": ["egg", "milk", "cheese"]},
    {"name": "Toast", "ingredients": ["bread", "butter"]},
]

# Step 2: User input
user_ingredients = ["Egg", " Milk ", "butter"]

# Step 3: Make it not case sensitive & remove spaces 
clean_user_ingredients = []
for ingredient in user_ingredients:
    clean_user_ingredients.append(ingredient.strip().lower())

# Step 4: Compare user ingredients to recipe ingredients
results = []

for recipe in recipes:
    matched = 0
    missing = []

    for ingredient in recipe["ingredients"]:
        clean_ingredient = ingredient.strip().lower()

        if clean_ingredient in clean_user_ingredients:
            matched += 1
        else:
            missing.append(clean_ingredient)

    score = matched / len(recipe["ingredients"])

    results.append({
        "name": recipe["name"],
        "matched": matched,
        "total": len(recipe["ingredients"]),
        "missing": missing,
        "score": score
    })

# Step 5: Rank recipes by match score
results.sort(key=lambda x: x["score"], reverse=True)

# Step 6: Display recommendations
print("You can make:")

for result in results:
    print(
        f"- {result['name']}: {result['matched']}/{result['total']} ingredients matched "
        f"- missing: {', '.join(result['missing'])}"
    )
