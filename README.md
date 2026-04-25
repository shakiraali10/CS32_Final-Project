# CS32_Final-Project
CS 32 Final Project- By Shakira Ali and Zaid Ahmed
# Ingredient-Based Recipe Recommender

## Project Description

This project is a Python-based recipe recommendation system that suggests meals based on ingredients a user already has at home. The program compares a user’s ingredient list to a set of recipes, identifies which ingredients match, and determines which ingredients are missing. It then ranks the recipes based on how closely they match the user’s available ingredients.

The goal of this project is to make it easier for users to decide what they can cook without needing to search through recipes manually, while also helping them see what additional ingredients they might need.

---

## Features

* Accepts user input as a list of ingredients
* Cleans and standardizes ingredient text (removes extra spaces and ignores capitalization)
* Compares user ingredients to recipe ingredients
* Calculates a match score as a percentage
* Ranks recipes from best match to worst match
* Labels recipes based on match quality (Perfect Match, Great Match, etc.)
* Displays missing ingredients for each recipe
* Highlights recipes that can be made with all available ingredients
* Generates a simple shopping list based on missing ingredients from top matches

---

## How to Run

1. Make sure Python is installed on your computer.
2. Download or clone the project files.
3. Ensure the following files are in the same folder:

   * `recipe_recommender.py`
   * `recipes.json`
4. Open the file in an IDE or run it from the terminal.
5. Run the program:

   ```
   python recipe_recommender.py
   ```
6. When prompted, enter ingredients separated by commas.

Example input:
egg, milk, butter, bread

---

## Project Structure

* `recipe_recommender.py` — main program that runs the recommender
* `recipes.json` — dataset containing recipe names, categories, and ingredients

---

## Setup Requirements

This project uses standard Python and does not require any external libraries or additional installation steps.

---

## External Contributions

Some general ideas for structuring the project (such as separating data into a JSON file and organizing code into functions) were inspired by common programming practices and online resources. No external code was directly copied.

---

## Use of Generative AI

Generative AI tools were used to help improve the organization of the code, refine comments, and suggest small feature improvements such as the shopping list and match scoring format. All code was reviewed, tested, and edited to ensure full understanding.

---

## Future Improvements

* Expand the dataset with more recipes
* Add filtering by category (e.g., breakfast, lunch, dinner)
* Improve ingredient matching (for example, handling plural forms or similar ingredients)
* Add a graphical interface for easier interaction
* Allow users to save or favorite recipes
