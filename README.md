# CS32_Final-Project  
CS 32 Final Project — Shakira Ali and Zaid Ahmed  

# Ingredient-Based Recipe Recommender

## Project Description

This project is a Python-based recipe recommendation system that suggests meals based on ingredients a user already has at home. The program compares a user’s ingredient list to a set of recipes, identifies which ingredients match, and determines which ingredients are missing. It then ranks the recipes based on how closely they match the user’s available ingredients.

The goal of this project is to make it easier for users to decide what they can cook without needing to search through recipes manually, while also helping them reduce food waste and understand what additional ingredients they might need.

---

## Features

- Accepts user input as a list of ingredients  
- Cleans and standardizes ingredient text (removes extra spaces, punctuation, and ignores capitalization)  
- Handles simple variations in ingredient names (e.g., plural forms and partial matches)  
- Compares user ingredients to recipe ingredients  
- Calculates a match score as a percentage  
- Ranks recipes from best match to worst match using multiple criteria  
- Labels recipes based on match quality (Perfect Match, Great Match, etc.)  
- Displays both matched and missing ingredients for each recipe  
- Explains why each recipe is ranked where it is  
- Highlights recipes that can be made with all available ingredients  
- Generates a smart shopping list based on missing ingredients from top matches  
- Includes a Remy (Ratatouille) narrator for user interaction  
- Opens a Remy GIF collection for a more engaging experience  
- Provides optional Spotify playlist suggestions for cooking  

---

## How to Run

### Requirements
- Python 3 installed on your computer  
- A file named `recipes.json` in the same folder as the program  

### Steps

1. Download or clone the project files.  
2. Ensure the following files are in the same folder:
   - `recipe_recommender.py`  
   - `recipes.json`  
   - `README.md`  

3. Open the project in a local IDE (such as VS Code) or a terminal.  

4. Run the program:

5. When prompted, enter ingredients separated by commas.  



---

## Project Structure

- `recipe_recommender.py` — main program that runs the recommender  
- `recipes.json` — dataset containing recipe names, categories, and ingredients  
- `README.md` — project documentation  

---

## Setup Notes

This project uses only standard Python libraries and does not require installing external packages.

The program will automatically open:
- A web browser tab with Remy (Ratatouille) GIFs  
- Spotify playlist links (if selected by the user)  

---

## External Contributions

General design ideas (such as using JSON for data storage and organizing code into functions) were inspired by standard programming practices.

No external code was directly copied from tutorials or other sources.

---

## Use of Generative AI

Generative AI tools (ChatGPT) were used to assist with:
- Improving code organization and readability  
- Suggesting enhancements to ingredient matching logic  
- Adding features such as the shopping list, ranking explanations, and playlist integration  
- Refining comments and documentation  

All generated code was reviewed, tested, modified, and fully understood before being included in the final submission.

---

## Future Improvements

- Expand the dataset with more recipes  
- Improve ingredient matching using more advanced techniques (e.g., synonyms or NLP)  
- Add filtering by category (breakfast, lunch, dinner, etc.)  
- Build a graphical user interface (GUI) or web-based version  
- Allow users to save or favorite recipes  

---

## GitHub Submission Notes

- Code is organized, readable, and includes comments for key logic  
- Unused or outdated code has been removed  
- README includes setup instructions and project explanation  

